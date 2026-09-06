"""approve 只改指定规则的 decision_origin，history 和 decided_at 不动。"""
from upstream_monitor.approve import rule_ids_from_pr_diff, run_approve
from upstream_monitor.yamlio import dump_yaml, load_yaml

MERGE_ID = "humanizer-fixture"


def _set_all_model_proposed(repo_paths):
    doc = load_yaml(repo_paths.decisions_yaml(MERGE_ID))
    for r in doc["rules"]:
        r["decision_origin"] = "model-proposed"
    dump_yaml(doc, repo_paths.decisions_yaml(MERGE_ID))
    return doc


def test_approve_with_explicit_rule_list_only_changes_those(repo_paths):
    before = _set_all_model_proposed(repo_paths)
    before_by_id = {r["id"]: r for r in before["rules"]}

    changed = run_approve(repo_paths, MERGE_ID, rules=["ALL-PROT-001"])

    assert changed == ["ALL-PROT-001"]
    after = load_yaml(repo_paths.decisions_yaml(MERGE_ID))
    after_by_id = {r["id"]: r for r in after["rules"]}

    assert after_by_id["ALL-PROT-001"]["decision_origin"] == "human-approved"
    assert after_by_id["ALL-P-001"]["decision_origin"] == "model-proposed"
    assert after_by_id["EN-S-001"]["decision_origin"] == "model-proposed"

    # history 和 decided_at 不动。
    for rid in before_by_id:
        assert after_by_id[rid]["decided_at"] == before_by_id[rid]["decided_at"]
        assert after_by_id[rid]["history"] == before_by_id[rid]["history"]
        assert after_by_id[rid]["decision_revision"] == before_by_id[rid]["decision_revision"]


def test_approve_without_filter_changes_all_model_proposed(repo_paths):
    _set_all_model_proposed(repo_paths)

    changed = run_approve(repo_paths, MERGE_ID)

    assert set(changed) == {"ALL-PROT-001", "ALL-P-001", "EN-S-001"}
    after = load_yaml(repo_paths.decisions_yaml(MERGE_ID))
    assert all(r["decision_origin"] == "human-approved" for r in after["rules"])


def test_rule_ids_from_pr_diff_only_reads_added_lines():
    diff_text = (
        "--- a/decisions.yaml\n"
        "+++ b/decisions.yaml\n"
        "@@ -1,2 +1,3 @@\n"
        "-  id: ALL-P-001\n"
        "+  id: ALL-P-001\n"
        "+  id: EN-S-001\n"
    )
    assert rule_ids_from_pr_diff(diff_text) == {"ALL-P-001", "EN-S-001"}
