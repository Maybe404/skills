"""渲染 skills/<id>/SOURCES.md，以及 catalog 的 README 表格。

SOURCES.md 部分从 prototype/render_sources.py 移植，逻辑不变。
"""
from __future__ import annotations

import datetime
import re
from pathlib import Path
from typing import Any

from upstream_monitor.paths import RepoPaths
from upstream_monitor.yamlio import load_json, load_yaml

LANDED_DECISIONS = {"adopted", "adopted-with-modification"}

DECISION_LABELS = {
    "adopted": "adopted（采用）",
    "adopted-with-modification": "adopted-with-modification（改写后采用）",
    "duplicate": "duplicate（重复）",
    "rejected": "rejected（不采用）",
    "deferred": "deferred（暂缓）",
    "reference-only": "reference-only（仅供参考）",
    "unverified": "unverified（未核实）",
    "retired": "retired（已撤回）",
}

KIND_LABELS = {
    "original": "original",
    "adapted": "adapted",
    "aggregated": "aggregated",
}

STATUS_LABELS = {
    "active": "可用",
    "planned": "计划中",
    "archived": "已停用",
}


def compute_source_stats(sources_doc: dict, decisions_doc: dict) -> dict[str, dict]:
    source_ids = [s["id"] for s in sources_doc.get("sources", [])]
    stats: dict[str, dict] = {sid: {"total": 0, "landed": 0, "by_decision": {}} for sid in source_ids}

    for rule in decisions_doc.get("rules", []):
        rule_id = rule["id"]
        decision = rule.get("decision")
        referenced = {
            src["source_id"]
            for src in rule.get("sources", [])
            if src.get("type") == "upstream" and src.get("source_id") in stats
        }
        for sid in referenced:
            stats[sid]["total"] += 1
            if decision in LANDED_DECISIONS:
                stats[sid]["landed"] += 1
            stats[sid]["by_decision"].setdefault(decision, []).append(rule_id)

    for sid in stats:
        for decision in stats[sid]["by_decision"]:
            stats[sid]["by_decision"][decision].sort()

    return stats


def read_license_text(snapshots_dir: Path, source_id: str) -> str | None:
    license_path = snapshots_dir / source_id / "LICENSE"
    if not license_path.exists():
        return None
    return license_path.read_text(encoding="utf-8")


def extract_copyright_author(license_text: str) -> str | None:
    m = re.search(r"^Copyright \(c\) \d{4}[a-z, ]*\s+(.+)$", license_text, re.MULTILINE)
    return m.group(1).strip() if m else None


def repo_link(repository: str) -> str:
    return f"[{repository}](https://github.com/{repository})"


def decision_label(decision: str) -> str:
    return DECISION_LABELS.get(decision, decision)


