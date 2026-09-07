"""`upstream-monitor validate` 的实现。

吸收 prototype/check_merge.py 的 format、anchors、coverage 三项，再加：

- catalog 与 skills/、merges/ 的三方一致性：catalog 的 path 目录存在；
  merge_instance 非空则该目录存在，且其 sources.yaml 的 merge_id 与目录名一致。
- main 分支上不允许存在 decision_origin 为 model-proposed 的规则。

decisions.yaml 是否存在决定校验范围：没有这份文件的实例（以后的 merge 实例
不再产出它，见 README）只校验 catalog、sources.yaml、lock 的 schema 和三方
一致性，跳过全部规则/证据/覆盖相关检查，不因为文件缺失而报错；有的话行为
不变。
"""
from __future__ import annotations

import collections
import re
from pathlib import Path

from upstream_monitor.anchors import locate
from upstream_monitor.coverage import check_coverage
from upstream_monitor.diagnostics import Report
from upstream_monitor.github_client import FileNotFound, GitHubClient, NetworkError, RepoNotFound, RepoPrivate
from upstream_monitor.gitutil import current_branch
from upstream_monitor.paths import RepoPaths
from upstream_monitor.schemas import iter_errors
from upstream_monitor.yamlio import load_json, load_yaml

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


def _validate_schema_one(schemas_dir: Path, name: str, target: Path, rep: Report) -> None:
    if not target.exists():
        rep.add("BLOCK", f"文件不存在: {target}")
        return
    doc = load_yaml(target) if target.suffix in (".yaml", ".yml") else load_json(target)
    errs = iter_errors(schemas_dir, name, doc)
    if errs:
        for e in errs:
            rep.add("BLOCK", f"schema 失败 {target}: {e}")
    else:
        rep.ok(f"{target} 通过 schema 校验")


def validate_schema(paths: RepoPaths, merge_id: str, rep: Report, has_decisions: bool = True) -> None:
    f = {
        "sources": paths.sources_yaml(merge_id),
        "lock": paths.lock_json(merge_id),
    }
    for catalog_file in paths.catalog_entries():
        _validate_schema_one(paths.schemas_dir, "catalog", catalog_file, rep)
    _validate_schema_one(paths.schemas_dir, "sources", f["sources"], rep)
    _validate_schema_one(paths.schemas_dir, "lock", f["lock"], rep)
    if has_decisions:
        _validate_schema_one(paths.schemas_dir, "decisions", paths.decisions_yaml(merge_id), rep)


def validate_cross_refs(paths: RepoPaths, merge_id: str, rep: Report) -> dict:
    """返回已加载的三份文档，供后续检查复用。"""
    D = load_yaml(paths.decisions_yaml(merge_id))
    S = load_yaml(paths.sources_yaml(merge_id))
    L = load_json(paths.lock_json(merge_id))
    rules = D["rules"]

    if not (D["merge_id"] == S["merge_id"] == L["merge_id"] == merge_id):
        rep.add(
            "BLOCK",
            f"{merge_id}: merge_id 不一致: decisions={D['merge_id']} sources={S['merge_id']} "
            f"lock={L['merge_id']} dir={merge_id}",
        )
    else:
        rep.ok(f"{merge_id}: merge_id 一致")

    src_by_id = {s["id"]: s for s in S["sources"]}
    lineage_of = {s["id"]: s["lineage"] for s in S["sources"]}
    bad = {
        (r["id"], ev["source_id"])
        for r in rules
        for ev in r["sources"]
        if ev["type"] == "upstream" and ev["source_id"] not in src_by_id
    }
    for rid, sid in sorted(bad):
        rep.add("BLOCK", f"{merge_id}/{rid}: source_id 不在 sources.yaml: {sid}")
    if not bad:
        rep.ok(f"{merge_id}: 全部 source_id 都在 sources.yaml")
    if set(L["sources"]) != set(src_by_id):
        rep.add(
            "HIGH",
            f"{merge_id}: lock 与 sources 的 id 集合不一致: "
            f"lock only={set(L['sources']) - set(src_by_id)} "
            f"sources only={set(src_by_id) - set(L['sources'])}",
        )
    else:
        rep.ok(f"{merge_id}: lock 与 sources id 集合一致")

    bad_ec = [
        (r["id"], r["evidence_count"], len(r["sources"]))
        for r in rules
        if r["evidence_count"] != len(r["sources"])
    ]
    for rid, ec, n in bad_ec:
        rep.add("HIGH", f"{merge_id}/{rid}: evidence_count={ec} 但 sources 长度={n}")
    if not bad_ec:
        rep.ok(f"{merge_id}: evidence_count 全部一致")

    bad_is = []
    for r in rules:
        lins = {
            lineage_of.get(ev["source_id"], f"?{ev['source_id']}") if ev["type"] == "upstream" else "self"
            for ev in r["sources"]
        }
        if r["independent_sources"] != len(lins):
            bad_is.append((r["id"], r["independent_sources"], len(lins), sorted(lins)))
    for rid, got, exp, lins in bad_is:
        rep.add("HIGH", f"{merge_id}/{rid}: independent_sources={got} 但去重 lineage 数={exp} {lins}")
    if not bad_is:
        rep.ok(f"{merge_id}: independent_sources 全部一致")

    return {"decisions": D, "sources": S, "lock": L}


