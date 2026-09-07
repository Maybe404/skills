# 写完九份 references 之后的数据层修复

五个写作 agent 在写 references 时报了一批数据层问题：证据锚点共用、relations 缺项、rule_summary 与正文口径不一致、rationale 过期。这份文件记这一轮修了什么，供报告 0006 合并。

范围只在 `merges/maybe-humanizer/decisions.yaml`、`merges/maybe-humanizer/work/`，以及九份 references 里因规则内容变化而必须同步的段落。`skills/maybe-humanizer/SKILL.md`、`evals/`、`SOURCES.md`、`reports/0006`、`CHANGELOG.md` 由另一路并行处理，本轮没有碰。

## 一 校验结果

| 命令 | 修复前 | 修复后 |
|---|---|---|
| `validate --offline --merge maybe-humanizer` | BLOCK 0 / HIGH 0 / MED 24 / LOW 0 | BLOCK 0 / HIGH 0 / MED 0 / LOW 0 |
| `validate --merge maybe-humanizer`（联网核上游锚点） | BLOCK 0 / HIGH 0 / MED 32 / LOW 247 | BLOCK 0 / HIGH 0 / MED 0 / LOW 250 |

联网那一次的 32 条 MED = 24 条共用锚点 + 8 条弱定位有歧义（ambiguous）。**修复后 ambiguous 为 0。**

LOW 从 247 变成 250，净增 3。LOW 是弱定位提示（`ok-substring`、`weak-heading`），不是错误。本轮新增的 6 条 LOW 都出于同一个原因：同一条上游正文行或同一个段落里拆出了两条以上规则，anchor 没有各自的行首可用，只能用行内子串区分。逐条见第二节末尾。

## 二 证据锚点（A）

改了 80 条证据的 anchor，`decisions.yaml`、`work/units/<source_id>.md`、`work/coverage.md` 三处同步，每处各 80 行。其中 72 条来自 24 组共用 (path, anchor) 的 MED，8 条来自弱定位有歧义的 MED。

写法按 `skills/skill-merge/references/extraction.md`：`<小节标题> / <该行行首原文>`，子锚点取上游那一行经 markdown 清洗（去列表符号、序号、反引号、强调标记）之后的行首文本，不写描述性文字。子锚点里不含 ` / `，那个串是 anchor 自己的分隔符。

按规则和来源分组：

| 规则 | 来源 | 改了几条 |
|---|---|---|
| ALL-M-009 | writing-style-skill | 1 |
| ALL-M-010 | writing-style-skill | 1 |
| ALL-M-011 | writing-style-skill | 1 |
| ALL-M-012 | writing-style-skill | 1 |
| ALL-M-013 | writing-style-skill | 1 |
| ALL-M-015 | writing-style-skill | 1 |
| ALL-M-016 | writing-style-skill | 1 |
| ALL-M-017 | op7418-humanizer-zh | 2 |
| ALL-M-018 | shuorenhua | 2 |
| ALL-M-019 | shuorenhua | 3 |
| ALL-PROC-007 | shuorenhua | 3 |
| ALL-PROC-014 | qu-ai-wei | 2 |
| ALL-PROC-024 | qu-ai-wei | 1 |
| ALL-PROC-036 | ai-zixun-humanizer-zh | 7 |
| ALL-PROC-040 | shuorenhua | 6 |
| ALL-PROC-042 | shuorenhua | 4 |
| ALL-PROC-043 | shuorenhua | 4 |
| ALL-PROC-045 | shuorenhua | 3 |
| ALL-PROT-017 | ai-zixun-humanizer-zh | 2 |
| ALL-PROT-017 | op7418-humanizer-zh | 2 |
| ALL-PROT-019 | qu-ai-wei | 2 |
| ALL-PROT-031 | shuorenhua | 2 |
| ALL-PROT-032 | shuorenhua | 5 |
| ZH-G-003 | shuorenhua | 7 |
| ZH-M-006 | shuorenhua | 2 |
| ZH-P-001 | shuorenhua | 2 |
| ZH-P-011 | ai-zixun-humanizer-zh | 2 |
| ZH-P-025 | ai-zixun-humanizer-zh | 2 |
| ZH-PROC-003 | ai-zixun-humanizer-zh | 2 |
| ZH-S-003 | ai-zixun-humanizer-zh | 3 |
| ZH-S-004 | ai-zixun-humanizer-zh | 3 |

