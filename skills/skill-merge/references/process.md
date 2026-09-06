# 流程定义

每一步写清输入、输出、完成标准。完成标准没有全部满足就不进下一步。

## merge 步骤 1：入围

**输入**：`merges/<id>/sources.yaml`，其中 status 为 candidate 的全部来源；`merges/<id>/sources.lock.json` 里对应的 availability、stars_history、forks。

**做什么**

1. 逐个确认可达性。lock 里 availability 不是 ok 的来源，把 selection_status 记为 inaccessible，用 `upstream-monitor issue --merge <id> --source <source_id> --kind source-unavailable` 开一条 issue，不进后续步骤。
2. 按 lineage 聚类。先跑 `upstream-monitor lineage --merge <id>` 拿机械聚类结果（快照文本相似度，加 `merges/<id>/lineage-relations.yaml` 里人工核实的同源关系），再逐簇人工判断。判断同源的依据：fork 关系、README 里写明的改编来源、SKILL.md 的小节结构和模式表条目高度重合。同源的填同一个 lineage 值；无法判断的先各自单列，理由写进 notes。lineage 命令只算簇、只写 lineage 字段，代表作由人定。
3. 每个谱系选一个 representative：优先选内容最全、维护最近的那个，热度只作参考不作依据。读它的全文。
4. 同谱系的其余成员只读与 representative 的差异。差异只有措辞、翻译、排版的记 duplicate；差异含 representative 没有的规则的记 derivative，把差异部分列出来留给步骤 2。
5. 谱系不适用于本 skill 的体裁或语言时记 low-priority，理由写进 reason。

**输出**：改写后的 sources.yaml，每条来源的 lineage、selection_status、status、reason、status_changed_at 都已填。

**完成标准**：`upstream-monitor validate --merge <id>` 通过；没有 selection_status 仍为空的来源；每个 lineage 恰有一个 representative；每条不进入步骤 2 的来源都写了 reason。

## merge 步骤 2：拆规则

**输入**：步骤 1 选出的 representative 全文，以及 derivative 的差异部分。

**做什么**：按 `extraction.md` 的模板把每份文本拆成规则单元，写进 `merges/<id>/work/units/<source_id>.md`。拆完先自查：每个单元能不能拿一句话去判定它是否被违反；答不上来的不是规则单元，合并到别的单元或丢弃。

来源多于三个时按 `skills/subagent/SKILL.md` 的规则派 subagent 并行，一个 subagent 拆一个来源，验收物是该来源的规则单元清单，由 subagent 直接写进 `merges/<id>/work/units/<source_id>.md`。派发前的审批方式按那个文件执行。

派 subagent 用 `skills/subagent/SKILL.md` 里的 Opus 档，不用默认档。拆规则不是抄写：`intent` 那一行要判断原作者针对的是什么现象，`existing` 那一行要判断和已有规则像不像，两件事都得读懂上游为什么这么写。归并（步骤 3）和写 skill 正文（步骤 4）同理，也是这一档；默认档只用于抓取、比对、跑校验、统计、渲染这类机械活。

metadata-only 来源不交给 subagent 抓全文，由你按 `license-policy.md` 的口径处理，拆出的单元不含原文摘录。

**输出**：`merges/<id>/work/units/<source_id>.md`，每个单元含类别码、language、rule_summary、正例反例、来源锚点、intent、existing。

**完成标准**：每个入围来源都有清单；每个单元有锚点、intent 和 existing 三行；metadata-only 来源的单元里没有原文摘录。

## merge 步骤 3：归并

**输入**：步骤 2 的全部规则单元清单。

**做什么**

1. 按语义聚类。同一条规则的不同表述进一个簇，措辞差异不算不同规则。
2. 每个簇计 evidence_count（簇内单元数）和 independent_sources（簇内单元去掉同 lineage 重复后的来源数）。
3. 按 `criteria.md` 逐条裁决，得到 decision。
4. 写 decisions.yaml。规则 id 一经分配不改；改结论时 decision_revision 加一、旧值追加进 history；只追加证据、补 relations 或改 rationale 而不改结论的，revision 和 history 都不动，decision_origin 也保持原值。新条目的 decision_origin 一律先写 model-proposed。
5. 互相矛盾的簇不合并，两条都记，取舍写进报告。
6. 把规则之间的关系落进 relations，见下面"规则关系要落成 relations"。

