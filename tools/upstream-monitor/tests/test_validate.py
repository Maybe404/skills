"""validate 对一份故意坏掉的 decisions.yaml 报错：锚点不存在、source_id 不存在、
main 分支上有 model-proposed。"""
from upstream_monitor.validate import validate
from upstream_monitor.yamlio import dump_yaml, load_yaml

MERGE_ID = "humanizer-fixture"


def _load(repo_paths):
    return load_yaml(repo_paths.decisions_yaml(MERGE_ID))


def test_valid_fixture_passes(repo_paths):
    rep = validate(repo_paths, merge_id=MERGE_ID, branch="feature", check_upstream_anchors=False)
    assert not rep.failed(), rep.render_text()


def test_missing_local_anchor_is_blocked(repo_paths):
    doc = _load(repo_paths)
    doc["rules"][0]["local"]["anchor"] = "### 这个锚点在文件里根本不存在"
    dump_yaml(doc, repo_paths.decisions_yaml(MERGE_ID))

    rep = validate(repo_paths, merge_id=MERGE_ID, branch="feature", check_upstream_anchors=False)

    assert rep.failed()
    assert any("anchor" in m and "找不到" in m for m in rep.by_severity()["BLOCK"])


def test_nonexistent_source_id_is_blocked(repo_paths):
    doc = _load(repo_paths)
    doc["rules"][0]["sources"][0]["source_id"] = "upstream-does-not-exist"
    dump_yaml(doc, repo_paths.decisions_yaml(MERGE_ID))

    rep = validate(repo_paths, merge_id=MERGE_ID, branch="feature", check_upstream_anchors=False)

    assert rep.failed()
    assert any("source_id 不在 sources.yaml" in m for m in rep.by_severity()["BLOCK"])


def test_model_proposed_on_main_branch_is_blocked(repo_paths):
    doc = _load(repo_paths)
    doc["rules"][0]["decision_origin"] = "model-proposed"
    dump_yaml(doc, repo_paths.decisions_yaml(MERGE_ID))

    rep = validate(repo_paths, merge_id=MERGE_ID, branch="main", check_upstream_anchors=False)

    assert rep.failed()
    assert any("model-proposed" in m for m in rep.by_severity()["BLOCK"])


def test_model_proposed_on_non_main_branch_is_not_blocked_for_that_reason(repo_paths):
    doc = _load(repo_paths)
    doc["rules"][0]["decision_origin"] = "model-proposed"
    dump_yaml(doc, repo_paths.decisions_yaml(MERGE_ID))

    rep = validate(repo_paths, merge_id=MERGE_ID, branch="feature", check_upstream_anchors=False)

    assert not any("model-proposed" in m for m in rep.by_severity()["BLOCK"])


def test_shared_path_and_anchor_across_evidence_is_med(repo_paths):
    doc = _load(repo_paths)
    for r in doc["rules"]:
        if r["id"] == "ALL-P-001":
            # 两条证据本来分别指向 source-a、source-b 各自的 anchor；
            # 改成 path+anchor 完全相同，模拟“共用锚点没加各自行首文本”。
            r["sources"][1]["path"] = r["sources"][0]["path"]
            r["sources"][1]["anchor"] = r["sources"][0]["anchor"]
    dump_yaml(doc, repo_paths.decisions_yaml(MERGE_ID))

    rep = validate(repo_paths, merge_id=MERGE_ID, branch="feature", check_upstream_anchors=False)

    assert not rep.failed(), rep.render_text()
    assert any(
        "共用锚点要加各自行首文本" in m and "ALL-P-001" in m for m in rep.by_severity()["MED"]
    )


def test_rationale_mentions_rule_id_without_relation_entry_is_high(repo_paths):
    doc = _load(repo_paths)
    for r in doc["rules"]:
        if r["id"] == "ALL-P-001":
            r["rationale"] = r["rationale"] + " 与 ALL-PROT-001 互补，共同覆盖保护类与模式类要求。"
            # 故意不在 relations 里补上指向 ALL-PROT-001 的条目。
    dump_yaml(doc, repo_paths.decisions_yaml(MERGE_ID))

    rep = validate(repo_paths, merge_id=MERGE_ID, branch="feature", check_upstream_anchors=False)

    assert rep.failed()
    assert any(
        "rationale 提到与 ALL-PROT-001" in m and "relations 里没有指向" in m
        for m in rep.by_severity()["HIGH"]
    )


def test_rationale_mentions_rule_id_with_matching_relation_is_not_flagged(repo_paths):
    doc = _load(repo_paths)
    for r in doc["rules"]:
        if r["id"] == "ALL-P-001":
            r["rationale"] = r["rationale"] + " 与 ALL-PROT-001 互补，共同覆盖保护类与模式类要求。"
            r["relations"] = [{"type": "pairs-with", "rule_id": "ALL-PROT-001"}]
        if r["id"] == "ALL-PROT-001":
            r["relations"] = [{"type": "pairs-with", "rule_id": "ALL-P-001"}]
    dump_yaml(doc, repo_paths.decisions_yaml(MERGE_ID))

    rep = validate(repo_paths, merge_id=MERGE_ID, branch="feature", check_upstream_anchors=False)

    assert not any("rationale 提到与" in m for m in rep.by_severity()["HIGH"])


def test_ambiguous_upstream_anchor_is_med_not_block(repo_paths):
    doc = _load(repo_paths)
    # 去掉 EN-S-001：它和 ALL-P-001 一样引用 upstream-fixture-source-b:SKILL.md，
    # validate_upstream_anchors 对同一 (source_id, path) 的第二次查找会命中内部缓存，
    # 缓存只记"cached"这个通用理由、丢失了 metadata-only 的原始理由，导致误报 HIGH。
    # 这是 text_for() 缓存逻辑本身的问题，与本次要修的两个 anchors 缺陷无关，
    # 这里去掉这条规则只是为了不让本测试意外撞上它；该问题在报告的“未解决问题”里说明。
    doc["rules"] = [r for r in doc["rules"] if r["id"] != "EN-S-001"]
    for r in doc["rules"]:
        if r["id"] == "ALL-PROT-001":
            r["sources"][0]["anchor"] = "## Anchor heading / never invent a fact"
    dump_yaml(doc, repo_paths.decisions_yaml(MERGE_ID))

    snapshot = (
        repo_paths.root
        / "merges"
        / MERGE_ID
        / "snapshots"
        / "upstream-fixture-source-a"
        / "SKILL.source.md"
    )
    text = snapshot.read_text(encoding="utf-8")
    snapshot.write_text(
        text + "\nSome sample content demonstrating protection ideas: never invent a fact, again.\n",
        encoding="utf-8",
    )

    rep = validate(repo_paths, merge_id=MERGE_ID, branch="feature")

    assert not rep.failed(), rep.render_text()
    assert any("弱定位有歧义" in m for m in rep.by_severity()["MED"])


def test_gibberish_upstream_sub_anchor_is_high(repo_paths):
    doc = _load(repo_paths)
    for r in doc["rules"]:
        if r["id"] == "ALL-PROT-001":
            r["sources"][0]["anchor"] = "## Anchor heading / 这段胡说的子锚点在原文里不存在"
    dump_yaml(doc, repo_paths.decisions_yaml(MERGE_ID))

    rep = validate(repo_paths, merge_id=MERGE_ID, branch="feature")

    assert rep.failed()
    assert any("anchor 定位不到" in m for m in rep.by_severity()["HIGH"])
