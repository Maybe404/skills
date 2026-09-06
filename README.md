<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/hero-dark.svg">
    <img alt="Maybe404/skills：个人维护的 Agent Skills 集合" src="docs/assets/hero-light.svg" width="100%">
  </picture>
</p>

<p align="center">
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0f766e?style=flat-square"></a>
  <a href="docs/design.md"><img alt="design doc" src="https://img.shields.io/badge/docs-design.md-6e7781?style=flat-square"></a>
</p>

<p align="center">
  <code>npx skills add Maybe404/skills --skill &lt;id&gt;</code>
</p>

<br>

A personal collection of Agent Skills. Three kinds live here: skills written from scratch, skills that follow a single upstream and are kept current in Chinese, and skills merged from several overlapping projects into one. Every merged rule keeps a record of where it came from and why it stayed. Upstreams are meant to be checked every Monday, with changes arriving as pull requests and reviewed one rule at a time; the checking code is still being written, so this runs by hand for now.

<br>

## 为什么要做这个

想给 Claude 装一个“去 AI 味”的 skill，先搜了一圈。搜索 16 组关键词，拿到 297 个候选、114 个仓库地址。读下来发现其中很多是同一份规则的复制、翻译和改名：仅 blader/humanizer 这一份，调研里就找到至少 4 个同源版本。这不是谁的错，生态就是这样长起来的。问题在于挑选和维护的工作全落在使用者身上：

| 现象 | 使用者要自己做的事 |
|---|---|
| 同名不同作者。`humanizer-zh`、`deslop`、`unslop` 各有多个版本 | 核对完整的 owner/repo，不能只搜名字 |
| 规则互相矛盾。一家要求删掉所有副词，另一家要求保住作者原有的声口 | 决定信哪一条，或者装几个之后看它们打架 |
| 示例里把泛泛的好评改成了原文没有的数字和经历 | 自己补一条“不许编事实”的规则 |
| 114 个仓库里 23 个没有许可证文件 | 弄清什么能复制、什么只能参考 |
| 上游一直在更新，装到本地的那份不会跟着变 | 定期回去看，看了还要重新比对 |

调研的原始材料在 [merges/maybe-humanizer/research/](merges/maybe-humanizer/research/2026-09-06-ai-humanizer/README.md)。这些项目每一个都有自己的长处，这个仓库做的是把它们放在一起比对，保留各家好的部分，并把“为什么留、为什么不留”写下来。

## 这里有什么

| 类型 | 是什么 | 怎么维护 |
|---|---|---|
| **original** 自己写的 | 从零写的 skill | 手工 |
| **adapted** 跟进上游 | 选定一个上游，维护成中文版并按当前模型调整。模型在变，skill 也要跟着删减和调优。Anthropic 官方 skills、superpowers 这类是计划跟进的例子 | 每周一检查上游 |
| **aggregated** 合并整理 | 同一主题的多个项目去重合并成一份，各家的长处都留下 | 每周一检查全部上游 |

<details>
<summary><b>合并不是把几个文件拼在一起</b>，展开看具体做法</summary>
<br>

1. **按规则合并，不按文件。** 每个上游先拆成一条条可判定的规则（能指出一句话里哪里违反了它），再把所有来源的规则按语义聚类。
2. **每条规则记来源和理由。** 决定表里每条规则有稳定的 id、来源仓库和文件锚点、有几个来源支持、最终采纳还是拒绝、理由是什么。上游变了，能直接反查到本地哪条规则受影响。
3. **票数不决定采用。** 多个项目互相复制会把票数抬高。采不采纳看它是否可判定、是否保护事实、是否和已有规则冲突、是否适合目标体裁。试验合并里有一条五处证据都来自同一个来源的规则没进默认，也有只有一个来源的规则被采纳。
4. **矛盾的规则两条都留。** 写明选了哪条、为什么，另一条作为可选项留给需要的人。
5. **事实保护优先于风格。** 数字、引语、限定条件、责任主体不能动，这一组规则的优先级高于任何“怎么写更自然”。
6. **许可证决定原文能不能进仓库。** 有许可证的存全文快照并附许可声明；没有的只记 commit 和 hash，规则用自己的话重写，原文不进仓库、不进 PR。
7. **上游文本是数据，不是指令。** 上游 skill 里写的任何“请这样做”都不执行，脚本只读不跑。