metadata-only 来源（upstream-jzocb-writing-style-skill）的 7 条另说。它的原文不进仓库，本轮按 `sources.lock.json` 的 `last_seen_commit`（`d94826e1cd48f5403b82a5a909efdfab96221259`）用 `gh api` 临时拉到 scratchpad 核对，核完丢弃。原来的 anchor 写成 `observe.py / record_final 里对 original 与 final 内容是否一致的判断` 这类描述性文字，`observe.py` 在文件里作为子串出现四次、又不在行首，所以判成有歧义；描述性文字本身按 extraction.md 也不该进 anchor。改成函数定义那一行的行首原文：

| 规则 | 新 anchor |
|---|---|
| ALL-M-009 | `def record_final(args):` |
| ALL-M-015 | `def record_final(args):` |
| ALL-M-010 | `def compute_hash(content):` |
| ALL-M-016 | `def show_stats(args):` |
| ALL-M-011 / ALL-M-012 / ALL-M-013 | `def extract_improvements(args):` |

函数定义行与小节标题同性质，是定位信息不是正文内容，不含上游的规则表述，符合 metadata-only 的口径。同一个 anchor 出现在多条规则上不触发共用锚点检查——那条检查只看同一条规则内部。

剩下的 1 条有歧义是 ALL-PROC-024 的 `至多两条具体结构`，它在 qu-ai-wei 的门检示例块里出现两次，改成那一行的行首原文 `【门检】判断：AI 高频写作症状`。

新增的 6 条 LOW（弱定位为子串）逐条如下，都是同一条上游正文行或同一段里拆出了两条以上规则，没有第二个行首可用：

| 规则 | anchor | 原因 |
|---|---|---|
| ALL-PROT-019 | `### 1. 冻结不可丢失内容 / 再建立论证图` | 信息账本与论证图写在上游同一句里 |
| ALL-PROT-031 | `## 5. No-touch and keep rules / 不要自行假定存在术语表` | 与 ALL-PROT-031 的另一条证据同段 |
| ALL-PROT-032 | `数值、正式指标名、字段名、命令和引用原文按字面保护 / 命令和引用原文` | 五类保护对象写在同一行 |
| ALL-PROT-032 | `引用原文、命令、接口名、参数名、字段名、配置项、日志、报错 / 接口名、参数名、字段名、配置项` | 同上 |
| ALL-PROT-032 | `引用原文、命令、接口名、参数名、字段名、配置项、日志、报错 / 日志、报错` | 同上 |
| ALL-M-018 | `### Annotation mode / 不替作者设计怎么去补` | 压缩试验的判据与标注要求写在同一个列表项里 |

## 三 relations 补齐（B）

补了 4 对、8 条有向 relation，全部是 `pairs-with`，双向记。只补 relations 不改 decision 或 rule_summary，按 `process.md` 的口径，`decision_revision`、`history`、`decision_origin` 都不动。

| 一端 | 另一端 | note 写的分界 |
|---|---|---|
| EN-P-014 | EN-P-015 | 两条在 represents、stands as 上重叠，同一处只判一条：回避系动词、能直接换回 is / are 的归 EN-P-015；给一件普通事实追加时代意义的归 EN-P-014 |
| EN-P-004 | EN-P-049 | it's worth noting 同时在两条词表里，同一处只计一次命中：作为不承载信息的短语删掉走 EN-P-004；作为陈述事实之前的预先辩解删掉走 EN-P-049 |
| ALL-PROC-044 | ALL-PROT-014 | ALL-PROC-044 的整句空话标注按 ALL-PROT-014 的口径落地：写进改动说明的单独一节，不插进正文 |
| ALL-M-003 | ALL-M-024 | ALL-M-003 的中文八十字门槛是本仓库新补、未核的等价门槛，按 ALL-M-024 说明里要带同样的保留 |

正文点名情况：EN-P-014 与 EN-P-015 的小节原本已经互相点名，不用改；其余三对补了单侧的一句——`patterns-en.md` 的 EN-P-004 小节补点 EN-P-049，`process.md` 的 ALL-PROC-044 小节补点 ALL-PROT-014，`protection.md` 的 ALL-PROT-014 小节补点 ALL-PROC-044，`measurement.md` 的 ALL-M-003 与 ALL-M-024 小节各补一句。

