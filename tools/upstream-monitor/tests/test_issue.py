"""issue 的幂等和正文不含上游原文。"""
import json

from upstream_monitor.issue import FakeGhIssueClient, render_issue_body, run_issue
from upstream_monitor.yamlio import load_json

MERGE_ID = "humanizer-fixture"
UPSTREAM_SNIPPET = (
    "Some sample content demonstrating protection ideas: never invent a fact,"
)


def test_issue_does_not_reopen_when_open_issue_still_open(repo_paths):
    lock_path = repo_paths.lock_json(MERGE_ID)
    lock = load_json(lock_path)
    lock["sources"]["upstream-fixture-source-a"]["open_issue"] = 7
    lock_path.write_text(json.dumps(lock), encoding="utf-8")

    client = FakeGhIssueClient(issues={7: "OPEN"})

    result = run_issue(
        repo_paths, client, MERGE_ID, "upstream-fixture-source-a", "source-unavailable"
    )

    assert result["idempotent"] is True
    assert result["issue_number"] == 7
    assert client.created_issues == []

    after = load_json(lock_path)
    assert after["sources"]["upstream-fixture-source-a"]["open_issue"] == 7


def test_issue_reopens_when_previous_issue_is_closed(repo_paths):
    lock_path = repo_paths.lock_json(MERGE_ID)
    lock = load_json(lock_path)
    lock["sources"]["upstream-fixture-source-a"]["open_issue"] = 7
    lock_path.write_text(json.dumps(lock), encoding="utf-8")

    client = FakeGhIssueClient(issues={7: "CLOSED"})

    result = run_issue(
        repo_paths, client, MERGE_ID, "upstream-fixture-source-a", "source-unavailable"
    )

    assert result["idempotent"] is False
    assert len(client.created_issues) == 1
    created = client.created_issues[0]
    assert set(created["labels"]) == {f"upstream:{MERGE_ID}", "source-unavailable"}
    # 首次调用时标签不存在，应当先建标签。
    assert set(client.created_labels) == {f"upstream:{MERGE_ID}", "source-unavailable"}

    after = load_json(lock_path)
    assert after["sources"]["upstream-fixture-source-a"]["open_issue"] == created["number"]


def test_issue_does_not_create_label_when_it_already_exists(repo_paths):
    client = FakeGhIssueClient(labels={f"upstream:{MERGE_ID}", "needs-decision"})

    run_issue(repo_paths, client, MERGE_ID, "upstream-fixture-source-a", "needs-decision")

    assert client.created_labels == []


def test_dry_run_only_renders_body_without_any_gh_call(repo_paths):
    lock_path = repo_paths.lock_json(MERGE_ID)
    lock = load_json(lock_path)
    lock["sources"]["upstream-fixture-source-a"]["open_issue"] = 7
    lock_path.write_text(json.dumps(lock), encoding="utf-8")

    # 空 client：如果 dry-run 意外发起了任何 gh 调用，下面的方法都会因为没有
    # 预置状态而返回“看似正常但错误”的默认值，用 created_* 断言能抓到误调用。
    client = FakeGhIssueClient()

    result = run_issue(
        repo_paths,
        client,
        MERGE_ID,
        "upstream-fixture-source-a",
        "source-unavailable",
        dry_run=True,
    )

    assert result["dry_run"] is True
    assert "body" in result
    assert client.created_issues == []
    assert client.created_labels == []

    after = load_json(lock_path)
    assert after["sources"]["upstream-fixture-source-a"]["open_issue"] == 7  # 未被改动


def test_body_does_not_contain_upstream_raw_text(repo_paths):
    client = FakeGhIssueClient()

    result = run_issue(
        repo_paths, client, MERGE_ID, "upstream-fixture-source-a", "source-unavailable", dry_run=True
    )

    assert UPSTREAM_SNIPPET not in result["body"]
    # 但事实字段（source_id、repository、commit、hash、stars）应当都在。
    assert "upstream-fixture-source-a" in result["body"]
    assert "fixture-owner/source-a" in result["body"]
    assert "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" in result["body"]


def test_needs_decision_body_attaches_locate_output_without_raw_text(repo_paths):
    client = FakeGhIssueClient()

    result = run_issue(
        repo_paths, client, MERGE_ID, "upstream-fixture-source-a", "needs-decision", dry_run=True
    )

    assert UPSTREAM_SNIPPET not in result["body"]
    assert "ALL-PROT-001" in result["body"]  # 引用 source-a 的规则出现在受影响清单里
    assert "EN-S-001" not in result["body"]  # 只由 source-b 支持，不应出现


def test_retire_impact_body_attaches_retire_output(repo_paths):
    client = FakeGhIssueClient()

    result = run_issue(
        repo_paths, client, MERGE_ID, "upstream-fixture-source-b", "retire-impact", dry_run=True
    )

    assert UPSTREAM_SNIPPET not in result["body"]
    # EN-S-001 只由 source-b 支持，应当出现在 retire-impact 的影响范围里。
    assert "EN-S-001" in result["body"]
    assert "ALL-P-001" not in result["body"]  # 由 source-a 和 source-b 共同支持，不是唯一来源


def test_render_issue_body_uses_custom_detail():
    source = {"id": "upstream-x-y", "repository": "x/y", "paths": ["SKILL.md"]}
    body = render_issue_body("new-candidate", "m", source, None, None, "自定义决定说明")
    assert "自定义决定说明" in body
