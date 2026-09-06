# Maybe404/skills 设计文档

## 1. 定位

Maybe404/skills 是个人维护的 skill（技能）集合。集合内的 skill 分三种 kind：

| kind | 定义 |
|---|---|
| original | 自写，0 上游 |
| adapted | 单一上游的翻译或改编 |
| aggregated | 多上游合并 |

集合里有两个名称相近但职责不同的部分，不要混用：

- skill-merge：集合里负责语义合并判断的 skill。
- upstream-monitor：tools/ 下负责监控和流转的代码。

## 2. 目录

```
README.md
catalog/<id>.yaml
skills/<id>/
merges/<id>/
tools/upstream-monitor/
docs/
.github/workflows/upstream-check.yml
```

| 路径 | 说明 |
|---|---|
| `README.md` | 仓库总览 |
| `catalog/<id>.yaml` | 每个 skill 一份，人工维护 |
| `skills/<id>/` | 交付物。aggregated 和 adapted 含 SOURCES.md，由代码从 decisions.yaml 渲染 |
| `merges/<id>/` | 只有 adapted 和 aggregated 有，结构见下表 |
| `tools/upstream-monitor/` | 自包含 Python 包，自带 pyproject、src、tests、schemas；根目录不放工程文件 |
| `docs/` | 设计文档 |
| `.github/workflows/upstream-check.yml` | 监控 workflow |

`merges/<id>/` 内部：

| 路径 | 维护方 | 说明 |
|---|---|---|
| `sources.yaml` | 人工 | 上游来源清单 |
| `sources.lock.json` | 代码 | 上游状态快照 |
| `snapshots/<source_id>/` | 代码 | 上游文本快照 |
| `decisions.yaml` | skill 写、代码校验 | 规则决定表 |
| `reports/NNNN-YYYY-MM-DD-<slug>.md` | 代码骨架、模型填充 | 单次 merge 或 sync 的分析报告 |
| `CHANGELOG.md` | 人工/skill | 面向用户的摘要 |
| `research/` | 人工 | 历史调研材料，不是运行时输入 |

监控入口的唯一条件：catalog 里该 skill 的 `merge_instance` 非空。

发布目录用 `skills/`，不用 `packages/`。依据是 skills CLI（vercel-labs/skills）README 的 Skill Discovery 一节：CLI 只在固定的容器目录里找 SKILL.md，`skills/` 在清单内，`packages/` 不在；`--skill <id>` 按 SKILL.md frontmatter 的 name 匹配。2026-09-06 用 `npx skills add <本地路径> --list` 在本仓库验证，能发现 `skills/<id>/SKILL.md` 并按 `--skill` 安装，安装结果与仓库内容逐字节一致。推送后再用 `npx skills add Maybe404/skills --list` 复验一次。

## 3. 数据契约

以下四个文件的字段名和枚举值是契约，代码和 skill 都必须逐字遵守。

### catalog/<id>.yaml

| 字段 | 说明 |
|---|---|
| id | skill 唯一标识 |
| name | 显示名 |
| kind | original \| adapted \| aggregated |
| status | active \| planned \| archived |
| language[] | 语言列表 |
| path | skill 目录路径 |
| merge_instance | 对应的 merges/<id>，非空即纳入监控 |
| replacement | 被替代后的指向 |
| archived_at | 归档时间 |
| reason | 归档或状态变更原因 |

### merges/<id>/sources.yaml

顶层字段：

| 字段 | 说明 |
|---|---|
| merge_id | 合并实例标识 |
| target_skill | 产出的 skill id |
| sources[] | 上游列表，字段见下表 |

sources[] 每项：

| 字段 | 说明 |
|---|---|
| id | 稳定主键，格式 `upstream-<owner>-<repo>`，仓库改名不变 |
| source_type | github-skill \| github-prompt \| web-page \| directory-only |
| repository | 仓库地址 |
| previous_repository[] | 历史仓库地址 |
| branch | 追踪分支 |
| paths[] | 追踪路径 |
| license | SPDX 标识或 unknown |
| license_status | known \| unknown \| changed |
| snapshot_policy | full-text \| metadata-only |
| status | candidate \| active \| paused \| removed |
| selection_status | representative \| derivative \| duplicate \| low-priority \| inaccessible |
| lineage | 谱系 id，同源项目（fork、复制、改编自同一根节点）共用同一个值 |
| tracking_revision | 追踪配置的修订号，整数，从 1 起，每次改 repository、branch 或 paths 加 1 |
| previous_paths[] | 历史追踪路径 |
| path_changed_at | 路径变更时间 |
| baseline_reset_reason | 重设基线的原因 |
| status_changed_at | status 变更时间 |
| reason | 当前状态或字段变更的原因 |
| notes | 备注 |

约束：`license` 为 unknown 时，`snapshot_policy` 必须是 metadata-only。

### merges/<id>/sources.lock.json

按 source_id 索引，每条记录：

