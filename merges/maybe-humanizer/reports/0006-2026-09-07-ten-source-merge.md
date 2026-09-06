# maybe-humanizer 合并报告 0006

日期：2026-09-07
模式：merge
触发：首次全量合并的收尾（10 个来源、四批归并、一次全局复核、一轮正文写作）

## 1 范围

这一份是 maybe-humanizer 这轮合并的总报告。前五份报告各自记一个阶段，这一份把它们合起来看，并记下最后一步（写正文、重写 SKILL.md、扩 evals、渲染 SOURCES.md）做了什么。

**处理了哪些来源。**10 个上游，分四批读完：

| 批次 | 报告 | 来源 | 新增规则 | 追加证据 |
|---|---|---|---|---|
| 首次合并 | 0001-2026-09-06-initial-merge.md | petergyang/no-ai-slop、LifelongLazyLearner/qu-ai-wei、Aboudjem/humanizer-skill、jzOcb/writing-style-skill | 144 | 无（首批） |
| 中文批 | 0002-2026-09-06-zh-batch.md | MrGeDiao/shuorenhua、ai-zixun/humanizer-zh、op7418/Humanizer-zh | 72 | 38 条 |
| 英文批一 | 0003-2026-09-07-en-batch-1.md | blader/humanizer、hardikpandya/stop-slop | 34 | 48 条 |
| 英文批二 | 0004-2026-09-07-en-batch-2.md | conorbronsdon/avoid-ai-writing | 57 | 69 条 |
| 全局复核 | 0005-2026-09-07-global-review.md | 无新来源 | 0 | 无 |
| 写作与收尾 | 本报告 | 无新来源 | 0 | 无 |

**处理了哪些文件。**四批与全局复核只写 `merges/maybe-humanizer/` 下的裁决与工作文件。本轮收尾写的是交付文件：`skills/maybe-humanizer/` 下的九份 references（301 个小节）、重写的 SKILL.md、扩到 26 条的 evals、渲染出来的 SOURCES.md，加上 `merges/maybe-humanizer/CHANGELOG.md` 和 `catalog/maybe-humanizer.yaml`。逐个文件见第 7 节。

**提交区间。**`main` 上的试验版停在 05ba15b（四来源试验版，随 PR #2 并进 699efee）。本分支 `full-merge-intake` 从那里长出来，到本报告为止的提交见第 9 节。这不是 sync 模式，10 个来源都没有 `last_accepted_commit`，四批读的都是各自 `last_seen_commit` 那一版。

**不在范围内的。**`sources.yaml` 登记了 59 条来源，只有 10 条拆过规则单元。剩下 49 条一条都没进第 2 步：其中 9 条在入围时就定了不拆（5 条 low-priority、2 条 duplicate、2 条 derivative，理由写在各自的 `reason` 里），另外 40 条的 `selection_status` 仍是 representative。这 40 条决定了「首次全量合并算不算做完」，报告 0005 第 10 节第 2 条已经把三种处理方式和各自的代价写出来交给用户，本轮没有动 `sources.yaml`。

## 2 来源清单

10 个 `status: active` 的来源。stars 取 `sources.lock.json` 里 `stars_history` 的最后一条，全部 observed_at 为 2026-09-06T14:51:10Z。stars 和 forks 是热度，不是采用依据：本表里证据最多的 conorbronsdon（204 条）stars 排第四，stars 最高的 blader（43,945）证据数排第四。

| id | repository | branch | lineage | selection_status | license | snapshot_policy | stars | forks | 证据条数 | 支持的规则数 |
|---|---|---|---|---|---|---|---|---|---|---|
| `upstream-petergyang-no-ai-slop` | petergyang/no-ai-slop | main | no-ai-slop | representative | MIT | full-text | 7337 | 548 | 55 | 42 |
| `upstream-lifelonglazylearner-qu-ai-wei` | LifelongLazyLearner/qu-ai-wei | main | qu-ai-wei | representative | MIT | full-text | 531 | 41 | 65 | 46 |
| `upstream-jzocb-writing-style-skill` | jzOcb/writing-style-skill | main | writing-style-skill | low-priority | unknown | metadata-only | 264 | 28 | 16 | 16 |
| `upstream-aboudjem-humanizer-skill` | Aboudjem/humanizer-skill | main | aboudjem-humanizer | representative | MIT | full-text | 215 | 32 | 118 | 84 |
| `upstream-mrgediao-shuorenhua` | MrGeDiao/shuorenhua | main | mrgediao-shuorenhua | representative | MIT | full-text | 1445 | 72 | 135 | 63 |
| `upstream-op7418-humanizer-zh` | op7418/Humanizer-zh | main | blader-humanizer | derivative | MIT | full-text | 16764 | 1117 | 33 | 27 |
| `upstream-ai-zixun-humanizer-zh` | ai-zixun/humanizer-zh | main | ai-zixun-humanizer-zh | representative | MIT | full-text | 138 | 15 | 66 | 43 |
| `upstream-blader-humanizer` | blader/humanizer | main | blader-humanizer | representative | MIT | full-text | 43945 | 3670 | 77 | 60 |
| `upstream-hardikpandya-stop-slop` | hardikpandya/stop-slop | main | hardikpandya-stop-slop | representative | MIT | full-text | 16853 | 1218 | 35 | 30 |
| `upstream-conorbronsdon-avoid-ai-writing` | conorbronsdon/avoid-ai-writing | main | conorbronsdon-avoid-ai-writing | representative | MIT | full-text | 4144 | 349 | 204 | 126 |

各来源快照的 commit：no-ai-slop `000650b15698`、qu-ai-wei `39da1cfac4f0`、writing-style-skill `d94826e1cd48`、aboudjem `275af9489079`、shuorenhua `d2d0ce27da29`、op7418 `91f3d394db84`、ai-zixun `f75f1ac9735c`、blader `e2e92e7b4b82`、stop-slop `8da1f030185b`、conorbronsdon `801c2360f360`。

`upstream-jzocb-writing-style-skill` 是唯一的 metadata-only 来源，许可证未知。它的 16 条单元只描述做法、不引原文，本轮写正文时它对应的规则一律自造例子（写作计划第 2 节的硬约束）。

两个 lineage 各有两个来源：`blader-humanizer` 下有 blader/humanizer（representative）与 op7418/Humanizer-zh（derivative，中文改写版）。其余八个 lineage 各只有一个来源入围。

## 3 统计

### 3.1 全库总量（脚本从 decisions.yaml 算）

- 来源数：入围 10 / 登记 59
- 规则单元数：804（`merges/maybe-humanizer/work/units/` 下十份清单）
- 聚类数：307（一个簇一条规则，簇 id 即规则 id，见 `work/clusters.md`）
- 规则数：307

各 decision 计数：

| decision | 条数 | 占比 |
|---|---|---|
| adopted | 173 | 56.4% |
| adopted-with-modification | 78 | 25.4% |
| rejected | 32 | 10.4% |
| reference-only | 16 | 5.2% |
| deferred | 5 | 1.6% |
| duplicate | 2 | 0.7% |
| unverified | 1 | 0.3% |
| retired | 0 | 0 |

落进默认规则的是 adopted 加 adopted-with-modification，共 251 条。剩下 56 条分两处：conflicts.md 收 40 条（32 rejected、2 duplicate、5 deferred、1 unverified），optional.md 收 16 条 reference-only。EN-S-001 是 adopted-with-modification 但默认不启用，落在 optional.md，所以 optional.md 是 17 个小节。

按 category 分布：

| category | 条数 | 落点 |
|---|---|---|
| pattern | 129 | patterns-common.md 13、patterns-zh.md 30、patterns-en.md 79，另 7 条未落地 |
| process | 66 | process.md 54，另 12 条未落地 |
| protection | 47 | protection.md 46，另 1 条未落地 |
| measurement | 34 | measurement.md 18，另 16 条未落地 |
| style-opinion | 20 | 全部未落进模式表：optional.md 8、conflicts.md 12 |
| genre | 11 | genres.md 10，另 1 条未落地 |

按 language 分布：both 152、en 102、zh 53。

`decision_origin`：model-proposed 172、human-approved 135。172 条待 `upstream-monitor approve` 翻成 human-approved，见第 10 节。写作后修正把 ALL-P-002 与 ALL-P-004 从 human-approved 退回 model-proposed（改了 rule_summary），因此这两个数比全局复核（0005）记的 170 / 137 各挪了 2。

独立来源分布（`independent_sources`）：

| 独立来源数 | 规则条数 |
|---|---|
| 1 | 200 |
| 2 | 45 |
| 3 | 30 |
| 4 | 16 |
| 5 | 10 |
| 6 | 2 |
| 7 | 4 |

200 条只有一个独立来源，占 65%。这个数字本身不是采用依据（criteria.md 第 3 条），单来源里既有 ALL-PROT-010、ALL-M-001 这类采用的，也有 EN-S-005 至 EN-S-011 这类拒绝的。另外这个字段是按 lineage 机械去重算出来的，与实质独立性有出入，见第 10 节。

model-proposed 的 172 条按 category：pattern 69、process 34、protection 28、measurement 17、style-opinion 16、genre 8。

`relations` 共 524 条有向边：pairs-with 392、excepts 67、conflicts-with 62、supersedes 3。全局复核结束时是 516 条，写作后修正补了 4 对双向 pairs-with。

### 3.2 四批各自的增量

新增规则按批（一条规则归到它第一次拿到证据的那一批）：

| 批次 | 新增 | adopted | awm | rejected | reference-only | deferred | duplicate | unverified |
|---|---|---|---|---|---|---|---|---|
| 0001 首次合并 | 144 | 87 | 33 | 10 | 7 | 4 | 2 | 1 |
| 0002 中文批 | 72 | 47 | 11 | 9 | 5 | 0 | 0 | 0 |
| 0003 英文批一 | 34 | 9 | 12 | 11 | 2 | 0 | 0 | 0 |
| 0004 英文批二 | 57 | 30 | 22 | 2 | 2 | 1 | 0 | 0 |
| 0005 全局复核 | 0 | | | | | | | |
| 合计 | 307 | 173 | 78 | 32 | 16 | 5 | 2 | 1 |

上表的 decision 是**当前值**，不是各批当时的裁决值。全局复核改判过两条（ALL-PROC-027 从 duplicate 改 rejected、ALL-PROC-031 保持 duplicate），所以按批分列的和与各批报告第 3 节的原始数字有出入：0001 报告当时记 rejected 9、duplicate 3，现在是 10 和 2。

新增规则按 category 分批：

| 批次 | protection | process | pattern | measurement | genre | style-opinion |
|---|---|---|---|---|---|---|
| 0001 | 20 | 34 | 64 | 18 | 3 | 5 |
| 0002 | 17 | 16 | 22 | 8 | 4 | 5 |
| 0003 | 3 | 6 | 13 | 1 | 2 | 9 |
| 0004 | 7 | 10 | 30 | 7 | 2 | 1 |

新增规则按 language 分批：

| 批次 | both | zh | en |
|---|---|---|---|
| 0001 | 86 | 12 | 46 |
| 0002 | 31 | 41 | 0 |
| 0003 | 11 | 0 | 23 |
| 0004 | 24 | 0 | 33 |