def validate_sources_lock_only(paths: RepoPaths, merge_id: str, rep: Report) -> None:
    """没有 decisions.yaml 的实例：只核对 sources.yaml 与 lock 的 merge_id 和
    来源 id 集合是否一致，不涉及任何规则/证据层面的检查。"""
    S = load_yaml(paths.sources_yaml(merge_id))
    L = load_json(paths.lock_json(merge_id))
    if not (S["merge_id"] == L["merge_id"] == merge_id):
        rep.add(
            "BLOCK",
            f"{merge_id}: merge_id 不一致: sources={S['merge_id']} lock={L['merge_id']} dir={merge_id}",
        )
    else:
        rep.ok(f"{merge_id}: merge_id 一致（sources、lock；没有 decisions.yaml）")

    src_by_id = {s["id"]: s for s in S["sources"]}
    if set(L["sources"]) != set(src_by_id):
        rep.add(
            "HIGH",
            f"{merge_id}: lock 与 sources 的 id 集合不一致: "
            f"lock only={set(L['sources']) - set(src_by_id)} "
            f"sources only={set(src_by_id) - set(L['sources'])}",
        )
    else:
        rep.ok(f"{merge_id}: lock 与 sources id 集合一致")


def validate_rule_ids(merge_id: str, rules: list[dict], rep: Report) -> None:
    dups = [k for k, v in collections.Counter(r["id"] for r in rules).items() if v > 1]
    if dups:
        rep.add("BLOCK", f"{merge_id}: 重复的规则 id: {dups}")
    else:
        rep.ok(f"{merge_id}: {len(rules)} 个规则 id 唯一")

    groups: dict[tuple[str, str], list[int]] = collections.defaultdict(list)
    for r in rules:
        m = RULE_ID.match(r["id"])
        if not m:
            rep.add("BLOCK", f"{merge_id}/{r['id']}: id 不符合 extraction.md 的前缀/类别码格式")
            continue
        pre, code, num = m.groups()
        if pre != LANG_PREFIX[r["language"]]:
            rep.add("HIGH", f"{merge_id}/{r['id']}: 前缀 {pre} 与 language={r['language']} 不符")
        if code != CAT_CODE[r["category"]]:
            rep.add("HIGH", f"{merge_id}/{r['id']}: 类别码 {code} 与 category={r['category']} 不符")
        groups[(pre, code)].append(int(num))
    for g, nums in sorted(groups.items()):
        if sorted(nums) != list(range(1, len(nums) + 1)):
            rep.add("MED", f"{merge_id}/{g[0]}-{g[1]}-: 编号不是从 001 起连续递增，实际 {sorted(nums)}")


