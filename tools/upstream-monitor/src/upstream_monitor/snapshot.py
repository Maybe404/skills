"""`upstream-monitor snapshot` 的实现。

把 full-text 来源的追踪文件按 last_seen_commit 写进
merges/<id>/snapshots/<source_id>/，附 LICENSE；更新 lock 的 stored_path。
metadata-only 来源拒绝执行。
"""
from __future__ import annotations

from pathlib import Path

from upstream_monitor.github_client import FileNotFound, GitHubClient
from upstream_monitor.paths import RepoPaths
from upstream_monitor.schemas import validate_doc
from upstream_monitor.yamlio import dump_json, load_json, load_yaml


class MetadataOnlyError(Exception):
    """对 metadata-only 来源调用 snapshot 时抛出，调用方据此拒绝执行。"""


class SnapshotResult:
    def __init__(self, source_id: str, files_written: list[str], license_written: str | None):
        self.source_id = source_id
        self.files_written = files_written
        self.license_written = license_written


def snapshot_one_source(
    paths: RepoPaths, client: GitHubClient, merge_id: str, source: dict, lock_entry: dict
) -> tuple[dict, SnapshotResult]:
    if source["snapshot_policy"] != "full-text":
        raise MetadataOnlyError(
            f"{source['id']}: snapshot_policy 是 {source['snapshot_policy']}，"
            "metadata-only 来源不保存原文，拒绝执行 snapshot。"
        )

    commit = lock_entry.get("last_seen_commit")
    if not commit:
        raise ValueError(f"{source['id']}: lock 里没有 last_seen_commit，请先跑一次 check。")

    repo = source["repository"]
    snap_dir = paths.snapshots_dir(merge_id) / source["id"]
    written: list[str] = []
    files_by_path = {f["original_path"]: dict(f) for f in lock_entry.get("files", [])}

    for original_path in source["paths"]:
        content = client.get_file(repo, original_path, commit)
        stored_rel = f"merges/{merge_id}/snapshots/{source['id']}/" + paths.skill_source_path(
            source["id"], original_path
        )
        dest = paths.root / stored_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(content)
        written.append(stored_rel)
        entry = files_by_path.setdefault(original_path, {})
        entry["original_path"] = original_path
        entry["stored_path"] = stored_rel

    license_written = None
    try:
        lic_path, lic_content = client.get_license(repo, commit)
    except FileNotFound:
        lic_path, lic_content = None, None
    if lic_content is not None:
        dest = snap_dir / "LICENSE"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(lic_content)
        license_written = str(dest.relative_to(paths.root))

    new_entry = dict(lock_entry)
    new_entry["files"] = [files_by_path[p] for p in source["paths"]]
    return new_entry, SnapshotResult(source["id"], written, license_written)


def run_snapshot(
    paths: RepoPaths, client: GitHubClient, merge_id: str, source_id: str | None = None
) -> list[SnapshotResult]:
    S = load_yaml(paths.sources_yaml(merge_id))
    lock_path = paths.lock_json(merge_id)
    L = load_json(lock_path)
    sources = S["sources"]
    if source_id:
        sources = [s for s in sources if s["id"] == source_id]
        if not sources:
            raise KeyError(f"{merge_id}: 找不到来源 {source_id}")
    else:
        sources = [s for s in sources if s["snapshot_policy"] == "full-text"]

    results: list[SnapshotResult] = []
    lock_sources = dict(L["sources"])
    for source in sources:
        entry = lock_sources.get(source["id"])
        if entry is None:
            raise KeyError(f"{merge_id}: lock 里没有来源 {source['id']}，请先跑一次 check。")
        new_entry, result = snapshot_one_source(paths, client, merge_id, source, entry)
        lock_sources[source["id"]] = new_entry
        results.append(result)

    new_lock = dict(L)
    new_lock["sources"] = lock_sources
    validate_doc(paths.schemas_dir, "lock", new_lock, target=str(lock_path))
    dump_json(new_lock, lock_path)
    return results