**分批**

一个上下文处理不了超过约 300 条单元：聚类要求同时看到全部单元的 rule_summary，超过这个量级就会漏聚。来源多时按 6 到 8 个来源分批，一批的单元总数控制在 300 条以内。

- 第一批：decisions.yaml 为空时按全量归并做，即上面的第 1 到 6 步。
- 之后每一批：按 `sync` 的"添加上游"路径与现有 decisions.yaml 比对——与已有规则重复的按 sync 步骤 3 的两条路径二选一处理（记 duplicate，或者给已有规则追加证据），不新建规则；确实是新规则的新建条目；与已有规则矛盾的两条都留，双向记 conflicts-with。
- 批与批之间顺序进行，不并行：后一批要看到前一批已经落进 decisions.yaml 的结论，否则同一条规则会在两批里各建一条。
- 全部批次做完后再做一次全局冲突复核（把全部 adopted 和 adopted-with-modification 的 rule_summary 通读一遍，找跨批次的矛盾和重复），然后重写 skill 正文。分批期间不要每批都改一遍正文。

每批做完跑一次 `upstream-monitor validate --merge <id>`，不通过不进下一批。

**规则关系要落成 relations**

rationale 里凡是写了"与 X 冲突""与 X 互补""是 X 的例外""取代 X"、并且指向另一条规则 id 的，都要同时在 relations 里记一条结构化的，rationale 的文字不删。只在 rationale 的自然语言里写不算做完：规则上百条之后，自然语言里的关系只能靠 grep 规则 id 才找得到，也没法校验双向性。

type 用 decisions.schema.json 的四个取值：`conflicts-with`（两条互相矛盾，双向记，A 指 B 则 B 也要指 A）、`pairs-with`（两条配套、各管一半，双向记）、`excepts`（两条按范围分域或互为例外，单向记，note 里写清边界）、`supersedes`（本规则取代对方，单向记）。

relations 只记两条规则作为本仓库当前结论都成立时的关系。"上游原来的写法与某条冲突，所以改写了"这类历史原因不记——被否掉的写法不是本仓库的结论，记成常驻关系会失真，那类只留在 rationale 里。

**decision_origin 不进 history**

decision_origin 从 model-proposed 翻成 human-approved 由 `upstream-monitor approve --merge <id> [--pr <n>] [--rule <id>]` 做，不追加 history、不动 decided_at。history 只记 decision 的变化：换一个人确认同一个结论，不是一次新的决定。

**输出**：`merges/<id>/decisions.yaml`，以及 `merges/<id>/work/` 下的聚类表和覆盖表。

**完成标准**：`upstream-monitor validate --merge <id>` 通过（含 schema、id 格式、evidence_count 与 independent_sources 的一致性、relations 的完整性和双向性、work/ 与 decisions.yaml 的一致性）；每条 rule 的 sources 里的 source_id 都能在 sources.yaml 找到；metadata-only 来源支持的规则，rationale 里没有原文；rationale 里点了名的规则关系在 relations 里都有对应条目。

## merge 步骤 4：写 skill

**输入**：decisions.yaml 里 decision 为 adopted 或 adopted-with-modification 的规则。

**做什么**：写 `skills/<id>/SKILL.md` 和 references。SKILL.md 只放流程和判断规则，模式表、词表、清单进 references，中英文规则分表。写完回填每条规则的 local.skill、local.path、local.anchor，再跑 `upstream-monitor render --merge <id>` 生成 `skills/<id>/SOURCES.md`。

**输出**：`skills/<id>/SKILL.md`、`skills/<id>/references/*`、更新过 local 的 decisions.yaml、渲染出的 SOURCES.md。

**完成标准**：`upstream-monitor validate --merge <id>` 通过——它逐条核 local.anchor 能否在 local.path 里唯一定位到，也核 work/ 里的单元清单、聚类表、覆盖表与 decisions.yaml 是否一致；SKILL.md 里没有出现只在 references 才展开的完整表格；`skills/<id>/SOURCES.md` 是渲染出来的，不手写。

## merge 步骤 5：验证

**输入**：写好的 skill。

**做什么**：写 evals 覆盖三类样本，逐类给出通过和失败的条数。