def validate_local_anchors(root: Path, merge_id: str, rules: list[dict], rep: Report) -> None:
    cache: dict[str, str | None] = {}
    for r in rules:
        rel, anc = r["local"]["path"], r["local"]["anchor"]
        if rel not in cache:
            p = root / rel
            cache[rel] = p.read_text(encoding="utf-8") if p.exists() else None
        txt = cache[rel]
        landed = r["decision"] in LANDED
        if txt is None:
            rep.add("BLOCK", f"{merge_id}/{r['id']} ({r['decision']}): local.path 不存在 {rel}")
            continue
        if anc is None:
            if landed:
                rep.add("BLOCK", f"{merge_id}/{r['id']} ({r['decision']}): 已落地规则的 local.anchor 为 null")
            continue
        n = txt.count(anc)
        if n == 0:
            rep.add(
                "BLOCK" if landed else "HIGH",
                f"{merge_id}/{r['id']} ({r['decision']}): anchor 在 {rel} 中找不到: {anc!r}",
            )
        elif n > 1:
            rep.add(
                "HIGH" if landed else "MED",
                f"{merge_id}/{r['id']} ({r['decision']}): anchor 在 {rel} 中命中 {n} 次: {anc!r}",
            )


def validate_history(merge_id: str, rules: list[dict], rep: Report) -> None:
    no_hist = [r["id"] for r in rules if not r.get("history")]
    if no_hist:
        rep.add("MED", f"{merge_id}: {len(no_hist)} 条没有 history: {no_hist[:10]}")
    mism = [r["id"] for r in rules if r.get("history") and r["history"][-1]["decision"] != r["decision"]]
    if mism:
        rep.add("HIGH", f"{merge_id}: history 末条与当前 decision 不一致: {mism}")
    else:
        rep.ok(f"{merge_id}: history 末条与当前 decision 一致")
    badrev = [r["id"] for r in rules if r.get("history") and len(r["history"]) != r["decision_revision"]]
    if badrev:
        rep.add("MED", f"{merge_id}: decision_revision 与 history 长度不符: {badrev[:10]}（共 {len(badrev)}）")
    else:
        rep.ok(f"{merge_id}: decision_revision 与 history 长度一致")


def validate_relations(merge_id: str, rules: list[dict], rep: Report) -> None:
    ids = {r["id"] for r in rules}
    edges: dict[str, set[tuple[str, str]]] = collections.defaultdict(set)
    for r in rules:
        seen = set()
        for e in r.get("relations", []):
            key = (e["type"], e["rule_id"])
            if key in seen:
                rep.add("MED", f"{merge_id}/{r['id']}: relations 里有重复的 {e['type']} -> {e['rule_id']}")
            seen.add(key)
            if e["rule_id"] == r["id"]:
                rep.add("HIGH", f"{merge_id}/{r['id']}: relations 指向自己")
            elif e["rule_id"] not in ids:
                rep.add("BLOCK", f"{merge_id}/{r['id']}: relations 的 rule_id 不存在: {e['rule_id']}")
            edges[e["type"]].add((r["id"], e["rule_id"]))
    oneway = [(t, a, b) for t in SYMMETRIC for a, b in edges[t] if (b, a) not in edges[t]]
    for t, a, b in sorted(oneway):
        rep.add("HIGH", f"{merge_id}: {t} 是单向的: {a} 指向 {b}，但 {b} 没有指回 {a}")
    if not oneway:
        rep.ok(f"{merge_id}: conflicts-with 与 pairs-with 全部双向")


def validate_shared_evidence_anchors(merge_id: str, rules: list[dict], rep: Report) -> None:
    """同一条规则的多条证据若 (path, anchor) 完全相同，说明共用锚点没有加各自的行首文本区分。"""
    found = False
    for r in rules:
        counts = collections.Counter(
            (ev["path"], ev["anchor"]) for ev in r["sources"] if ev.get("anchor")
        )
        for (path, anchor), n in sorted(counts.items()):
            if n > 1:
                found = True
                rep.add(
                    "MED",
                    f"{merge_id}/{r['id']}: {n} 条证据共用同一个 (path, anchor)：{path!r} {anchor!r}，"
                    f"共用锚点要加各自行首文本",
                )
    if not found:
        rep.ok(f"{merge_id}: 同一规则内没有证据共用 (path, anchor)")


RATIONALE_RELATION_MENTION = re.compile(
    r"与\s*((?:ZH|EN|ALL)-[A-Z]{1,5}-\d{3})\s*(?:冲突|互补|例外|取代)"
)