追加证据（这一批给已有规则补了证据、结论不变）：0002 补 38 条、0003 补 48 条、0004 补 69 条，合计 155 条。按 `decisions.schema.json` 的口径，只追加证据不加 `decision_revision`，这三批都没加，见第 10 节。

全局复核（0005）改了 8 条规则的 `rule_summary` 或 `decision`（EN-P-003、ALL-M-002、ALL-PROT-019、ALL-PROC-007、ALL-PROC-027、ZH-M-006、ALL-M-019、ZH-PROC-004），另有 11 条改裁决理由、41 条新增关系、54 条改落点，合并 0 条、retired 0 条。relations 从 477 条增到 516 条。

### 3.3 本轮写作的增量

不改 decision，只写正文。九份 references 共 301 个 `###` 小节，与 307 条规则的差是 6：5 条 deferred 加 1 条 unverified 不建小节，列在 conflicts.md 末尾的表里。

| 文件 | 小节数 | 行数 |
|---|---|---|
| references/protection.md | 46 | 611 |
| references/process.md | 54 | 633 |
| references/patterns-common.md | 13 | 180 |
| references/patterns-zh.md | 30 | 351 |
| references/patterns-en.md | 79 | 904 |
| references/genres.md | 10 | 125 |
| references/measurement.md | 18 | 237 |
| references/conflicts.md | 34 | 376 |
| references/optional.md | 17 | 195 |
| 合计 | 301 | 3612 |

SKILL.md 从 97 行重写成 140 行，正文引用 79 个规则 id，全部存在于 decisions.yaml 且全部是 adopted 或 adopted-with-modification。evals 从 14 条扩到 26 条。

## 4 覆盖矩阵

行是规则 id，列是 10 个来源，格子里写这个来源给这条规则提供了几条证据，没有证据的留空。307 条按 category 分成六张表，不省略行。最后两列的 `ev` 是 `evidence_count`、`ind` 是 `independent_sources`。

来源列的缩写：pg = petergyang/no-ai-slop，qw = LifelongLazyLearner/qu-ai-wei，ws = jzOcb/writing-style-skill，ab = Aboudjem/humanizer-skill，sr = MrGeDiao/shuorenhua，op = op7418/Humanizer-zh，az = ai-zixun/humanizer-zh，bl = blader/humanizer，ss = hardikpandya/stop-slop，cb = conorbronsdon/avoid-ai-writing。

每一条证据在上游的具体 anchor 不在本表里，逐条列在四份分批报告的第 4 节；单元到规则的完整映射（804 条）在 `work/coverage.md`，簇的成员清单在 `work/clusters.md`。

### 4.1 protection（事实保护）（47 条）

| 规则 id | decision | pg | qw | ws | ab | sr | op | az | bl | ss | cb | ev | ind |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL-PROT-001 | adopted | 2 | 2 |  | 1 | 2 | 1 | 2 | 2 |  | 2 | 14 | 7 |
| ALL-PROT-002 | adopted | 1 |  |  | 1 | 1 |  |  |  |  | 1 | 4 | 4 |
| ALL-PROT-003 | adopted | 1 | 1 |  |  | 1 |  | 1 | 1 |  |  | 5 | 5 |
| ALL-PROT-004 | adopted-with-modification |  | 1 |  |  |  |  | 1 |  |  |  | 2 | 2 |
| ALL-PROT-005 | adopted-with-modification |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |
| ALL-PROT-006 | adopted-with-modification |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |
| ALL-PROT-007 | adopted-with-modification |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |
| ALL-PROT-008 | adopted |  | 2 |  | 1 |  |  |  | 1 |  |  | 4 | 3 |
| ALL-PROT-009 | adopted |  | 1 |  | 1 | 4 |  |  | 1 |  | 2 | 9 | 5 |
| ALL-PROT-010 | adopted |  | 2 |  |  |  |  |  |  |  |  | 2 | 1 |
| ALL-PROT-011 | adopted |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |
| ALL-PROT-012 | adopted | 1 | 1 |  |  | 1 |  |  |  |  | 1 | 4 | 4 |
| ALL-PROT-013 | adopted-with-modification |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ALL-PROT-014 | adopted |  | 1 |  |  | 1 |  | 1 |  |  |  | 3 | 3 |
| ALL-PROT-015 | adopted |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |
| ALL-PROT-016 | adopted |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |
| ALL-PROT-017 | adopted | 2 | 1 |  | 1 |  | 2 | 2 | 3 |  | 2 | 13 | 6 |
| ALL-PROT-018 | adopted |  | 1 |  |  | 1 |  |  | 1 |  | 2 | 5 | 4 |
| ALL-PROT-019 | adopted-with-modification |  | 3 |  |  | 2 |  |  | 1 |  | 1 | 7 | 4 |
| ALL-PROT-020 | adopted |  | 1 |  |  | 1 |  |  | 1 |  |  | 3 | 3 |
| ALL-PROT-021 | adopted |  |  |  |  |  |  | 1 |  |  |  | 1 | 1 |
| ALL-PROT-022 | adopted |  |  |  |  | 2 |  |  |  |  |  | 2 | 1 |
| ALL-PROT-023 | adopted |  |  |  |  | 4 |  |  |  |  |  | 4 | 1 |
| ALL-PROT-024 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ALL-PROT-025 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ALL-PROT-026 | adopted-with-modification |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ALL-PROT-027 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ALL-PROT-028 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ALL-PROT-029 | adopted |  |  |  |  | 2 |  |  |  |  |  | 2 | 1 |
| ALL-PROT-030 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ALL-PROT-031 | adopted |  |  |  |  | 3 |  |  |  |  |  | 3 | 1 |
| ALL-PROT-032 | adopted |  |  |  |  | 5 |  |  |  |  |  | 5 | 1 |
| ALL-PROT-033 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ALL-PROT-034 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ALL-PROT-035 | rejected |  |  |  |  |  |  |  | 1 |  |  | 1 | 1 |
| ALL-PROT-036 | adopted |  |  |  |  |  |  |  | 1 |  |  | 1 | 1 |
| ALL-PROT-037 | adopted |  |  |  |  |  |  |  | 1 |  | 1 | 2 | 2 |
| ALL-PROT-038 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-PROT-039 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-PROT-040 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-PROT-041 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-PROT-042 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-PROT-043 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-PROT-001 | adopted |  |  |  |  |  |  |  |  |  | 4 | 4 | 1 |
| ZH-PROT-001 | adopted |  |  |  |  |  |  | 1 |  |  |  | 1 | 1 |
| ZH-PROT-002 | adopted-with-modification |  |  |  |  |  |  | 1 |  |  |  | 1 | 1 |
| ZH-PROT-003 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |

### 4.2 process（流程）（66 条）

| 规则 id | decision | pg | qw | ws | ab | sr | op | az | bl | ss | cb | ev | ind |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL-PROC-001 | adopted | 2 |  | 1 | 1 | 1 |  |  |  |  |  | 5 | 4 |
| ALL-PROC-002 | adopted | 1 |  |  | 1 |  |  |  |  |  |  | 2 | 2 |
| ALL-PROC-003 | adopted | 2 | 1 |  |  |  |  |  |  |  |  | 3 | 2 |
| ALL-PROC-004 | adopted | 1 | 1 |  |  |  |  |  |  |  |  | 2 | 2 |
| ALL-PROC-005 | adopted |  | 2 |  |  |  |  | 2 |  |  |  | 4 | 2 |
| ALL-PROC-006 | adopted |  | 2 |  |  |  |  |  |  |  |  | 2 | 1 |
| ALL-PROC-007 | adopted-with-modification | 3 |  |  | 3 | 3 |  |  |  |  | 2 | 11 | 4 |
| ALL-PROC-008 | adopted-with-modification | 2 | 2 |  |  |  |  |  |  |  | 1 | 5 | 3 |
| ALL-PROC-009 | adopted | 1 | 2 |  |  |  |  |  | 2 |  |  | 5 | 3 |
| ALL-PROC-010 | adopted-with-modification |  | 2 |  |  | 1 |  |  |  |  |  | 3 | 2 |
| ALL-PROC-011 | adopted |  | 1 |  |  |  |  | 2 | 1 |  |  | 4 | 3 |
| ALL-PROC-012 | adopted-with-modification |  | 2 |  |  |  |  |  | 1 |  |  | 3 | 2 |
| ALL-PROC-013 | adopted |  | 2 |  |  |  |  |  |  |  |  | 2 | 1 |
| ALL-PROC-014 | adopted-with-modification | 2 | 2 |  | 3 |  |  |  | 2 | 1 | 2 | 12 | 6 |
| ALL-PROC-015 | adopted |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |
| ALL-PROC-016 | adopted |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ALL-PROC-017 | adopted |  |  |  | 1 |  |  |  |  |  | 1 | 2 | 2 |
| ALL-PROC-018 | adopted |  |  |  | 1 |  |  |  |  |  | 3 | 4 | 2 |
| ALL-PROC-019 | adopted-with-modification |  |  |  | 1 | 1 |  |  |  |  | 2 | 4 | 3 |
| ALL-PROC-020 | adopted |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |
| ALL-PROC-021 | adopted-with-modification |  | 3 |  |  |  |  |  | 2 |  |  | 5 | 2 |
| ALL-PROC-022 | adopted |  | 2 |  |  |  |  |  |  |  |  | 2 | 1 |
| ALL-PROC-023 | adopted |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |
| ALL-PROC-024 | adopted-with-modification |  | 2 |  |  | 1 |  |  |  |  | 2 | 5 | 3 |
| ALL-PROC-025 | adopted-with-modification |  |  |  | 1 | 1 |  | 1 |  |  | 3 | 6 | 4 |
| ALL-PROC-026 | reference-only |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ALL-PROC-027 | rejected |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ALL-PROC-028 | adopted-with-modification |  | 1 |  |  |  |  | 1 |  |  | 1 | 3 | 3 |
| ALL-PROC-029 | adopted | 1 | 2 |  | 1 | 1 |  |  |  |  | 3 | 8 | 5 |
| ALL-PROC-030 | adopted-with-modification | 2 |  |  |  |  | 1 | 1 |  |  |  | 4 | 3 |
| ALL-PROC-031 | duplicate |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ALL-PROC-032 | reference-only |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-PROC-033 | deferred |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-PROC-034 | rejected |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-PROC-035 | rejected |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ALL-PROC-036 | rejected |  |  |  |  |  |  | 8 |  |  |  | 8 | 1 |
| ALL-PROC-037 | adopted |  |  |  |  |  |  | 1 |  |  | 1 | 2 | 2 |
| ALL-PROC-038 | adopted |  |  |  |  | 1 |  | 1 |  |  |  | 2 | 2 |
| ALL-PROC-039 | adopted-with-modification |  |  |  |  | 2 |  |  |  |  | 1 | 3 | 2 |
| ALL-PROC-040 | adopted |  |  |  |  | 7 |  |  |  |  |  | 7 | 1 |
| ALL-PROC-041 | rejected |  |  |  |  | 3 |  |  |  |  |  | 3 | 1 |
| ALL-PROC-042 | adopted |  |  |  |  | 9 |  |  |  |  |  | 9 | 1 |
| ALL-PROC-043 | adopted |  |  |  |  | 5 |  |  |  |  |  | 5 | 1 |
| ALL-PROC-044 | adopted-with-modification |  |  |  |  | 2 |  |  |  |  |  | 2 | 1 |
| ALL-PROC-045 | adopted |  |  |  |  | 5 |  |  |  |  |  | 5 | 1 |
| ALL-PROC-046 | rejected |  |  |  |  | 2 | 1 | 1 |  |  |  | 4 | 3 |
| ALL-PROC-047 | adopted |  |  |  |  |  |  |  | 1 |  |  | 1 | 1 |
| ALL-PROC-048 | adopted |  |  |  |  |  |  |  | 1 |  |  | 1 | 1 |
| ALL-PROC-049 | adopted-with-modification |  |  |  |  |  |  |  | 1 |  |  | 1 | 1 |
| ALL-PROC-050 | adopted-with-modification |  |  |  |  |  |  |  | 1 |  |  | 1 | 1 |
| ALL-PROC-051 | adopted-with-modification |  |  |  |  |  |  |  | 1 |  | 1 | 2 | 2 |
| ALL-PROC-052 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 4 | 4 | 1 |
| ALL-PROC-053 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 2 | 2 | 1 |
| ALL-PROC-054 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-PROC-055 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-PROC-056 | adopted |  |  |  |  |  |  |  |  |  | 3 | 3 | 1 |
| ALL-PROC-057 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 5 | 5 | 1 |
| ALL-PROC-058 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 3 | 3 | 1 |
| ALL-PROC-059 | rejected |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-PROC-060 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-PROC-001 | adopted |  |  |  |  |  |  |  | 2 |  |  | 2 | 1 |
| EN-PROC-002 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ZH-PROC-001 | rejected |  |  |  |  |  | 1 |  |  |  |  | 1 | 1 |
| ZH-PROC-002 | adopted-with-modification |  |  |  |  |  |  | 2 |  |  |  | 2 | 1 |
| ZH-PROC-003 | adopted |  |  |  |  |  |  | 3 |  |  |  | 3 | 1 |
| ZH-PROC-004 | adopted-with-modification |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |

