"""`upstream-monitor lineage` 的实现。

从 prototype/lineage.py 吸收：把 merges/<id>/sources.yaml 里未 removed 的
候选来源按同源关系聚类，供入围阶段判断谁是代表作、谁是衍生版本。语义
判断（选哪个做代表作、要不要采纳）不在这里，只算出候选分组和相似度证据；
`--write` 时把聚类结果写回 sources.yaml 的 `lineage` 字段，不改
`selection_status`——代表作由人定。

两类信号，任何一类满足即合并：

1. **文本相似度**：读每个来源的"SKILL 主文件"（paths 里第一个以 SKILL.md
   结尾的路径；source_type 为 github-prompt 时用 README.md），按
   upstream_monitor.normalize 的同一套归一化规则处理后，用标准库
   difflib.SequenceMatcher.ratio() 两两比较。选 difflib 而不是字符 n-gram
   Jaccard，是因为仓库里 diff.py 已经用 difflib 做上游前后版本比对，两处
   用同一个相似度概念；ratio() 基于最长公共子序列，对整体结构（小节顺序、
   模式编号）比无序的 n-gram 集合更敏感，这正是判断"同一份表格改写/翻译
   而来"时最有区分度的信号。这个信号只对同语言的两份文本有效：中文译文
   和英文原文逐字比较时 ratio() 几乎恒为 0，检测不出翻译关系，见下一类
   信号。只对 snapshot_policy 为 full-text 且已有 snapshots/ 快照的来源
   生效；metadata-only 或快照缺失的来源记入 skipped，不参与自动相似度。
2. **人工核实的关系**：读 merges/<id>/lineage-relations.yaml（不存在就
   跳过，只用自动相似度），格式为列表，每项 {from, to, relation, evidence}，
   relation 取 translation（翻译）、adaptation（结构相同的改编/精简）、
   fork（GitHub fork 关系）、copy（直接复制）之一，evidence 是一句人工
   判断依据。这类关系覆盖文本相似度信号覆盖不到的跨语言、跨仓库同源
   判断——翻译、改编只有配合章节结构、模式编号的实际比对才可信，仅仅
   "参考了同一篇文章"不构成同源。

阈值：--threshold 默认 0.55。选这个值是因为同语言的直接翻译/复制版本的
ratio 在 0.9 以上，结构相近但独立扩写的版本落在 0.6-0.85，完全独立的作品
普遍低于 0.3；0.55 卡在两者之间，宁可漏判（留给人工在 lineage-relations.yaml
里核实）也不错判独立作品为同源。

--write 时，同一簇的全部成员写入同一个 lineage 值：取簇内 source id 字典
序最小的一个，保证结果确定、可复现，不依赖聚类过程的遍历顺序。
"""
from __future__ import annotations

import difflib
import itertools
from pathlib import Path
from typing import Any

from upstream_monitor.normalize import normalize_bytes
from upstream_monitor.paths import RepoPaths
from upstream_monitor.schemas import validate_doc
from upstream_monitor.yamlio import dump_yaml, load_yaml

DEFAULT_THRESHOLD = 0.55
RELATION_KINDS = {"translation", "adaptation", "fork", "copy"}


def resolve_primary_path(source: dict) -> str | None:
    paths = source.get("paths") or []
    for p in paths:
        if p.endswith("SKILL.md"):
            return p
    if source.get("source_type") == "github-prompt":
        for p in paths:
            if p.endswith("README.md"):
                return p
    return paths[0] if paths else None


def snapshot_path_for(paths: RepoPaths, merge_id: str, source_id: str, primary_path: str) -> Path:
    if primary_path.endswith("SKILL.md"):
        stored_rel = primary_path[: -len("SKILL.md")] + "SKILL.source.md"
    else:
        stored_rel = primary_path
    return paths.snapshots_dir(merge_id) / source_id / stored_rel


def load_text(paths: RepoPaths, merge_id: str, source: dict) -> tuple[str | None, str]:
    """返回 (归一化后的文本或 None, 读取说明/跳过原因)。"""
    primary = resolve_primary_path(source)
    if primary is None:
        return None, "无 paths，跳过"
    sid = source["id"]
    if source.get("snapshot_policy") != "full-text":
        return None, "metadata-only，无快照可比，跳过"
    fp = snapshot_path_for(paths, merge_id, sid, primary)
    if not fp.exists():
        return None, f"快照缺失: {fp}"
    raw = fp.read_bytes()
    return normalize_bytes(raw).decode("utf-8", errors="replace"), f"snapshots/{sid}/{primary}"


class UnionFind:
    def __init__(self, items: list[str]) -> None:
        self.parent = {i: i for i in items}

    def find(self, x: str) -> str:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: str, b: str) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb


def load_relations(path: Path) -> list[dict]:
    """读 lineage-relations.yaml；文件不存在时返回空列表。"""
    if not path.exists():
        return []
    data = load_yaml(path) or []
    for item in data:
        relation = item.get("relation")
        if relation not in RELATION_KINDS:
            raise ValueError(
                f"{path}: 未知的 relation {relation!r}，必须是 {sorted(RELATION_KINDS)} 之一"
            )
        for key in ("from", "to", "evidence"):
            if not item.get(key):
                raise ValueError(f"{path}: 每项必须有 from、to、evidence，缺 {key!r}: {item!r}")
    return list(data)