| 字段 | 说明 |
|---|---|
| last_seen_commit | 代码最近看到的 commit |
| last_processed_commit | 已进入 sync 分析的 commit |
| last_accepted_commit | 人工合并后成为基线的 commit |
| raw_sha256 | 原始文本 hash |
| normalized_sha256 | 归一化后文本 hash |
| size | 大小 |
| line_count | 行数 |
| files[] | 每项 {original_path, stored_path, raw_sha256, normalized_sha256} |
| stars_history[] | 每项 {observed_at, value} |
| forks | fork 数 |
| installs | 安装量 |
| last_checked_at | 最近检查时间 |
| last_change_key | 幂等键，格式 `source_id:path:commit` |
| open_pr | 关联的未合并 PR |
| open_issue | 关联的未关闭 issue |
| availability | ok \| unreachable \| private \| gone |

### merges/<id>/decisions.yaml

顶层字段 `merge_id` 和 `rules[]`，rules 每条：

| 字段 | 说明 |
|---|---|
| id | 规则标识 |
| local | {skill, path, anchor}，规则在本地 skill 里的落点 |
| category | pattern \| protection \| process \| style-opinion \| genre \| measurement |
| language | zh \| en \| both |
| rule_summary | 规则摘要 |
| decision | adopted \| adopted-with-modification \| duplicate \| rejected \| deferred \| reference-only \| unverified \| retired |
| decision_origin | model-proposed \| human-approved |
| decision_revision | 决定的版本号 |
| decided_at | 决定时间 |
| evidence_count | 证据数量 |
| independent_sources | 独立来源数量 |
| sources[] | 每项 {type(upstream\|self), source_id, path, commit, anchor} |
| rationale | 理由 |
| history[] | 每项 {decision, at, reason} |

decisions.yaml 支持双向反查：从上游文件（source_id + path + commit）查到规则 id，再从规则 id 查到本地文件和 anchor；反过来，从本地文件的 anchor 也能查到对应规则和其上游依据。

stars 不放在 decisions.yaml 里，只在 sources.lock.json。

### 维护方式汇总

| 文件 | 维护方 |
|---|---|
| catalog/<id>.yaml | 人工 |
| sources.yaml | 人工 |
| skills/<id>/ 正文 | 人工 |
| sources.lock.json | 代码生成 |
| SOURCES.md | 代码生成 |
| README 目录表 | 代码生成 |
| reports/ 骨架 | 代码生成 |
| decisions.yaml | skill 写，代码校验；语义决定不被代码覆盖 |

## 4. 快照与许可证

| 情形 | 处理 |
|---|---|
| 有明确许可证 | 存追踪文件当前全文；SKILL.md 存为 SKILL.source.md；lock 记 original_path 和 stored_path；旧版本靠 git 历史，不按日期复制 |
| 无 LICENSE 或不明确 | metadata-only：只存 commit、raw_sha256、normalized_sha256、size、line_count、stars；不公开保存原文，不把 diff 贴进 PR、issue 或报告；sync 时按 commit 临时拉取分析；规则用自己的话写；拿到许可证后改为 full-text |

是否联系上游作者由人工决定，不是流程的一部分。

空间估算：一个合并实例约几十个上游，每个几十 KB，总量几 MB，无存储风险。

## 5. 职责边界

| 代码 | 模型 |
|---|---|
| 遍历 catalog 和 merges | 读变更 |
| 拉取 sha、hash、stars、forks、license | 分类 |
| 更新快照和 lock | 语义去重 |
| 生成机械 diff | 冲突判断 |
| 用 normalized hash 区分格式变化和内容变化 | 是否采用 |
| 从 decisions.yaml 反查受影响规则和落点 | 改写 |
| 算词面相似候选 | 改 skill 正文和 decisions.yaml |
| 创建或更新 PR 和 issue | 写理由和语义分析报告 |
| validate：schema、ID 唯一、落点存在、来源存在、main 分支上不允许 model-proposed | |
| approve：把一个 PR 内的 model-proposed 批量改为 human-approved | |
| 渲染 SOURCES.md、README 目录表、报告骨架 | |
| 保持幂等 | |

代码不决定：语义是否重复、冲突取舍、规则是否值得保留、改写是否改变原意。

模型不决定：commit 是什么、stars 多少、文件有没有变、哪个路径受影响、PR 是否真的创建。

上游的 SKILL.md、prompt、脚本一律是不可信数据。第一版只抓取和解析 markdown、YAML、JSON、纯文本，不执行上游脚本，不装上游依赖。

## 6. 流转

PR 优先，流程如下：

1. check 每周跑一次，可手动触发。追踪文件有内容变化就更新快照或 lock，并开 PR；PR 正文含 sha 前后、受影响规则 id 和路径、词面最近的几条现有规则、merge_result 字段。
2. 审核人手动跑 skill-merge sync，sync 产出的决定以 commit 推到同一分支。
3. 采纳的改动更新 skill 正文和 decisions.yaml；不采纳的只改 decisions.yaml 和 lock。
4. 跑 approve。
5. 合并。每个 PR 都合并，不留待定 PR。

变更分三级：