### 4.3 pattern（写法模式）（129 条）

| 规则 id | decision | pg | qw | ws | ab | sr | op | az | bl | ss | cb | ev | ind |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL-P-001 | adopted-with-modification | 1 | 2 |  | 2 |  | 1 | 1 | 1 | 1 | 4 | 13 | 7 |
| ALL-P-002 | adopted | 1 |  |  | 3 |  |  | 1 | 3 |  | 3 | 11 | 5 |
| ALL-P-003 | adopted |  |  | 1 | 1 |  |  |  |  |  |  | 2 | 2 |
| ALL-P-004 | adopted | 1 | 1 |  | 2 |  |  | 1 | 1 | 1 | 2 | 9 | 7 |
| ALL-P-005 | adopted |  | 1 |  | 1 |  |  | 1 | 1 |  | 3 | 7 | 5 |
| ALL-P-006 | adopted | 1 | 1 |  |  |  |  |  |  |  |  | 2 | 2 |
| ALL-P-007 | adopted | 1 |  |  | 1 | 2 | 1 | 2 |  | 1 | 1 | 9 | 7 |
| ALL-P-008 | adopted |  |  |  | 1 |  |  | 1 |  |  | 2 | 4 | 3 |
| ALL-P-009 | adopted |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |
| ALL-P-010 | adopted | 1 |  |  |  | 2 |  |  |  |  |  | 3 | 2 |
| ALL-P-011 | adopted |  |  |  | 1 |  | 1 |  |  |  |  | 2 | 2 |
| ALL-P-012 | adopted |  |  |  |  | 2 |  | 1 |  |  |  | 3 | 2 |
| ALL-P-013 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-001 | adopted | 1 |  |  | 1 |  |  |  | 1 |  | 1 | 4 | 4 |
| EN-P-002 | adopted |  |  |  | 1 |  |  |  | 1 |  | 2 | 4 | 3 |
| EN-P-003 | adopted | 2 |  |  |  |  |  |  |  |  | 4 | 6 | 2 |
| EN-P-004 | adopted | 1 |  |  | 1 |  |  |  | 1 | 1 | 2 | 6 | 5 |
| EN-P-005 | adopted |  |  |  | 1 |  |  |  |  |  | 1 | 2 | 2 |
| EN-P-006 | adopted | 2 |  |  | 1 |  |  |  | 1 | 2 | 1 | 7 | 5 |
| EN-P-007 | adopted | 2 |  |  | 3 |  |  |  | 2 | 2 | 4 | 13 | 5 |
| EN-P-008 | adopted | 1 |  |  |  |  |  |  | 1 |  | 3 | 5 | 3 |
| EN-P-009 | adopted | 1 |  |  | 1 |  |  |  |  | 2 | 3 | 7 | 4 |
| EN-P-010 | adopted | 1 |  |  |  |  |  |  |  |  |  | 1 | 1 |
| EN-P-011 | adopted | 1 |  |  |  |  |  |  |  |  |  | 1 | 1 |
| EN-P-012 | adopted |  |  |  | 1 |  |  |  | 1 |  | 1 | 3 | 3 |
| EN-P-013 | adopted | 1 |  |  | 1 |  |  |  | 1 |  | 1 | 4 | 4 |
| EN-P-014 | adopted | 1 |  |  | 2 |  |  |  | 1 |  | 1 | 5 | 4 |
| EN-P-015 | adopted | 1 |  |  | 1 |  |  |  | 1 |  | 1 | 4 | 4 |
| EN-P-016 | adopted | 1 |  |  |  |  |  |  |  |  |  | 1 | 1 |
| EN-P-017 | adopted | 1 |  |  | 1 |  |  |  | 2 |  | 2 | 6 | 4 |
| EN-P-018 | adopted |  |  |  | 2 |  |  |  | 2 |  | 1 | 5 | 3 |
| EN-P-019 | adopted | 1 |  |  | 1 |  |  |  |  |  | 1 | 3 | 3 |
| EN-P-020 | adopted |  |  |  | 1 |  |  |  | 1 |  |  | 2 | 2 |
| EN-P-021 | adopted |  |  |  | 1 |  |  |  | 1 |  | 1 | 3 | 3 |
| EN-P-022 | adopted | 2 |  |  |  |  |  |  |  | 2 | 4 | 8 | 3 |
| EN-P-023 | adopted | 1 |  |  | 2 |  |  |  | 1 |  | 2 | 6 | 4 |
| EN-P-024 | adopted | 1 |  |  | 1 |  |  |  | 1 | 1 | 1 | 5 | 5 |
| EN-P-025 | adopted | 1 |  |  |  |  |  |  | 1 | 1 | 1 | 4 | 4 |
| EN-P-026 | adopted-with-modification | 1 |  |  | 1 |  |  |  |  |  | 1 | 3 | 3 |
| EN-P-027 | adopted-with-modification |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| EN-P-028 | adopted |  |  |  | 3 |  |  |  | 3 |  | 3 | 9 | 3 |
| EN-P-029 | adopted |  |  |  | 1 |  |  |  | 1 |  | 2 | 4 | 3 |
| EN-P-030 | adopted-with-modification |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| EN-P-031 | adopted |  |  |  | 1 |  |  |  | 1 |  | 2 | 4 | 3 |
| EN-P-032 | adopted |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| EN-P-033 | adopted |  |  |  | 1 |  |  |  | 1 |  | 1 | 3 | 3 |
| EN-P-034 | reference-only |  |  |  | 1 |  |  |  |  | 1 |  | 2 | 2 |
| EN-P-035 | adopted-with-modification |  |  |  | 1 |  |  |  | 1 |  | 1 | 3 | 3 |
| EN-P-036 | adopted |  |  |  | 1 |  |  |  | 1 |  | 1 | 3 | 3 |
| EN-P-037 | adopted-with-modification |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| EN-P-038 | adopted |  |  |  | 4 |  |  |  |  |  | 4 | 8 | 2 |
| EN-P-039 | adopted-with-modification |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| EN-P-040 | adopted-with-modification |  |  |  | 2 |  |  |  |  |  |  | 2 | 1 |
| EN-P-041 | adopted |  |  |  | 1 |  |  |  | 1 |  |  | 2 | 2 |
| EN-P-042 | adopted-with-modification |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| EN-P-043 | adopted |  |  |  |  |  |  |  | 1 |  |  | 1 | 1 |
| EN-P-044 | adopted-with-modification |  |  |  |  |  |  |  | 1 |  | 1 | 2 | 2 |
| EN-P-045 | adopted |  |  |  |  |  |  |  | 1 |  | 1 | 2 | 2 |
| EN-P-046 | adopted |  |  |  |  |  |  |  | 3 |  |  | 3 | 1 |
| EN-P-047 | adopted-with-modification |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 2 |
| EN-P-048 | adopted |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-P-049 | adopted-with-modification |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-P-050 | adopted-with-modification |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-P-051 | adopted-with-modification |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-P-052 | adopted-with-modification |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-P-053 | rejected |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-P-054 | rejected |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-P-055 | adopted-with-modification |  |  |  |  |  |  |  |  | 1 | 1 | 2 | 2 |
| EN-P-056 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 2 | 2 | 1 |
| EN-P-057 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-058 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-059 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-060 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-061 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-062 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-063 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 3 | 3 | 1 |
| EN-P-064 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-065 | rejected |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-066 | adopted |  |  |  |  |  |  |  |  |  | 2 | 2 | 1 |
| EN-P-067 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-068 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-069 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-070 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-071 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-072 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-073 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-074 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 2 | 2 | 1 |
| EN-P-075 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-076 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-077 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-078 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-079 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-080 | adopted |  |  |  |  |  |  |  |  |  | 2 | 2 | 1 |
| EN-P-081 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-082 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-083 | reference-only |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-P-084 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ZH-P-001 | adopted |  | 1 |  | 1 | 4 | 2 | 1 |  |  |  | 9 | 5 |
| ZH-P-002 | adopted |  |  |  | 1 | 1 | 1 |  |  |  |  | 3 | 3 |
| ZH-P-003 | adopted |  |  |  | 1 |  |  | 2 |  |  |  | 3 | 2 |
| ZH-P-004 | adopted |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ZH-P-005 | adopted |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ZH-P-006 | adopted |  |  |  | 1 |  |  | 1 |  |  |  | 2 | 2 |
| ZH-P-007 | adopted |  |  |  | 1 |  | 1 |  |  |  |  | 2 | 2 |
| ZH-P-008 | adopted |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |
| ZH-P-009 | adopted-with-modification |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |
| ZH-P-010 | unverified |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ZH-P-011 | adopted-with-modification |  |  |  | 1 | 2 |  | 2 |  |  |  | 5 | 3 |
| ZH-P-012 | rejected |  |  |  |  |  | 1 |  |  |  |  | 1 | 1 |
| ZH-P-013 | adopted |  |  |  |  |  | 2 |  |  |  |  | 2 | 1 |
| ZH-P-014 | adopted |  |  |  |  |  | 1 |  |  |  |  | 1 | 1 |
| ZH-P-015 | adopted |  |  |  |  |  | 1 | 1 |  |  |  | 2 | 2 |
| ZH-P-016 | adopted |  |  |  |  |  | 1 |  |  |  |  | 1 | 1 |
| ZH-P-017 | adopted |  |  |  |  |  | 1 |  |  |  |  | 1 | 1 |
| ZH-P-018 | adopted |  |  |  |  |  | 1 |  |  |  |  | 1 | 1 |
| ZH-P-019 | adopted |  |  |  |  |  | 1 |  |  |  |  | 1 | 1 |
| ZH-P-020 | adopted |  |  |  |  |  | 1 |  |  |  |  | 1 | 1 |
| ZH-P-021 | adopted |  |  |  |  |  | 1 |  |  |  |  | 1 | 1 |
| ZH-P-022 | adopted |  |  |  |  | 1 | 2 |  |  |  |  | 3 | 2 |
| ZH-P-023 | adopted |  |  |  |  |  | 1 |  |  |  |  | 1 | 1 |
| ZH-P-024 | adopted |  |  |  |  | 1 |  | 1 |  |  |  | 2 | 2 |
| ZH-P-025 | adopted-with-modification |  |  |  |  |  |  | 3 |  |  |  | 3 | 1 |
| ZH-P-026 | adopted-with-modification |  |  |  |  |  |  | 1 |  |  |  | 1 | 1 |
| ZH-P-027 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ZH-P-028 | adopted |  |  |  |  | 2 |  |  |  |  |  | 2 | 1 |
| ZH-P-029 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ZH-P-030 | adopted |  |  |  |  | 2 |  |  |  |  |  | 2 | 1 |
| ZH-P-031 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ZH-P-032 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |

