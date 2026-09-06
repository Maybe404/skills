"""pr 的幂等：同一变更键第二次不重复开 PR。"""
import json

from upstream_monitor.github_client import FakeGitHubClient
from upstream_monitor.pr import change_key_for, run_pr


def test_pr_does_not_reopen_when_change_key_and_open_pr_match(repo_paths):
    merge_id = "humanizer-fixture"
    source_id = "upstream-fixture-source-a"
    lock_path = repo_paths.lock_json(merge_id)
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    entry = lock["sources"][source_id]

    change_key = change_key_for(source_id, ["SKILL.md"], entry["last_seen_commit"])
    entry["last_change_key"] = change_key
    entry["open_pr"] = 42
    lock_path.write_text(json.dumps(lock), encoding="utf-8")

    # 空 client：如果代码没有在幂等短路前返回，任何网络调用都会因为仓库不存在而报错。
    empty_client = FakeGitHubClient({})

    result = run_pr(repo_paths, empty_client, merge_id, source_id, dry_run=True)

    assert result["idempotent"] is True
    assert result["open_pr"] == 42
    assert result["change_key"] == change_key


def test_pr_would_open_when_change_key_differs(repo_paths):
    merge_id = "humanizer-fixture"
    source_id = "upstream-fixture-source-a"

    client = FakeGitHubClient(
        {
            "fixture-owner/source-a": {
                "meta": {"stars": 10, "forks": 1},
                "branches": {"main": "a" * 40},
                "files": {
                    ("a" * 40, "SKILL.md"): b"content",
                    (None, "SKILL.md"): b"content",
                },
            }
        }
    )
    # from_commit 为 None（尚无 last_accepted_commit）时 diff 直接跳过取旧版本。
    result = run_pr(repo_paths, client, merge_id, source_id, dry_run=True)

    assert result["idempotent"] is False
    assert "body" in result
    assert result["branch"].startswith(f"upstream-sync/")