1. 真人写的原文，不该被改。判据：输出与输入的差异只在标点和排版，语义无变化。
2. 带数字、版本号、命令、接口字段、责任主体的段落，事实不得漂移。判据：逐个比对原文和输出里的数字、标识符、条件关系，一处不同即失败。
3. 套话段落，套话要被清理。判据：预先标出的套话在输出里消失，且没有引入新的套话。

先跑第 2 类，再看第 1 类和第 3 类。第 2 类有失败的，不看风格结果，直接回步骤 3 改规则。

**输出**：evals 文件、结果、以及按 `templates/report.md` 写的合并报告。

**完成标准**：三类都跑过并记录条数；第 2 类零失败；报告的十个章节都有内容或写明"无"。

## sync

**输入**：`sync <id> [pr号]`。给了 PR 号就用那个 PR 的 diff；没给就用 `upstream-monitor locate --merge <id> --source <source_id> --diff <文件>` 的输出，取全部 last_processed_commit 落后于 last_seen_commit 的来源。

merge 步骤 3 的第二批起也走这条路径：那时"diff"换成该批来源的规则单元清单，其余各步相同。

**做什么**

1. 用 `upstream-monitor diff` 取变更，`upstream-monitor locate` 反查它触及的本地规则 id。
2. metadata-only 来源按 commit 临时拉取比对，比完丢弃，不写进 snapshots/，不引用原文。
3. 逐条与 decisions.yaml 比对：重述记 duplicate；矛盾的单列进"冲突与取舍"；新规则按 `extraction.md` 拆成单元。

   找对照规则的顺序：先看单元的 `existing` 行，它给出拆规则时就看出来的疑似对应规则；再靠锚点反查；最后拿新单元的 rule_summary 与全部落地规则的 rule_summary 做一次语义比对。三步都要做，不能只信 `existing`——那一行是拆单个来源时写的，写它的人没看过别的来源，跨来源的重复它给不出。锚点反查也只能找到 diff 直接触及的那几条，跨来源的重复和矛盾锚点反查不到。首次合并后的 sync 干跑里，hunk 2 与 ALL-PROT-018 的矛盾就是因为只走了锚点反查而漏掉的。

   **duplicate 和追加证据只能选一个。**记 duplicate 时，只在新单元这一条上记，被它重复的那条规则不追加证据：同一段上游文本不能同时出现在两条规则的 sources 里，否则 evidence_count 和覆盖统计会把它重复计数。要把这段文本算成已有规则的新证据，就不记 duplicate，改为在那条规则上追加一条 sources 并把 decision_revision 加一。
4. 按 `criteria.md` 裁决。
5. 写 decisions.yaml，decision_origin 一律 model-proposed，人工确认由 `upstream-monitor approve` 做。rationale 里点名了另一条规则的关系（冲突、互补、例外、取代），同时落进 relations，规则见步骤 3 的"规则关系要落成 relations"。
6. 改 skill 正文，跑 `upstream-monitor render --merge <id>` 重新渲染 SOURCES.md。
7. 用 `upstream-monitor report new --merge <id> --slug <slug>` 生成报告骨架（它按目录里最大的四位序号加一命名，章节按 `templates/report.md` 的十节），再逐节填。
8. 按 `templates/changelog-entry.md` 在 CHANGELOG.md 顶部新增一节。
9. 按 `templates/pr-body.md` 写 PR 正文；`upstream-monitor pr` 会按同一份模板生成，手写时对齐它的结构。

**输出**：更新后的 decisions.yaml、skill 正文、重新渲染的 SOURCES.md、一份报告、一节 CHANGELOG、一份 PR 正文。

**完成标准**：`upstream-monitor validate --merge <id>` 通过；diff 里的每条变更都有对应结论，没有"看过但没记"的；报告和 CHANGELOG 都已写；涉及冲突或许可证的已打 needs-decision 标签，并用 `upstream-monitor issue --merge <id> --source <source_id> --kind needs-decision` 开了 issue。

## sync 的三个 commit 怎么用

- last_seen_commit：upstream-monitor 最近看到的上游提交，不代表分析过。
- last_processed_commit：已经进入 sync 分析的提交。sync 的比对区间是 last_accepted_commit 到 last_seen_commit。
- last_accepted_commit：人工合并 PR 后成为基线的提交。下一次比对以它为起点。

这三个字段由 upstream-monitor 写，skill 只读。
