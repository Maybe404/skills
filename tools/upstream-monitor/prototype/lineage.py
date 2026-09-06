#!/usr/bin/env python3
"""入围阶段的谱系聚类：把 sources.yaml 里的候选来源按同源关系分组。

用途见 skills/skill-merge/references/process.md 步骤 1 第 2 条："按 lineage
聚类。判断同源的依据：fork 关系、README 里写明的改编来源、SKILL.md 的小节
结构和模式表条目高度重合。"本脚本只算出候选分组和相似度证据，不改写
sources.yaml——lineage、selection_status 是否采纳由人工写回。

三类信号，任何一类满足即合并：

1. **文本相似度**：读每个来源的"SKILL 主文件"（paths 里第一个以 SKILL.md
   结尾的路径；source_type 为 github-prompt 时用 README.md），按
   upstream_monitor.normalize 的同一套归一化规则处理后，用标准库
   difflib.SequenceMatcher.ratio() 两两比较。选 difflib 而不是字符 n-gram
   Jaccard，是因为仓库里 diff.py 已经用 difflib 做上游前后版本比对，两处用
   同一个相似度概念；ratio() 基于最长公共子序列，对整体结构（小节顺序、
   模式编号）比无序的 n-gram 集合更敏感，这正是判断"同一份表格改写/翻译
   而来"时最有区分度的信号。
   这个信号只对同语言的两份文本有效：中文译文和英文原文逐字比较时
   ratio() 几乎恒为 0，检测不出翻译关系，见下一类信号。
2. **fork 关系**：来自 evidence.json 的 parent 字段（GitHub API 记录的
   fork 上游），或人工核实到的 git fork 关系。
3. **人工核实的跨语言改编**：翻译、本地化声明只有配合章节结构、模式编号
   的实际比对（人工读一遍两份 SKILL.md 的标题列表）才可信——仅仅"参考了
   同一篇 Wikipedia 词条"不构成同源，这与仓库里 upstream-aboudjem-humanizer-skill
   现有条目的结论一致（该条目与 blader/humanizer 同样引用 Wikipedia，但
   核实为独立作品）。这类关系写在 KNOWN_RELATIONS 里，每条附一句人工判断
   依据，供复核。

阈值：--threshold 默认 0.55。选这个值是因为同语言的直接翻译/复制版本
（如 hairyf/skills 的 writing-humanizer-zh 抄自 op7418/Humanizer-zh）的
ratio 在 0.9 以上，结构相近但独立扩写的版本（如 z0gSh1u 的 humanizer-cn，
增删了部分小节）落在 0.6-0.85，完全独立的作品普遍低于 0.3；0.55 卡在两者
之间，宁可漏判（留给人工在 notes 里核实）也不错判独立作品为同源。

用法：

    python3 tools/upstream-monitor/prototype/lineage.py \\
        --root . --merge merges/maybe-humanizer \\
        --scratch-dir <metadata-only 来源的临时抓取目录> \\
        [--threshold 0.55] [--known-relations known_relations.json]

输出到 stdout：每个簇的成员、簇内最小相似度、簇间最大相似度、以及每条
KNOWN_RELATIONS 是否在自动聚类结果之外新增了什么。不写任何文件。
"""
from __future__ import annotations

import argparse
import difflib
import itertools
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from upstream_monitor.normalize import normalize_bytes  # noqa: E402
from upstream_monitor.yamlio import load_yaml  # noqa: E402


