# skills

个人维护的 Agent Skill 集合。仓库地址：`Maybe404/skills`。

安装单个 skill：

```bash
npx skills add Maybe404/skills --skill <id>
```

安装仓库内全部 skill：

```bash
npx skills add Maybe404/skills --all
```

## kind 的含义

每个 skill 在 `catalog/<id>.yaml` 里标注一个 `kind` 字段，取值只有三种：

- `original`：自己从零写的 skill。
- `adapted`：基于单一上游项目翻译或改编而成，内容主要来自那一个来源。
- `aggregated`：合并多个上游项目的内容而成，没有单一来源。

## 目录说明

| 目录 | 内容 |
| --- | --- |
| `catalog/` | 每个 skill 一份 `<id>.yaml`，记录 id、名称、kind、状态、语言、路径等元数据。是 skill 清单的唯一数据源。 |
| `skills/` | 各个 skill 的实际内容，每个子目录是一个可安装的 skill，包含 `SKILL.md` 及其引用的 references/scripts/examples 等文件。 |
| `merges/` | 每个 `adapted` 和 `aggregated` 型 skill 的上游清单、快照、决定表、报告和过程材料，子目录名对应 skill id。`merges/<id>/research/` 是合并前的调研记录（候选清单、来源核验、检索日志等），只是历史存档，不是运行时输入，工具和 skill 本身都不读取这个目录。 |
| `tools/` | 维护本仓库用的脚本和工具，不是面向最终用户的 skill 内容。 |
| `docs/` | 仓库自身的说明文档，记录约定和流程。 |
| `.github/` | GitHub 相关配置，例如 CI 工作流。 |

## 现有 skill

| id | kind | 用途 | 安装命令 |
| --- | --- | --- | --- |
| `en-zh-translation` | original | 把英文文本翻译成中文，或检查、修订已有的中文译文 | `npx skills add Maybe404/skills --skill en-zh-translation` |
| `subagent` | original | subagent 派发规则和编排模式 | `npx skills add Maybe404/skills --skill subagent` |
| `skill-merge` | original | 把多个上游 skill 归并成一个 skill，并处理上游的后续变更 | `npx skills add Maybe404/skills --skill skill-merge` |

规划中、尚未有内容的 skill 在 `catalog/` 里 status 为 `planned`，目前有 `maybe-humanizer`（去 AI 味改写，合并多个上游）。

聚合型（`aggregated`）skill 的来源列表和许可证信息见各自目录下的 `SOURCES.md`。仓库的整体设计见 [docs/design.md](docs/design.md)。