### 4.4 measurement（度量与验收）（34 条）

| 规则 id | decision | pg | qw | ws | ab | sr | op | az | bl | ss | cb | ev | ind |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL-M-001 | adopted | 1 |  |  |  |  |  |  |  |  | 1 | 2 | 2 |
| ALL-M-002 | adopted |  |  |  | 4 |  |  |  | 2 |  | 2 | 8 | 3 |
| ALL-M-003 | adopted-with-modification |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ALL-M-004 | adopted |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ALL-M-005 | rejected |  |  |  | 3 |  |  |  |  |  |  | 3 | 1 |
| ALL-M-006 | reference-only |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-M-007 | reference-only |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-M-008 | deferred |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-M-009 | deferred |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-M-010 | rejected |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-M-011 | deferred |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-M-012 | rejected |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-M-013 | duplicate |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-M-014 | rejected |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-M-015 | rejected |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-M-016 | rejected |  |  | 1 |  |  |  |  |  |  |  | 1 | 1 |
| ALL-M-017 | reference-only |  |  |  |  |  | 2 |  |  | 2 |  | 4 | 2 |
| ALL-M-018 | adopted |  |  |  |  | 2 |  |  |  |  | 1 | 3 | 2 |
| ALL-M-019 | adopted-with-modification |  |  |  |  | 3 |  |  |  |  |  | 3 | 1 |
| ALL-M-020 | adopted-with-modification |  |  |  |  |  |  |  | 1 |  |  | 1 | 1 |
| ALL-M-021 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-M-022 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-M-023 | adopted |  |  |  |  |  |  |  |  |  | 3 | 3 | 1 |
| ALL-M-024 | adopted |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-M-025 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-M-026 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| EN-M-001 | adopted-with-modification |  |  |  | 1 |  |  |  |  |  | 3 | 4 | 2 |
| EN-M-002 | deferred |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ZH-M-001 | adopted |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ZH-M-002 | reference-only |  |  |  |  |  | 1 |  |  |  |  | 1 | 1 |
| ZH-M-003 | reference-only |  |  |  |  |  |  | 1 |  |  |  | 1 | 1 |
| ZH-M-004 | adopted |  |  |  |  |  |  | 1 |  |  |  | 1 | 1 |
| ZH-M-005 | adopted |  |  |  |  | 1 |  | 1 |  |  |  | 2 | 2 |
| ZH-M-006 | adopted-with-modification |  |  |  |  | 5 |  |  |  |  |  | 5 | 1 |

### 4.5 genre（体裁）（11 条）

| 规则 id | decision | pg | qw | ws | ab | sr | op | az | bl | ss | cb | ev | ind |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL-G-001 | adopted-with-modification |  | 1 |  |  | 1 |  | 1 |  |  |  | 3 | 3 |
| ALL-G-002 | adopted-with-modification |  |  |  | 1 |  |  | 1 | 1 |  | 1 | 4 | 4 |
| ALL-G-003 | adopted |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ALL-G-004 | adopted |  |  |  |  | 1 |  |  |  |  |  | 1 | 1 |
| ALL-G-005 | rejected |  |  |  |  |  |  |  | 1 |  |  | 1 | 1 |
| ALL-G-006 | adopted-with-modification |  |  |  |  |  |  |  | 1 |  | 1 | 2 | 2 |
| ALL-G-007 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ALL-G-008 | adopted-with-modification |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ZH-G-001 | adopted |  |  |  |  |  | 2 |  |  |  |  | 2 | 1 |
| ZH-G-002 | adopted-with-modification |  |  |  |  | 6 |  |  |  |  |  | 6 | 1 |
| ZH-G-003 | adopted |  |  |  |  | 7 |  |  |  |  |  | 7 | 1 |

### 4.6 style-opinion（风格意见）（20 条）

| 规则 id | decision | pg | qw | ws | ab | sr | op | az | bl | ss | cb | ev | ind |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL-S-001 | rejected |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| ALL-S-002 | reference-only |  |  |  | 1 |  |  |  |  |  | 1 | 2 | 2 |
| EN-S-001 | adopted-with-modification |  |  |  | 5 |  |  |  |  |  | 6 | 11 | 2 |
| EN-S-002 | reference-only |  |  |  | 7 |  |  |  |  |  | 1 | 8 | 2 |
| EN-S-003 | rejected |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |
| EN-S-004 | rejected |  |  |  |  |  |  |  | 1 |  |  | 1 | 1 |
| EN-S-005 | rejected |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-S-006 | rejected |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-S-007 | rejected |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-S-008 | rejected |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-S-009 | rejected |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-S-010 | reference-only |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-S-011 | rejected |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-S-012 | reference-only |  |  |  |  |  |  |  |  | 1 |  | 1 | 1 |
| EN-S-013 | reference-only |  |  |  |  |  |  |  |  |  | 1 | 1 | 1 |
| ZH-S-001 | rejected |  |  |  |  |  | 1 |  |  |  |  | 1 | 1 |
| ZH-S-002 | rejected |  |  |  |  |  |  | 1 |  |  |  | 1 | 1 |
| ZH-S-003 | reference-only |  |  |  |  |  |  | 3 |  |  |  | 3 | 1 |
| ZH-S-004 | reference-only |  |  |  |  |  |  | 3 |  |  |  | 3 | 1 |
| ZH-S-005 | rejected |  |  |  |  |  |  | 1 |  |  |  | 1 | 1 |

## 5 冲突与取舍

四批加一次全局复核一共处理了 54 组冲突，逐组的完整写法（各方主张什么、为什么选这一条、被放弃的那条记成什么、relations 怎么记）在各自的报告里。下表一组一行，指向所在报告的小节。给上游作者看的版本在 `skills/maybe-humanizer/references/conflicts.md`，那里每条固定写四段：主张、针对的现象、本仓库的选择、怎么开启。

| 组 | 争的是什么 | 结论 | 出处 |
|---|---|---|---|
| 破折号 | 零容忍还是分级 | 分级，落 EN-P-026 | 0001 §5.1 |
| 结构 | 默认保留还是按需重建 | 按授权档分，落 ALL-PROC-012 与 ALL-PROC-030 | 0001 §5.2 |
| 人味 | 保留原有的还是注入新的 | 只保留，落 ALL-PROT-017 与 ALL-PROT-018 | 0001 §5.3 |
| 声口 | 保留输入的还是改成某一档 | 默认保留输入，档位记 reference-only（后改判） | 0001 §5.4 |
| 保留语 | 保留犹疑还是删掉不自信 | 保留，落 ALL-PROT-004 | 0001 §5.5 |
| 证据数 | 能不能自动决定采用 | 不能，ALL-M-014 记 rejected | 0001 §5.6 |
| 验收 | 打分器还是自查清单 | 自查清单，ALL-M-005 记 rejected | 0001 §5.7 |
| 单来源强风格意见 | 进不进默认规则 | 不进，记 reference-only 或 rejected | 0001 §5.8 |
| 改动幅度 | 一条轴还是两条轴 | 两条轴，立 ALL-PROC-042 | 0002 §5.1 |
| 输出契约 | 默认附不附改动说明 | 附，ALL-PROC-046 记 rejected | 0002 §5.2 |
| 注入个性 | 保留原有的还是补出新的 | 只保留，ZH-PROC-001 与 ZH-S-001 记 rejected | 0002 §5.3 |
| 并列项 | 数量本身算不算模板信号 | 不算，ZH-P-012 记 rejected | 0002 §5.4 |
| 中文长破折号 | 分级还是零容忍 | 分级，ZH-S-002 记 rejected | 0002 §5.5 |
| 术语译法 | 读者友好还是指称精确 | 指称精确，ZH-S-005 记 rejected | 0002 §5.6 |
| 单文件兜底 | 降级运行还是说明读不到 | 说明读不到，ALL-PROC-035 记 rejected | 0002 §5.7 |
| 套用真人作者的声音 | 做不做 | 不做，ALL-PROC-036 记 rejected | 0002 §5.8 |
| 命中标注 | 行内标注还是单独一节 | 单独一节 | 0002 §5.9 |
| 代码注释 | 整体跳过还是按窄例外处理 | 窄例外，落 ALL-PROT-026 | 0002 §5.10 |
| 系统行为主语 | 分域，不是冲突 | 两条并存，落 ALL-PROT-033 与 ALL-P-004 | 0002 §5.11 |
| 中文批五条 | 没进默认规则的理由 | 逐条见报告 | 0002 §5.12 |
| ZH-P-011 | 从 unverified 改判 | 改判 adopted-with-modification | 0002 §5.13 |
| U-ohz-012 | 示例补写事实 | 不当规则采纳 | 0002 §5.14 |
| 破折号 | 四方口径并进一方 | 并进 EN-P-026 | 0003 §5.1 |
| 改写能不能加观点 | 能还是不能 | 不能，ALL-PROT-035 记 rejected | 0003 §5.2 |
| 虚构文本 | 整体不适用还是只豁免一条 | 整体不适用，ALL-G-005 记 rejected | 0003 §5.3 |
| stop-slop 四条强禁令 | 无条件禁还是带例外 | 四条全记 rejected | 0003 §5.4 |
| 删全部保留语 | 含 most 在内 | 记 rejected，EN-S-011 | 0003 §5.5 |
| 引号 | 原稿混用时怎么办 | 按取值顺序统一，落 EN-P-044 | 0003 §5.6 |
| 两条纯形式的句首禁令 | 采不采纳 | 不采纳 | 0003 §5.7 |
| 两条判据圈不准的句型禁令 | 采不采纳 | 不采纳，EN-P-053 与 EN-P-054 | 0003 §5.8 |
| 英文批一两条 reference-only | 名单 | 见报告 | 0003 §5.9 |
| 四处改了上游默认值的采纳 | 怎么改 | 见报告 | 0003 §5.10 |
| 两条中英对应规则 | 分立还是合成 both | 分立 | 0003 §5.11 |
| 假备选方案 | 三条单元合一条 | 合成一条 | 0003 §5.12 |
| cut quotables | 判据比上游宽 | 放宽后采纳 | 0003 §5.13 |
| 上游示例与上游规则自相矛盾 | 三处怎么处理 | 见报告 | 0003 §5.14 |
| 破折号 | 第四方口径收口 | 并进 EN-P-026，改密度算法 | 0004 §5.1 |
| 五个声口档位 | reference-only 还是可选项 | 改判为默认不启用的可选项，EN-S-001 | 0004 §5.2 |
| 四条轴 | 本仓库两条加上游两条 | 分两层，立 ALL-PROC-058 | 0004 §5.3 |
| 拆规则清单列出的九处冲突 | 逐一裁决 | 见报告，含本批唯一一组 conflicts-with | 0004 §5.4 |
| 执行强度上限 | 三条单元合一条元规则 | 立 ALL-PROC-056 | 0004 §5.5 |
| 结构优先于词汇 | 论证采不采纳 | 采纳规则、不采纳论证 | 0004 §5.6 |
| 误伤控制 | 写进哪里 | 五条落法不一，定为正文三段式 | 0004 §5.7 |
| 英文批二两条 rejected | 理由 | 见报告 | 0004 §5.8 |
| 英文批二三条不进默认规则 | 理由 | 见报告 | 0004 §5.9 |
| 两处中英对应规则 | 分立还是合成 | 分立 | 0004 §5.10 |
| 上游自述的改编来源 | 算不算独立来源 | 按工具口径填字段，实质判断写进 rationale | 0004 §5.11 |
| 多条单元合成一条规则 | 六处 | 见报告 | 0004 §5.12 |
| ALL-PROC-027 与 ALL-PROC-041 | 同一主张两批两种结论 | 027 从 duplicate 改判 rejected | 0005 §5.1 |
| ALL-PROC-007 与第三种工作模式 | 说「两种」而实有三种 | 改 rule_summary 指向 ALL-PROC-052 | 0005 §5.2 |
| 两张体裁档位表 | ZH-G-002 与 ALL-G-007 | 两张都留，各答一个问题 | 0005 §5.3 |
| ALL-PROC-010 与 ALL-M-022 | 一组都不跳过 vs 只处理前两档 | 改成单向 excepts | 0005 §5.4 |
| 三组 conflicts-with | rationale 单向点名 | 补齐成双向 | 0005 §5.5 |
| 四条中文排版规则 | 关系记什么 | pairs-with，分两层 | 0005 §5.6 |

