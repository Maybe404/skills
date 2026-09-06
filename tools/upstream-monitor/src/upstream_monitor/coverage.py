"""merges/<id>/work/ 下单元清单、覆盖表、聚类表与 decisions.yaml 的一致性校验。

这三份文件是拆规则和归并阶段的中间产物（见
skills/skill-merge/references/extraction.md），按流程要进仓库，路径固定为
merges/<id>/work/units/<source_id>.md、work/coverage.md、work/clusters.md
（clusters.md 可选）。逻辑从 prototype/check_merge.py 的 coverage 子命令移植。
"""
from __future__ import annotations

import collections
import re
from pathlib import Path

from upstream_monitor.diagnostics import Report

UNIT_HEAD = re.compile(r"^#{2,4}\s+(U-[a-z]+-\d{3})\s*$", re.M)
ANCHOR_LINE = re.compile(r"^\s*-?\s*anchor:\s*(.+?)\s*$", re.M)
ANCHOR_INLINE = re.compile(r"anchor:\s*(``[^`]+``|`[^`]+`|\"[^\"]+\"|'[^']+'|[^;\n]+)")
COVERAGE_ROW = re.compile(
    r"^\|\s*(U-[a-z]+-\d{3})\s*\|([^|]*)\|(.*)\|\s*([A-Z]+-[A-Z]+-\d{3})\s*\|([^|]*)\|"
)
CLUSTER_ROW = re.compile(r"^\|\s*([A-Z]+-[A-Z]+-\d{3})\s*\|([^|]*)\|")


def unquote(s: str) -> str:
    s = s.strip()
    for a in ("``", "`", '"', "'"):
        if s.startswith(a) and s.endswith(a) and len(s) > 2 * len(a) - 1:
            return s[len(a) : -len(a)].strip()
    return s


def norm_anchor(s: str | None) -> str:
    return (
        (s or "")
        .replace("\\", "")
        .replace("`", "")
        .replace("“", '"')
        .replace("”", '"')
        .replace("‘", "'")
        .replace("’", "'")
        .strip()
        .strip('"')
        .strip()
    )


def parse_units(units_dir: Path) -> dict[str, dict]:
    """单元清单目录，每个来源一份 `<source_id>.md`。"""
    out: dict[str, dict] = {}
    for p in sorted(units_dir.glob("*.md")):
        sid = p.stem
        text = p.read_text(encoding="utf-8")
        heads = list(UNIT_HEAD.finditer(text))
        for i, m in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            body = text[m.end() : end]
            am = ANCHOR_LINE.search(body) or ANCHOR_INLINE.search(body)
            out[m.group(1)] = {"source_id": sid, "anchor": unquote(am.group(1)) if am else None}
    return out


