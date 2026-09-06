"""check 的四种结果：无变化、格式变化、内容变化、不可达。"""
from upstream_monitor.check import CHANGE_CONTENT, CHANGE_FORMAT, CHANGE_NO_CHANGE, CHANGE_UNREACHABLE, check_one_source
from upstream_monitor.github_client import FakeGitHubClient
from upstream_monitor.normalize import normalized_sha256, raw_sha256

REPO = "acme/example"
COMMIT_1 = "1" * 40
COMMIT_2 = "2" * 40

SOURCE = {
    "id": "upstream-acme-example",
    "source_type": "github-skill",
    "repository": REPO,
    "branch": "main",
    "paths": ["SKILL.md"],
    "license": "MIT",
}


def base_lock_entry(content: bytes, commit: str) -> dict:
    return {
        "last_seen_commit": commit,
        "last_processed_commit": None,
        "last_accepted_commit": None,
        "raw_sha256": raw_sha256(content),
        "normalized_sha256": normalized_sha256(content),
        "size": len(content),
        "line_count": content.count(b"\n"),
        "files": [
            {
                "original_path": "SKILL.md",
                "stored_path": None,
                "raw_sha256": raw_sha256(content),
                "normalized_sha256": normalized_sha256(content),
            }
        ],
        "stars_history": [{"observed_at": "2026-01-01T00:00:00Z", "value": 1}],
        "forks": 0,
        "installs": None,
        "last_checked_at": "2026-01-01T00:00:00Z",
        "last_change_key": None,
        "open_pr": None,
        "open_issue": None,
        "availability": "ok",
    }


def make_client(content: bytes, commit: str) -> FakeGitHubClient:
    return FakeGitHubClient(
        {
            REPO: {
                "meta": {"stars": 42, "forks": 3},
                "branches": {"main": commit},
                "files": {(commit, "SKILL.md"): content},
            }
        }
    )


def test_no_change_when_commit_and_raw_hash_unchanged():
    content = b"# hello\nworld\n"
    client = make_client(content, COMMIT_1)
    entry = base_lock_entry(content, COMMIT_1)

    new_entry, result = check_one_source(client, SOURCE, entry, now="2026-02-01T00:00:00Z")

    assert result["change"] == CHANGE_NO_CHANGE
    assert new_entry["last_seen_commit"] == COMMIT_1
    assert new_entry["forks"] == 3
    assert len(new_entry["stars_history"]) == 2


def test_format_change_when_only_whitespace_differs():
    old_content = b"# hello\nworld\n"
    new_content = b"# hello   \r\nworld\r\n"  # 只有 CRLF 和行尾空白变了
    client = make_client(new_content, COMMIT_2)
    entry = base_lock_entry(old_content, COMMIT_1)

    new_entry, result = check_one_source(client, SOURCE, entry, now="2026-02-01T00:00:00Z")

    assert result["change"] == CHANGE_FORMAT
    assert new_entry["raw_sha256"] != entry["raw_sha256"]
    assert new_entry["normalized_sha256"] == entry["normalized_sha256"]


def test_content_change_when_normalized_hash_differs():
    old_content = b"# hello\nworld\n"
    new_content = b"# hello\nthere\n"
    client = make_client(new_content, COMMIT_2)
    entry = base_lock_entry(old_content, COMMIT_1)

    new_entry, result = check_one_source(client, SOURCE, entry, now="2026-02-01T00:00:00Z")

    assert result["change"] == CHANGE_CONTENT
    assert new_entry["normalized_sha256"] != entry["normalized_sha256"]


def test_unreachable_when_file_missing():
    content = b"# hello\nworld\n"
    entry = base_lock_entry(content, COMMIT_1)
    client = FakeGitHubClient(
        {
            REPO: {
                "meta": {"stars": 42, "forks": 3},
                "branches": {"main": COMMIT_2},
                "files": {},  # SKILL.md 在新 commit 下 404
            }
        }
    )

    new_entry, result = check_one_source(client, SOURCE, entry, now="2026-02-01T00:00:00Z")

    assert result["change"] == CHANGE_UNREACHABLE
    assert new_entry["availability"] == "unreachable"
