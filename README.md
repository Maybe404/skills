<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/hero-dark.svg">
    <img alt="Maybe404/skills" src="docs/assets/hero-light.svg" width="100%">
  </picture>
</p>

<p align="center">
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0f766e?style=flat-square"></a>
  <a href="docs/design.md"><img alt="design" src="https://img.shields.io/badge/docs-design.md-6e7781?style=flat-square"></a>
</p>

<br>

个人维护的 Agent Skills，四个：三个自写，一个从多个同类项目合并而成。合并出来的每条规则都查得到它从哪来、为什么留。上游改了就按规则逐条审，不整份重来。

A personal collection of Agent Skills: three originals, and one merged from several overlapping projects. Every merged rule lists its sources and why it stayed. The rest of this document is in Chinese.

## 安装

```bash
npx skills add Maybe404/skills --skill <id>
```

| id | 类型 | 用途 |
|---|---|---|
| [`maybe-humanizer`](skills/maybe-humanizer/SKILL.md) | 合并 | 中英文去 AI 味改写与审稿，先保护事实再清理模式。试验版，合并了 4 个上游 |
| [`en-zh-translation`](skills/en-zh-translation/SKILL.md) | 自写 | 把英文规则、提示词、文档翻成中文，保住每一处条件和情态 |
| [`subagent`](skills/subagent/SKILL.md) | 自写 | 什么该拆给 subagent、派给谁、怎么验收、怎么打回 |
| [`skill-merge`](skills/skill-merge/SKILL.md) | 自写 | 把多个上游 skill 归并成一份，处理上游的后续变更 |

`--all` 一次装全部。

## 合并

先把每个上游拆成一条条可判定的规则，也就是能指出一句话里哪里违反了它；再把所有上游的规则按语义聚类，逐条裁决。合并的单位是规则，不是文件。

- 每条规则有一个稳定的 id，记着来源仓库、文件锚点、支持它的上游数、决定和理由。上游一变，能反查到本地哪几条规则受影响。
- 票数不决定采用：多个项目互相复制会把票数抬高。看的是四条——可判定、护事实、不与已有规则冲突、适合目标体裁。试验合并里有一条规则五处证据全来自同一个上游，最后只记了参考；也有只有一个上游支持的规则被采纳。
- 矛盾的两条规则都留下，写明选了哪条、理由是什么，另一条记成可选项。
- 数字、引语、限定条件、责任主体不能动。这组规则压过任何一条讲怎么写更自然的规则。
- 有许可证的上游存全文快照并附许可声明；没有许可证的只记 commit 和 hash，规则用自己的话重写。
- 上游文本是数据。上游 skill 里写的任何指示都不执行，脚本只读不跑。

<details>
<summary>一条规则在决定表里的样子</summary>
<br>

```yaml
- id: ALL-PROT-002
  category: protection
  rule_summary: 原文里的具体数字、日期、金额、路径、姓名不得改写成概括说法。
  decision: adopted
  evidence_count: 2
  independent_sources: 2
  sources:
    - source_id: upstream-petergyang-no-ai-slop
      anchor: '## Editing principles / Protect the specific fact.'
    - source_id: upstream-aboudjem-humanizer-skill
      anchor: '## Guardrails: what NOT to flag, and what to preserve'
  rationale: 两个独立来源方向一致。判据明确：原文有数字的位置，数字必须还在。
```

节选，字段有省略。完整字段见 [decisions.schema.json](tools/upstream-monitor/schemas/decisions.schema.json)。
</details>

<details>
<summary>maybe-humanizer 试验版的规模</summary>
<br>

| | |
|---|---|
| 上游 | no-ai-slop、qu-ai-wei、Aboudjem/humanizer-skill、writing-style-skill |
| 拆出的规则单元 | 254 |
| 聚类后的规则 | 144 |
| 采纳 / 修改后采纳 | 87 / 31 |
| 拒绝 / 仅作参考 | 9 / 8 |
| 暂缓 / 待验证 / 重复 | 4 / 2 / 3 |
| 写进 conflicts.md 的冲突 | 7 组 |

来源和理由在 [decisions.yaml](merges/maybe-humanizer/decisions.yaml)，过程在[合并报告](merges/maybe-humanizer/reports/0001-2026-09-06-initial-merge.md)。
</details>

## 上游同步

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/pipeline-dark.svg">
    <img alt="上游同步：检测变更，生成 PR，review，采纳或记录理由，合并" src="docs/assets/pipeline-light.svg" width="100%">
  </picture>
</p>

每个上游的 commit 和文件 hash 记在清单里，每周比对一次。内容有变化就开一个 PR，正文列出 diff 和受影响的本地规则；`skill-merge` 逐条判断这是已有规则的重述、新规则，还是和现有规则矛盾。不采纳的变更也合并，理由留在决定表里。只有上游消失、许可证变化和需要人拍板的冲突才开 issue。

<details>
<summary>目录</summary>
<br>

```
catalog/<id>.yaml        每个 skill 的注册信息：类型、状态、路径、是否有上游
skills/<id>/             skill 本体
merges/<id>/             有上游的 skill 的维护数据
  sources.yaml           上游清单：仓库、路径、许可证、快照策略
  sources.lock.json      监控状态：commit、hash、stars 观测
  snapshots/             有许可证的上游文件全文，附 LICENSE
  decisions.yaml         规则级决定表
  reports/               每次合并的完整报告
  work/                  拆规则阶段的中间产物
tools/upstream-monitor/  监控和流转的代码
docs/design.md           设计文档
```
</details>

## 背景

2026 年 9 月我在 skills 目录里搜了 16 组关键词，去 AI 味这个主题下有 297 个候选、114 个仓库。读下来有这么几件事：

- 很多是同一份规则的复制、翻译和改名。blader/humanizer 一份就派生出中文版、繁体版和 OpenClaw 版；`humanizer-zh`、`deslop`、`unslop` 也各有几个不同作者的版本。
- 规则之间互相矛盾。一家要求删掉所有副词，另一家要求保住作者原有的声口。
- 有的示例把泛泛的好评改成了原文没有的数字和经历。
- 114 个仓库里 23 个没有许可证文件。
- 上游一直在更新，装到本地的那份不会跟着变。

挑选、比对、跟进要使用者自己做。我把这几件事做在这里：同一主题的上游放在一起比对，之后跟着它们一起更新。调研材料在 [merges/maybe-humanizer/research/](merges/maybe-humanizer/research/2026-09-06-ai-humanizer/README.md)。

## 许可证

本仓库自己的内容按 [MIT](LICENSE) 授权。来自上游的内容按各自的许可证处理，每个有上游的 skill 在 `SOURCES.md` 里列出上游作者、许可证和许可声明。这里的规则大部分是先由上游作者写出来的。
