"""没有 decisions.yaml、没有 work/ 的 merge 实例：validate、render、
pr --dry-run 都要能跑通，不因为这两样东西缺失而报错或崩溃。

decisions.yaml、work/ 这套只是 maybe-humanizer 这一个实例的历史产物；以后
新建的 merge 实例不会有它们（流程简化后，PR 正文直接放上游 diff，不再反查
本地规则），所以这里用 dump_yaml/dump_json 动态搭一个只有 sources.yaml、
sources.lock.json 和一份快照的最小实例，不往 tests/fixtures/repo/ 里加静态
夹具文件（做法与 test_lineage.py 里 _build_merge 一致）。
"""
from __future__ import annotations

from upstream_monitor.github_client import FakeGitHubClient
from upstream_monitor.normalize import normalized_sha256, raw_sha256
from upstream_monitor.pr import run_pr
from upstream_monitor.render import render_sources_for_merge
from upstream_monitor.validate import validate
from upstream_monitor.yamlio import dump_json, dump_yaml

MERGE_ID = "nodec-fixture"
FULL_TEXT_ID = "upstream-nodec-full"
META_ID = "upstream-nodec-meta"
COMMIT = "c" * 40

OLD_SNAPSHOT_TEXT = (
    "---\n"
    "name: nodec-full\n"
    "description: fixture with no decision ledger\n"
    "---\n"
    "\n"
    "# NODEC Full\n"
    "\n"
    "Original snapshot line before any upstream change.\n"
)

LICENSE_TEXT = (
    "MIT License\n"
    "\n"
    "Copyright (c) 2026 Fixture Owner\n"
    "\n"
    "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
    "of this software, subject to standard MIT terms.\n"
)


def _source(sid: str, repo: str, snapshot_policy: str, status: str) -> dict:
    return {
        "id": sid,
        "source_type": "github-skill",
        "repository": repo,
        "previous_repository": [],
        "branch": "main",
        "paths": ["SKILL.md"],
        "license": "MIT" if snapshot_policy == "full-text" else "unknown",
        "license_status": "known" if snapshot_policy == "full-text" else "unknown",
        "snapshot_policy": snapshot_policy,
        "status": status,
        "selection_status": "representative",
        "lineage": sid,
        "tracking_revision": 1,
        "previous_paths": [],
        "path_changed_at": None,
        "baseline_reset_reason": None,
        "status_changed_at": "2026-01-01T00:00:00Z",
        "reason": "pytest 夹具：没有 decisions.yaml 的实例。",
        "notes": None,
    }


def _lock_entry(*, commit: str, content: bytes | None, stored_path: str | None) -> dict:
    return {
        "last_seen_commit": commit,
        "last_processed_commit": None,
        "last_accepted_commit": None,
        "raw_sha256": raw_sha256(content) if content is not None else None,
        "normalized_sha256": normalized_sha256(content) if content is not None else None,
        "size": len(content) if content is not None else None,
        "line_count": content.count(b"\n") if content is not None else None,
        "files": [
            {
                "original_path": "SKILL.md",
                "stored_path": stored_path,
                "raw_sha256": raw_sha256(content) if content is not None else None,
                "normalized_sha256": normalized_sha256(content) if content is not None else None,
            }
        ],
        "stars_history": [{"observed_at": "2026-01-01T00:00:00Z", "value": 3}],
        "forks": 0,
        "installs": None,
        "last_checked_at": "2026-01-01T00:00:00Z",
        "last_change_key": None,
        "open_pr": None,
        "open_issue": None,
        "availability": "ok",
    }