# ---------------------------------------------------------------------------
# 人工核实的跨语言/跨仓库同源关系。text 相似度信号覆盖不到的关系写在这里，
# 每条必须附 evidence：要么是 GitHub fork 关系，要么是人工比对过章节结构
# 和模式编号之后的结论。不满足"结构高度重合"的，即使 README 自称
# "基于/参考了某项目"，也不进这张表——见模块 docstring 第 3 类信号的说明。
# ---------------------------------------------------------------------------
KNOWN_RELATIONS: list[dict] = [
    {
        "a": "upstream-kevintsai1202-humanizer-zh-tw",
        "b": "upstream-op7418-humanizer-zh",
        "relation": "fork",
        "evidence": "GitHub API repos/kevintsai1202/Humanizer-zh-TW 的 parent 字段为 op7418/Humanizer-zh。",
    },
    {
        "a": "upstream-op7418-humanizer-zh",
        "b": "upstream-blader-humanizer",
        "relation": "translation",
        "evidence": (
            "人工比对 SKILL.md 标题列表：op7418 的 24 条模式与 blader 的 35 条模式中前 24 条"
            "（Content/Language and grammar/Style/Chatbot/Filler 五个分组）逐条一一对应、顺序相同，"
            "是同一份模式表的翻译。op7418 在译文之外新增了'核心规则速查''质量评分''完整示例'等小节，"
            "属于翻译基础上的增补，不是纯措辞差异，见 sources.yaml 里的 selection_status 说明。"
        ),
    },
    {
        "a": "upstream-hairyf-skills",
        "b": "upstream-op7418-humanizer-zh",
        "relation": "copy",
        "evidence": (
            "人工比对 SKILL.md 标题列表：hairyf/skills 的 skills/writing-humanizer-zh/SKILL.md 与"
            "op7418/Humanizer-zh 的标题、模式编号、小节顺序逐字相同（包括'快速检查清单''质量评分'等"
            "op7418 独有的增补小节），判定为直接复制，非独立翻译。"
        ),
    },
    {
        "a": "upstream-z0gsh1u-oh-my-writing-skill",
        "b": "upstream-op7418-humanizer-zh",
        "relation": "translation-derivative",
        "evidence": (
            "人工比对标题列表：z0gSh1u 的 humanizer-cn 与 op7418 分组结构相同（内容模式/语言和语法模式/"
            "风格模式/交流模式/填充和模糊），模式编号从 24 条精简为 22 条，且没有 op7418 的'质量评分'"
            "小节，是同一谱系内容量更小的版本，不是独立扩写。"
        ),
    },
    {
        "a": "upstream-z123-cloud-humanizer",
        "b": "upstream-lifelonglazylearner-qu-ai-wei",
        "relation": "copy",
        "evidence": (
            "人工读取内容：z123-cloud/humanizer 的 SKILL.md frontmatter name 字段为'qu-ai-wei'、"
            "version '0.7.0'，description 与 LifelongLazyLearner/qu-ai-wei 的'不虚构事实，让终稿干净、"
            "精准''冲突仲裁顺序六级''强制附打磨报告'等措辞高度重合，判定为同一内容的复制/未同步 fork，"
            "而非独立的'humanizer'项目（仓库名和实际内容不符）。"
        ),
    },
]


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


def snapshot_path_for(root: Path, merge: str, source_id: str, primary_path: str) -> Path:
    if primary_path.endswith("SKILL.md"):
        stored_rel = primary_path[: -len("SKILL.md")] + "SKILL.source.md"
    else:
        stored_rel = primary_path
    return root / "merges" / merge / "snapshots" / source_id / stored_rel