def validate_rationale_relations(merge_id: str, rules: list[dict], rep: Report) -> None:
    """rationale 里点名"与 <规则 id> 冲突/互补/例外/取代"，relations 里必须有一条指向该 id。"""
    found = False
    for r in rules:
        mentioned = set(RATIONALE_RELATION_MENTION.findall(r.get("rationale") or ""))
        related_ids = {e["rule_id"] for e in r.get("relations", [])}
        for other_id in sorted(mentioned - related_ids):
            found = True
            rep.add(
                "HIGH",
                f"{merge_id}/{r['id']}: rationale 提到与 {other_id} 冲突/互补/例外/取代，"
                f"但 relations 里没有指向 {other_id} 的条目",
            )
    if not found:
        rep.ok(f"{merge_id}: rationale 里点名的规则关系都已在 relations 里落地")


def validate_upstream_anchors(
    root: Path, merge_id: str, docs: dict, rep: Report, client: GitHubClient | None
) -> None:
    D, S, L = docs["decisions"], docs["sources"], docs["lock"]
    src_by_id = {s["id"]: s for s in S["sources"]}
    stored = {
        (sid, fe["original_path"]): fe["stored_path"]
        for sid, entry in L["sources"].items()
        for fe in entry["files"]
    }
    cache: dict[tuple[str, str], tuple[str | None, str]] = {}

    def text_for(sid: str, path: str) -> tuple[str | None, str]:
        key = (sid, path)
        if key in cache:
            return cache[key]
        sp = stored.get(key, "MISSING")
        if sp == "MISSING":
            result = (None, "lock 的 files[] 里没有这个路径")
            cache[key] = result
            return result
        if sp is None:
            if client is None:
                result = (None, "metadata-only，未提供 GitHub client")
                cache[key] = result
                return result
            repo = src_by_id[sid]["repository"]
            commit = L["sources"][sid]["last_seen_commit"]
            try:
                content = client.get_file(repo, path, commit)
            except (FileNotFound, RepoNotFound, RepoPrivate, NetworkError) as e:
                result = (None, f"拉取失败: {e}")
                cache[key] = result
                return result
            text = content.decode("utf-8", errors="replace")
            result = (text, f"{repo}@{commit}:{path}")
            cache[key] = result
            return result
        p = root / sp
        text = p.read_text(encoding="utf-8") if p.exists() else None
        result = (text, str(p))
        cache[key] = result
        return result

    for r in D["rules"]:
        for ev in r["sources"]:
            if ev["type"] != "upstream":
                continue
            sid, path = ev["source_id"], ev["path"]
            if sid not in src_by_id:
                continue  # 已经在 cross_refs 里报过
            if path not in src_by_id[sid]["paths"]:
                rep.add("HIGH", f"{merge_id}/{r['id']}: 证据路径不在 sources.yaml 的 paths 里: {sid}:{path}")
            want = L["sources"][sid]["last_seen_commit"]
            if ev["commit"] != want:
                rep.add("HIGH", f"{merge_id}/{r['id']}: commit {ev['commit']} 与 lock 的 {want} 不符")
            txt, where = text_for(sid, path)
            if txt is None:
                sev = "MED" if "metadata-only" in where or "拉取失败" in where else "HIGH"
                rep.add(sev, f"{merge_id}/{r['id']}: 拿不到上游正文（{sid}:{path}，{where}）")
                continue
            st, detail = locate(txt, ev["anchor"] or "")
            if st == "MISS":
                rep.add("HIGH", f"{merge_id}/{r['id']} ({sid}:{path}): anchor 定位不到 {ev['anchor']!r}；{detail}")
            elif st == "ambiguous":
                rep.add("MED", f"{merge_id}/{r['id']} ({sid}): 弱定位有歧义 {ev['anchor']!r}；{detail}")
            elif st in ("ok-substring", "weak-heading"):
                rep.add("LOW", f"{merge_id}/{r['id']} ({sid}): 弱定位 {ev['anchor']!r}；{detail}")