下面七组是这轮里改变了 skill 形态的取舍，各写一段。

**破折号：四方口径最后并成一条。**四个上游各给一套：aboudjem 分级（200 词以下零处、以上一到两处）、blader 带样本例外的禁令（EN-S-004）、stop-slop 无条件禁（EN-S-009）、conorbronsdon 按每千词折算加两种字形一并计入。前三方在 0001 与 0003 收口，第四方在 0004 收口。最终的 EN-P-026 取的是 conorbronsdon 那套的密度算法（200 词以下零处、以上按每千词至多一处向下取整）加上它的两个细节（`--` 与 em dash 一并计入，标题计入正文频率，列表里跟在加粗引导词后的破折号豁免），另保留 blader 的样本例外（走 ALL-PROC-049）。两条无条件禁令记 rejected 并与 EN-P-026 互相点名。选分级不选禁令的理由是保真：禁令会把作者原有的停顿改成句号，那是 ALL-PROT-017 管的东西。

**两条轴变四条轴，再分两层。**试验版只有一条改写力度轴（ALL-PROC-005），说不清「改得自然一点但一句都别删」。中文批立了编辑范围轴（ALL-PROC-042，structural / bounded / in-place），起因是中文长文走最宽档时缩水幅度依模型而定，同一篇可能少两成也可能少四成。英文批二又带来两条：语境档位（ALL-G-007）和声口档位（EN-S-001）。四条并列会互相架空，所以 0004 立了 ALL-PROC-058 把它们分成两层：授权层（力度、范围）回答允许改到什么程度，判据层（语境、声口）回答按什么标准判、写成什么声音；判据层可以要求查得更严，不能扩大授权。这是 SKILL.md 分诊段里最长的一节。

**人味：只保留，不注入。**三个中文上游里有两个把「注入个性」写成必做步骤，其中 ZH-PROC-001 还写成不分体裁的固定动作；blader 的 ALL-PROT-035 更克制，只允许加观点不允许加事实主张。三条全记 rejected。理由不是数量，是署名关系：补出来的反应是模型的反应，署在作者名下，读者无从分辨。上游那条 ALL-PROT-035 的分界（观点不可核对所以无害）在本仓库不成立，因为观点会被读成作者的立场。保留原有的那一半照收：ALL-PROT-017 明写作者的脏话、犹疑、跑题、自我纠正都属于作者。

**输出契约：默认仍附改动说明。**这是四批里证据最集中的一条反对意见，三个独立的中文来源都主张默认只给正文，理由一致且成立（拿了就发）。仍然保留 ALL-PROC-008 的理由不是票数，是这套规则的结构：现在的规则允许删整句、会把拿不准的删除列成待确认清单、会把「结论可能超出证据」单列一节、更正英文品牌名大小写时要点出来，这四件事都需要一个固定位置来写。用户说一句「只要终稿」就能拿到不带说明的版本（ALL-PROC-021），反过来则拿不回已经丢掉的判断依据。

**不打分。**ALL-M-005 要求按公式算一个 0 到 100 的分数并按分段给判语，其中最低一档写明「不该被任何检测器标记」。这落在 criteria.md 第 5 条第 1 款：把绕过检测器写成了达标条件。此外公式的三项权重没有校准依据，同一来源内部两套严重度量表互不一致，而分数会被当成结论用，与 ALL-PROT-012（不做作者身份鉴定）冲突。替代做法是 ALL-PROC-014 的自查清单加 ALL-M-022 的三档处理顺序：排序而不打分。

**声口档位从只作参考改成可以用的选项。**试验版把 EN-S-001 记 reference-only，理由是「授权改写不等于授权更换声口」。英文批二给了它两样此前没有的东西：每一档的可核对目标（casual 是平均句长 14 词以内、通篇用缩写这类），以及一条覆盖全部五档的硬边界（只能把原文已经有的东西带出来，原文没有第一人称就不加）。有了这条硬边界，档位不再与 ALL-PROT-018 冲突，因此改判 adopted-with-modification，默认仍不启用，做法写在 optional.md。

**执行强度上限。**英文批二把三条单元合成 ALL-PROC-056。它管的是全部 307 条规则的执行方式，而不是某一条：命中数归零不是验收标准；词表和阈值是默认值；一稿改完仍留有不规整的用词和长短失衡的段落是正常结果。它与 ALL-PROC-010（四组检查一组都不跳过）方向相反、配套使用，两条在 process.md 与 SKILL.md 里都写在相邻位置。这条与 ALL-M-023、ALL-M-024 合起来回答同一件事的三个面（规则有多可靠、命中的证据力多强、据此该执行到多严），SKILL.md 用一节把三条串起来。

## 6 被拒绝规则与理由

32 条 rejected，一条一行。「criteria」列写对应 criteria.md 的哪一条。落在 criteria.md 第 5 条三类内容里的只有 ALL-M-005 一条，单独标出。完整的四段写法（含「他那个场景成立时怎么办」）在 `references/conflicts.md` 对应小节。

