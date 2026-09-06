"""`upstream-monitor retire` 的实现。

把来源状态改成 removed，记 status_changed_at 和 reason；然后从
decisions.yaml 算出只有这一个来源支持的规则，只输出清单，不改
decisions.yaml——规则是否跟着撤下是 skill-merge 的语义决定，不是这里的事。
"""
from __future__ import annotations

from upstream_monitor.check import now_iso
from upstream_monitor.paths import RepoPaths
from upstream_monitor.schemas import validate_doc
from upstream_monitor.yamlio import dump_yaml, load_yaml


def rules_only_supported_by(decisions: dict, source_id: str) -> list[dict]:
    out = []
    for r in decisions["rules"]:
        ids = {ev["source_id"] for ev in r["sources"]}
        if ids == {source_id}:
            out.append(r)
    return out


def run_retire(paths: RepoPaths, merge_id: str, source_id: str, reason: str) -> list[dict]:
    sources_path = paths.sources_yaml(merge_id)
    S = load_yaml(sources_path)
    source = next((s for s in S["sources"] if s["id"] == source_id), None)
    if source is None:
        raise KeyError(f"{merge_id}: 找不到来源 {source_id}")

    now = now_iso()
    source["status"] = "removed"
    source["status_changed_at"] = now
    source["reason"] = reason

    validate_doc(paths.schemas_dir, "sources", S, target=str(sources_path))
    dump_yaml(S, sources_path)

    decisions = load_yaml(paths.decisions_yaml(merge_id))
    return rules_only_supported_by(decisions, source_id)


def render_retire_markdown(merge_id: str, source_id: str, affected: list[dict]) -> str:
    lines = [
        f"# retire: {merge_id} / {source_id}",
        "",
        "来源状态已改为 removed。以下规则只有这一个来源支持，"
        "是否跟着撤下由 skill-merge 另做决定：",
        "",
        "| 规则 id | decision | local.skill | local.path | local.anchor |",
        "|---|---|---|---|---|",
    ]
    for r in affected:
        lines.append(
            f"| {r['id']} | {r['decision']} | {r['local']['skill']} | "
            f"{r['local']['path']} | {r['local']['anchor']} |"
        )
    if not affected:
        lines.append("| （无） | | | | |")
    lines.append("")
    return "\n".join(lines)
