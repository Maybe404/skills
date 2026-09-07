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
    # The name has to sit on the same line as the year; a bare "Copyright (c) 2026"
    # line yields None instead of swallowing the next paragraph of the license.
    m = re.search(
        r"^Copyright \(c\) \d{4}(?:\s*[-–,]\s*(?:\d{4}|present))*[ \t]+(\S.*)$",
        license_text,
        re.MULTILINE | re.IGNORECASE,
    )
    return m.group(1).strip() if m else None


def repo_link(repository: str) -> str:
    return f"[{repository}](https://github.com/{repository})"


def decision_label(decision: str) -> str:
    return DECISION_LABELS.get(decision, decision)


def classify_sources(
    sources_doc: dict, stats: dict[str, dict], has_decisions: bool = True
) -> dict[str, list[dict]]:
    """把 sources.yaml 的来源按主表/未合并/已移除三节分组。

    有 decisions.yaml 时（has_decisions=True）：

    - main：status 为 active，且在 decisions.yaml 里至少有一条证据。
    - unmerged：status 为 candidate 或 paused；或 status 为 active 但没有任何
      证据（这种情况额外记入 active_without_evidence，供调用方提醒）。
    - removed：status 为 removed，不变。

    没有 decisions.yaml 时（has_decisions=False），没有证据数据可判断，主表
    改为直接按 status 分：active 进主表，其余（candidate、paused 等）进
    "已登记、尚未合并"；active_without_evidence 恒为空。
    """
    main: list[dict] = []
    unmerged: list[dict] = []
    removed: list[dict] = []
    active_without_evidence: list[dict] = []
    for s in sources_doc.get("sources", []):
        status = s.get("status")
        if status == "removed":
            removed.append(s)
            continue
        if not has_decisions:
            if status == "active":
                main.append(s)
            else:
                unmerged.append(s)
            continue
        has_evidence = stats.get(s["id"], {"total": 0})["total"] > 0
        if status == "active" and has_evidence:
            main.append(s)
        elif status == "active":
            unmerged.append(s)
            active_without_evidence.append(s)
        else:
            # candidate、paused，以及 schema 允许但此处未枚举的其他状态，
            # 一律保守放进"已登记、尚未合并"一节，不静默丢弃。
            unmerged.append(s)
    return {
        "main": main,
        "unmerged": unmerged,
        "removed": removed,
        "active_without_evidence": active_without_evidence,
    }


def render_source_table(sources: list[dict], stats: dict[str, dict], has_decisions: bool = True) -> str:
    header_cols = ["id", "repository", "branch", "license", "snapshot_policy", "lineage", "selection_status"]
    if has_decisions:
        header_cols += ["支持的规则数", "落地的规则数"]
    rows = [
        "| " + " | ".join(header_cols) + " |",
        "|" + "---|" * len(header_cols),
    ]
    for s in sources:
        sid = s["id"]
        st = stats.get(sid, {"total": 0, "landed": 0})
        license_cell = s["license"]
        if s["license"] == "unknown":
            license_cell = "unknown（未取得许可证，本仓库不含其原文）"
        cells = [
            sid,
            repo_link(s["repository"]),
            s["branch"],
            license_cell,
            s["snapshot_policy"],
            s["lineage"],
            s["selection_status"],
        ]
        if has_decisions:
            cells += [str(st["total"]), str(st["landed"])]
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join(rows)


def render_unmerged_source_table(sources: list[dict]) -> str:
    if not sources:
        return "无。"
    rows = [
        "| id | repository | license | snapshot_policy | selection_status |",
        "|---|---|---|---|---|",
    ]
    for s in sources:
        license_cell = s["license"]
        if s["license"] == "unknown":
            license_cell = "unknown（未取得许可证，本仓库不含其原文）"
        rows.append(
            "| {id} | {repo} | {license} | {policy} | {selection} |".format(
                id=s["id"],
                repo=repo_link(s["repository"]),
                license=license_cell,
                policy=s["snapshot_policy"],
                selection=s["selection_status"],
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
    has_decisions: bool = True,
) -> str:
    stats = compute_source_stats(sources_doc, decisions_doc)
    groups = classify_sources(sources_doc, stats, has_decisions=has_decisions)
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
        render_source_table(groups["main"], stats, has_decisions=has_decisions),
        "",
        "## 已登记、尚未合并",
        "",
        "这些来源已登记并被监控，规则尚未合并进本 skill。",
        "",
        render_unmerged_source_table(groups["unmerged"]),
        "",
        "## 各来源详情",
        "",
    ]
    for s in groups["main"]:
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
    if has_decisions:
        parts.append(
            f"- 渲染依据：`merges/{merge_id}/decisions.yaml`（{len(decisions_doc.get('rules', []))} 条规则）"
            f"与 `merges/{merge_id}/sources.yaml`（{len(sources_doc.get('sources', []))} 个来源）。"
        )
    else:
        parts.append(
            f"- 渲染依据：`merges/{merge_id}/sources.yaml`（{len(sources_doc.get('sources', []))} 个来源）；"
            "当前实例没有 decisions.yaml，不含规则统计。"
        )
    parts.append("")
    parts.append("本文件由脚本从 decisions.yaml 和 sources.yaml 生成，不要手工编辑。")
    parts.append("")

    return "\n".join(parts)


def render_sources_for_merge(
    paths: RepoPaths, merge_id: str, out_path: Path | None = None
) -> tuple[str, list[str]]:
    """渲染 SOURCES.md，返回 (markdown, active_without_evidence)。

    active_without_evidence 是 status 为 active 但 decisions.yaml 里没有任何
    证据引用的来源 id 列表——这些来源被放进了"已登记、尚未合并"一节，调用方
    （cli）据此提醒使用者核对 sources.yaml 里的 status。没有 decisions.yaml
    的实例（以后的 merge 实例都不再产出这份文件）恒为空列表，主表直接按
    status 分（active 进主表），不再区分"有没有证据"。
    """
    sources_doc = load_yaml(paths.sources_yaml(merge_id))
    decisions_path = paths.decisions_yaml(merge_id)
    has_decisions = decisions_path.exists()
    decisions_doc = load_yaml(decisions_path) if has_decisions else {"merge_id": merge_id, "rules": []}
    lock_path = paths.lock_json(merge_id)
    generated_at = None
    if lock_path.exists():
        generated_at = load_json(lock_path).get("generated_at")

    stats = compute_source_stats(sources_doc, decisions_doc)
    groups = classify_sources(sources_doc, stats, has_decisions=has_decisions)
    active_without_evidence = [s["id"] for s in groups["active_without_evidence"]]

    md = render_sources_md(
        sources_doc,
        decisions_doc,
        paths.snapshots_dir(merge_id),
        generated_at,
        has_decisions=has_decisions,
    )

    target = out_path or (paths.skills_dir / sources_doc["target_skill"] / "SOURCES.md")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(md, encoding="utf-8")
    return md, active_without_evidence


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
