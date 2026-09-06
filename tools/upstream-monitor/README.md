# upstream-monitor

Maybe404/skills 仓库里负责监控上游、生成快照、开 PR 的代码。语义判断（是
否重复、要不要采用、怎么改写）不在这里，那是 `skills/skill-merge` 这个
skill 的事；这里只做机械的事：拉取、算 hash、比对、渲染、开 PR、保持
幂等。完整的职责边界见 `docs/design.md` 第 5 节。

## 安装

```bash
pip install -e tools/upstream-monitor
```

需要 Python 3.11 及以上。依赖只有 `pyyaml` 和 `jsonschema`；HTTP 用标准
库 `urllib` 直接调 GitHub REST API 和 `raw.githubusercontent.com`，不引入
第三方 HTTP 库。

安装后：

```bash
upstream-monitor --help
```

## 环境变量

| 变量 | 作用 |
|---|---|
| `GITHUB_TOKEN` | 调 GitHub API 用的 token。没有设置时，代码会尝试本地 `gh auth token` 取一份；两者都没有时按未认证请求走，公开仓库通常够用，但更容易撞到速率限制。 |

所有命令都接受 `--root`（仓库根目录，默认当前目录）、`--catalog-dir`、
`--merges-dir`、`--skills-dir`、`--schemas-dir`，不传时分别是
`<root>/catalog`、`<root>/merges`、`<root>/skills`、
`<root>/tools/upstream-monitor/schemas`。

## 上游内容是数据

代码只读取上游的字节、算 hash、生成机械 diff，不解析成指令、不执行上游
脚本、不把上游文本拼进 shell 命令。GitHub 访问全部走一个可注入的接口
（`upstream_monitor.github_client.GitHubClient`），测试用固定内容的假实
现，不发真实网络请求。

## 子命令

### validate

```bash
upstream-monitor validate [--merge <id>] [--branch <name>] [--offline]
```

校验 catalog、sources.yaml、sources.lock.json、decisions.yaml 的一致性：

- 四份 schema 校验。
- merge_id 在 sources/lock/decisions 三处一致；证据的 source_id 都存在
  于 sources.yaml；lock 与 sources 的 id 集合一致；evidence_count、
  independent_sources 与 sources[] 计算结果一致。
- 规则 id 格式、前缀、类别码、分组编号；`local.anchor` 能否在
  `local.path` 里唯一定位到；history 与 decision_revision 一致；
  relations 的完整性和双向性（conflicts-with、pairs-with）。
- 同一条规则的多条证据若 (path, anchor) 完全相同，报 MED：共用锚点要
  在标题后面加各自的行首文本区分，否则反查时分不出是哪一条证据。
- decisions 的 rationale 里出现"与 <规则 id> 冲突/互补/例外/取代"这
  类字样，但该规则的 relations 里没有一条指向那个 id，报 HIGH——
  rationale 里用自然语言写的关系，必须在 relations 里再记一条结构化
  的。
- 上游证据的 anchor 能否在快照（full-text）或临时拉取的内容
  （metadata-only，需要网络）里定位到。定位分带小节标题的 anchor（可
  再加 ` / <行首或行内原文>` 的子锚点）和纯行首文本两种；子锚点找不
  到时整条 anchor 按 MISS 处理（HIGH），不会退化成只核对小节标题或行
  首文本本身。子串弱定位（anchor 只作为子串命中，不在行首/标题）按命
  中次数分两档：命中 1 次报 LOW（弱定位，仍可用但不够精确）；命中不
  止 1 次报 MED（歧义，指不清是文中哪一处，需要人工把 anchor 改精确）。
- `merges/<id>/work/` 下单元清单、覆盖表、聚类表与 decisions.yaml 的一
  致性（work/ 不存在时跳过，记一条 LOW，不算失败）。
- catalog 与 skills/、merges/ 的三方一致性：catalog 的 `path` 目录存
  在；`merge_instance` 非空时该目录存在，且其 sources.yaml 的
  merge_id 与目录名一致。