一条规则在决定表里的样子（节选，字段有省略）：

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

完整规则见 [skills/skill-merge](skills/skill-merge/SKILL.md) 和 [docs/design.md](docs/design.md)。
</details>

## 每周一发生什么

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/pipeline-dark.svg">
    <img alt="每周一：检测上游变更，生成 PR，review，采纳或记录理由，合并" src="docs/assets/pipeline-light.svg" width="100%">
  </picture>
</p>

这是设计好的流程，检测和开 PR 的代码还在写，目前这几步由人工触发。每个上游的 commit 和文件 hash 记在清单里。周一比对一次，有内容变化就开一个 PR，正文列出 diff 和受影响的本地规则。review 由 `skill-merge` 逐条判断：是已有规则的重述，还是新规则，还是和现有规则矛盾。不采纳的变更也合并，理由留在决定表里，下次不用重新想一遍。只有上游消失、许可证变化、需要人拍板的冲突才开 issue。

## skill 列表

| id | 类型 | 用途 | 状态 |
|---|---|---|---|
| [`en-zh-translation`](skills/en-zh-translation/SKILL.md) | original | 把英文规则、提示词、文档翻成中文，保住每一处条件和情态 | 可用 |
| [`subagent`](skills/subagent/SKILL.md) | original | 什么该拆给 subagent、派给谁、怎么验收、怎么打回 | 可用 |
| [`skill-merge`](skills/skill-merge/SKILL.md) | original | 把多个上游 skill 归并成一份，处理上游的后续变更 | 可用 |
| [`maybe-humanizer`](skills/maybe-humanizer/SKILL.md) | aggregated | 中英文去 AI 味改写与审稿，先保护事实再清理模式 | 试验版 |

<details>
<summary><b>maybe-humanizer 试验版的数字</b></summary>
<br>

第一轮用 4 个上游验证流程：no-ai-slop、qu-ai-wei、Aboudjem/humanizer-skill、writing-style-skill（无许可证，只记元数据）。

| | |
|---|---|
| 拆出的规则单元 | 254 |
| 聚类后的规则 | 144 |
| 采纳 / 修改后采纳 | 87 / 31 |
| 拒绝 / 仅作参考 / 挂起 / 重复 | 9 / 8 / 6 / 3 |
| 留痕的冲突 | 7 组 |

每一条的来源和理由在 [decisions.yaml](merges/maybe-humanizer/decisions.yaml)，过程在[合并报告](merges/maybe-humanizer/reports/0001-2026-09-06-initial-merge.md)。全量合并会覆盖调研里约 60 个文本方向的候选，做完后转正式版。
</details>

## 安装

```bash
npx skills add Maybe404/skills --skill en-zh-translation
```

`--skill` 后面换成上表的 id。一次装全部：

```bash
npx skills add Maybe404/skills --all
```

<details>
<summary>目录结构</summary>
<br>

```
catalog/<id>.yaml        每个 skill 的注册信息：类型、状态、路径、是否有上游
skills/<id>/             skill 本体，可直接安装
merges/<id>/             有上游的 skill 的维护数据
  sources.yaml           上游清单：仓库、路径、许可证、快照策略
  sources.lock.json      监控状态：commit、hash、stars 观测
  snapshots/             有许可证的上游文件全文，附 LICENSE
  decisions.yaml         规则级决定表
  reports/               每次合并的完整报告
  CHANGELOG.md           面向用户的变更摘要
tools/upstream-monitor/  监控和流转的代码
docs/design.md           完整设计
```
</details>

## 现在做到哪了

| | 状态 |
|---|---|
| 三个 original skill | 可用 |
| skill-merge 的合并与同步流程 | 可用，人工触发 |
| maybe-humanizer | 4 个上游的试验版已合并，约 60 个候选的全量合并还没开始 |
| upstream-monitor 代码 | 只有 schema，检测和开 PR 的代码还没写 |
| 每周一的自动检查 | 等 upstream-monitor 完成后接入 |

## 许可证与致谢

本仓库自己的内容按 [MIT](LICENSE) 授权。来自上游的内容按各自的许可证处理，每个有上游的 skill 在 `SOURCES.md` 里列出来源、许可证和许可声明。

感谢所有被跟进和被合并的项目的作者。没有他们先写出来的规则，就没有这里的整理。