| 规则 id | 主张 | 拒绝理由 | criteria | 出处 |
|---|---|---|---|---|
| ALL-M-005 | 按公式算 0 到 100 的 AI 味分数并按分段给判语 | **落在第 5 条第 1 款**：最低分档定义为「不该被任何检测器标记」，把绕过检测器写成达标条件；权重无校准依据，两套量表自相矛盾，分数会被当成结论用，撞 ALL-PROT-012 | 第 5 条第 1 款 | 0001 §5.7 |
| ALL-M-010 | 用内容指纹配对初稿和定稿 | 工具实现规则，管两个文件怎么配对，不管文本怎么写，skill 的输出不会因它不同 | 第 3 条第 1 项 | 0001 §5.6 |
| ALL-M-012 | 提炼候选规则后先去重 | 去重是 skill-merge 归并阶段的动作，已在 skills/skill-merge/references/process.md 步骤 3 执行，不属于改写规则 | 第 3 条第 1 项 | 0001 §5.6 |
| ALL-M-014 | 按出现次数分三档，最高一档不经人工确认自动生效 | 证据数不能自动决定采用；本次合并本身就是反例，单来源的 ALL-PROT-010 采用了，五条证据的 EN-S-001 不进默认规则 | 第 3 条 | 0001 §5.6 |
| ALL-M-015 | 把字数变化百分比当改动幅度信号记下 | 不影响任何输出决策，且与 ALL-PROT-003 的关系是误导性的：字数少不等于删了实质，字数不变不等于没删 | 第 3 条第 1 项 | 0001 §5.6 |
| ALL-M-016 | 用未改动比例趋势判断规则好不好用 | 衡量的是跨会话风格档案的收敛度，本 skill 没有跨会话记录，指标无处可算；好不好用走 evals | 第 3 条第 1 项 | 0001 §5.6 |
| ALL-S-001 | 写作应当像人一样怪异、具体、不一致 | 不可判定：给一段文字，指不出哪个词或哪个结构违反了「要怪异」 | 第 2 条 | 0001 §5.8 |
| EN-S-003 | 选第二或第三个想到的词，用意外类比 | 不可判定：无法从成稿上指出哪个词是作者第一反应想到的，它约束的是写作过程不是结果 | 第 2 条 | 0001 §5.8 |
| ALL-PROC-034 | 改写规则文件前先备份旧版本 | 本 skill 不改写任何规则文件，没有备份对象；ALL-PROC-033 将来落地时版本管理由 git 承担 | 第 3 条第 1 项 | 0001 §5.6 |
| ZH-P-012 | 并列项默认取两项，三项改成两项或四项 | 现象成立但解法是把一个模板换成另一个模板：原文确实有三件事时，改两项要删一项（撞 ALL-PROT-003），改四项要补一项（撞 ALL-PROT-001） | 第 1 条 | 0002 §5.4 |
| ZH-S-001 | 改写时补出作者的反应和立场 | 补出来的反应是模型的反应，署在作者名下；「两边各说一句」这个现象已由 ALL-PROC-018 承认并处理 | 第 1 条 | 0002 §5.3 |
| ZH-S-002 | 中文正文完全禁用长破折号 | 中文破折号有真实用法（解释、转折、话锋中断），一刀切会把作者原有的停顿改成句号 | 第 4 条 | 0002 §5.5 |
| ZH-S-005 | PR 在中文长文里译成「代码审查」 | 两者不等价：PR 是变更提案，代码审查是其中一项活动；项目要固定译法写进自己的术语表 | 第 1 条 | 0002 §5.6 |
| ZH-PROC-001 | 无条件注入个性，不因体裁跳过 | 与 ZH-S-001 同一件事的流程版，且写成不分体裁的固定动作，技术与法律文本一并适用 | 第 1 条 | 0002 §5.3 |
| ALL-PROC-035 | 只加载 SKILL.md 时兜底规则直接生效 | 本仓库的 SKILL.md 不设计成「能单独工作但不完整」；读不到 references 时说明读不到，不降级运行 | 第 3 条第 1 项 | 0002 §5.7 |
| ALL-PROC-036 | 可选套用某位真人作者的声音 | 不减少 AI 痕迹，只换一种可辨认的腔调，且署名关系不清；要对齐文风的正确做法是给样本（ALL-PROC-037） | 第 3 条第 1 项 | 0002 §5.8 |
| ALL-PROC-041 | 按文本状态自动定改写档位 | 三档划分本身严谨，但把「该改多少」的决定权从用户措辞交给模型对文本状态的判断，与 ALL-PROC-005 相反 | 第 3 条第 3 项 | 0005 §5.1 |
| ALL-PROC-046 | 默认只给正文，不附改动说明 | 现在的规则会删整句、会列待确认清单、会单列超证据风险、会更正品牌名大小写，四件事都要有固定位置写；要正文说一句即可（ALL-PROC-021） | 第 3 条 | 0002 §5.2 |
| ALL-PROC-027 | 再设一档更激进的：句更短、态度更鲜明、去掉全部保留语 | 与 ALL-PROC-005 是同一件事的两种说法，且「去掉全部保留语」直接撞 ALL-PROT-004 | 第 3 条 | 0005 §5.1 |
| ALL-PROC-059 | `--style` 参数的解析规则 | 命令行参数解析不是改写规则，本仓库的 skill 没有这个参数；它服务的「点名当前跑哪种模式」已由 ALL-PROC-057 收下 | 第 3 条第 1 项 | 0004 §5.8 |
| ALL-PROT-035 | 改写时可以加观点、不加事实主张 | 上游把界线划在能不能被核对；本仓库的判断是观点会被读成作者的立场，加进去同样失真 | 第 1 条与第 8 条 | 0003 §5.2 |
| ALL-G-005 | 虚构文本豁免「不得编造细节」 | 本仓库对虚构文本的处理是整体不适用（ALL-G-003），不是只豁免一条；只豁免一条会让其余模式表继续套在小说上 | 第 3 条第 1 项与第 8 条 | 0003 §5.3 |
| EN-P-053 | 不用 "By the time X, I was Y." 开场 | 判据是一个具体句式的字面形状，圈不准：这个句式在真人写的个人叙事里同样常见，反例不成立 | 第 3 条第 2 项 | 0003 §5.8 |
| EN-P-054 | 不用 "X that isn't Y" 靠否定下定义 | 观察有道理但判据圈不出违反在哪：靠否定给出的定义在规格说明和对比语境里是正确写法 | 第 2 条 | 0003 §5.8 |
| EN-P-065 | 按无条件词表删保留语（perhaps、could potentially 等） | 这四个词多数时候承担真实的命题限定，无条件删会把有条件的说法变成确定的说法，撞 ALL-PROT-004 | 第 1 条与第 8 条 | 0004 §5.8 |
| EN-S-004 | 禁 em dash 与 en dash，样本除外 | 与 EN-P-026 的分级口径冲突；它的样本例外本仓库已由 ALL-PROC-049 收下 | 第 8 条 | 0003 §5.1 |
| EN-S-005 | 删掉全部副词，一个不留 | 判据是纯词形（No -ly words），会删掉承担命题限定的副词（possibly、roughly、arguably），撞 ALL-PROT-004；空强调那一半由 EN-P-003 收下 | 第 1 条 | 0003 §5.4 |
| EN-S-006 | 每句都要有一个人作主语 | 技术文档里描述系统行为的主语必须保留（ALL-PROT-033），换成人称主语会改变谁做了什么；「不隐藏施事者」那一半由 ALL-P-004 收下 | 第 1 条与第 8 条 | 0003 §5.4 |
| EN-S-007 | 一处被动语态都不留 | 被动语态在施事者不重要或未知时是正确写法；「隐藏施事者」那一半由 ALL-P-004 收下 | 第 1 条 | 0003 §5.4 |
| EN-S-008 | 并列项三项一律改两项 | 与 ZH-P-012 同一问题的英文侧：原文确实有三件事时改两项要删一项 | 第 1 条 | 0003 §5.4 |
| EN-S-009 | 全文一处破折号都不用 | 无条件禁令，与 EN-P-026 的分级口径冲突，理由同 ZH-S-002 | 第 1 条与第 8 条 | 0003 §5.1 |
| EN-S-011 | 软化语、强化语、保留语一律不留 | 判据看功能，会命中 most 这类限定词；上游自己的示例演示的正是删掉 most，那一处删除改变了命题范围 | 第 1 条 | 0003 §5.5 |

另有 2 条 duplicate（ALL-M-013 与 criteria.md 第 2 条是同一条要求；ALL-PROC-031 与 EN-S-001 的默认口径重复）、5 条 deferred、1 条 unverified，见第 10 节。

## 7 影响的本地文件

### 7.1 本轮（写正文与收尾）改的

| 文件 | 改了什么 |
|---|---|
| `skills/maybe-humanizer/references/protection.md` | 整份重写，46 个小节，611 行 |
| `skills/maybe-humanizer/references/process.md` | 整份重写，54 个小节，633 行 |
| `skills/maybe-humanizer/references/patterns-common.md` | 整份重写，13 个小节，180 行 |
| `skills/maybe-humanizer/references/patterns-zh.md` | 整份重写，30 个小节，351 行 |
| `skills/maybe-humanizer/references/patterns-en.md` | 整份重写，79 个小节，904 行 |
| `skills/maybe-humanizer/references/genres.md` | 整份重写，10 个小节，125 行 |
| `skills/maybe-humanizer/references/measurement.md` | 新文件，18 个小节，237 行 |
| `skills/maybe-humanizer/references/conflicts.md` | 整份重写并改变用途（只收未采纳），34 个小节加一张 deferred/unverified 表，376 行 |
| `skills/maybe-humanizer/references/optional.md` | 新文件，17 个小节，195 行 |
| `skills/maybe-humanizer/SKILL.md` | 整份重写，97 行改成 140 行；五段对应五个环节，末尾九行 references 表 |
| `skills/maybe-humanizer/evals/evals.json` | 14 条扩到 26 条，新增 12 条（中文技术文本 5 条、编辑范围三档 3 条、英文破折号按篇幅 1 条、声口可选项 1 条、就地改文件 1 条、执行强度上限 1 条） |
| `skills/maybe-humanizer/SOURCES.md` | 由 `upstream-monitor render --merge maybe-humanizer` 渲染，不手写 |
| `merges/maybe-humanizer/CHANGELOG.md` | 顶部加一节，面向用户写这轮之后的行为变化 |
| `merges/maybe-humanizer/reports/0006-2026-09-07-ten-source-merge.md` | 本报告 |
| `catalog/maybe-humanizer.yaml` | `reason` 改成「10 个来源合并完成，待独立验证后转 active」，`status` 保持 planned |
| `merges/maybe-humanizer/decisions.yaml` | 写正文时回填 conflicts.md 与 optional.md 里 49 条未落地规则的 `local.anchor`；写作后修正另改了 80 条证据 anchor、8 条 relations、4 条 rule_summary（各加一次 revision 与 history）、11 条 rationale。307 条规则的 `decision` 一条都没变 |

试验版的七份 references 里，`conflicts.md` 换了用途（原先混着未采纳与可选项两件事，现在只收未采纳），另外六份整份重写。新增 `measurement.md` 与 `optional.md` 两份。

### 7.2 前五批改的

- `merges/maybe-humanizer/sources.yaml` 与 `sources.lock.json`：59 条来源的登记与快照指纹。
- `merges/maybe-humanizer/snapshots/`：9 个 full-text 来源的原文快照（jzOcb 为 metadata-only，无快照）。
- `merges/maybe-humanizer/decisions.yaml`：307 条规则的裁决。
- `merges/maybe-humanizer/work/units/`：10 份拆规则清单，804 条单元。
- `merges/maybe-humanizer/work/clusters.md`、`work/coverage.md`：聚类与覆盖映射。
- `merges/maybe-humanizer/work/writing-plan.md`：正文写作计划，2928 行。
- `merges/maybe-humanizer/reports/0001` 至 `0005`。
- `tools/upstream-monitor/`：0004 与 0005 期间修过 anchors 定位与 validate 缓存，见 b6d0ebe 与 70fe1fd。

## 8 如何验证

### 8.1 已经跑过的

**全库校验。**

```
upstream-monitor validate --branch full-merge-intake --offline --merge maybe-humanizer
```

结果：`BLOCK 0、HIGH 0、MED 0、LOW 0`。写正文之前这个命令报 BLOCK 178（九份文件各自的小节缺失）与 MED 24（同一规则内多条证据共用 `(path, anchor)`）。BLOCK 由九份 references 写完归零；MED 24 由并行的另一个 agent 改 `work/units/` 归零，见第 11 节。

**SKILL.md 的规则 id。**正文引用 79 个规则 id，脚本比对 decisions.yaml，全部存在，且全部是 adopted 或 adopted-with-modification（不引用 rejected、deferred、duplicate 的 id）。references 表九行齐全，正文 140 行，未超 200 行上限。

**SOURCES.md 与 decisions.yaml 的一致性。**由 `upstream-monitor render` 从两份源文件渲染，数字不手写。渲染于 2026-09-06T22:57:45Z，核对结果：

- 主表 10 行，与 `sources.yaml` 里 `status: active` 的 10 条一致。
- 「已登记、尚未合并」49 行，与 `status: candidate` 的 49 条一致，10 + 49 = 59。
- 末尾「生成信息」写 307 条规则、59 个来源，与 decisions.yaml 和 sources.yaml 一致。
- 每个来源下按 decision 分组的规则清单由脚本从 decisions.yaml 算，「支持的规则数」与「落地的规则数」两列同源。

注意文件里「渲染时间」那一行取的是 `sources.lock.json` 的最后一次 `check` 时刻（2026-09-06T14:51:10Z），不是本次 render 的时刻。

### 8.2 evals：写了判据，本轮未跑

`skills/maybe-humanizer/evals/evals.json` 现在 26 条，JSON 合法，id 1 至 26 连续。按三类样本分：

| 类别 | 样本 id | 条数 |
|---|---|---|
| 第一类 真人原文，不该被改 | 1、2、3、4、26 | 5 |
| 第二类 事实不漂移 | 5、6、7、8、14、15、16、17、18、19、21、22、23 | 13 |
| 第三类 套话应被清理 | 9、10、11、12 | 4 |
| 模式与授权档位 | 13（审稿）、20、24、25 | 4 |

本轮新增的 12 条覆盖这次进来的规则：

- 中文技术文本五条（15 接口字段、16 命令、17 日志与报错原文、18 责任主体、19 条件关系七项），对应 shuorenhua 带进来的 ZH-PROT-003、ALL-PROT-032、ALL-PROT-022、ALL-PROT-033、ALL-PROT-023、ALL-PROT-024、ALL-PROT-028。
- 编辑范围三档各一条（20 structural、21 bounded、22 in-place）。21 用一段 1010 字、28 句的中文公开写作长文，判据是 ZH-PROC-004 的默认 bounded 与 ALL-M-019 的逐条核对；22 的判据写明字数与句数的回退检查（低于原文 85%，或句数变化超过约 10%）。
- 23 是一段约 1498 词的英文长文，含 3 处计入频率的破折号（2 处 em dash 加 1 处 `--`）与 4 处列表里豁免的 em dash，判据按 EN-P-026 的每千词一处折算。
- 24 是用户明确点名 casual 的样本，判据含「原文没有第一人称就不加第一人称」这条硬边界。
- 25 给的是文件路径，判据是 ALL-PROC-052 的五步动作与不贴回全文。
- 26 是一段全按最严执行就会被改出一致性的真人技术记录，判据逐条对 ALL-PROC-056 的三条上限。