def load_text(root: Path, merge: str, scratch_dir: Path | None, source: dict) -> tuple[str | None, str]:
    """返回 (归一化后的文本或 None, 读取说明)。"""
    primary = resolve_primary_path(source)
    if primary is None:
        return None, "无 paths，跳过"
    sid = source["id"]
    if source["snapshot_policy"] == "full-text":
        fp = snapshot_path_for(root, merge, sid, primary)
        if not fp.exists():
            return None, f"快照缺失: {fp}"
        raw = fp.read_bytes()
        return normalize_bytes(raw).decode("utf-8", errors="replace"), f"snapshots/{sid}/{primary}"
    else:
        if scratch_dir is None:
            return None, "metadata-only 且未提供 --scratch-dir，跳过"
        fp = scratch_dir / sid / primary
        if not fp.exists():
            return None, f"scratch 缺失: {fp}"
        raw = fp.read_bytes()
        return normalize_bytes(raw).decode("utf-8", errors="replace"), f"[metadata-only,不落盘] {sid}/{primary}"


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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--merge", required=True, help="merges/<merge> 的 <merge> 部分，例如 maybe-humanizer")
    ap.add_argument("--scratch-dir", default=None, help="metadata-only 来源的临时抓取目录，结构为 <dir>/<source_id>/<original_path>")
    ap.add_argument("--threshold", type=float, default=0.55)
    ap.add_argument("--known-relations", default=None, help="额外的人工核实关系 JSON 文件，格式同脚本内 KNOWN_RELATIONS")
    ap.add_argument("--json", default=None, help="把完整相似度矩阵和聚类结果写到这个路径（JSON），仅用于人工复核，不进正式产出")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    scratch_dir = Path(args.scratch_dir).resolve() if args.scratch_dir else None
    sources_yaml = root / "merges" / args.merge / "sources.yaml"
    doc = load_yaml(sources_yaml)
    sources = {s["id"]: s for s in doc["sources"] if s.get("status") != "removed"}

    texts: dict[str, str] = {}
    skipped: dict[str, str] = {}
    for sid, s in sources.items():
        text, info = load_text(root, args.merge, scratch_dir, s)
        if text is None:
            skipped[sid] = info
        else:
            texts[sid] = text

    ids = sorted(texts.keys())
    ratio: dict[tuple[str, str], float] = {}
    for a, b in itertools.combinations(ids, 2):
        r = difflib.SequenceMatcher(None, texts[a], texts[b]).ratio()
        ratio[(a, b)] = r

    known = list(KNOWN_RELATIONS)
    if args.known_relations:
        known.extend(json.loads(Path(args.known_relations).read_text(encoding="utf-8")))

    uf = UnionFind(list(sources.keys()))
    forced_edges: list[tuple[str, str, float | None]] = []
    for a, b in itertools.combinations(ids, 2):
        if ratio[(a, b)] >= args.threshold:
            uf.union(a, b)
    for rel in known:
        a, b = rel["a"], rel["b"]
        if a in sources and b in sources:
            uf.union(a, b)
            forced_edges.append((a, b, ratio.get((a, b)) or ratio.get((b, a))))

    clusters: dict[str, list[str]] = {}
    for sid in sources:
        root_id = uf.find(sid)
        clusters.setdefault(root_id, []).append(sid)

    print(f"# 谱系聚类结果  (merge={args.merge}, threshold={args.threshold})")
    print(f"参与比较的来源：{len(sources)}，可读到文本：{len(texts)}，跳过：{len(skipped)}")
    if skipped:
        print("跳过明细：")
        for sid, reason in sorted(skipped.items()):
            print(f"  - {sid}: {reason}")
    print()

    print("## 人工核实的跨语言/跨仓库关系 (KNOWN_RELATIONS)")
    for a, b, r in forced_edges:
        r_str = f"{r:.3f}" if r is not None else "n/a（至少一侧无正文可比）"
        print(f"  - {a}  <->  {b}   自动 ratio={r_str}")
    print()

    print(f"## 簇（共 {len(clusters)} 个，仅列成员数 >= 1；>1 的才是本轮真正的聚类）")
    cluster_list = sorted(clusters.values(), key=lambda m: (-len(m), m[0]))
    for members in cluster_list:
        members_sorted = sorted(members)
        if len(members_sorted) == 1:
            continue
        print(f"\n### 簇：{members_sorted[0]} 等 {len(members_sorted)} 个")
        for m in members_sorted:
            print(f"  - {m}")
        pair_ratios = [
            ratio.get((a, b)) or ratio.get((b, a))
            for a, b in itertools.combinations(members_sorted, 2)
            if (a in texts and b in texts)
        ]
        pair_ratios = [r for r in pair_ratios if r is not None]
        if pair_ratios:
            print(f"  簇内最小相似度: {min(pair_ratios):.3f}   簇内最大相似度: {max(pair_ratios):.3f}")
        else:
            print("  簇内相似度: 至少一个成员无正文可比（fork/人工关系判定）")

    singletons = [m[0] for m in cluster_list if len(m) == 1]
    print(f"\n## 未与任何来源同簇的单例（{len(singletons)} 个）")
    for sid in sorted(singletons):
        print(f"  - {sid}")

    # 簇间最大相似度：任取不同簇的两个成员里相似度最高的一对，用来检验阈值是否卡在合适的位置。
    max_inter = 0.0
    max_inter_pair = None
    root_of = {sid: uf.find(sid) for sid in sources}
    for a, b in itertools.combinations(ids, 2):
        if root_of[a] != root_of[b]:
            r = ratio[(a, b)]
            if r > max_inter:
                max_inter = r
                max_inter_pair = (a, b)
    print(f"\n## 簇间最大相似度（应明显低于阈值 {args.threshold}，否则说明阈值可能偏低）")
    if max_inter_pair:
        print(f"  {max_inter_pair[0]}  <->  {max_inter_pair[1]}   ratio={max_inter:.3f}")
    else:
        print("  (不足两个簇，无法比较)")

    if args.json:
        out = {
            "threshold": args.threshold,
            "clusters": [sorted(m) for m in cluster_list],
            "ratio": {f"{a}|{b}": r for (a, b), r in ratio.items()},
            "skipped": skipped,
            "known_relations_applied": [{"a": a, "b": b, "ratio": r} for a, b, r in forced_edges],
        }
        Path(args.json).write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\n完整矩阵已写到 {args.json}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