## 四 改了 rule_summary 的规则（C）

四条。每条 `decision_revision` 加一、`history` 追加一条写明改了什么、`decision_origin` 退回 `model-proposed`。`decision` 本身没变，所以 `decided_at` 不动，history 的 `at` 记 `2026-09-07T22:00:00Z`。

| 规则 | revision | origin | 改了什么 |
|---|---|---|---|
| ALL-P-002 | 1 → 2 | human-approved → model-proposed | 并入三项可数口径：一个大节至多留一处加粗短语（并给出改法：重构句子让重点出现在句首）、社交帖行尾少量 emoji 的例外、项目符号的正面清单 |
| ALL-P-004 | 1 → 2 | human-approved → model-proposed | 并入参考类语域碎句例外，以及三类假施事的通过条件（惯例性拟人、系统的字面行为、集体简称） |
| ZH-P-014 | 1 → 2 | model-proposed（不变） | 补一句「删的是铺垫层，不是限定命题成立范围的保留语（后者归 ALL-PROT-004）」 |
| ZH-P-025 | 1 → 2 | model-proposed（不变） | rule_summary 改写成显式四级顺序：用户本轮指定 > 项目声明 > 原文已一致则沿用 > 默认全角双引号 |

正文同步（grep 核过新增措辞在 `decisions.yaml` 和 references 两边都有）：

| 措辞 | references | decisions.yaml |
|---|---|---|
| 一个大节至多留一处加粗 | patterns-common.md | ✓ |
| 社交帖行尾 | patterns-common.md | ✓ |
| 功能对照、分步操作、接口参数 | patterns-common.md | ✓ |
| 三类假施事不算命中 | patterns-common.md | ✓ |
| 系统的字面行为 | patterns-common.md | ✓ |
| README 的功能清单、变更日志条目、参数文档、commit 标题 | patterns-common.md | ✓ |
| 不是限定命题成立范围的保留语 / ALL-PROT-004 | patterns-zh.md | ✓ |
| 取值按四级顺序 | patterns-zh.md | ✓ |
| 中文八十字门槛 | measurement.md | ✓ |

ALL-P-002 的正文改动最大：「社交帖行尾 emoji 例外」和「一个大节至多留一处加粗」原来记在「已知会漏掉什么」里，写的是本条**没有**采纳；现在两项都并进了规则，所以从「已知会漏掉什么」移到「判据」和「通过条件」，那一段改成写新的边界（「一个大节」按标题层级数、行尾与句中的分界判不了）。

**ALL-M-003 没有加 revision。**任务清单把它列在这一组里，但它这次的改动只有 rationale 和 relations，rule_summary 和 decision 都没动。按 `skills/skill-merge/references/process.md` 步骤 3 第 4 条：「只追加证据、补 relations 或改 rationale 的，revision、history、decision_origin 都不动。」照那一条办，rationale 里注明中文八十字门槛是本仓库新补、未核，并按 ALL-M-024 的口径写明未经本仓库验证；同时把它加进 ALL-M-024 的适用范围（rationale 那一句和新增的 relations note 各一处），`measurement.md` 的两个小节同步。

## 五 rationale 过期修正（D）

只改 rationale，revision、history、decision_origin 都不动。

| 规则 | 改了什么 |
|---|---|
| EN-S-005 | 「这四条可以补进 EN-P-003 的词表，本批不做，留给全局复核」改成已按 ALL-PROC-039 补进 EN-P-003 的代表项（EN-P-003 decision_revision 2） |
| ALL-M-014 | 两个反例按当前值改写：ALL-M-001 现在 independent_sources 为 2、采不采用不由这个数字定；EN-S-001 现在 evidence_count 11、independent_sources 2、decision 为 adopted-with-modification，落成 optional.md 里默认不启用的可选项 |
| ALL-PROT-001 | `references/conflicts.md 可选项一节` → `references/optional.md` |
| ALL-PROT-035 | 同上 |
| EN-S-010 | 同上 |
| EN-P-083 | 同上 |
| EN-S-013 | 同上 |
| ALL-M-006 | 「记 reference-only 写进 conflicts.md」→「记 reference-only，做法写进 references/optional.md」 |
| ZH-P-014 | 「这条边界对中文同样成立，本条正文里还没有写，留给全局复核」已过期（正文早已写，本轮又并进 rule_summary），改成陈述现状 |

