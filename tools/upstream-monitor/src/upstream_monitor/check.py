"""`upstream-monitor check` 的实现。

对 catalog 里 merge_instance 非空的实例，遍历 status 为 active 或 candidate
的来源，取 branch HEAD commit 和每个追踪文件的内容（只在内存里算 hash，
不落盘原文），与 lock 比对，更新 lock。语义分类（重复/冲突/是否采用）不在
这里做，这里只区分"没变化 / 格式变化 / 内容变化 / 不可达"。
"""
from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Any

from upstream_monitor.github_client import (
    FileNotFound,
    GitHubClient,
    NetworkError,
    RepoNotFound,
    RepoPrivate,
)
from upstream_monitor.normalize import normalized_sha256, raw_sha256, source_normalized_sha256, source_raw_sha256
from upstream_monitor.paths import RepoPaths
from upstream_monitor.schemas import SchemaValidationError, validate_doc
from upstream_monitor.yamlio import dump_json, dump_yaml, load_json, load_yaml

CHANGE_NO_CHANGE = "no-change"
CHANGE_FORMAT = "format-change"
CHANGE_CONTENT = "content-change"
CHANGE_UNREACHABLE = "unreachable"
CHANGE_PRIVATE = "private"
CHANGE_GONE = "gone"
CHANGE_SKIPPED = "skipped"

CHECKED_STATUSES = {"active", "candidate"}
GITHUB_SOURCE_TYPES = {"github-skill", "github-prompt"}


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def compute_line_count(raw: bytes) -> int:
    if not raw:
        return 0
    n = raw.count(b"\n")
    if not raw.endswith(b"\n"):
        n += 1
    return n


def _blank_lock_entry() -> dict[str, Any]:
    return {
        "last_seen_commit": None,
        "last_processed_commit": None,
        "last_accepted_commit": None,
        "raw_sha256": None,
        "normalized_sha256": None,
        "size": None,
        "line_count": None,
        "files": [],
        "stars_history": [],
        "forks": None,
        "installs": None,
        "last_checked_at": None,
        "last_change_key": None,
        "open_pr": None,
        "open_issue": None,
        "availability": "ok",
    }