**这 26 条本轮一条都没跑。**判据是写给独立验证 agent 的，实测结果由那一步填回本节。第二类样本有失败时，逐条列出失败样本与失败点。可以复跑的命令：

```
# 全库校验
upstream-monitor validate --branch full-merge-intake --offline --merge maybe-humanizer

# SKILL.md 引用的规则 id 是否都在 decisions.yaml 里
python - <<'PY'
import re, yaml
known={r['id'] for r in yaml.safe_load(open('merges/maybe-humanizer/decisions.yaml'))['rules']}
txt=open('skills/maybe-humanizer/SKILL.md').read()
ids=sorted(set(re.findall(r'\b(?:ALL|ZH|EN)-(?:PROT|PROC|P|M|G|S)-\d{3}\b', txt)))
print(len(ids), [i for i in ids if i not in known])
PY

# evals 的 JSON 合法性与条数
python -c "import json;d=json.load(open('skills/maybe-humanizer/evals/evals.json'));print(len(d['evals']))"

# SOURCES.md 重新渲染，与提交里的版本比对
upstream-monitor render --merge maybe-humanizer
git diff --stat skills/maybe-humanizer/SOURCES.md
```

### 8.3 独立验证要看的三件事

按 ALL-M-004，自己写完自己判不算验收。交给独立验证的三件事：

1. 26 条 evals 逐条跑，第二类零失败是转 active 的条件。
2. 九份 references 的正文与 decisions.yaml 的 `rule_summary` 是否一致：写正文的 agent 不得改 rule_summary，正文与它冲突时以 decisions.yaml 为准。
3. SKILL.md 的五段顺序与写作计划第 4 节是否逐条对得上，尤其 ALL-PROC-023 的五档原文照写、ALL-PROC-056 与 ALL-PROC-010 相邻、自查六步顺序。

## 9 如何回滚

回到 `main` 上的四来源试验版（05ba15b 引入，随 PR #2 并进 699efee）。这是分支级回滚，不是逐条改判：本分支 `full-merge-intake` 从头到尾没有合进 `main`。

**如果本分支还没合并（当前状态）：**

1. 不要合 `full-merge-intake`。`main` 上的 `skills/maybe-humanizer/` 仍是四来源试验版（SKILL.md 97 行、七份 references、144 条规则的 decisions.yaml），无需任何操作。
2. 需要保留分支上的裁决记录时，把 `merges/maybe-humanizer/` 单独 cherry-pick 过去，不带 `skills/maybe-humanizer/`；这样 catalog 的 `status` 仍是 planned，skill 行为不变。
3. 分支要丢掉时：`git worktree remove` 这个 worktree，再 `git branch -D full-merge-intake`。快照文件在 `merges/maybe-humanizer/snapshots/` 里，删掉之后 6 个来源的 `raw_sha256` 就没有对照物了，重跑 `upstream-monitor snapshot` 可以重建。

**如果本分支已经合并进 `main`，要退回试验版：**

1. `git revert -m 1 <合并提交>` 撤掉合并。这会一次性退回九份 references、SKILL.md、evals、SOURCES.md、CHANGELOG、catalog 和 decisions.yaml。
2. decisions.yaml 退回之后是 144 条规则的版本，全部 `decision_revision` 回到试验版的值。本轮之后新加的 163 条规则不存在，无需逐条改判。
3. `skills/maybe-humanizer/references/` 下要删掉 `measurement.md` 与 `optional.md` 两个新文件（revert 会做，确认一次）；`conflicts.md` 退回混装「未采纳加可选项」的旧版。
4. `catalog/maybe-humanizer.yaml` 的 `reason` 退回「四来源试验版……」那一段，`status` 本来就是 planned，不变。
5. `merges/maybe-humanizer/reports/0002` 至 `0006` 五份报告随 revert 一起消失。要保留记录的，先把这五份复制出去再 revert。
6. revert 之后跑一次 `upstream-monitor validate --branch main --offline --merge maybe-humanizer` 确认 BLOCK 0。试验版当时的 validate 是干净的。

**只想退回某一批**（例如保留前三批、退掉英文批二的 57 条）：不建议按提交回滚，因为 0004 的 69 条追加证据和 0005 的 41 条 relations 交叉在其他批的规则上。正确做法是逐条把那 57 条的 `decision` 改成 `retired`、`decision_revision` 加一、history 追加一条，再删掉九份 references 里对应的 57 个小节，最后重跑 validate。这 57 条的 id 列在 CHANGELOG 的「2026-09-07（英文批二）」一节。

## 10 未解决问题

五份报告和五个写作 agent 留下的问题，按主题归并。标 **[需用户拍板]** 的是缺一个决定就推不下去的。

### 10.1 这个 merge 实例算不算做完

**[需用户拍板] 40 条 representative 来源从来没有拆过规则单元。**`sources.yaml` 有 59 条来源，10 条贡献了证据，9 条在入围时就定了不拆，剩下 40 条的 `selection_status` 是 representative，按 skill-merge 的 process.md 步骤 1 它们应当进入第 2 步。三种处理各有代价：（a）认为做完了，把这 40 条改成 low-priority 并逐条写 reason；（b）认为没做完，正文照写但 catalog 保持 planned，等后续批次补上，代价是正文要重写多次；（c）按现在的 10 个来源出第一版，40 条走 sync 增量吸收，代价是 sync 的比对基线是一份还没有 evals 验证过的正文。本轮按 (c) 的形态交付：正文写完、catalog 保持 planned、reason 写明待独立验证。用户选 (a) 或 (b) 时，本轮的正文都不需要推倒。出处：0005 §10 第 2 条。

### 10.2 六条规则的状态未定

**[需用户拍板] 跨会话的个人风格学习功能做不做。**ALL-PROC-033（deferred）加依附它的 ALL-M-008、ALL-M-009、ALL-M-011（都 deferred）。做了会改变 skill 的形态：需要落盘、需要用户维护一份规则文件、需要 skill 改写自己的规则文件。最后一点本仓库是否接受也要定。出处：0001 §10.3 第 1 条。

**[需用户拍板] 两条中文模式的验证。**ZH-P-010（unverified）需要在中文真人原文样本上验证不误伤，或找到第二个独立来源。ZH-P-011 已在中文批改判 adopted-with-modification，不再是待验证。出处：0001 §10.2。

**EN-M-002（deferred）**：证据不足以判断，等后续来源。出处：0004。

这 6 条（5 deferred 加 1 unverified）的 `local.path` 指向 conflicts.md、`local.anchor` 为 null，正文里只在 conflicts.md 末尾的表里出现一行，不建小节。**[需用户拍板] 要不要给它们一份单独的文件。**出处：0005 §10 第 3 条。

### 10.3 字段口径与文档不一致

**[需用户拍板] `decision_revision` 与 `decision_origin` 的三处口径，四批都提过，仍未定，且已经有一处不一致。**（一）只追加证据时 `decision_revision` 加不加一：process.md 的 sync 步骤 3 说加，`decisions.schema.json` 说只在改 decision 时加；155 条追加证据的规则按 schema 处理（没加）。（二）改了 `rule_summary` 但 decision 值不变时怎么办：两份文档都没写，0004 与 0005 都加了 revision 并追加 history。（三）改了结论的 human-approved 规则要不要把 `decision_origin` 退回 model-proposed：0005 按 process.md 字面执行退回了 5 条，0004 改 EN-S-001 时没退回。**EN-S-001 现在是一条 human-approved 但结论由模型改过的规则，与那 5 条不一致，用户定口径之后要补齐。**出处：0002 §10、0003 §10、0004 §10 第 8 条、0005 §10 第 5 条。

**[需用户拍板] `supersedes` 的方向，任务说明与 schema 相反。**任务说明写「被并入的一条记 supersedes」，`decisions.schema.json` 写「supersedes 本规则取代 rule_id 那条」。本轮按 schema 执行，理由是 skill-merge 的 SKILL.md 明写以 schemas 为准，且仓库现有 3 条 supersedes 全部是「留下的那条指向被取代的那条」。本轮没有合并任何规则，分歧暂无实际后果，下一次有合并时必须先定。出处：0005 §10 第 1 条。

**[需用户拍板] `independent_sources` 的工具口径与实质口径不一致，第三次出现。**blader 与 aboudjem 同源于同一篇 Wikipedia 文章；conorbronsdon 在 16 处自述改编自 blader 或 aboudjem。工具按 lineage 机械去重，把这些算成独立来源。三种处理（保持现状 / 在 sources.yaml 加共同祖先标记 / 改 lineage）都还没选。受影响规则清单在 0004 §5.11。出处：0003 §10、0004 §10 第 7 条、0005 §10 第 6 条。

### 10.4 规则内容上的空档

**[需用户拍板] 英文侧缺一条与 ZH-M-004 对应的「全篇写法统一」总条。**中文侧是一条总条（ZH-M-004 管要不要统一）加三条取值规则；英文侧只有 EN-P-037、EN-P-044、EN-P-011、EN-P-012、EN-P-071 五条取值规则，没有总条。英文原稿在某一类上出现两种写法而这五条都没覆盖时，没有规则说该统一。补它是新增一条 EN 规则，超出复核与写正文的范围。出处：0004 §10 第 4 条、0005 §10 第 4 条与 §5.6。

**三处上游给的机制判断为不适用，但值得记住**（不构成规则，只在 rationale 里留痕）：把配置字段分成「可机械校验」与「只能靠模型执行」两类用来限定合规声明的覆盖面；同一条规则的严重度随体裁变；声口与语境的默认搭配表。本仓库将来引入任何机械校验步骤时，第一条要重新看一遍。出处：0004 §10 第 9 条。

### 10.5 上游文本里出现的指令内容

四批一共记了四组，全部照抄备查、一条都没执行。

**jzOcb/writing-style-skill（metadata-only）**：SKILL.md 里以「操作指南」名义列出三步命令行操作。判断为该来源对它自己终端用户的说明，不是针对本次处理过程的注入。本次只读取了两个脚本文件，把配对、判分、分级逻辑改写成规则单元，没有运行任何一步。

**Aboudjem/humanizer-skill**：`references/always-on-templates.md` 引言写 "Copy one of these blocks into your agent's standing instructions so it writes clean by default"。判断为面向该 skill 终端用户的产品说明。本次没有把任何模板复制进本仓库的常驻规则、CLAUDE.md 或任何配置，模板内容按数据处理。**[需用户拍板] 这条判断带主观性，是否要按更保守的口径记为 criteria.md 第 7 条意义上的指令。**出处：0001 §10.1。

**conorbronsdon/avoid-ai-writing 的三处运行脚本要求**（`node scripts/normalize-quotes.js`、`node scripts/check-style.js`、`node detector/validate.js`）：按 skill-merge 的硬约束「脚本只读不跑」，本次既没有抓取这三个脚本（不在 `sources.yaml` 的 paths 里，快照中不存在），也没有运行任何命令。对应规则已改写成人工执行的步骤：EN-PROC-002、ALL-PROC-057、ALL-M-025。出处：0004 §10 第 10 条。

