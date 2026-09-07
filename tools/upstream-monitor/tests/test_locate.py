"""locate 对一个人造 diff 能列出受影响规则，并给出词面最接近的候选。"""
from upstream_monitor.locate import render_locate_markdown, rules_for_source
from upstream_monitor.yamlio import load_yaml

DIFF = """--- SKILL.md@old
+++ SKILL.md@new
@@ -1,3 +1,4 @@
 # Source A

 ## Anchor heading
+不得编造原文没有的事实、数字或引语，这一点必须遵守。
"""


def test_locate_lists_rules_referencing_source(repo_paths):
    decisions = load_yaml(repo_paths.decisions_yaml("humanizer-fixture"))
    rules = rules_for_source(decisions, "upstream-fixture-source-a")
    ids = {r["id"] for r in rules}
    assert ids == {"ALL-PROT-001", "ALL-P-001"}


def test_locate_narrows_by_anchor_and_ranks_by_similarity(repo_paths):
    decisions = load_yaml(repo_paths.decisions_yaml("humanizer-fixture"))
    candidate_rules = rules_for_source(decisions, "upstream-fixture-source-a")

    md = render_locate_markdown(
        "humanizer-fixture", "upstream-fixture-source-a", candidate_rules, decisions["rules"], DIFF
    )

    # hunk 的上下文行含 "## Anchor heading"，ALL-PROT-001 和 ALL-P-001 的证据锚点都是它，
    # 因此两条都应该出现在"受影响规则"里。
    assert "ALL-PROT-001" in md
    assert "受影响规则" in md
    # 新增行讲的是"不得编造事实"，词面上应该和 ALL-PROT-001 的 rule_summary 更接近，
    # 排进"词面最接近"表格。
    assert "词面最接近的规则" in md
    assert "ALL-PROT-001" in md.split("词面最接近的规则")[1]
