"""`upstream-monitor locate` 的实现。

读 decisions.yaml，列出 sources 含指定来源的规则；给了 --diff 时，按 hunk
的上下文行和锚点收窄到受影响的规则，再对 diff 里新增的行与全部规则的
rule_summary 做字符 n-gram Jaccard 相似度，列出每个 hunk 最接近的三条。
输出 markdown，可以直接贴进 PR 正文。
"""
from __future__ import annotations

import re
from pathlib import Path

from upstream_monitor.anchors import locate as locate_anchor
from upstream_monitor.paths import RepoPaths
from upstream_monitor.yamlio import load_yaml

TOP_N = 3
NGRAM = 3


def rules_for_source(decisions: dict, source_id: str) -> list[dict]:
    out = []
    for r in decisions["rules"]:
        if any(ev["type"] == "upstream" and ev["source_id"] == source_id for ev in r["sources"]):
            out.append(r)
    return out


def _anchors_for_source(rule: dict, source_id: str) -> list[str]:
    return [
        ev["anchor"]
        for ev in rule["sources"]
        if ev["type"] == "upstream" and ev["source_id"] == source_id and ev["anchor"]
    ]


def parse_hunks(diff_text: str) -> list[dict]:
    hunks: list[dict] = []
    cur_old: str | None = None
    cur_new: str | None = None
    cur: dict | None = None
    for line in diff_text.splitlines():
        if line.startswith("--- "):
            cur_old = line[4:].strip()
            continue
        if line.startswith("+++ "):
            cur_new = line[4:].strip()
            continue
        if line.startswith("@@"):
            if cur is not None:
                hunks.append(cur)
            cur = {"header": line, "old_file": cur_old, "new_file": cur_new, "lines": []}
            continue
        if cur is not None:
            cur["lines"].append(line)
    if cur is not None:
        hunks.append(cur)
    return hunks


def hunk_context_and_added_text(hunk: dict) -> str:
    return "\n".join(ln[1:] for ln in hunk["lines"] if ln[:1] in (" ", "+") and not ln.startswith("+++"))


def hunk_added_text(hunk: dict) -> str:
    return "\n".join(ln[1:] for ln in hunk["lines"] if ln.startswith("+") and not ln.startswith("+++"))


def ngrams(text: str, n: int = NGRAM) -> set[str]:
    s = re.sub(r"\s+", "", text)
    if len(s) < n:
        return {s} if s else set()
    return {s[i : i + n] for i in range(len(s) - n + 1)}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 0.0
    union = a | b
    if not union:
        return 0.0
    return len(a & b) / len(union)


def rules_affected_by_hunk(candidate_rules: list[dict], source_id: str, hunk: dict) -> list[dict]:
    text = hunk_context_and_added_text(hunk)
    affected = []
    for r in candidate_rules:
        for anchor in _anchors_for_source(r, source_id):
            status, _ = locate_anchor(text, anchor)
            if status != "MISS":
                affected.append(r)
                break
    return affected


def closest_rules_for_hunk(all_rules: list[dict], hunk: dict, top_n: int = TOP_N) -> list[tuple[dict, float]]:
    added = ngrams(hunk_added_text(hunk))
    scored = []
    for r in all_rules:
        score = jaccard(added, ngrams(r["rule_summary"]))
        scored.append((r, score))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]


def render_locate_markdown(
    merge_id: str,
    source_id: str,
    candidate_rules: list[dict],
    all_rules: list[dict],
    diff_text: str | None,
) -> str:
    lines = [f"# locate: {merge_id} / {source_id}", ""]

    if diff_text is None:
        lines.append("## 引用该来源的规则")
        lines.append("")
        lines.append("| 规则 id | decision | local.path | 该来源的 anchor |")
        lines.append("|---|---|---|---|")
        for r in candidate_rules:
            anchors = "; ".join(_anchors_for_source(r, source_id)) or "（无）"
            lines.append(f"| {r['id']} | {r['decision']} | {r['local']['path']} | {anchors} |")
        if not candidate_rules:
            lines.append("| （无） | | | |")
        lines.append("")
        return "\n".join(lines)

    hunks = parse_hunks(diff_text)
    if not hunks:
        lines.append("diff 里没有解析到 hunk。")
        lines.append("")
        return "\n".join(lines)

    for i, hunk in enumerate(hunks, start=1):
        lines.append(f"## hunk {i}: {hunk['header']}")
        lines.append("")
        lines.append(f"文件：`{hunk.get('new_file') or hunk.get('old_file') or '未知'}`")
        lines.append("")
        affected = rules_affected_by_hunk(candidate_rules, source_id, hunk)
        lines.append("### 受影响规则（按上下文行和锚点收窄）")
        lines.append("")
        if affected:
            lines.append("| 规则 id | decision | local.path | local.anchor |")
            lines.append("|---|---|---|---|")
            for r in affected:
                lines.append(
                    f"| {r['id']} | {r['decision']} | {r['local']['path']} | {r['local']['anchor']} |"
                )
        else:
            lines.append("（按锚点没有直接命中的规则）")
        lines.append("")
        lines.append("### 词面最接近的规则（字符 3-gram Jaccard，前 3 条）")
        lines.append("")
        closest = closest_rules_for_hunk(all_rules, hunk)
        if closest and any(score > 0 for _, score in closest):
            lines.append("| 规则 id | rule_summary | 相似度 |")
            lines.append("|---|---|---|")
            for r, score in closest:
                lines.append(f"| {r['id']} | {r['rule_summary']} | {score:.2f} |")
        else:
            lines.append("（新增行与现有规则的词面相似度均为 0）")
        lines.append("")

    return "\n".join(lines)


def run_locate(
    paths: RepoPaths, merge_id: str, source_id: str, diff_path: Path | None = None
) -> str:
    decisions = load_yaml(paths.decisions_yaml(merge_id))
    candidate_rules = rules_for_source(decisions, source_id)
    diff_text = diff_path.read_text(encoding="utf-8") if diff_path else None
    return render_locate_markdown(merge_id, source_id, candidate_rules, decisions["rules"], diff_text)
