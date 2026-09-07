"""`upstream-monitor diff` 的实现。

默认取 last_accepted_commit 到 last_seen_commit，两个版本都从 GitHub 按
commit 现取，输出统一 diff。full-text 来源首次同步（没有 last_accepted_commit，
且调用方没有显式传 --from）时，没有基线 commit 可取，改用本地已有快照
（merges/<id>/snapshots/<source_id>/ 下 lock 记录的 stored_path）作为旧版本，
避免把"从未同步过"误判成"整份文件都是新增"；metadata-only 来源没有快照，
这种情况仍按无基线处理。metadata-only 来源的结果只能打到 stdout，调用方
（cli.py、pr.py）不得把返回值写入任何文件。
"""
from __future__ import annotations

import difflib

from upstream_monitor.github_client import FileNotFound, GitHubClient
from upstream_monitor.paths import RepoPaths
from upstream_monitor.yamlio import load_json, load_yaml

METADATA_ONLY_BANNER = "原文不得写入仓库、PR 或 issue（该来源为 metadata-only）"


def _fetch_text(client: GitHubClient, repo: str, path: str, commit: str | None) -> list[str]:
    if commit is None:
        return []
    try:
        raw = client.get_file(repo, path, commit)
    except FileNotFound:
        return []
    return raw.decode("utf-8", errors="replace").splitlines(keepends=True)


def _old_version(
    paths: RepoPaths,
    client: GitHubClient,
    source: dict,
    entry: dict,
    path: str,
    from_commit: str | None,
) -> tuple[list[str], str]:
    """返回 (旧版本的行列表, diff 头部用的标签后缀)。

    from_commit 非 None 时按常规从 GitHub 取该 commit 的内容。from_commit 为
    None（没有显式 --from，且 lock 里也没有 last_accepted_commit）时，
    full-text 来源改读本地快照；快照也没有（真正首次登记，从未跑过
    snapshot）或来源是 metadata-only 时，退回"无基线"。
    """
    if from_commit is not None:
        return _fetch_text(client, source["repository"], path, from_commit), from_commit
    if source["snapshot_policy"] == "full-text":
        stored = next(
            (f.get("stored_path") for f in entry.get("files", []) if f.get("original_path") == path),
            None,
        )
        if stored:
            p = paths.root / stored
            if p.exists():
                text = p.read_text(encoding="utf-8", errors="replace")
                return text.splitlines(keepends=True), f"本地快照 {stored}"
    return [], "(无基线)"


def run_diff(
    paths: RepoPaths,
    client: GitHubClient,
    merge_id: str,
    source_id: str,
    from_commit: str | None = None,
    to_commit: str | None = None,
) -> str:
    S = load_yaml(paths.sources_yaml(merge_id))
    L = load_json(paths.lock_json(merge_id))
    source = next((s for s in S["sources"] if s["id"] == source_id), None)
    if source is None:
        raise KeyError(f"{merge_id}: 找不到来源 {source_id}")
    entry = L["sources"].get(source_id)
    if entry is None:
        raise KeyError(f"{merge_id}: lock 里没有来源 {source_id}")

    from_c = from_commit or entry.get("last_accepted_commit")
    to_c = to_commit or entry.get("last_seen_commit")
    repo = source["repository"]

    chunks: list[str] = []
    if source["snapshot_policy"] == "metadata-only":
        chunks.append(METADATA_ONLY_BANNER)
        chunks.append("")

    if to_c is None:
        chunks.append(f"{source_id}: lock 里没有 last_seen_commit，先跑一次 check。")
        return "\n".join(chunks)

    for path in source["paths"]:
        old_lines, from_suffix = _old_version(paths, client, source, entry, path, from_c)
        new_lines = _fetch_text(client, repo, path, to_c)
        from_label = f"{path}@{from_suffix}"
        to_label = f"{path}@{to_c}"
        diff = difflib.unified_diff(old_lines, new_lines, fromfile=from_label, tofile=to_label)
        text = "".join(diff)
        if text:
            chunks.append(text)
        else:
            chunks.append(f"--- {from_label}\n+++ {to_label}\n（无差异）\n")

    return "\n".join(chunks)