def run_lineage(
    paths: RepoPaths,
    merge_id: str,
    threshold: float = DEFAULT_THRESHOLD,
    relations_path: Path | None = None,
    write: bool = False,
) -> dict[str, Any]:
    sources_path = paths.sources_yaml(merge_id)
    S = load_yaml(sources_path)
    sources = {s["id"]: s for s in S["sources"] if s.get("status") != "removed"}

    texts: dict[str, str] = {}
    skipped: dict[str, str] = {}
    for sid, s in sources.items():
        text, info = load_text(paths, merge_id, s)
        if text is None:
            skipped[sid] = info
        else:
            texts[sid] = text

    rel_path = relations_path or paths.lineage_relations_yaml(merge_id)
    relations = load_relations(rel_path)

    ids = sorted(texts.keys())
    ratio: dict[tuple[str, str], float] = {}
    for a, b in itertools.combinations(ids, 2):
        ratio[(a, b)] = difflib.SequenceMatcher(None, texts[a], texts[b]).ratio()

    uf = UnionFind(list(sources.keys()))
    for a, b in itertools.combinations(ids, 2):
        if ratio[(a, b)] >= threshold:
            uf.union(a, b)

    applied_relations: list[dict] = []
    for rel in relations:
        a, b = rel["from"], rel["to"]
        if a in sources and b in sources:
            uf.union(a, b)
            applied_relations.append(
                {
                    "from": a,
                    "to": b,
                    "relation": rel["relation"],
                    "evidence": rel["evidence"],
                    "auto_ratio": ratio.get((a, b), ratio.get((b, a))),
                }
            )

    clusters: dict[str, list[str]] = {}
    for sid in sources:
        clusters.setdefault(uf.find(sid), []).append(sid)
    cluster_list = sorted((sorted(members) for members in clusters.values()), key=lambda m: (-len(m), m[0]))

    lineage_of: dict[str, str] = {}
    for members in cluster_list:
        lineage_id = members[0]  # 簇内字典序最小的 id，确定、可复现
        for m in members:
            lineage_of[m] = lineage_id

    result: dict[str, Any] = {
        "merge_id": merge_id,
        "threshold": threshold,
        "relations_path": rel_path,
        "sources_count": len(sources),
        "texts_count": len(texts),
        "skipped": skipped,
        "clusters": cluster_list,
        "lineage_of": lineage_of,
        "ratio": ratio,
        "applied_relations": applied_relations,
        "written": False,
    }

    if write:
        new_sources = []
        for s in S["sources"]:
            s2 = dict(s)
            if s["id"] in lineage_of:
                s2["lineage"] = lineage_of[s["id"]]
            new_sources.append(s2)
        new_S = dict(S)
        new_S["sources"] = new_sources
        validate_doc(paths.schemas_dir, "sources", new_S, target=str(sources_path))
        dump_yaml(new_S, sources_path)
        result["written"] = True

    return result


def render_lineage_text(result: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"# 谱系聚类结果  (merge={result['merge_id']}, threshold={result['threshold']})")
    lines.append(
        f"参与比较的来源：{result['sources_count']}，可读到文本：{result['texts_count']}，"
        f"跳过：{len(result['skipped'])}"
    )
    if result["skipped"]:
        lines.append("跳过明细：")
        for sid, reason in sorted(result["skipped"].items()):
            lines.append(f"  - {sid}: {reason}")
    lines.append("")

    lines.append(f"## 人工核实关系（{result['relations_path']}）")
    if result["applied_relations"]:
        for rel in result["applied_relations"]:
            r = rel["auto_ratio"]
            r_str = f"{r:.3f}" if r is not None else "n/a（至少一侧无正文可比）"
            lines.append(
                f"  - {rel['from']}  --{rel['relation']}-->  {rel['to']}   "
                f"自动 ratio={r_str}   依据：{rel['evidence']}"
            )
    else:
        lines.append("  （无，或文件不存在）")
    lines.append("")

    multi = [m for m in result["clusters"] if len(m) > 1]
    lines.append(f"## 簇（共 {len(result['clusters'])} 个，仅列成员数 > 1 的 {len(multi)} 个）")
    for members in multi:
        lineage_id = result["lineage_of"][members[0]]
        lines.append(f"\n### 簇：{members[0]} 等 {len(members)} 个（lineage={lineage_id}）")
        for m in members:
            lines.append(f"  - {m}")
        pair_ratios = [
            result["ratio"].get((a, b)) or result["ratio"].get((b, a))
            for a, b in itertools.combinations(members, 2)
        ]
        pair_ratios = [r for r in pair_ratios if r is not None]
        if pair_ratios:
            lines.append(f"  簇内最小相似度: {min(pair_ratios):.3f}   簇内最大相似度: {max(pair_ratios):.3f}")
        else:
            lines.append("  簇内相似度: 至少一个成员无正文可比（fork/人工关系判定）")

    singletons = [m[0] for m in result["clusters"] if len(m) == 1]
    lines.append(f"\n## 未与任何来源同簇的单例（{len(singletons)} 个）")
    for sid in sorted(singletons):
        lines.append(f"  - {sid}")

    return "\n".join(lines)
