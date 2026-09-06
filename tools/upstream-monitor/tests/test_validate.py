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