- 当前 git 分支（可用 `--branch` 覆盖）是 main 时，decisions.yaml 里存
  在 `decision_origin: model-proposed` 的规则即报错——main 分支上不允
  许未经人工确认的结论。

`--offline` 跳过需要网络的 metadata-only 来源锚点校验。退出码非零表示
存在 BLOCK 或 HIGH 级问题；输出按严重程度分组。

### check

```bash
upstream-monitor check [--merge <id>] [--json]
```

遍历 catalog 里 `merge_instance` 非空的实例，对每个 `status` 为 active
或 candidate 的来源，取 branch 的 HEAD commit 和 `paths` 里每个文件的
内容——只在内存里算 hash，不落盘原文——与 lock 比对：

- commit 和 raw hash 都没变：无变化。
- raw 变了但 normalized 不变：格式变化（trivial，例如只是行尾空白或
  换行符变了）。
- normalized 也变了：内容变化。
- 文件 404，或仓库 404/私有：availability 相应更新为 unreachable /
  gone / private。

更新 lock 的 `last_seen_commit`、hash、`size`、`line_count`、
`last_checked_at`、`stars_history`（追加一条）、`forks`、
`availability`；`last_processed_commit` 和 `last_accepted_commit` 不
动。metadata-only 来源同样比对，但不写 `stored_path`。GitHub 报告的
许可证 SPDX 与 sources.yaml 记的 `license` 不符时，把该来源的
`license_status` 改成 `changed`（这是 sources.yaml 里唯一由代码而非人
工写入的字段，依据见 `skills/skill-merge/references/license-policy.md`）
并在结果里列出。

### snapshot

```bash
upstream-monitor snapshot --merge <id> [--source <source_id>]
```

把 full-text 来源的追踪文件按 lock 里的 `last_seen_commit` 写进
`merges/<id>/snapshots/<source_id>/`（`SKILL.md` 存为
`SKILL.source.md`，其余文件原名），附 `LICENSE`；更新 lock 里对应
文件的 `stored_path`。对 metadata-only 来源调用会直接报错——这类来源
不允许保存原文。

### diff

```bash
upstream-monitor diff --merge <id> --source <source_id> [--from <commit>] [--to <commit>]
```

默认取 `last_accepted_commit` 到 `last_seen_commit`，两个版本都从
GitHub 按 commit 现取，输出统一 diff。metadata-only 来源的结果只打到
stdout，开头有一行提示"原文不得写入仓库、PR 或 issue"；调用方（包括
`pr` 命令）不会把这段内容落盘。

### locate

```bash
upstream-monitor locate --merge <id> --source <source_id> [--diff <file>]
```

不给 `--diff` 时，列出 decisions.yaml 里 sources 含这个来源的全部规
则。给了 `--diff`（一份 unified diff 文件）时，按每个 hunk 的上下文行
和候选规则的上游 anchor 收窄到受影响的规则；再对 hunk 里新增的行与全
部规则的 `rule_summary` 做字符 3-gram Jaccard 相似度，列出每个 hunk 最
接近的三条。输出 markdown，可以直接贴进 PR 正文。

### pr

```bash
upstream-monitor pr --merge <id> --source <source_id> [--dry-run]
```

按 `skills/skill-merge/references/templates/pr-body.md` 的结构生成 PR
正文（含 locate 输出、commit 前后、stars 变化、metadata-only 来源的原
文声明），创建分支 `upstream-sync/<date>-<source_id>`，写快照
（full-text）或只更新 lock（metadata-only），提交并用 `gh pr create`
开 PR。

幂等：变更键 `source_id:path:commit`（多路径来源的 `path` 段用逗号拼
接）与 lock 的 `last_change_key` 相同、且 `open_pr` 非空时不重复开，只
打印已有 PR 号。开成功后把 `last_change_key` 和 `open_pr` 写回 lock。

