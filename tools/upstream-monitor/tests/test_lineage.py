"""lineage 的聚类和阈值：三段人造文本，两段近似、一段独立。"""
from upstream_monitor.lineage import load_relations, run_lineage
from upstream_monitor.schemas import SchemaValidationError
from upstream_monitor.yamlio import dump_yaml, load_yaml

MERGE_ID = "lineage-fixture"

TEXT_BASE = """# Demo Skill

## Section One

Pattern one: keep sentences varied in length, do not repeat the same shape.

## Section Two

Pattern two: avoid repeating the same connector words across paragraphs.

## Section Three

Pattern three: cite only facts already present in the source draft.
"""

TEXT_NEAR_DUP = """# Demo Skill

## Section One

Pattern one: keep sentences varied in length, do not repeat the same shape.

## Section Two

Pattern two: avoid repeating the same connector words across paragraphs.

## Section Three

Pattern three: cite only facts already present in the source draft, verified twice.
"""

TEXT_DIFFERENT = """# Recipe Notes

## Ingredients

Two cups of flour, one egg, a pinch of salt, and warm water.

## Steps

Mix the dry ingredients first, then fold in the egg and water slowly.
"""


def _source(sid: str, repo: str, lineage: str, snapshot_policy: str = "full-text") -> dict:
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
        "status": "candidate",
        "selection_status": "representative",
        "lineage": lineage,
        "tracking_revision": 1,
        "previous_paths": [],
        "path_changed_at": None,
        "baseline_reset_reason": None,
        "status_changed_at": "2026-01-01T00:00:00Z",
        "reason": "pytest 夹具。",
        "notes": None,
    }


def _build_merge(repo_paths, extra_sources=None):
    """在 repo_paths（临时仓库副本）里新建一个 merge 实例，三个来源：
    a（基线）、b（近似改写，应与 a 同簇）、c（完全独立，应保持单例）。
    """
    merge_dir = repo_paths.merge_dir(MERGE_ID)
    snapshots = repo_paths.snapshots_dir(MERGE_ID)

    sources = [
        _source("upstream-demo-a", "demo-owner/a", "upstream-demo-a"),
        _source("upstream-demo-b", "demo-owner/b", "upstream-demo-b"),
        _source("upstream-demo-c", "demo-owner/c", "upstream-demo-c"),
    ]
    if extra_sources:
        sources.extend(extra_sources)

    doc = {"merge_id": MERGE_ID, "target_skill": MERGE_ID, "sources": sources}
    dump_yaml(doc, repo_paths.sources_yaml(MERGE_ID))

    for sid, text in [
        ("upstream-demo-a", TEXT_BASE),
        ("upstream-demo-b", TEXT_NEAR_DUP),
        ("upstream-demo-c", TEXT_DIFFERENT),
    ]:
        d = snapshots / sid
        d.mkdir(parents=True, exist_ok=True)
        (d / "SKILL.source.md").write_text(text, encoding="utf-8")

    return merge_dir


def test_clusters_near_duplicate_pair_at_default_threshold(repo_paths):
    _build_merge(repo_paths)

    result = run_lineage(repo_paths, MERGE_ID)

    multi = [m for m in result["clusters"] if len(m) > 1]
    assert multi == [["upstream-demo-a", "upstream-demo-b"]]
    singles = {m[0] for m in result["clusters"] if len(m) == 1}
    assert singles == {"upstream-demo-c"}
    assert result["written"] is False


def test_high_threshold_keeps_near_duplicates_apart(repo_paths):
    _build_merge(repo_paths)

    result = run_lineage(repo_paths, MERGE_ID, threshold=0.99)

    assert all(len(m) == 1 for m in result["clusters"])


def test_metadata_only_source_is_skipped_not_crashed(repo_paths):
    extra = [_source("upstream-demo-d", "demo-owner/d", "upstream-demo-d", snapshot_policy="metadata-only")]
    _build_merge(repo_paths, extra_sources=extra)

    result = run_lineage(repo_paths, MERGE_ID)

    assert result["skipped"]["upstream-demo-d"] == "metadata-only，无快照可比，跳过"
    assert result["sources_count"] == 4
    assert result["texts_count"] == 3


def test_write_sets_shared_lineage_and_validates_schema(repo_paths):
    _build_merge(repo_paths)

    result = run_lineage(repo_paths, MERGE_ID, write=True)

    assert result["written"] is True
    after = load_yaml(repo_paths.sources_yaml(MERGE_ID))
    by_id = {s["id"]: s for s in after["sources"]}
    # a、b 同簇，写回同一个 lineage 值（簇内字典序最小的 id）。
    assert by_id["upstream-demo-a"]["lineage"] == "upstream-demo-a"
    assert by_id["upstream-demo-b"]["lineage"] == "upstream-demo-a"
    # c 是单例，lineage 不受影响地写成自身 id。
    assert by_id["upstream-demo-c"]["lineage"] == "upstream-demo-c"
    # selection_status 不受 lineage 聚类影响。
    assert all(s["selection_status"] == "representative" for s in after["sources"])


def test_known_relation_merges_otherwise_unrelated_sources(repo_paths, tmp_path):
    _build_merge(repo_paths)
    relations_path = tmp_path / "lineage-relations.yaml"
    dump_yaml(
        [
            {
                "from": "upstream-demo-a",
                "to": "upstream-demo-c",
                "relation": "fork",
                "evidence": "人工核实：c 是 a 的 GitHub fork（测试夹具）。",
            }
        ],
        relations_path,
    )

    result = run_lineage(repo_paths, MERGE_ID, relations_path=relations_path)

    multi = [sorted(m) for m in result["clusters"] if len(m) > 1]
    assert sorted(multi) == [
        ["upstream-demo-a", "upstream-demo-b", "upstream-demo-c"],
    ]
    assert result["applied_relations"][0]["relation"] == "fork"


def test_missing_relations_file_returns_empty_list(tmp_path):
    assert load_relations(tmp_path / "does-not-exist.yaml") == []


def test_unknown_relation_kind_raises(tmp_path):
    relations_path = tmp_path / "lineage-relations.yaml"
    dump_yaml(
        [{"from": "a", "to": "b", "relation": "not-a-real-kind", "evidence": "x"}],
        relations_path,
    )
    try:
        load_relations(relations_path)
        assert False, "应当抛出 ValueError"
    except ValueError as e:
        assert "not-a-real-kind" in str(e)


def test_write_with_invalid_source_type_fails_schema(repo_paths):
    _build_merge(repo_paths)
    doc = load_yaml(repo_paths.sources_yaml(MERGE_ID))
    doc["sources"][0]["status"] = "not-a-real-status"
    dump_yaml(doc, repo_paths.sources_yaml(MERGE_ID))

    try:
        run_lineage(repo_paths, MERGE_ID, write=True)
        assert False, "应当抛出 SchemaValidationError"
    except SchemaValidationError:
        pass