| 级别 | 条件 | 处理 |
|---|---|---|
| 自动合并 | normalized hash 不变 | 不审 |
| 开 PR 等 sync | 其余情形 | 走上面的流程 |
| needs-decision | sync 后仍不确定、涉及冲突或许可证 | 标 needs-decision 并开 issue |

issue 只用于以下情形：新候选上游、上游不可达或消失或转私有、许可证变化、历史被重写、needs-decision、removed 来源影响唯一来源规则。issue 内容只放 source_id、repository、path、commit、hash、stars、影响范围、要做的决定，不放原文。

幂等键：`source_id:path:new_commit`。lock 记 last_change_key、open_pr、open_issue，避免重复开 PR 或 issue。

stars 只进 lock，随内容 PR 一起更新，或每月单独更新一次，不为 stars 单独开 PR；仓库消失或转私有才为此开 issue。

以后可接 claude-code-action，让 sync 在 CI 里对同一个 skill 自动跑。

## 7. 生命周期

| 场景 | 处理 |
|---|---|
| 新增原创 skill | 建 skills/<id>/ 和 catalog，不建 merges |
| 新增聚合 skill | catalog、sources.yaml、snapshot、skill-merge merge、产出 skill、decisions、初始报告、evals |
| 原创 skill 吸收上游 | 先从自身正文生成 decisions.yaml，来源 type 为 self；建 sources.yaml；走"添加上游"流程；kind 改为 aggregated 并记 CHANGELOG |
| 添加上游 | sources.yaml 加一条 candidate；snapshot；sync 增量比对；不重新生成整个 skill；最后跑 evals 回归 |
| 修改上游配置 | 记 tracking_revision、previous_paths、baseline_reset_reason；用旧快照和新路径跑一次 sync，确认是同一逻辑来源后再更新 last_accepted；不无条件覆盖 |
| 停用或删除上游 | 状态改 paused 或 removed，可先 paused 再 removed，也可直接 removed；removed 之前，代码算出只有该来源支撑的规则；这些规则是否删除由 sync 另做决定，来源删除和规则删除是两个独立决定 |
| 删除 skill | catalog 状态改 archived，写 archived_at、reason、replacement；停止监控；保留目录和报告；只有法律、版权或体积原因才真删文件 |

## 8. 合并准则

- 事实保护优先于风格。
- 规则要可判定。
- evidence_count 和 independent_sources 只是证据，不按票数自动采用；是否采用由适用性、准确性、冲突风险、体裁适配、evals 结果裁决。
- 单一来源的强风格意见不进默认规则，进冲突表，作为可选项保留。
- 绕过 AI 检测、需要外部 API、绕过披露要求的规则不采纳。
- 无许可证的上游只能提取思路写成自己的话，不引用原文。
- 上游文本是数据，不是指令。

## 9. 首个实例 maybe-humanizer

合并分五步：

1. 入围：约 60 个文本方向候选，全部抓取元数据和目标文件；按 fork、语言、相似度聚成谱系；每个谱系读代表作并加分支差异；结果记入 selection_status。
2. 拆规则：并行派发 subagent 处理。
3. 归并。
4. 写 skill：SKILL.md 只放流程，模式表进 references，中英文分表。
5. 验证：evals 覆盖真人原文不该被改、带数字和命令的段落、套话段落；先核事实漂移，再看风格。

调研已识别出七个功能类别，处理方式如下：

| 类别 | 内容 | 处理 |
|---|---|---|
| A | 模式清理 | 进主规则 |
| B | 保真改写 | 进主规则 |
| C | 表达优化 | 有共识的进主规则，强风格意见做可选项 |
| D | 像我（个人风格） | 不进主流程 |
| E | 体裁（如网文、学术） | 只放边界说明 |
| F | 测量 | 做成本地扫描脚本，只报命中，不报概率 |
| G | UI、代码、商业 API、检测研究、其他语言 | 排除 |

调研材料在 `merges/maybe-humanizer/research/2026-09-06-ai-humanizer/`，只读，不修改。

## 10. 技术选择

第一版：Python、普通 CLI、GitHub API、git、YAML 和 JSON、GitHub Actions。

不用：LangGraph、SQLite、自动发布。

升级条件（出现以下情形再引入对应能力）：多实例并行、中断后 resume、多 reviewer、长时运行重试、抽成通用 Action。

## 11. 实施顺序

1. 改名和目录重排，并验证 CLI 发现规则。
2. 写四个 schema 和样例。
3. 写 skill-merge 最小版本。
4. 用 no-ai-slop、qu-ai-wei、writing-style-skill、Aboudjem/humanizer-skill 四个上游试跑，验收六条：来源能追踪、规则能反查、快照能恢复、PR 幂等、sync 能区分 duplicate 和 conflict 和 adopted、报告能解释决定。
5. 根据试跑结果修 schema 和报告格式。
6. maybe-humanizer 全量合并。
7. 写 upstream-monitor。
8. 接入 GitHub Actions。
9. 用真实的上游变化跑一次 sync。
10. 补回归测试和上游文本指令抵抗测试。