def check_one_source(
    client: GitHubClient, source: dict, lock_entry: dict | None, now: str
) -> tuple[dict, dict]:
    """返回 (更新后的 lock_entry, 结果描述)。不修改传入的 lock_entry。"""
    sid = source["id"]
    result: dict[str, Any] = {"source_id": sid, "license_changed": False}
    entry = dict(lock_entry) if lock_entry else _blank_lock_entry()

    if source["source_type"] not in GITHUB_SOURCE_TYPES:
        result["change"] = CHANGE_SKIPPED
        result["detail"] = f"source_type={source['source_type']!r} 不是 GitHub 来源，check 跳过"
        entry["last_checked_at"] = now
        return entry, result

    repo = source["repository"]

    try:
        meta = client.get_repo_meta(repo)
    except RepoNotFound:
        entry["availability"] = "gone"
        entry["last_checked_at"] = now
        result.update(change=CHANGE_GONE, detail=f"仓库不可达（404）：{repo}")
        return entry, result
    except RepoPrivate:
        entry["availability"] = "private"
        entry["last_checked_at"] = now
        result.update(change=CHANGE_PRIVATE, detail=f"仓库已转为私有：{repo}")
        return entry, result
    except NetworkError as e:
        entry["availability"] = "unreachable"
        entry["last_checked_at"] = now
        result.update(change=CHANGE_UNREACHABLE, detail=str(e))
        return entry, result

    try:
        head_commit = client.get_head_commit(repo, source["branch"])
    except RepoNotFound:
        entry["availability"] = "gone"
        entry["last_checked_at"] = now
        result.update(change=CHANGE_GONE, detail=f"分支不可达：{repo}@{source['branch']}")
        return entry, result
    except NetworkError as e:
        entry["availability"] = "unreachable"
        entry["last_checked_at"] = now
        result.update(change=CHANGE_UNREACHABLE, detail=str(e))
        return entry, result

    file_raws: list[bytes] = []
    files_result = []
    unreachable_paths = []
    for path in source["paths"]:
        try:
            raw = client.get_file(repo, path, head_commit)
        except FileNotFound:
            unreachable_paths.append(path)
            continue
        except NetworkError as e:
            unreachable_paths.append(f"{path}（{e}）")
            continue
        file_raws.append(raw)
        files_result.append(
            {
                "original_path": path,
                "raw_sha256": raw_sha256(raw),
                "normalized_sha256": normalized_sha256(raw),
                "size": len(raw),
                "line_count": compute_line_count(raw),
            }
        )

    entry["forks"] = meta.forks
    entry["stars_history"] = list(entry.get("stars_history", [])) + [
        {"observed_at": now, "value": meta.stars}
    ]
    entry["last_checked_at"] = now

    if unreachable_paths:
        entry["availability"] = "unreachable"
        result.update(change=CHANGE_UNREACHABLE, detail=f"以下追踪文件不可达: {unreachable_paths}")
        return entry, result

    entry["availability"] = "ok"
    new_raw_hash = source_raw_sha256(file_raws)
    new_norm_hash = source_normalized_sha256(file_raws)
    old_raw_hash = entry.get("raw_sha256")
    old_norm_hash = entry.get("normalized_sha256")
    old_commit = entry.get("last_seen_commit")

    if old_commit == head_commit and old_raw_hash == new_raw_hash:
        result["change"] = CHANGE_NO_CHANGE
    elif old_norm_hash == new_norm_hash:
        result["change"] = CHANGE_FORMAT
    else:
        result["change"] = CHANGE_CONTENT
    result["old_commit"] = old_commit
    result["new_commit"] = head_commit

    old_files_by_path = {f["original_path"]: f for f in entry.get("files", [])}
    new_files = []
    for fr in files_result:
        old = old_files_by_path.get(fr["original_path"], {})
        new_files.append(
            {
                "original_path": fr["original_path"],
                "stored_path": old.get("stored_path"),
                "raw_sha256": fr["raw_sha256"],
                "normalized_sha256": fr["normalized_sha256"],
            }
        )

    entry["last_seen_commit"] = head_commit
    entry["raw_sha256"] = new_raw_hash
    entry["normalized_sha256"] = new_norm_hash
    entry["size"] = sum(fr["size"] for fr in files_result)
    entry["line_count"] = sum(fr["line_count"] for fr in files_result)
    entry["files"] = new_files

    if meta.license_spdx and source["license"] != "unknown" and meta.license_spdx != source["license"]:
        result["license_changed"] = True
        result["license_detail"] = f"sources.yaml 记 {source['license']!r}，GitHub 现报 {meta.license_spdx!r}"
    elif meta.license_spdx is None and source["license"] != "unknown":
        result["license_changed"] = True
        result["license_detail"] = f"sources.yaml 记 {source['license']!r}，GitHub 现无法识别许可证"

    return entry, result


def run_check(
    paths: RepoPaths,
    client: GitHubClient,
    merge_id: str | None = None,
) -> list[dict]:
    """对一个或全部 merge 实例跑 check，写回 lock（和许可证变化时的 sources.yaml）。

    返回逐来源的结果列表，每项含 merge_id、source_id、change、detail 等字段。
    """
    if merge_id is not None:
        merge_ids = [merge_id]
    else:
        merge_ids = [
            Path(doc.get("merge_instance")).name
            for doc in (load_yaml(p) for p in paths.catalog_entries())
            if doc.get("merge_instance")
        ]

    now = now_iso()
    all_results: list[dict] = []

    for mid in merge_ids:
        sources_path = paths.sources_yaml(mid)
        lock_path = paths.lock_json(mid)
        S = load_yaml(sources_path)
        L = load_json(lock_path)
        sources = S["sources"]
        lock_sources = dict(L["sources"])

        license_dirty = False
        for source in sources:
            sid = source["id"]
            if source["status"] not in CHECKED_STATUSES:
                continue
            entry, result = check_one_source(client, source, lock_sources.get(sid), now)
            result["merge_id"] = mid
            lock_sources[sid] = entry
            all_results.append(result)

            if result.get("license_changed") and source.get("license_status") != "changed":
                source["license_status"] = "changed"
                license_dirty = True

        new_lock = {"merge_id": mid, "generated_at": now, "sources": lock_sources}
        validate_doc(paths.schemas_dir, "lock", new_lock, target=str(lock_path))
        dump_json(new_lock, lock_path)

        if license_dirty:
            validate_doc(paths.schemas_dir, "sources", S, target=str(sources_path))
            dump_yaml(S, sources_path)

    return all_results
