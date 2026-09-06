# 流程定义

每一步写清输入、输出、完成标准。完成标准没有全部满足就不进下一步。

## merge 步骤 1：入围

**输入**：`merges/<id>/sources.yaml`，其中 status 为 candidate 的全部来源；`merges/<id>/sources.lock.json` 里对应的 availability、stars_history、forks。

**做什么**

1. 逐个确认可达性。lock 里 availability 不是 ok 的来源，把 selection_status 记为 inaccessible，开一条 issue，不进后续步骤。
2. 按 lineage 聚类。判断同源的依据：fork 关系、README 里写明的改编来源、SKILL.md 的小节结构和模式表条目高度重合。同源的填同一个 lineage 值；无法判断的先各自单列，理由写进 notes。
3. 每个谱系选一个 representative：优先选内容最全、维护最近的那个，热度只作参考不作依据。读它的全文。
4. 同谱系的其余成员只读与 representative 的差异。差异只有措辞、翻译、排版的记 duplicate；差异含 representative 没有的规则的记 derivative，把差异部分列出来留给步骤 2。
5. 谱系不适用于本 skill 的体裁或语言时记 low-priority，理由写进 reason。

**输出**：改写后的 sources.yaml，每条来源的 lineage、selection_status、status、reason、status_changed_at 都已填。

**完成标准**：sources.yaml 通过 sources.schema.json 校验；没有 selection_status 仍为空的来源；每个 lineage 恰有一个 representative；每条不进入步骤 2 的来源都写了 reason。

## merge 步骤 2：拆规则

**输入**：步骤 1 选出的 representative 全文，以及 derivative 的差异部分。

**做什么**：按 `extraction.md` 的模板把每份文本拆成规则单元。拆完先自查：每个单元能不能拿一句话去判定它是否被违反；答不上来的不是规则单元，合并到别的单元或丢弃。

来源多于三个时按 `skills/subagent/SKILL.md` 的规则派 subagent 并行，一个 subagent 拆一个来源，验收物是该来源的规则单元清单（Markdown，不进仓库，直接回到主循环）。派发前的审批方式按那个文件执行。

metadata-only 来源不交给 subagent 抓全文，由你按 `license-policy.md` 的口径处理，拆出的单元不含原文摘录。

**输出**：全部来源的规则单元清单，每个单元含类别码、language、rule_summary、正例反例、来源锚点。

**完成标准**：每个入围来源都有清单；每个单元有锚点；metadata-only 来源的单元里没有原文摘录。

## merge 步骤 3：归并

**输入**：步骤 2 的全部规则单元清单。

**做什么**

1. 按语义聚类。同一条规则的不同表述进一个簇，措辞差异不算不同规则。
2. 每个簇计 evidence_count（簇内单元数）和 independent_sources（簇内单元去掉同 lineage 重复后的来源数）。
3. 按 `criteria.md` 逐条裁决，得到 decision。
4. 写 decisions.yaml。规则 id 一经分配不改；改结论时 decision_revision 加一、旧值追加进 history。decision_origin 一律先写 model-proposed。
5. 互相矛盾的簇不合并，两条都记，取舍写进报告。

**输出**：`merges/<id>/decisions.yaml`。

**完成标准**：通过 decisions.schema.json 校验；每条 rule 的 sources 里的 source_id 都能在 sources.yaml 找到；每条的 evidence_count 等于 sources 长度；metadata-only 来源支持的规则，rationale 里没有原文。

## merge 步骤 4：写 skill

**输入**：decisions.yaml 里 decision 为 adopted 或 adopted-with-modification 的规则。

**做什么**：写 `skills/<id>/SKILL.md` 和 references。SKILL.md 只放流程和判断规则，模式表、词表、清单进 references，中英文规则分表。写完回填每条规则的 local.skill、local.path、local.anchor。

**输出**：`skills/<id>/SKILL.md`、`skills/<id>/references/*`、更新过 local 的 decisions.yaml。

**完成标准**：每条 adopted 和 adopted-with-modification 的规则的 local.anchor 都能在对应文件里定位到；SKILL.md 里没有出现只在 references 才展开的完整表格；`skills/<id>/SOURCES.md` 由代码渲染，不手写。

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

**输入**：`sync <id> [pr号]`。给了 PR 号就用那个 PR 的 diff；没给就用 upstream-monitor 的 locate 输出，取全部 last_processed_commit 落后于 last_seen_commit 的来源。

**做什么**

1. 取 diff 和它触及的本地规则 id。
2. metadata-only 来源按 commit 临时拉取比对，比完丢弃，不写进 snapshots/，不引用原文。
3. 逐条与 decisions.yaml 比对：重述记 duplicate；矛盾的单列进"冲突与取舍"；新规则按 `extraction.md` 拆成单元。
4. 按 `criteria.md` 裁决。
5. 写 decisions.yaml，decision_origin 一律 model-proposed。
6. 改 skill 正文。
7. 写报告到 `merges/<id>/reports/NNNN-YYYY-MM-DD-<slug>.md`，NNNN 是四位序号，接着目录里最大的那个加一。
8. 按 `templates/changelog-entry.md` 在 CHANGELOG.md 顶部新增一节。
9. 按 `templates/pr-body.md` 写 PR 正文。

**输出**：更新后的 decisions.yaml、skill 正文、一份报告、一节 CHANGELOG、一份 PR 正文。

**完成标准**：decisions.yaml 通过校验；diff 里的每条变更都有对应结论，没有"看过但没记"的；报告和 CHANGELOG 都已写；涉及冲突或许可证的已打 needs-decision 标签并开 issue。

## sync 的三个 commit 怎么用

- last_seen_commit：upstream-monitor 最近看到的上游提交，不代表分析过。
- last_processed_commit：已经进入 sync 分析的提交。sync 的比对区间是 last_accepted_commit 到 last_seen_commit。
- last_accepted_commit：人工合并 PR 后成为基线的提交。下一次比对以它为起点。

这三个字段由 upstream-monitor 写，skill 只读。
