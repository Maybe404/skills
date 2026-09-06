#!/usr/bin/env python3
"""渲染 skills/<id>/SOURCES.md。

逻辑独立成函数，供 tools/upstream-monitor 的 render 命令以后直接复用：
- load_sources / load_decisions / load_lock：只做 YAML/JSON 解析。
- compute_source_stats：从 decisions.yaml 统计每个 source_id 支持的规则数
  和落地（adopted / adopted-with-modification）的规则数，按 decision 分组。
- render_license_block：从 snapshots/<source_id>/LICENSE 读取 MIT 全文，
  逐字节返回，不做任何改写。
- render_sources_md：把以上结果拼成 SOURCES.md 的正文。

用法：
    python3 render_sources.py \
        --sources merges/<id>/sources.yaml \
        --decisions merges/<id>/decisions.yaml \
        --lock merges/<id>/sources.lock.json \
        --snapshots-dir merges/<id>/snapshots \
        [--out skills/<id>/SOURCES.md]

不传 --out 时输出到 stdout。
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

LANDED_DECISIONS = {"adopted", "adopted-with-modification"}

# decisions.yaml 里出现的 decision 取值到中文标签的映射，仅用于分组标题，
# 不改变原始取值本身（原始取值仍然逐字打印在括号里）。
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


def load_yaml(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_sources(path: Path) -> dict:
    return load_yaml(path)


def load_decisions(path: Path) -> dict:
    return load_yaml(path)


def load_lock(path: Path) -> dict:
    return load_json(path)


def compute_source_stats(sources_doc: dict, decisions_doc: dict) -> dict[str, dict]:
    """按 source_id 统计支持的规则数、落地的规则数，以及按 decision 分组的规则 id 列表。

    一条规则的 sources[] 里可能重复出现同一个 source_id（例如同一来源的
    两处不同 anchor 都是这条规则的证据），这种情况只算一条规则，不重复计数。
    """
    source_ids = [s["id"] for s in sources_doc.get("sources", [])]
    stats: dict[str, dict] = {
        sid: {"total": 0, "landed": 0, "by_decision": {}} for sid in source_ids
    }

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
    with open(license_path, "r", encoding="utf-8") as f:
        return f.read()


def extract_copyright_author(license_text: str) -> str | None:
    m = re.search(r"^Copyright \(c\) \d{4}[a-z, ]*\s+(.+)$", license_text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return None


def repo_link(repository: str) -> str:
    return f"[{repository}](https://github.com/{repository})"


def decision_label(decision: str) -> str:
    return DECISION_LABELS.get(decision, decision)


def render_source_table(sources_doc: dict, stats: dict[str, dict]) -> str:
    rows = []
    header = (
        "| id | repository | branch | license | snapshot_policy | lineage | "
        "selection_status | 支持的规则数 | 落地的规则数 |"
    )
    sep = "|---|---|---|---|---|---|---|---|---|"
    rows.append(header)
    rows.append(sep)
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


def render_full_text_section(s: dict, stats_entry: dict, snapshots_dir: Path) -> str:
    sid = s["id"]
    license_text = read_license_text(snapshots_dir, sid)
    if license_text is None:
        raise FileNotFoundError(f"snapshot_policy 是 full-text，但找不到 LICENSE：{sid}")
    author = extract_copyright_author(license_text) or "未知"
    lines = []
    lines.append(f"### {sid}")
    lines.append("")
    lines.append(f"- 作者：{author}")
    lines.append(f"- 仓库：{repo_link(s['repository'])}")
    lines.append(f"- 许可证：{s['license']}")
    lines.append("")
    lines.append("许可声明原文（逐字节照抄自 "
                  f"`merges/maybe-humanizer/snapshots/{sid}/LICENSE`）：")
    lines.append("")
    lines.append("```")
    lines.append(license_text.rstrip("\n"))
    lines.append("```")
    lines.append("")
    lines.append("支持的规则，按 decision 分组：")
    lines.append("")
    lines.append(render_rule_list_by_decision(stats_entry["by_decision"]))
    return "\n".join(lines)


def render_metadata_only_section(s: dict, stats_entry: dict) -> str:
    sid = s["id"]
    lines = []
    lines.append(f"### {sid}")
    lines.append("")
    lines.append(f"- 仓库：{repo_link(s['repository'])}")
    lines.append("- 许可证：未知，未取得许可证，本仓库不含其原文。")
    lines.append(
        "- 本来源按 metadata-only 处理：只记录了追踪文件的 commit 和哈希，"
        "不保存原文；它支持的规则都是用自己的话重写的，不引用原文的例句、"
        "词表条目或措辞。"
    )
    lines.append("")
    lines.append("支持的规则，按 decision 分组：")
    lines.append("")
    lines.append(render_rule_list_by_decision(stats_entry["by_decision"]))
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

    parts: list[str] = []
    parts.append(f"# {target_skill} 来源")
    parts.append("")
    parts.append(
        f"`skills/{target_skill}/` 正文是对下列来源的重写，不是上游内容的转载。"
        "上游各来源的著作权归各自作者所有。"
    )
    parts.append("")
    parts.append("## 来源表")
    parts.append("")
    parts.append(render_source_table(sources_doc, stats))
    parts.append("")
    parts.append("## 各来源详情")
    parts.append("")
    for s in sources_doc.get("sources", []):
        if s.get("status") == "removed":
            continue
        sid = s["id"]
        entry = stats.get(sid, {"total": 0, "landed": 0, "by_decision": {}})
        if s["snapshot_policy"] == "full-text":
            parts.append(render_full_text_section(s, entry, snapshots_dir))
        else:
            parts.append(render_metadata_only_section(s, entry))
        parts.append("")

    parts.append("## 已移除的来源")
    parts.append("")
    parts.append(render_removed_section(sources_doc))
    parts.append("")

    parts.append("## 生成信息")
    parts.append("")
    ts = generated_at or datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    parts.append(f"- 渲染时间：{ts}")
    parts.append(
        f"- 渲染依据：`merges/{merge_id}/decisions.yaml`（{len(decisions_doc.get('rules', []))} 条规则）"
        f"与 `merges/{merge_id}/sources.yaml`（{len(sources_doc.get('sources', []))} 个来源）。"
    )
    parts.append("")
    parts.append("本文件由脚本从 decisions.yaml 和 sources.yaml 生成，不要手工编辑。")
    parts.append("")

    return "\n".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", required=True, type=Path)
    parser.add_argument("--decisions", required=True, type=Path)
    parser.add_argument("--lock", required=False, type=Path)
    parser.add_argument("--snapshots-dir", required=True, type=Path)
    parser.add_argument("--out", required=False, type=Path)
    parser.add_argument("--generated-at", required=False, type=str)
    args = parser.parse_args()

    sources_doc = load_sources(args.sources)
    decisions_doc = load_decisions(args.decisions)
    generated_at = args.generated_at
    if generated_at is None and args.lock is not None and args.lock.exists():
        lock_doc = load_lock(args.lock)
        generated_at = lock_doc.get("generated_at")

    md = render_sources_md(sources_doc, decisions_doc, args.snapshots_dir, generated_at)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
    else:
        sys.stdout.write(md)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