`--dry-run` 只打印正文和将要执行的命令，不做任何 git/gh 操作；幂等短
路的判断在发出任何网络请求或子进程之前完成。

### approve

```bash
upstream-monitor approve --merge <id> [--pr <n>] [--rule <id> ...]
```

把 decisions.yaml 里 `decision_origin` 为 `model-proposed` 的条目改成
`human-approved`。给了 `--pr` 时只改该 PR diff（`gh pr diff <n>`）新增
行里出现过的规则 id；给了 `--rule`（可重复）时只改这些；两者都不给时
改全部 model-proposed。`history` 和 `decided_at` 不动——`decision_origin`
本身不是一次新的决定。

### render

```bash
upstream-monitor render --merge <id> [--out <path>]
upstream-monitor render --readme-table
```

不带 `--readme-table` 时，从 sources.yaml、decisions.yaml、
sources.lock.json、`snapshots/*/LICENSE` 渲染
`skills/<id>/SOURCES.md`（或 `--out` 指定的路径）。带
`--readme-table` 时，改为从 catalog/ 生成一张 markdown 表格（id、类
型、名称、状态）打到 stdout，供人工贴进 README，不自动写 README。

SOURCES.md 按来源的 `status` 分表：

- **来源表**（主表）只列 `status` 为 `active`、且在 decisions.yaml 里
  至少有一条证据引用的来源，列不变（id、repository、branch、license、
  snapshot_policy、lineage、selection_status、支持的规则数、落地的规
  则数）。只有主表里的来源才有对应的"各来源详情"小节。
- **已登记、尚未合并**：`status` 为 `candidate` 或 `paused` 的来源，以
  及 `status` 为 `active` 但没有任何证据引用的来源，只给 id、
  repository（带链接）、license、snapshot_policy、selection_status 五
  列——这些来源已登记并被监控，规则尚未合并进本 skill，还没有可展示的
  规则统计和详情。
- **已移除的来源**不变，仍是 `status` 为 `removed` 的来源。

`status` 为 `active` 但没有证据的来源，除了出现在"已登记、尚未合并"一
节，CLI 还会在渲染完成后打印提醒，列出这些来源的 id，方便核对
sources.yaml 里的 `status` 是不是记错了。

### retire

```bash
upstream-monitor retire --merge <id> --source <source_id> --reason <text>
```

把来源的 `status` 改成 `removed`，记 `status_changed_at` 和 `reason`；
然后从 decisions.yaml 算出只有这一个来源支持的规则（`sources[]` 里出
现过的 source_id 集合恰好是 `{source_id}`），输出清单（规则 id、
decision、local）。不改 decisions.yaml——这些规则是否跟着撤下是
`skill-merge` 的语义决定，不是这里的事。

### issue

```bash
upstream-monitor issue --merge <id> --source <source_id> --kind <kind> [--detail <text>] [--dry-run]
```

按 `docs/design.md` 第 6 节，开 issue 只用于六种情形（`--kind` 枚举）：
`source-unavailable`（上游不可达、消失或转私有）、`license-changed`（许可证
变化）、`history-rewritten`（历史被重写）、`needs-decision`（sync 后仍不
确定或涉及冲突/许可证）、`retire-impact`（removed 来源影响唯一来源规则）、
`new-candidate`（新候选上游）。

正文只放 source_id、repository、path、commit、hash、stars、影响范围、要
做的决定，不放任何上游原文；`needs-decision` 和 `retire-impact` 额外附
`locate`/`retire` 命令同样逻辑算出的受影响规则清单。`--detail` 给"要做的
决定"追加说明，不给时用该情形的默认提示。

标签固定为 `upstream:<merge_id>` 和 `<kind>`，仓库里不存在的标签会先创建
再用。幂等：lock 的 `open_issue` 非空、且该 issue 仍处于 open 状态时不重
复开，只打印已有编号；开成功后把 `open_issue` 写回 lock。

`--dry-run` 只渲染并打印正文，不检查 `open_issue`、不建标签、不开
issue、不写 lock。