任务清单里点名的 ZH-S-001 和 EN-S-012 两条，rationale 里没有出现 `conflicts.md`，也没有「可选项一节」这个说法（ZH-S-001 记 rejected，收尾写的是冲突双记；EN-S-012 记 reference-only，收尾写的是按 ALL-PROC-025 写进项目 style guide）。这两条无处可改，没有动。改到的另外两条（ALL-PROT-001、ALL-M-006）不在原清单里，是同一处过期指向，一并改了。

## 六 跨文件核对（E）

核对脚本三项，全部零未解决项。

| 检查 | 口径 | 结果 |
|---|---|---|
| 1 正文里的规则 id 都存在 | 九份 references 正文里出现的每个 `(ZH\|EN\|ALL)-XXX-000` 都能在 decisions.yaml 找到 | 307 个 id 全部命中，未知 0 |
| 2 非采用规则的引用有落点 | 被正文引用、decision 为 rejected / reference-only / deferred / unverified / duplicate / retired 的规则，目标要在 conflicts.md 或 optional.md 里有小节；deferred 与 unverified 在表里有行也算 | 56 条非采用规则全部有落点，缺 0 |
| 3 关系双向点名 | 每条 conflicts-with 与 pairs-with，两端各自的正文小节里都要出现对方的 id | 454 条有向边（227 个无序对），修完缺 0 |

第 3 项修完前缺 8 处（16 条报告行，一处缺两边各报一次），逐条补了一句，没有重写小节：

| 文件 | 小节 | 补点了谁 |
|---|---|---|
| genres.md | ZH-G-002 | ALL-G-002 |
| optional.md | EN-S-013 | ZH-M-002 |
| process.md | ALL-PROC-014 | ALL-PROC-045、ALL-PROC-051 |
| process.md | ALL-PROC-017 | ALL-PROC-007 |
| process.md | ALL-PROC-042 | ALL-PROC-058 |
| process.md | ALL-PROC-057 | ALL-PROC-008 |
| protection.md | ALL-PROT-025 | ALL-PROT-020 |

另有 4 条报告行是脚本口径的问题，不是数据问题：ALL-M-011 与 EN-M-002 都是 deferred，正文里只有 conflicts.md 末尾表里的一行、没有小节。查过那两行，各自已经点名了对方（ALL-M-011 那行点了 ALL-M-014，EN-M-002 那行点了 ALL-M-024），所以把「表行也算小节」写进脚本口径，不改数据。

脚本在 `scratchpad/crosscheck.py`，只读，没有进仓库。

## 七 改动文件

| 文件 | 改了什么 |
|---|---|
| `merges/maybe-humanizer/decisions.yaml` | 80 条证据 anchor；8 条 relations；4 条 rule_summary + revision + origin + history；11 条 rationale |
| `merges/maybe-humanizer/work/coverage.md` | 80 行的 anchor 列 |
| `merges/maybe-humanizer/work/units/upstream-ai-zixun-humanizer-zh.md` | 21 条单元的 anchor |
| `merges/maybe-humanizer/work/units/upstream-mrgediao-shuorenhua.md` | 43 条单元的 anchor |
| `merges/maybe-humanizer/work/units/upstream-lifelonglazylearner-qu-ai-wei.md` | 5 条单元的 anchor |
| `merges/maybe-humanizer/work/units/upstream-op7418-humanizer-zh.md` | 4 条单元的 anchor |
| `merges/maybe-humanizer/work/units/upstream-jzocb-writing-style-skill.md` | 7 条单元的 anchor |
| `skills/maybe-humanizer/references/patterns-common.md` | ALL-P-002 判据、通过条件、已知会漏掉什么；ALL-P-004 通过条件 |
| `skills/maybe-humanizer/references/patterns-zh.md` | ZH-P-025 判据改成显式四级顺序 |
| `skills/maybe-humanizer/references/patterns-en.md` | EN-P-004 通过条件补点 EN-P-049 |
| `skills/maybe-humanizer/references/process.md` | ALL-PROC-044、ALL-PROC-014、ALL-PROC-017、ALL-PROC-042、ALL-PROC-057 各补一句点名 |
| `skills/maybe-humanizer/references/protection.md` | ALL-PROT-014、ALL-PROT-025 各补一句点名 |
| `skills/maybe-humanizer/references/measurement.md` | ALL-M-003、ALL-M-024 的未核标注与互相点名 |
| `skills/maybe-humanizer/references/genres.md` | ZH-G-002 补点 ALL-G-002 |
| `skills/maybe-humanizer/references/optional.md` | EN-S-013 补点 ZH-M-002 |
| `merges/maybe-humanizer/work/post-writing-fixes.md` | 本文件 |

