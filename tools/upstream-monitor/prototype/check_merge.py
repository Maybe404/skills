#!/usr/bin/env python3
"""校验一个 merge 实例的结构、锚点和覆盖。

三个子命令，各自独立，路径都是参数，没有写死的仓库路径：

- `format`   ：schema 校验、交叉引用、id 格式与唯一性、local.anchor 定位、
               history 与 decision_revision、relations 的完整性和双向性。
- `anchors`  ：decisions.yaml 里每条证据的上游 anchor 能不能在快照里定位到。
- `coverage` ：拆规则阶段的单元清单、覆盖表、聚类表与 decisions.yaml 是否一致。

用法：

    python3 check_merge.py format   --root . --merge merges/maybe-humanizer
    python3 check_merge.py anchors  --root . --merge merges/maybe-humanizer \\
        --fetch-dir /tmp/fetch
    python3 check_merge.py coverage --root . --merge merges/maybe-humanizer \\
        --units /tmp/units --coverage /tmp/merge/coverage.md \\
        --clusters /tmp/merge/clusters.md

`--fetch-dir` 给 metadata-only 来源用：这类来源的原文不在仓库里，按 lock 的
commit 临时拉到仓库外的一个目录，目录结构与上游仓库内路径一致
（`<fetch-dir>/<source_id>/<original_path>`）。不给这个参数时，
metadata-only 来源的证据只报"快照不在仓库内，跳过"，不算失败。

`coverage` 的三个输入是拆规则阶段的中间产物，按流程不进仓库，因此路径必须
显式传入。三个子命令都在有 BLOCK 或 HIGH 级问题时以非零码退出。

依赖：pyyaml、jsonschema。
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import sys
from typing import Any

import yaml

# ---------------------------------------------------------------- 通用

SEVERITIES = ("BLOCK", "HIGH", "MED", "LOW")
FAIL_ON = {"BLOCK", "HIGH"}


class Report:
    """收集问题并按严重程度汇总。"""

    def __init__(self) -> None:
        self.problems: list[tuple[str, str]] = []

    def add(self, severity: str, message: str) -> None:
        assert severity in SEVERITIES, severity
        self.problems.append((severity, message))
        print(f"[{severity}] {message}")

    def ok(self, message: str) -> None:
        print(f"  PASS {message}")

    def summary(self) -> int:
        counts = collections.Counter(s for s, _ in self.problems)
        print()
        print("=" * 70)
        print("问题汇总:", dict(counts) if self.problems else "无")
        return 1 if any(counts[s] for s in FAIL_ON) else 0


def load_any(path: pathlib.Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if path.suffix in (".yaml", ".yml"):
        return yaml.safe_load(text)
    return json.loads(text)


def merge_files(root: pathlib.Path, merge: pathlib.Path) -> dict[str, pathlib.Path]:
    m = merge if merge.is_absolute() else root / merge
    return {
        "dir": m,
        "sources": m / "sources.yaml",
        "lock": m / "sources.lock.json",
        "decisions": m / "decisions.yaml",
    }


# ---------------------------------------------------------------- markdown 定位

HEAD = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
QUOTE = re.compile(r"^\s*(?:>\s?)+")


def unquote_md(line: str) -> str:
    """去掉引用块的 `> ` 前缀。引用块里的标题仍然是标题。"""
    return QUOTE.sub("", line)


def heading_lines(lines: list[str]) -> dict[int, tuple[int, str]]:
    """返回 {行号: (层级, 标题文本)}，围栏代码块里的 # 行不算标题。

    上游文件里经常有把 markdown 报告模板整段放进代码块的写法，块里的
    `## AI Pattern Report` 不是标题；不排除掉会把它上面那个小节提前截断，
    小节内的子锚点就定位不到了。
    """
    out: dict[int, tuple[int, str]] = {}
    in_fence = False
    for i, ln in enumerate(lines):
        ln = unquote_md(ln)
        if FENCE.match(ln):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEAD.match(ln)
        if m:
            out[i] = (len(m.group(1)), m.group(2).strip())
    return out


def strip_md(line: str) -> str:
    """去掉行首的列表符号、序号、表格竖线和行内的强调标记。"""
    s = unquote_md(line).strip()
    s = re.sub(r"^[-*+]\s+", "", s)
    s = re.sub(r"^\d+\.\s+", "", s)
    s = re.sub(r"^\|\s*", "", s)
    return s.replace("**", "").replace("`", "").replace("*", "").strip()


def find_heading(heads: dict[int, tuple[int, str]], want: str) -> tuple[list[int], str]:
    w = want.lstrip("#").strip()
    exact = [i for i, (_, t) in heads.items() if t == w]
    if exact:
        return sorted(exact), "heading-exact"
    loose = [i for i, (_, t) in heads.items() if w in t]
    return sorted(loose), ("heading-contains" if loose else "none")


def section_bounds(heads: dict[int, tuple[int, str]], total: int, idx: int) -> tuple[int, int]:
    level = heads[idx][0]
    for j in sorted(heads):
        if j > idx and heads[j][0] <= level:
            return idx, j
    return idx, total


def locate(text: str, anchor: str) -> tuple[str, str]:
    """在 text 里定位 anchor。

    anchor 的写法见 skills/skill-merge/references/extraction.md：小节标题原文，
    或稳定的行首文本，多级之间用 " / " 分隔。

    返回 (status, detail)，status 取 ok-heading / ok-linestart / ok-substring /
    weak-heading / MISS。
    """
    lines = text.splitlines()
    heads = heading_lines(lines)
    parts = [p.strip() for p in (anchor or "").split(" / ")]
    head, rest = parts[0], parts[1:]

    if head.startswith("#"):
        hits, how = find_heading(heads, head)
        if not hits:
            return "MISS", f"小节标题找不到: {head!r}"
        if not rest:
            return ("ok-heading" if how == "heading-exact" else "weak-heading",
                    f"{how}, {len(hits)} 处")
        for i in hits:
            a, b = section_bounds(heads, len(lines), i)
            body = lines[a:b]
            for sub in rest:
                target = sub.strip('"')
                if any(strip_md(ln).startswith(sub) or strip_md(ln).startswith(target)
                       for ln in body):
                    continue
                if any(target in ln for ln in body):
                    return "ok-substring", f"{how}; 子锚点 {sub!r} 只作为子串出现在小节内"
                break
            else:
                return ("ok-linestart" if how == "heading-exact" else "weak-heading",
                        f"{how}; 子锚点均在行首")
        return "MISS", f"小节 {head!r} 找到但子锚点 {rest} 定位不到"

    for ln in lines:
        if strip_md(ln).startswith(head):
            if not rest:
                return "ok-linestart", "行首文本"
            break
    if any(head in ln for ln in lines):
        return "ok-substring", "只作为子串出现，不在行首"
    return "MISS", f"行首文本找不到: {head!r}"


# ---------------------------------------------------------------- format

CAT_CODE = {
    "pattern": "P",
    "protection": "PROT",
    "process": "PROC",
    "style-opinion": "S",
    "genre": "G",
    "measurement": "M",
}
LANG_PREFIX = {"zh": "ZH", "en": "EN", "both": "ALL"}
RULE_ID = re.compile(r"^(ZH|EN|ALL)-(P|PROT|PROC|S|G|M)-(\d{3})$")
LANDED = {"adopted", "adopted-with-modification"}
SYMMETRIC = ("conflicts-with", "pairs-with")


def cmd_format(args: argparse.Namespace) -> int:
    from jsonschema import Draft202012Validator, FormatChecker

    root = pathlib.Path(args.root).resolve()
    f = merge_files(root, pathlib.Path(args.merge))
    schemas = pathlib.Path(args.schemas) if args.schemas else root / "tools/upstream-monitor/schemas"
    rep = Report()

    print("=" * 70)
    print("1.1 schema 校验")
    print("=" * 70)
    targets = [("sources.schema.json", f["sources"]),
               ("lock.schema.json", f["lock"]),
               ("decisions.schema.json", f["decisions"])]
    catalog_dir = pathlib.Path(args.catalog_dir) if args.catalog_dir else root / "catalog"
    if catalog_dir.is_dir():
        for c in sorted(catalog_dir.glob("*.yaml")):
            targets.insert(0, ("catalog.schema.json", c))
    for schema_name, target in targets:
        schema = load_any(schemas / schema_name)
        Draft202012Validator.check_schema(schema)
        v = Draft202012Validator(schema, format_checker=FormatChecker())
        errs = sorted(v.iter_errors(load_any(target)), key=lambda e: list(e.path))
        if errs:
            for e in errs:
                rep.add("BLOCK", f"schema 失败 {target}: /{'/'.join(str(x) for x in e.path)}: {e.message}")
        else:
            rep.ok(f"{target.relative_to(root)} <- {schema_name}")

    D, S, L = load_any(f["decisions"]), load_any(f["sources"]), load_any(f["lock"])
    rules = D["rules"]
    print(f"\n规则总数: {len(rules)}")

    print("=" * 70)
    print("1.2 merge_id 一致 / source_id 存在性")
    print("=" * 70)
    if not (D["merge_id"] == S["merge_id"] == L["merge_id"] == f["dir"].name):
        rep.add("BLOCK", f"merge_id 不一致: decisions={D['merge_id']} sources={S['merge_id']} "
                         f"lock={L['merge_id']} dir={f['dir'].name}")
    else:
        rep.ok("merge_id 一致")

    src_by_id = {s["id"]: s for s in S["sources"]}
    lineage_of = {s["id"]: s["lineage"] for s in S["sources"]}
    bad = {(r["id"], ev["source_id"]) for r in rules for ev in r["sources"]
           if ev["type"] == "upstream" and ev["source_id"] not in src_by_id}
    for rid, sid in sorted(bad):
        rep.add("BLOCK", f"{rid} 的 source_id 不在 sources.yaml: {sid}")
    if not bad:
        rep.ok("全部 source_id 都在 sources.yaml")
    if set(L["sources"]) != set(src_by_id):
        rep.add("HIGH", f"lock 与 sources 的 id 集合不一致: "
                        f"lock only={set(L['sources'])-set(src_by_id)} "
                        f"sources only={set(src_by_id)-set(L['sources'])}")
    else:
        rep.ok("lock 与 sources id 集合一致")

    print("=" * 70)
    print("1.3 evidence_count 与 independent_sources")
    print("=" * 70)
    bad_ec = [(r["id"], r["evidence_count"], len(r["sources"])) for r in rules
              if r["evidence_count"] != len(r["sources"])]
    for rid, ec, n in bad_ec:
        rep.add("HIGH", f"{rid}: evidence_count={ec} 但 sources 长度={n}")
    if not bad_ec:
        rep.ok(f"evidence_count 全部 {len(rules)} 条一致")
    bad_is = []
    for r in rules:
        lins = {lineage_of.get(ev["source_id"], f"?{ev['source_id']}")
                if ev["type"] == "upstream" else "self" for ev in r["sources"]}
        if r["independent_sources"] != len(lins):
            bad_is.append((r["id"], r["independent_sources"], len(lins), sorted(lins)))
    for rid, got, exp, lins in bad_is:
        rep.add("HIGH", f"{rid}: independent_sources={got} 但去重 lineage 数={exp} {lins}")
    if not bad_is:
        rep.ok(f"independent_sources 全部 {len(rules)} 条一致")

    print("=" * 70)
    print("1.4 规则 id 唯一与格式")
    print("=" * 70)
    dups = [k for k, v in collections.Counter(r["id"] for r in rules).items() if v > 1]
    if dups:
        rep.add("BLOCK", f"重复的规则 id: {dups}")
    else:
        rep.ok(f"{len(rules)} 个 id 唯一")
    groups: dict[tuple[str, str], list[int]] = collections.defaultdict(list)
    for r in rules:
        m = RULE_ID.match(r["id"])
        if not m:
            rep.add("BLOCK", f"{r['id']}: id 不符合 extraction.md 的前缀/类别码格式")
            continue
        pre, code, num = m.groups()
        if pre != LANG_PREFIX[r["language"]]:
            rep.add("HIGH", f"{r['id']}: 前缀 {pre} 与 language={r['language']} 不符")
        if code != CAT_CODE[r["category"]]:
            rep.add("HIGH", f"{r['id']}: 类别码 {code} 与 category={r['category']} 不符")
        groups[(pre, code)].append(int(num))
    for g, nums in sorted(groups.items()):
        if sorted(nums) != list(range(1, len(nums) + 1)):
            rep.add("MED", f"{g[0]}-{g[1]}-: 编号不是从 001 起连续递增，实际 {sorted(nums)}")
    print("  分组: " + ", ".join(f"{a}-{b}({len(v)})" for (a, b), v in sorted(groups.items())))

    print("=" * 70)
    print("1.5 local.anchor 在 local.path 里唯一定位")
    print("=" * 70)
    cache: dict[str, str | None] = {}
    stats: collections.Counter = collections.Counter()
    for r in rules:
        rel, anc = r["local"]["path"], r["local"]["anchor"]
        if rel not in cache:
            p = root / rel
            cache[rel] = p.read_text(encoding="utf-8") if p.exists() else None
        txt = cache[rel]
        landed = r["decision"] in LANDED
        if txt is None:
            rep.add("BLOCK", f"{r['id']} ({r['decision']}): local.path 不存在 {rel}")
            continue
        if anc is None:
            if landed:
                rep.add("BLOCK", f"{r['id']} ({r['decision']}): 已落地规则的 local.anchor 为 null")
            stats["null-anchor"] += 1
            continue
        n = txt.count(anc)
        stats[f"hit{min(n, 2)}"] += 1
        if n == 0:
            rep.add("BLOCK" if landed else "HIGH",
                    f"{r['id']} ({r['decision']}): anchor 在 {rel} 中找不到: {anc!r}")
        elif n > 1:
            rep.add("HIGH" if landed else "MED",
                    f"{r['id']} ({r['decision']}): anchor 在 {rel} 中命中 {n} 次: {anc!r}")
    print("  统计:", dict(stats))
    print("  decision 分布:", dict(collections.Counter(r["decision"] for r in rules)))

    print("=" * 70)
    print("1.6 history 与 decision_revision")
    print("=" * 70)
    no_hist = [r["id"] for r in rules if not r.get("history")]
    if no_hist:
        rep.add("MED", f"{len(no_hist)} 条没有 history: {no_hist[:10]}")
    mism = [r["id"] for r in rules if r.get("history") and r["history"][-1]["decision"] != r["decision"]]
    if mism:
        rep.add("HIGH", f"history 末条与当前 decision 不一致: {mism}")
    else:
        rep.ok("history 末条与当前 decision 一致")
    badrev = [r["id"] for r in rules if r.get("history") and len(r["history"]) != r["decision_revision"]]
    if badrev:
        rep.add("MED", f"decision_revision 与 history 长度不符: {badrev[:10]}（共 {len(badrev)}）")
    else:
        rep.ok("decision_revision 与 history 长度一致")
    print("  decision_origin:", dict(collections.Counter(r["decision_origin"] for r in rules)))
    print("  decision_revision:", dict(collections.Counter(r["decision_revision"] for r in rules)))

    print("=" * 70)
    print("1.7 relations 的完整性与双向性")
    print("=" * 70)
    ids = {r["id"] for r in rules}
    edges: dict[str, set[tuple[str, str]]] = collections.defaultdict(set)
    counts: collections.Counter = collections.Counter()
    for r in rules:
        seen = set()
        for e in r.get("relations", []):
            counts[e["type"]] += 1
            key = (e["type"], e["rule_id"])
            if key in seen:
                rep.add("MED", f"{r['id']}: relations 里有重复的 {e['type']} -> {e['rule_id']}")
            seen.add(key)
            if e["rule_id"] == r["id"]:
                rep.add("HIGH", f"{r['id']}: relations 指向自己")
            elif e["rule_id"] not in ids:
                rep.add("BLOCK", f"{r['id']}: relations 的 rule_id 不存在: {e['rule_id']}")
            edges[e["type"]].add((r["id"], e["rule_id"]))
    oneway = [(t, a, b) for t in SYMMETRIC for a, b in edges[t] if (b, a) not in edges[t]]
    for t, a, b in sorted(oneway):
        rep.add("HIGH", f"{t} 是单向的: {a} 指向 {b}，但 {b} 没有指回 {a}")
    if not oneway:
        rep.ok("conflicts-with 与 pairs-with 全部双向")
    print("  relations 计数:", dict(counts) if counts else "无")

    return rep.summary()


# ---------------------------------------------------------------- anchors

def cmd_anchors(args: argparse.Namespace) -> int:
    root = pathlib.Path(args.root).resolve()
    f = merge_files(root, pathlib.Path(args.merge))
    fetch_dir = pathlib.Path(args.fetch_dir).resolve() if args.fetch_dir else None
    rep = Report()

    D, S, L = load_any(f["decisions"]), load_any(f["sources"]), load_any(f["lock"])
    src_by_id = {s["id"]: s for s in S["sources"]}
    stored = {(sid, fe["original_path"]): fe["stored_path"]
              for sid, entry in L["sources"].items() for fe in entry["files"]}

    cache: dict[tuple[str, str], str | None] = {}

    def text_for(sid: str, path: str) -> tuple[str | None, str]:
        """返回 (正文, 来源说明)。metadata-only 来源的正文不在仓库内。"""
        key = (sid, path)
        if key in cache:
            return cache[key], "cached"
        sp = stored.get(key, "MISSING")
        if sp == "MISSING":
            cache[key] = None
            return None, "lock 的 files[] 里没有这个路径"
        if sp is None:
            if fetch_dir is None:
                cache[key] = None
                return None, "metadata-only，未给 --fetch-dir"
            p = fetch_dir / sid / path
        else:
            p = root / sp
        cache[key] = p.read_text(encoding="utf-8") if p.exists() else None
        return cache[key], str(p)

    print("=" * 70)
    print("2.1 每条证据的上游 anchor 定位")
    print("=" * 70)
    stats: collections.Counter = collections.Counter()
    per_source: collections.Counter = collections.Counter()
    total = 0
    for r in D["rules"]:
        for ev in r["sources"]:
            if ev["type"] != "upstream":
                continue
            total += 1
            sid, path = ev["source_id"], ev["path"]
            per_source[sid] += 1
            if sid not in src_by_id:
                rep.add("BLOCK", f"{r['id']}: source_id 不在 sources.yaml: {sid}")
                continue
            if path not in src_by_id[sid]["paths"]:
                rep.add("HIGH", f"{r['id']}: 证据路径不在 sources.yaml 的 paths 里: {sid}:{path}")
                stats["BAD-PATH"] += 1
            want = L["sources"][sid]["last_seen_commit"]
            if ev["commit"] != want:
                rep.add("HIGH", f"{r['id']}: commit {ev['commit']} 与 lock 的 {want} 不符")
                stats["BAD-COMMIT"] += 1
            txt, where = text_for(sid, path)
            if txt is None:
                stats["NO-TEXT"] += 1
                sev = "MED" if where == "metadata-only，未给 --fetch-dir" else "HIGH"
                rep.add(sev, f"{r['id']}: 拿不到上游正文（{sid}:{path}，{where}）")
                continue
            st, detail = locate(txt, ev["anchor"] or "")
            stats[st] += 1
            if st == "MISS":
                rep.add("HIGH", f"{r['id']} ({sid}:{path}): anchor 定位不到 {ev['anchor']!r}；{detail}")
            elif st in ("ok-substring", "weak-heading"):
                rep.add("LOW", f"{r['id']} ({sid}): 弱定位 {ev['anchor']!r}；{detail}")

    print(f"\n证据条目总数: {total}")
    print("按来源:", dict(per_source))
    print("定位结果:", dict(stats))
    return rep.summary()


# ---------------------------------------------------------------- coverage

UNIT_HEAD = re.compile(r"^#{2,4}\s+(U-[a-z]+-\d{3})\s*$", re.M)
ANCHOR_LINE = re.compile(r"^\s*-?\s*anchor:\s*(.+?)\s*$", re.M)
ANCHOR_INLINE = re.compile(r"anchor:\s*(``[^`]+``|`[^`]+`|\"[^\"]+\"|'[^']+'|[^;\n]+)")
COVERAGE_ROW = re.compile(
    r"^\|\s*(U-[a-z]+-\d{3})\s*\|([^|]*)\|(.*)\|\s*([A-Z]+-[A-Z]+-\d{3})\s*\|([^|]*)\|")
CLUSTER_ROW = re.compile(r"^\|\s*([A-Z]+-[A-Z]+-\d{3})\s*\|([^|]*)\|")


def unquote(s: str) -> str:
    s = s.strip()
    for a in ("``", "`", '"', "'"):
        if s.startswith(a) and s.endswith(a) and len(s) > 2 * len(a) - 1:
            return s[len(a):-len(a)].strip()
    return s


def norm_anchor(s: str | None) -> str:
    return ((s or "").replace("\\", "").replace("`", "")
            .replace("“", '"').replace("”", '"')
            .replace("‘", "'").replace("’", "'").strip().strip('"').strip())


def parse_units(units_dir: pathlib.Path) -> dict[str, dict]:
    """单元清单目录，每个来源一份 `<source_id>.md`。"""
    out: dict[str, dict] = {}
    for p in sorted(units_dir.glob("*.md")):
        sid = p.stem
        text = p.read_text(encoding="utf-8")
        heads = list(UNIT_HEAD.finditer(text))
        for i, m in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            body = text[m.end():end]
            am = ANCHOR_LINE.search(body) or ANCHOR_INLINE.search(body)
            out[m.group(1)] = {"source_id": sid,
                               "anchor": unquote(am.group(1)) if am else None}
    return out


def cmd_coverage(args: argparse.Namespace) -> int:
    root = pathlib.Path(args.root).resolve()
    f = merge_files(root, pathlib.Path(args.merge))
    rep = Report()

    D = load_any(f["decisions"])
    rules = {r["id"]: r for r in D["rules"]}
    units = parse_units(pathlib.Path(args.units))
    cov = []
    for line in pathlib.Path(args.coverage).read_text(encoding="utf-8").splitlines():
        m = COVERAGE_ROW.match(line)
        if m:
            cov.append((m.group(1), m.group(2).strip(), m.group(3).strip(),
                        m.group(4), m.group(5).strip()))

    # 单元 id 的来源简称 -> source_id，从单元清单反推，不写死
    abbr = {u.split("-")[1]: v["source_id"] for u, v in units.items()}

    print("=" * 70)
    print("3.1 单元清单")
    print("=" * 70)
    print(f"  单元 {len(units)} 条:", dict(collections.Counter(u["source_id"] for u in units.values())))
    noanchor = [k for k, v in units.items() if not v["anchor"]]
    if noanchor:
        rep.add("MED", f"{len(noanchor)} 条单元解析不到 anchor: {noanchor[:10]}")

    print("=" * 70)
    print("3.2 覆盖：每条单元恰好归入一条规则")
    print("=" * 70)
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

    print("=" * 70)
    print("3.3 覆盖表的规则 id 与 decisions.yaml")
    print("=" * 70)
    unknown = sorted({c[3] for c in cov} - set(rules))
    if unknown:
        rep.add("BLOCK", f"覆盖表里的未知规则 id: {unknown}")
    unused = sorted(set(rules) - {c[3] for c in cov})
    if unused:
        rep.add("HIGH", f"decisions.yaml 里没有任何单元归属的规则: {unused}")
    if not (unknown or unused):
        rep.ok("规则 id 双向对得上")

    print("=" * 70)
    print("3.4 decision 列一致")
    print("=" * 70)
    bad = [(u, rid, d, rules[rid]["decision"]) for u, _, _, rid, d in cov
           if rid in rules and d != rules[rid]["decision"]]
    for b in bad:
        rep.add("HIGH", f"{b[0]} -> {b[1]}: 覆盖表写 {b[2]}，decisions.yaml 是 {b[3]}")
    if not bad:
        rep.ok("decision 列全部一致")

    print("=" * 70)
    print("3.5 成员单元数与 evidence_count / 来源分布")
    print("=" * 70)
    members: dict[str, list[str]] = collections.defaultdict(list)
    for u, _, _, rid, _ in cov:
        members[rid].append(u)
    bad_n = [(rid, len(members.get(rid, [])), r["evidence_count"]) for rid, r in rules.items()
             if len(members.get(rid, [])) != r["evidence_count"]]
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

    print("=" * 70)
    print("3.6 三处 anchor 一致")
    print("=" * 70)
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

    if args.clusters:
        print("=" * 70)
        print("3.7 聚类表与覆盖表")
        print("=" * 70)
        clusters: dict[str, list[str]] = collections.defaultdict(list)
        for line in pathlib.Path(args.clusters).read_text(encoding="utf-8").splitlines():
            m = CLUSTER_ROW.match(line)
            if m:
                clusters[m.group(1)].extend(re.findall(r"U-[a-z]+-\d{3}", m.group(2)))
        bad_c = [(rid, sorted(set(clusters.get(rid, []))), sorted(set(members.get(rid, []))))
                 for rid in sorted(set(clusters) | set(members))
                 if sorted(set(clusters.get(rid, []))) != sorted(set(members.get(rid, [])))]
        for rid, a, b in bad_c:
            rep.add("HIGH", f"{rid}: 聚类表 {a}，覆盖表 {b}")
        if not bad_c:
            rep.ok(f"{len(clusters)} 个簇与覆盖表一致")

    return rep.summary()


# ---------------------------------------------------------------- CLI

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p: argparse.ArgumentParser) -> None:
        p.add_argument("--root", default=".", help="仓库根目录，默认当前目录")
        p.add_argument("--merge", required=True, help="merge 实例目录，例如 merges/maybe-humanizer")

    p1 = sub.add_parser("format", help="schema、交叉引用、id、local.anchor、relations")
    common(p1)
    p1.add_argument("--schemas", help="schema 目录，默认 <root>/tools/upstream-monitor/schemas")
    p1.add_argument("--catalog-dir", help="catalog 目录，默认 <root>/catalog")
    p1.set_defaults(func=cmd_format)

    p2 = sub.add_parser("anchors", help="上游证据 anchor 能否在快照里定位")
    common(p2)
    p2.add_argument("--fetch-dir", help="metadata-only 来源的临时拉取目录（仓库之外）")
    p2.set_defaults(func=cmd_anchors)

    p3 = sub.add_parser("coverage", help="单元清单、覆盖表、聚类表与 decisions.yaml 的一致性")
    common(p3)
    p3.add_argument("--units", required=True, help="单元清单目录，每个来源一份 <source_id>.md")
    p3.add_argument("--coverage", required=True, help="覆盖表 markdown 文件")
    p3.add_argument("--clusters", help="聚类表 markdown 文件，可选")
    p3.set_defaults(func=cmd_coverage)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