def check_coverage(
    decisions: dict,
    units_dir: Path,
    coverage_md: Path,
    clusters_md: Path | None,
    rep: Report,
) -> None:
    rules = {r["id"]: r for r in decisions["rules"]}
    units = parse_units(units_dir)
    cov = []
    for line in coverage_md.read_text(encoding="utf-8").splitlines():
        m = COVERAGE_ROW.match(line)
        if m:
            cov.append(
                (m.group(1), m.group(2).strip(), m.group(3).strip(), m.group(4), m.group(5).strip())
            )

    abbr = {u.split("-")[1]: v["source_id"] for u, v in units.items()}

    noanchor = [k for k, v in units.items() if not v["anchor"]]
    if noanchor:
        rep.add("MED", f"{len(noanchor)} 条单元解析不到 anchor: {noanchor[:10]}")

    cnt = collections.Counter(c[0] for c in cov)
    dup = {k: v for k, v in cnt.items() if v > 1}
    missing = sorted(set(units) - set(cnt))
    extra = sorted(set(cnt) - set(units))
    if dup:
        rep.add("BLOCK", f"覆盖表里重复归属的单元: {dup}")
    if missing:
        rep.add("BLOCK", f"单元清单里有、覆盖表里没有: {missing}")
    if extra:
        rep.add("BLOCK", f"覆盖表里有、单元清单里没有: {extra}")
    if not (dup or missing or extra):
        rep.ok(f"{len(cov)} 行覆盖表与 {len(units)} 条单元一一对应")

    unknown = sorted({c[3] for c in cov} - set(rules))
    if unknown:
        rep.add("BLOCK", f"覆盖表里的未知规则 id: {unknown}")
    unused = sorted(set(rules) - {c[3] for c in cov})
    if unused:
        rep.add("HIGH", f"decisions.yaml 里没有任何单元归属的规则: {unused}")
    if not (unknown or unused):
        rep.ok("规则 id 双向对得上")

    bad = [
        (u, rid, d, rules[rid]["decision"])
        for u, _, _, rid, d in cov
        if rid in rules and d != rules[rid]["decision"]
    ]
    for b in bad:
        rep.add("HIGH", f"{b[0]} -> {b[1]}: 覆盖表写 {b[2]}，decisions.yaml 是 {b[3]}")
    if not bad:
        rep.ok("decision 列全部一致")

    members: dict[str, list[str]] = collections.defaultdict(list)
    for u, _, _, rid, _ in cov:
        members[rid].append(u)
    bad_n = [
        (rid, len(members.get(rid, [])), r["evidence_count"])
        for rid, r in rules.items()
        if len(members.get(rid, [])) != r["evidence_count"]
    ]
    for rid, got, want in bad_n:
        rep.add("HIGH", f"{rid}: 覆盖表成员 {got} 条，evidence_count {want}")
    bad_s = []
    for rid, r in rules.items():
        want = collections.Counter(ev["source_id"] for ev in r["sources"] if ev["type"] == "upstream")
        got = collections.Counter(abbr.get(u.split("-")[1], u) for u in members.get(rid, []))
        if want != got:
            bad_s.append((rid, dict(got), dict(want)))
    for rid, got, want in bad_s:
        rep.add("HIGH", f"{rid}: 覆盖表来源 {got}，decisions.sources {want}")
    if not (bad_n or bad_s):
        rep.ok("成员数与来源分布全部一致")

    n_bad = 0
    for u, _, canc, rid, _ in cov:
        ua = units.get(u, {}).get("anchor")
        if ua and norm_anchor(canc) != norm_anchor(ua):
            rep.add("HIGH", f"{u} ({rid}): 覆盖表 anchor={canc!r} 与单元清单 {ua!r} 不一致")
            n_bad += 1
        if rid in rules:
            ancs = {norm_anchor(ev["anchor"]) for ev in rules[rid]["sources"]}
            if norm_anchor(canc) not in ancs:
                rep.add("HIGH", f"{u} -> {rid}: 覆盖表 anchor {canc!r} 在 decisions.yaml 里找不到")
                n_bad += 1
    if not n_bad:
        rep.ok("覆盖表、单元清单、decisions.yaml 的 anchor 一致")

    if clusters_md is not None and clusters_md.exists():
        clusters: dict[str, list[str]] = collections.defaultdict(list)
        for line in clusters_md.read_text(encoding="utf-8").splitlines():
            m = CLUSTER_ROW.match(line)
            if m:
                clusters[m.group(1)].extend(re.findall(r"U-[a-z]+-\d{3}", m.group(2)))
        bad_c = [
            (rid, sorted(set(clusters.get(rid, []))), sorted(set(members.get(rid, []))))
            for rid in sorted(set(clusters) | set(members))
            if sorted(set(clusters.get(rid, []))) != sorted(set(members.get(rid, [])))
        ]
        for rid, a, b in bad_c:
            rep.add("HIGH", f"{rid}: 聚类表 {a}，覆盖表 {b}")
        if not bad_c:
            rep.ok(f"{len(clusters)} 个簇与覆盖表一致")