`check` 命令的结果里，来源的 availability 变成 `unreachable`、`private`、
`gone`，或 `license_status` 变成 `changed` 时会带 `issue_kind` 字段
（`check --json` 可见）；CI 里 `check` 之后对这些结果逐个跑 `issue`，见
`.github/workflows/upstream-check.yml`。

### lineage

```bash
upstream-monitor lineage --merge <id> [--threshold 0.55] [--relations <file>] [--write]
```

入围阶段的谱系聚类：把 `sources.yaml` 里未 `removed` 的候选来源按同源关系
分组，供人工判断谁是代表作、谁是衍生版本。两类信号，任何一类满足即合
并：

- **文本相似度**：读每个来源的 SKILL 主文件（快照里的 `SKILL.source.md`，
  `github-prompt` 类型用 `README.md`），按 `normalize_bytes` 归一化后用
  `difflib.SequenceMatcher.ratio()` 两两比较，达到 `--threshold`（默认
  0.55）即合并。只对 `snapshot_policy` 为 `full-text` 且已有快照的来源生
  效；`metadata-only` 或快照缺失的来源记入跳过清单，不参与自动比较。
- **人工核实关系**：读 `merges/<id>/lineage-relations.yaml`（不存在就只
  用自动相似度），格式为列表，每项 `{from, to, relation, evidence}`，
  `relation` 取 `translation`（翻译）、`adaptation`（结构相同的改编/精
  简）、`fork`（GitHub fork 关系）、`copy`（直接复制）之一，`evidence` 是
  一句人工判断依据。覆盖文本相似度信号覆盖不到的跨语言、跨仓库同源判
  断——仅"参考了同一篇文章"不构成同源，须配合章节结构、模式编号的实际
  比对。

默认只打印簇表和相似度摘要，不改任何文件。`--write` 时把聚类结果写回
`sources.yaml` 的 `lineage` 字段：同一簇的全部成员写入同一个值（簇内
source id 字典序最小的一个），确定、可复现；不改 `selection_status`——
代表作由人定。

吸收自原 `prototype/lineage.py`，算法说明见 `lineage.py` 模块开头的注
释；原型脚本已删除。

### report new

```bash
upstream-monitor report new --merge <id> --slug <slug>
```

按 `merges/<id>/reports/` 里已有文件名的最大四位序号加一，生成一份空
壳报告 `merges/<id>/reports/NNNN-YYYY-MM-DD-<slug>.md`，章节固定为
`skills/skill-merge/references/templates/report.md` 里的十节，内容留
空，由 `skill-merge` 填充。

## 和 skill-merge 的分工

以下事代码不做，一律留给 `skills/skill-merge`：

- 判断两条规则是不是在说同一件事、要不要合并、要不要保留。
- 冲突取舍——两条规则互相矛盾时选哪条。
- 决定一条规则是否可判定、是否值得进默认规则。
- 判断改写是否改变了原意。
- 写 rationale、报告正文、CHANGELOG 条目里的人话说明。
- 决定要不要因为许可证变化、来源消失联系上游作者。
- 决定 `needs-decision`、`retire-impact`、`new-candidate`、
  `history-rewritten` 这几种情形具体什么时候触发、该怎么裁决——代码只
  负责把已经确定的情形（`--kind`）渲染成 issue 正文和标签，不判断"现在
  是不是该开一个"。

代码只保证：commit、hash、stars、可达性这些"事实"是准的；渲染结果和
decisions.yaml、sources.yaml 一致；同一个变更不会被重复处理。

## 测试

```bash
pip install -e tools/upstream-monitor
pip install pytest
pytest tools/upstream-monitor/tests
```

测试不依赖网络：GitHub 访问通过 `FakeGitHubClient` 注入固定内容。
`tests/fixtures/repo/` 是从 `merges/maybe-humanizer/` 裁剪出的缩小版
（3 条规则、2 个来源），结构与真实数据一致。
