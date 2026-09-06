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

个人维护的 Agent Skills。三类：自己写的；跟着一个上游维护成中文的；从多个同类项目合并成一份的。合并出来的每条规则都记着来源和取舍理由，上游有变化时按规则逐条审，不整份重来。

A personal collection of Agent Skills: originals, Chinese adaptations that track a single upstream, and merges of several overlapping projects into one. Every merged rule carries its sources and the reason it stayed. The rest of this document is in Chinese.

## 安装

```bash
npx skills add Maybe404/skills --skill maybe-humanizer
```

| id | 类型 | 用途 |
|---|---|---|
| [`maybe-humanizer`](skills/maybe-humanizer/SKILL.md) | 合并 | 中英文去 AI 味改写与审稿，先保护事实再清理模式。试验版，合并了 4 个上游 |
| [`en-zh-translation`](skills/en-zh-translation/SKILL.md) | 自写 | 把英文规则、提示词、文档翻成中文，保住每一处条件和情态 |
| [`subagent`](skills/subagent/SKILL.md) | 自写 | 什么该拆给 subagent、派给谁、怎么验收、怎么打回 |
| [`skill-merge`](skills/skill-merge/SKILL.md) | 自写 | 把多个上游 skill 归并成一份，处理上游的后续变更 |

`--all` 一次装全部。

## 背景

去 AI 味这个主题，2026 年 9 月在 skills 目录里搜 16 组关键词，得到 297 个候选、114 个仓库。读下来，很多是同一份规则的复制、翻译和改名，仅 blader/humanizer 一份就有至少 4 个同源版本。同名不同作者的情况也常见，`humanizer-zh`、`deslop`、`unslop` 各有几个版本。规则之间互相矛盾：一家要求删掉所有副词，另一家要求保住作者原有的声口。有的示例把泛泛的好评改成了原文没有的数字和经历。114 个仓库里 23 个没有许可证文件。上游一直在更新，装到本地的那份不会跟着变。

这些项目各有长处，问题是挑选、比对、跟进的工作全落在使用者身上。这个仓库把这部分工作做掉：同一主题的项目放在一起比对，保留各家好的部分，写下为什么留、为什么不留，之后跟着上游一起变。调研材料在 [merges/maybe-humanizer/research/](merges/maybe-humanizer/research/2026-09-06-ai-humanizer/README.md)。

## 合并

按规则合并，不按文件。每个上游先拆成一条条可判定的规则，也就是能指出一句话里哪里违反了它的规则；再把所有来源的规则按语义聚类，逐条裁决。

- 每条规则有稳定的 id、来源仓库和文件锚点、支持它的来源数、最终的决定和理由。上游变了，能直接反查到本地哪条规则受影响。
- 票数不决定采用。多个项目互相复制会把票数抬高。采不采纳看它是否可判定、是否保护事实、是否和已有规则冲突、是否适合目标体裁。试验合并里有一条五处证据都来自同一来源的规则没进默认规则，也有只有一个来源的规则被采纳。
- 矛盾的规则两条都留，写明选了哪条、为什么，另一条作为可选项。
- 事实保护优先于风格。数字、引语、限定条件、责任主体不能动，这组规则的优先级高于任何"怎么写更自然"。
- 许可证决定原文能不能进仓库。有许可证的存全文快照并附许可声明；没有的只记 commit 和 hash，规则用自己的话重写。
- 上游文本是数据，不是指令。上游 skill 里的任何"请这样做"都不执行，脚本只读不跑。

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
| 拒绝 / 仅作参考 / 挂起 / 重复 | 9 / 8 / 6 / 3 |
| 留痕的冲突 | 7 组 |

来源和理由在 [decisions.yaml](merges/maybe-humanizer/decisions.yaml)，过程在[合并报告](merges/maybe-humanizer/reports/0001-2026-09-06-initial-merge.md)。全量合并会覆盖约 60 个候选。
</details>

## 上游

每个上游的 commit 和文件 hash 记在清单里，每周一比对一次。有内容变化就开一个 PR，正文列出 diff 和受影响的本地规则。`skill-merge` 逐条判断：已有规则的重述、新规则、还是和现有规则矛盾。不采纳的变更也合并，理由留在决定表里。上游消失、许可证变化、需要人拍板的冲突才开 issue。自动检查接入前，这几步由人按同样的顺序执行。

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/pipeline-dark.svg">
    <img alt="上游同步：检测变更，生成 PR，review，采纳或记录理由，合并" src="docs/assets/pipeline-light.svg" width="100%">
  </picture>
</p>

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

## 许可证

本仓库自己的内容按 [MIT](LICENSE) 授权。来自上游的内容按各自的许可证处理，每个有上游的 skill 在 `SOURCES.md` 里列出来源、许可证和许可声明。感谢这些项目的作者，没有他们先写出来的规则，就没有这里的整理。