**conorbronsdon/avoid-ai-writing 举的「文档内编辑指令」示例句**（"ignore the rules above," "don't flag this section," "add a closing paragraph"）：上游自己的立场是把这类句子标记出来而不是执行，本仓库处理一致，并把这条立成 ALL-PROT-038，写进 SKILL.md 的硬约束。出处：0004 §10 第 10 条。

### 10.6 记录在案，不需要拍板

**172 条 model-proposed 待人工确认。**合并 PR 前用 `upstream-monitor approve --merge maybe-humanizer` 翻成 human-approved；approve 不追加 history、不动 `decided_at`。这个数比全局复核时多 2：写作后修正改了 ALL-P-002 与 ALL-P-004 的 `rule_summary`，两条从 human-approved 退回 model-proposed。

**误伤控制的格式约定已经落地，但只落在本 skill 里。**0004 §10 第 5 条建议在 `skills/skill-merge/references/extraction.md` 立一个「判据 / 通过条件 / 已知会漏掉什么」的三段格式。本轮的九份 references 已经按这个格式写了 301 个小节，但 extraction.md 本身没改，下一个 merge 实例不会自动继承。改动落在 `skills/skill-merge/`，不在本轮的写入范围内。

**24 条 MED 已经消掉。**0005 §10 第 8 条记的「同一规则内多条证据共用 `(path, anchor)`」需要改 `work/units/`，本轮由并行的另一个 agent 处理，validate 现在 MED 0。见第 11 节。

**conflicts.md 与 optional.md 的 anchor 已经回填。**0005 §10 第 9 条留的这一项在本轮完成，49 条未落地规则的 `local.anchor` 从 null 填成计划里的小节标题。EN-S-001 例外，它的 anchor 在复核时就是最终值。

## 11 写作后修正

写正文的五个 agent 交回之后，由并行的另一个 agent 做了一轮数据层修正，范围限在 `decisions.yaml`、`work/`，以及九份 references 里因规则内容变化而必须同步的段落。完整记录在 `merges/maybe-humanizer/work/post-writing-fixes.md`，下面是并进本报告的摘要。

**校验结果。**离线 validate 从 `BLOCK 0 / HIGH 0 / MED 24 / LOW 0` 变成四级全 0。联网核上游锚点那一次从 `MED 32 / LOW 247` 变成 `MED 0 / LOW 250`：32 条 MED 是 24 条共用 `(path, anchor)` 加 8 条弱定位有歧义，修完 ambiguous 为 0；LOW 净增 3，LOW 是弱定位提示不是错误。

**改了 80 条证据的 anchor**（`decisions.yaml`、`work/units/`、`work/coverage.md` 三处同步）。72 条来自 24 组共用锚点，8 条来自有歧义的弱定位。写法按 extraction.md 的 `<小节标题> / <该行行首原文>`。metadata-only 来源 jzOcb 的 7 条特殊处理：原来的 anchor 是描述性文字，改成函数定义行的行首原文（`def record_final(args):` 这类），函数定义行是定位信息不是正文内容，符合 metadata-only 的口径；核对时按 `last_seen_commit` 临时拉取原文、核完丢弃，仓库里仍然没有它的原文。

**补了 4 对双向 `pairs-with`**（8 条有向边），只补 relations、不改 decision 或 rule_summary，因此 `decision_revision`、`history`、`decision_origin` 都不动：EN-P-014↔EN-P-015（represents / stands as 的分界）、EN-P-004↔EN-P-049（it's worth noting 同时在两条词表里，同一处只计一次）、ALL-PROC-044↔ALL-PROT-014（整句空话的标注落在改动说明的单独一节，不插正文）、ALL-M-003↔ALL-M-024（中文八十字门槛是本仓库新补、未核，说明里要带同样的保留）。relations 从 516 条增到 524 条。

**改了 4 条规则的 `rule_summary`**，各自 `decision_revision` 加一、`history` 追加一条，`decision` 不变：

| 规则 | rev | origin | 改了什么 |
|---|---|---|---|
| ALL-P-002 | 1→2 | human-approved→model-proposed | 并入三项可数口径：一个大节至多一处加粗、社交帖行尾 emoji 例外、项目符号的正面清单 |
| ALL-P-004 | 1→2 | human-approved→model-proposed | 并入参考类语域碎句例外与三类假施事的通过条件 |
| ZH-P-014 | 1→2 | model-proposed（不变） | 补一句「删的是铺垫层，不是限定命题成立范围的保留语」 |
| ZH-P-025 | 1→2 | model-proposed（不变） | 取值改写成显式四级顺序 |

ALL-P-002 的正文改动最大：「社交帖行尾 emoji 例外」和「一个大节至多一处加粗」原先记在「已知会漏掉什么」里（写的是本条没有采纳），现在两项都并进规则，从那一段移到「判据」和「通过条件」。

**改了 11 条规则的 rationale**（不动 revision、history、origin），全部是过期指向：7 条把 `references/conflicts.md 可选项一节` 改成 `references/optional.md`（拆文件之后旧路径不成立），另 4 条（EN-S-005、ALL-M-014、ZH-P-014、ALL-M-006）把「留给全局复核」这类已经完成的话改成陈述现状。

**跨文件核对三项，全部零未解决项**：九份 references 正文里出现的 307 个规则 id 全部存在于 decisions.yaml；56 条非采用规则被正文引用时全部在 conflicts.md 或 optional.md 有落点（deferred 与 unverified 在表里有行也算）；454 条有向边（227 个无序对）的两端小节互相点名，修前缺 8 处、逐条补一句后缺 0。核对脚本只读，没有进仓库。

**这一轮留下的五条问题**已按主题并进第 10 节的口径，其中三条是新的，记在这里：

1. 6 条新增 LOW 消不掉。上游把两条以上规则写在同一行或同一段里时，anchor 没有第二个行首可用，只能落到行内子串。要消掉只有合并规则单元或接受子串定位两条路，本轮都没做。
2. op7418 的 `### 如何增加语调` 少抄了一个全角冒号，5 处 anchor 靠 `heading-contains` 兜住，判成 `weak-heading`。本轮只动了其中 2 处的子锚点，没补冒号（补了会让同一来源的 5 处 anchor 分成两种写法）。
3. jzOcb 的 7 条 anchor 精度降级：改成函数定义行之后，`def extract_improvements(args):` 覆盖 88 行、`def record_final(args):` 覆盖 60 行，接近 extraction.md「不超过一屏」的上限。再细就要引上游代码或 prompt 正文，metadata-only 不允许。

另两条与第 10 节已有的条目重合：ALL-M-003 的 revision 该不该加，属于 §10.3 那个未定的口径问题；ALL-P-002 与 ALL-P-004 退回 model-proposed 之后要重新 approve，属于 §10.6。

## 附 A 改动文件

本报告作者（收尾这一步）写的：

- `skills/maybe-humanizer/SKILL.md`（整份重写，140 行）
- `skills/maybe-humanizer/evals/evals.json`（14 条扩到 26 条）
- `skills/maybe-humanizer/SOURCES.md`（`upstream-monitor render --merge maybe-humanizer` 渲染）。**本轮的渲染在 2026-09-06T22:57:45Z 执行**，排在本报告作者其余改动全部写完之后。文件末尾「生成信息」里的「渲染时间」写的是 2026-09-06T14:51:10Z，那是 `sources.lock.json` 里最后一次 `check` 的时刻，不是这次渲染的时刻；并行改 decisions.yaml 的那个 agent 在此之后还改过 decisions.yaml（anchor、relations、rule_summary、rationale），因此在 2026-09-06T23:01:30Z 重跑了一次 render，输出与 22:57:45Z 那次逐字节一致：那一轮修正没有动任何规则的 `decision`，而 SOURCES.md 只渲染 decision 分组与计数。
- `merges/maybe-humanizer/reports/0006-2026-09-07-ten-source-merge.md`（本报告）
- `merges/maybe-humanizer/CHANGELOG.md`（顶部加一节）
- `catalog/maybe-humanizer.yaml`（`reason` 改写，`status` 保持 planned）

没有动的：`merges/maybe-humanizer/decisions.yaml`、`merges/maybe-humanizer/work/`、`skills/maybe-humanizer/references/`。这三处由写正文的五个 agent 和做写作后修正的那个 agent 负责，本报告作者一个字没改。

没有执行的：`git commit`、`git push`。

## 附 B 未解决问题

按第 10 节归并。需要用户拍板的九条：

1. 40 条 representative 来源拆不拆，决定这个 merge 实例算不算做完（§10.1）
2. 跨会话个人风格学习功能做不做，连带 4 条 deferred 规则（§10.2）
3. ZH-P-010 的验证路径（§10.2）
4. 6 条 deferred/unverified 要不要单独一份文件（§10.2）
5. `decision_revision` 与 `decision_origin` 的三处口径，含 EN-S-001 的不一致（§10.3）
6. `supersedes` 的方向（§10.3）
7. `independent_sources` 的实质口径（§10.3）
8. 英文侧「全篇写法统一」总条补不补（§10.4）
9. Aboudjem 那段引言的指令口径（§10.5）

不需要拍板、但要有人做的三条：172 条 model-proposed 待 approve（含写作后修正退回的 ALL-P-002、ALL-P-004）；`skills/skill-merge/references/extraction.md` 的三段格式约定未写进去；26 条 evals 未跑。

## 附 C 后续建议（只写，不动手）

1. **先跑 evals 再考虑转 active。**catalog 的 `reason` 已经写明这一点。第二类样本（事实不漂移）零失败是硬条件，13 条里任何一条失败都说明保真规则在正文里没落到位。跑之前不要合进 `main`。
2. **evals 还缺三类样本。**26 条里没有：繁体中文的拒绝样本（ALL-G-001 划在适用范围外）、虚构文本的样本（ALL-G-003 要求先说明模式表不适用再问）、凭证扫描的样本（ALL-PROT-011 是硬约束，输入里带 API key 时应立刻停）。这三条都是「该停手时停不停手」的检验，比模式清理的样本更值得补。
3. **`skills/skill-merge/references/extraction.md` 补三段格式约定。**本轮的 301 个小节已经按「判据 / 通过条件 / 已知会漏掉什么」写了，这个格式是英文批二那份上游最值得学的地方，但它现在只存在于本 skill 的正文里。写进 extraction.md 之后下一个 merge 实例才会继承。
4. **`anchors.locate` 的弱定位还在。**0004 §10 第 6 条记的代码问题（非小节标题的 anchor 不检查子锚点、116 条 ok-substring 的弱定位）本轮由改 `work/units/` 绕过去了，`tools/upstream-monitor/` 里那一支代码没改。下一批来源进来时同样的问题会重新出现。
5. **SOURCES.md 的 49 条「已登记、尚未合并」需要一个复查节奏。**它们现在 `status: candidate`，`upstream-monitor check` 不会为它们拉 commit。决定按 §10.1 的哪一条走之后，把复查节奏写进 `sources.yaml` 的 reason 或仓库的 README。
6. **考虑给 SKILL.md 加一份最小样例。**现在 SKILL.md 只写流程，一条实际的输入到输出没有。en-zh-translation 用 `examples/rule-paragraph.md` 放了一份完整对照，maybe-humanizer 可以照做，放一段原文加改写稿加改动说明的完整样例。这不属于本轮范围，写在这里备查。