def render_source_table(sources_doc: dict, stats: dict[str, dict]) -> str:
    rows = [
        "| id | repository | branch | license | snapshot_policy | lineage | "
        "selection_status | 支持的规则数 | 落地的规则数 |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for s in sources_doc.get("sources", []):
        if s.get("status") == "removed":
            continue
        sid = s["id"]
        st = stats.get(sid, {"total": 0, "landed": 0})
        license_cell = s["license"]
        if s["license"] == "unknown":
            license_cell = "unknown（未取得许可证，本仓库不含其原文）"
        rows.append(
            "| {id} | {repo} | {branch} | {license} | {policy} | {lineage} | "
            "{selection} | {total} | {landed} |".format(
                id=sid,
                repo=repo_link(s["repository"]),
                branch=s["branch"],
                license=license_cell,
                policy=s["snapshot_policy"],
                lineage=s["lineage"],
                selection=s["selection_status"],
                total=st["total"],
                landed=st["landed"],
            )
        )
    return "\n".join(rows)


def render_rule_list_by_decision(by_decision: dict[str, list[str]]) -> str:
    if not by_decision:
        return "（没有规则引用这个来源）"
    lines = []
    for decision in sorted(by_decision.keys()):
        rule_ids = by_decision[decision]
        lines.append(f"- {decision_label(decision)}：{', '.join(rule_ids)}")
    return "\n".join(lines)


def render_full_text_section(s: dict, stats_entry: dict, snapshots_dir: Path, merge_id: str) -> str:
    sid = s["id"]
    license_text = read_license_text(snapshots_dir, sid)
    if license_text is None:
        raise FileNotFoundError(f"snapshot_policy 是 full-text，但找不到 LICENSE：{sid}")
    author = extract_copyright_author(license_text) or "未知"
    lines = [
        f"### {sid}",
        "",
        f"- 作者：{author}",
        f"- 仓库：{repo_link(s['repository'])}",
        f"- 许可证：{s['license']}",
        "",
        "许可声明原文（逐字节照抄自 "
        f"`merges/{merge_id}/snapshots/{sid}/LICENSE`）：",
        "",
        "```",
        license_text.rstrip("\n"),
        "```",
        "",
        "支持的规则，按 decision 分组：",
        "",
        render_rule_list_by_decision(stats_entry["by_decision"]),
    ]
    return "\n".join(lines)


def render_metadata_only_section(s: dict, stats_entry: dict) -> str:
    sid = s["id"]
    lines = [
        f"### {sid}",
        "",
        f"- 仓库：{repo_link(s['repository'])}",
        "- 许可证：未知，未取得许可证，本仓库不含其原文。",
        (
            "- 本来源按 metadata-only 处理：只记录了追踪文件的 commit 和哈希，"
            "不保存原文；它支持的规则都是用自己的话重写的，不引用原文的例句、"
            "词表条目或措辞。"
        ),
        "",
        "支持的规则，按 decision 分组：",
        "",
        render_rule_list_by_decision(stats_entry["by_decision"]),
    ]
    return "\n".join(lines)


def render_removed_section(sources_doc: dict) -> str:
    removed = [s for s in sources_doc.get("sources", []) if s.get("status") == "removed"]
    if not removed:
        return "无。"
    lines = []
    for s in removed:
        lines.append(
            f"- {s['id']}（{repo_link(s['repository'])}）："
            f"于 {s.get('status_changed_at', '未知时间')} 移除，"
            f"原因：{s.get('reason', '未记录')}"
        )
    return "\n".join(lines)


def render_sources_md(
    sources_doc: dict,
    decisions_doc: dict,
    snapshots_dir: Path,
    generated_at: str | None = None,
) -> str:
    stats = compute_source_stats(sources_doc, decisions_doc)
    target_skill = sources_doc.get("target_skill", sources_doc.get("merge_id"))
    merge_id = sources_doc.get("merge_id")

    parts: list[str] = [
        f"# {target_skill} 来源",
        "",
        (
            f"`skills/{target_skill}/` 正文是对下列来源的重写，不是上游内容的转载。"
            "上游各来源的著作权归各自作者所有。"
        ),
        "",
        "## 来源表",
        "",
        render_source_table(sources_doc, stats),
        "",
        "## 各来源详情",
        "",
    ]
    for s in sources_doc.get("sources", []):
        if s.get("status") == "removed":
            continue
        sid = s["id"]
        entry = stats.get(sid, {"total": 0, "landed": 0, "by_decision": {}})
        if s["snapshot_policy"] == "full-text":
            parts.append(render_full_text_section(s, entry, snapshots_dir, merge_id))
        else:
            parts.append(render_metadata_only_section(s, entry))
        parts.append("")

    parts.append("## 已移除的来源")
    parts.append("")
    parts.append(render_removed_section(sources_doc))
    parts.append("")

    parts.append("## 生成信息")
    parts.append("")
    ts = generated_at or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    parts.append(f"- 渲染时间：{ts}")
    parts.append(
        f"- 渲染依据：`merges/{merge_id}/decisions.yaml`（{len(decisions_doc.get('rules', []))} 条规则）"
        f"与 `merges/{merge_id}/sources.yaml`（{len(sources_doc.get('sources', []))} 个来源）。"
    )
    parts.append("")
    parts.append("本文件由脚本从 decisions.yaml 和 sources.yaml 生成，不要手工编辑。")
    parts.append("")

    return "\n".join(parts)


def render_sources_for_merge(paths: RepoPaths, merge_id: str, out_path: Path | None = None) -> str:
    sources_doc = load_yaml(paths.sources_yaml(merge_id))
    decisions_doc = load_yaml(paths.decisions_yaml(merge_id))
    lock_path = paths.lock_json(merge_id)
    generated_at = None
    if lock_path.exists():
        generated_at = load_json(lock_path).get("generated_at")

    md = render_sources_md(sources_doc, decisions_doc, paths.snapshots_dir(merge_id), generated_at)

    target = out_path or (paths.skills_dir / sources_doc["target_skill"] / "SOURCES.md")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(md, encoding="utf-8")
    return md


def render_readme_table(paths: RepoPaths) -> str:
    """从 catalog/ 渲染供 README 引用的 skill 表格，不写 README。"""
    rows = [
        "| id | 类型 | 名称 | 状态 |",
        "|---|---|---|---|",
    ]
    for cf in paths.catalog_entries():
        doc = load_yaml(cf)
        skill_id = doc["id"]
        link = f"[`{skill_id}`]({doc['path']}/SKILL.md)"
        rows.append(
            "| {link} | {kind} | {name} | {status} |".format(
                link=link,
                kind=KIND_LABELS.get(doc["kind"], doc["kind"]),
                name=doc["name"],
                status=STATUS_LABELS.get(doc["status"], doc["status"]),
            )
        )
    return "\n".join(rows) + "\n"