def validate_coverage_for_merge(paths: RepoPaths, merge_id: str, decisions: dict, rep: Report) -> None:
    work = paths.work_dir(merge_id)
    units_dir = work / "units"
    coverage_md = work / "coverage.md"
    clusters_md = work / "clusters.md"
    if not (units_dir.is_dir() and coverage_md.exists()):
        rep.add("LOW", f"{merge_id}: work/units 或 work/coverage.md 不存在，跳过覆盖校验")
        return
    check_coverage(decisions, units_dir, coverage_md, clusters_md if clusters_md.exists() else None, rep)


def validate_catalog_consistency(paths: RepoPaths, rep: Report) -> None:
    for cf in paths.catalog_entries():
        doc = load_yaml(cf)
        cid = doc.get("id", cf.stem)
        skill_dir = paths.root / doc["path"]
        if not skill_dir.is_dir():
            rep.add("BLOCK", f"catalog/{cid}: path 目录不存在: {doc['path']}")
        else:
            rep.ok(f"catalog/{cid}: path 目录存在")

        mi = doc.get("merge_instance")
        if mi:
            merge_dir = paths.root / mi
            if not merge_dir.is_dir():
                rep.add("BLOCK", f"catalog/{cid}: merge_instance 目录不存在: {mi}")
                continue
            sources_file = merge_dir / "sources.yaml"
            if not sources_file.exists():
                rep.add("BLOCK", f"catalog/{cid}: {mi}/sources.yaml 不存在")
                continue
            merge_id_in_sources = load_yaml(sources_file).get("merge_id")
            expected = Path(mi).name
            if merge_id_in_sources != expected:
                rep.add(
                    "BLOCK",
                    f"catalog/{cid}: {mi}/sources.yaml 的 merge_id={merge_id_in_sources!r} "
                    f"与目录名 {expected!r} 不一致",
                )
            else:
                rep.ok(f"catalog/{cid}: merge_instance 一致")


def validate_main_branch(
    paths: RepoPaths, merge_ids: list[str], branch_override: str | None, rep: Report
) -> None:
    branch = branch_override or current_branch(paths.root)
    if branch is None:
        rep.add("LOW", "无法确定当前 git 分支，跳过 main 分支上 model-proposed 的检查")
        return
    if branch != "main":
        return
    for mid in merge_ids:
        dpath = paths.decisions_yaml(mid)
        if not dpath.exists():
            continue
        D = load_yaml(dpath)
        offenders = [r["id"] for r in D["rules"] if r["decision_origin"] == "model-proposed"]
        if offenders:
            rep.add(
                "BLOCK",
                f"{mid}: main 分支上存在 decision_origin=model-proposed 的规则，"
                f"合并前必须先 approve: {offenders}",
            )


def validate(
    paths: RepoPaths,
    merge_id: str | None = None,
    branch: str | None = None,
    client: GitHubClient | None = None,
    check_upstream_anchors: bool = True,
) -> Report:
    rep = Report()

    if merge_id is None:
        validate_catalog_consistency(paths, rep)

    merge_ids = [merge_id] if merge_id else paths.merge_ids()
    for mid in merge_ids:
        has_decisions = paths.decisions_yaml(mid).exists()
        validate_schema(paths, mid, rep, has_decisions=has_decisions)
        if not has_decisions:
            # 以后的 merge 实例不再产出 decisions.yaml（见 tools/upstream-monitor/README.md），
            # 只校验 sources/lock 的 schema 和一致性，decisions 相关检查全部跳过，不报错。
            validate_sources_lock_only(paths, mid, rep)
            rep.ok(f"{mid}: 没有 decisions.yaml，跳过规则、证据、覆盖等 decisions 相关校验")
            continue
        docs = validate_cross_refs(paths, mid, rep)
        rules = docs["decisions"]["rules"]
        validate_rule_ids(mid, rules, rep)
        validate_local_anchors(paths.root, mid, rules, rep)
        validate_history(mid, rules, rep)
        validate_relations(mid, rules, rep)
        validate_shared_evidence_anchors(mid, rules, rep)
        validate_rationale_relations(mid, rules, rep)
        if check_upstream_anchors:
            validate_upstream_anchors(paths.root, mid, docs, rep, client)
        validate_coverage_for_merge(paths, mid, docs["decisions"], rep)

    validate_main_branch(paths, merge_ids, branch, rep)
    return rep