`conflicts.md` 没有改动。`SKILL.md`、`evals/`、`SOURCES.md`、`reports/0006`、`CHANGELOG.md`、`catalog/` 不在本轮范围内。

## 八 未解决问题

1. **6 条新增 LOW 无法消掉。**上游把两条以上规则写在同一行或同一段里时，anchor 没有第二个行首可用，只能落到行内子串。逐条见第二节末尾的表。要消掉只有两条路：合并那几条规则单元，或者接受子串定位。本轮两条都没做，只记账。
2. **`### 如何增加语调` 仍然是弱定位。**op7418 的上游标题原文带一个全角冒号（`### 如何增加语调：`），decisions.yaml 里 5 处 anchor 都少了这个冒号，靠 `heading-contains` 兜住，判成 `weak-heading`。本轮只动了其中 2 处（ALL-PROT-017 的两条证据）的子锚点，没有补冒号——补了会让同一个来源的 5 处 anchor 分成两种写法。
3. **ALL-M-003 的 revision 没有加。**理由见第四节末尾：它这次没有改 rule_summary，按 process.md 不该加。如果口径应当是「凡是这一组里的规则都加一」，这一条要回头补。
4. **jzocb 的 7 条 anchor 精度降级。**改成函数定义行之后，`def extract_improvements(args):` 覆盖 88 行、`def record_final(args):` 覆盖 60 行，接近 extraction.md「不超过一屏」的上限。再细就要引上游的代码行或 prompt 正文，那是 metadata-only 不允许的，所以停在这一层。
5. **ALL-P-002 与 ALL-P-004 的 origin 退回了 model-proposed。**两条原来是 human-approved，本轮改了 rule_summary，按 process.md 退回。合 PR 前要用 `upstream-monitor approve` 重新确认。同批需要重新确认的还有 ZH-P-014、ZH-P-025（本来就是 model-proposed）。

## 九 后续建议（只写，不动手）

1. 把 op7418 那 5 处 `### 如何增加语调` 一次性补上全角冒号，10 条 `heading-contains` 的 LOW 里有 5 条出自这里。同一次可以扫一遍所有 `weak-heading`，它们多半是同一类标题原文抄漏。
2. 现在 250 条 LOW 里有 106 条是「只作为子串出现，不在行首」，其中很大一部分是同一个原因：anchor 把上游那一行的 markdown 前缀一起抄了进来（`- 优先保信息，再谈风格。`、`5. 保留作者原意`、`**Repeated empty concessions:**`），而 `anchors.py` 的 `strip_md` 会先去掉列表符号、序号、反引号和 `**` 再做行首匹配，于是匹配不上、退回子串。106 条里 42 条带 `**`，另有一批带 `- ` 或序号。把这些前缀从 anchor 里去掉是一次机械替换，能把弱定位的比例压下来一大截。分布上 34 条来自 `upstream-conorbronsdon-avoid-ai-writing`、33 条来自 `upstream-mrgediao-shuorenhua`，其余分散在四个来源。
3. `ALL-PROT-032` 现在有 5 条证据落在上游的同两行上（五类按字面保护的对象各拆一条单元）。按 extraction.md「共用同一条判定逻辑就是一个单元」的判据，这五条更像一个单元。下一次全量合并复核单元粒度时值得一并看 ALL-PROT-031、ALL-M-018，它们是同样的形状。
4. 跨文件核对的三项脚本可以并进 `upstream-monitor validate`：第 1 项和第 3 项是纯结构检查，第 2 项要认「小节」和「表行」两种落点。并进去之后正文与 decisions.yaml 的脱节就不用靠人记着查。
5. `ZH-S-001` 与 `EN-S-012` 的 rationale 里没有写这两条落在哪份 references 里（一条 rejected、一条 reference-only）。其余同类规则都写了落点，这两条缺一句，补上口径才齐。
