"""`upstream-monitor pr` 的实现。

创建分支、写快照或只更新 lock、提交、用 `gh pr create` 开 PR。PR 正文只放
机械事实：元数据块（commit 前后、stars、forks、许可证、快照策略）、
full-text 来源的完整上游 diff、metadata-only 来源的原文声明（不含原文，只给
commit 和 hash）。是否采用、怎么改写这些语义判断不在这里——PR 不反查本地
decisions.yaml，也不附 locate 输出，由 skill-merge 读 PR 里的 diff 和本地
skill 决定。

幂等键 `source_id:path:commit`：path 段在来源只追踪一个文件时就是那个路径，
追踪多个文件时用逗号拼接（schema 只要求不含冒号，没有规定多路径怎么表示，
这是本实现的约定）。同一个键、且 lock 里 open_pr 非空时不重复开 PR。

真正执行 git / gh 的部分只在 dry_run=False 时跑；dry_run（含幂等短路）
不发起任何子进程，方便离线测试。
"""
from __future__ import annotations

import datetime
import re
import subprocess
from pathlib import Path

from upstream_monitor.diff import run_diff
from upstream_monitor.github_client import GitHubClient
from upstream_monitor.paths import RepoPaths
from upstream_monitor.schemas import validate_doc
from upstream_monitor.snapshot import snapshot_one_source
from upstream_monitor.yamlio import dump_json, load_json, load_yaml


def change_key_for(source_id: str, paths_list: list[str], commit: str) -> str:
    path_field = paths_list[0] if len(paths_list) == 1 else ",".join(paths_list)
    return f"{source_id}:{path_field}:{commit}"


def render_pr_title(merge_id: str, source_id: str) -> str:
    return f"chore({merge_id}): sync upstream {source_id}"


def render_pr_body(
    merge_id: str,
    source: dict,
    entry: dict,
    diff_text: str | None,
) -> str:
    source_id = source["id"]
    from_commit = entry.get("last_accepted_commit") or "(无基线)"
    to_commit = entry.get("last_seen_commit")
    stars_hist = entry.get("stars_history", [])
    stars_before = stars_hist[-2]["value"] if len(stars_hist) >= 2 else None
    stars_after = stars_hist[-1]["value"] if stars_hist else None

    lines: list[str] = []
    lines.append("## 元数据\n")
    lines.append(f"- merge_id：{merge_id}")
    lines.append(f"- 来源：{source_id}，{source['repository']}，{source['branch']}")
    lines.append(f"- 提交区间：{from_commit} .. {to_commit}")
    lines.append(f"- 追踪文件：{', '.join(source['paths'])}")
    lines.append(f"- snapshot_policy：{source['snapshot_policy']}")
    lines.append(f"- 许可证：{source['license']}")
    lines.append(
        f"- stars：{stars_before if stars_before is not None else '未知'} -> "
        f"{stars_after if stars_after is not None else '未知'}"
    )
    lines.append(f"- forks：{entry.get('forks', '未知')}")
    lines.append("")

    if source["snapshot_policy"] == "metadata-only":
        lines.append("## 原文声明\n")
        lines.append(f"本 PR 不含来源 `{source_id}` 的任何原文，snapshots/ 未新增内容。")
        lines.append("")
        lines.append(f"- commit：{to_commit}")
        lines.append(f"- raw_sha256：{entry.get('raw_sha256')}")
        lines.append(f"- normalized_sha256：{entry.get('normalized_sha256')}")
        lines.append("")
        lines.append(
            f"原文请本地用 `upstream-monitor diff --merge {merge_id} --source {source_id}` 查看。"
        )
    else:
        lines.append("## 上游 diff\n")
        text = (diff_text or "").strip()
        lines.append(text if text else "无变化。")

    lines.append("")
    return "\n".join(lines)


def _run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, check=True)


def run_pr(
    paths: RepoPaths,
    client: GitHubClient,
    merge_id: str,
    source_id: str,
    dry_run: bool = True,
) -> dict:
    """返回一个结果字典，字段视是否幂等短路、是否 dry_run 而不同。"""
    sources_path = paths.sources_yaml(merge_id)
    lock_path = paths.lock_json(merge_id)
    S = load_yaml(sources_path)
    L = load_json(lock_path)
    source = next((s for s in S["sources"] if s["id"] == source_id), None)
    if source is None:
        raise KeyError(f"{merge_id}: 找不到来源 {source_id}")
    entry = L["sources"].get(source_id)
    if entry is None:
        raise KeyError(f"{merge_id}: lock 里没有来源 {source_id}，请先跑一次 check。")

    commit = entry.get("last_seen_commit")
    if not commit:
        raise ValueError(f"{source_id}: lock 里没有 last_seen_commit，请先跑一次 check。")

    change_key = change_key_for(source_id, source["paths"], commit)

    if entry.get("last_change_key") == change_key and entry.get("open_pr"):
        return {
            "idempotent": True,
            "change_key": change_key,
            "open_pr": entry["open_pr"],
            "message": f"变更键 {change_key} 已经开过 PR #{entry['open_pr']}，不重复开。",
        }

    diff_text = None
    if source["snapshot_policy"] == "full-text":
        diff_text = run_diff(paths, client, merge_id, source_id)
    body = render_pr_body(merge_id, source, entry, diff_text)
    title = render_pr_title(merge_id, source_id)
    date = datetime.date.today().isoformat()
    branch = f"upstream-sync/{date}-{source_id}"

    commands = [
        ["git", "checkout", "-b", branch],
    ]
    if source["snapshot_policy"] == "full-text":
        commands.append(["<internal>", "snapshot", source_id])
    commands += [
        ["git", "add", "-A"],
        ["git", "commit", "-m", title],
        ["git", "push", "-u", "origin", branch],
        ["gh", "pr", "create", "--title", title, "--body-file", "<临时文件>", "--head", branch],
    ]

    result = {
        "idempotent": False,
        "change_key": change_key,
        "branch": branch,
        "title": title,
        "body": body,
        "commands": commands,
    }

    if dry_run:
        return result

    _run(["git", "checkout", "-b", branch], paths.root)

    new_entry = entry
    if source["snapshot_policy"] == "full-text":
        new_entry, _snap_result = snapshot_one_source(paths, client, merge_id, source, entry)

    _run(["git", "add", "-A"], paths.root)
    _run(["git", "commit", "-m", title], paths.root)
    _run(["git", "push", "-u", "origin", branch], paths.root)

    body_file = paths.root / f".upstream-monitor-pr-body-{source_id}.md"
    body_file.write_text(body, encoding="utf-8")
    try:
        pr_out = _run(
            ["gh", "pr", "create", "--title", title, "--body-file", str(body_file), "--head", branch],
            paths.root,
        )
    finally:
        body_file.unlink(missing_ok=True)

    pr_number = None
    m = re.search(r"/pull/(\d+)", pr_out.stdout)
    if m:
        pr_number = int(m.group(1))

    new_entry = dict(new_entry)
    new_entry["last_change_key"] = change_key
    new_entry["open_pr"] = pr_number
    L2 = dict(L)
    L2["sources"] = dict(L["sources"])
    L2["sources"][source_id] = new_entry
    validate_doc(paths.schemas_dir, "lock", L2, target=str(lock_path))
    dump_json(L2, lock_path)

    result["open_pr"] = pr_number
    result["pr_url"] = pr_out.stdout.strip()
    return result