def _build_merge(repo_paths) -> None:
    """搭一个没有 decisions.yaml、没有 work/ 的 merge 实例：一个 full-text
    来源（status=active，已有快照但从未跑过 pr，last_accepted_commit 为
    null——首次同步的典型状态），一个 metadata-only 候选来源。"""
    sources_doc = {
        "merge_id": MERGE_ID,
        "target_skill": MERGE_ID,
        "sources": [
            _source(FULL_TEXT_ID, "fixture-owner/nodec-full", "full-text", "active"),
            _source(META_ID, "fixture-owner/nodec-meta", "metadata-only", "candidate"),
        ],
    }
    dump_yaml(sources_doc, repo_paths.sources_yaml(MERGE_ID))

    snap_dir = repo_paths.snapshots_dir(MERGE_ID) / FULL_TEXT_ID
    snap_dir.mkdir(parents=True, exist_ok=True)
    (snap_dir / "SKILL.source.md").write_text(OLD_SNAPSHOT_TEXT, encoding="utf-8")
    (snap_dir / "LICENSE").write_text(LICENSE_TEXT, encoding="utf-8")

    old_bytes = OLD_SNAPSHOT_TEXT.encode("utf-8")
    # metadata-only 来源的 hash 照样由 check 算出（只是不落盘原文），
    # 这里用一段固定字节代表它上次 check 时的内容，模拟真实的已检查状态。
    meta_bytes = b"# metadata-only fixture content, never stored to disk\n"
    lock_doc = {
        "merge_id": MERGE_ID,
        "generated_at": "2026-01-01T00:00:00Z",
        "sources": {
            FULL_TEXT_ID: _lock_entry(
                commit=COMMIT,
                content=old_bytes,
                stored_path=f"merges/{MERGE_ID}/snapshots/{FULL_TEXT_ID}/SKILL.source.md",
            ),
            META_ID: _lock_entry(commit=COMMIT, content=meta_bytes, stored_path=None),
        },
    }
    dump_json(lock_doc, repo_paths.lock_json(MERGE_ID))


def test_validate_passes_without_decisions_yaml(repo_paths):
    _build_merge(repo_paths)
    assert not repo_paths.decisions_yaml(MERGE_ID).exists()
    assert not repo_paths.work_dir(MERGE_ID).exists()

    rep = validate(repo_paths, merge_id=MERGE_ID, branch="feature", check_upstream_anchors=False)

    assert not rep.failed(), rep.render_text()
    assert any("没有 decisions.yaml" in m for m in rep.oks)


def test_render_sources_md_without_decisions_yaml(repo_paths):
    _build_merge(repo_paths)

    md, active_without_evidence = render_sources_for_merge(repo_paths, MERGE_ID)

    # 没有 decisions.yaml 时没有"证据"概念，active_without_evidence 恒为空。
    assert active_without_evidence == []
    # active 的 full-text 来源进主表，去掉"支持的规则数、落地的规则数"两列。
    assert FULL_TEXT_ID in md
    assert "支持的规则数" not in md
    assert "落地的规则数" not in md
    # candidate 来源仍出现在"已登记、尚未合并"一节。
    assert META_ID in md


def test_pr_dry_run_without_decisions_yaml(repo_paths):
    _build_merge(repo_paths)
    new_content = (
        "---\nname: nodec-full\n---\n\n# NODEC Full\n\nUpdated line after upstream change.\n"
    ).encode("utf-8")
    client = FakeGitHubClient(
        {
            "fixture-owner/nodec-full": {
                "meta": {"stars": 5, "forks": 1},
                "branches": {"main": COMMIT},
                "files": {(COMMIT, "SKILL.md"): new_content},
            }
        }
    )

    result = run_pr(repo_paths, client, MERGE_ID, FULL_TEXT_ID, dry_run=True)

    assert result["idempotent"] is False
    body = result["body"]
    # 完整的上游 diff 代替了受影响规则表和 locate 输出，且没有反查 decisions.yaml。
    assert "## 上游 diff" in body
    assert "受影响规则" not in body
    assert "locate" not in body
    assert "decisions.yaml" not in body


def test_pr_dry_run_metadata_only_without_decisions_yaml(repo_paths):
    _build_merge(repo_paths)
    # metadata-only 来源：pr 不应该发起任何网络调用取原文，空 client 就够。
    client = FakeGitHubClient({})

    result = run_pr(repo_paths, client, MERGE_ID, META_ID, dry_run=True)

    assert result["idempotent"] is False
    body = result["body"]
    assert "原文声明" in body
    assert "upstream-monitor diff" in body
    assert "受影响规则" not in body
