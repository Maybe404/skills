# 拆规则清单：upstream-hardikpandya-stop-slop

## 1 来源摘要

- 文件（本仓库快照，四份全部在追踪范围内）：
  - `merges/maybe-humanizer/snapshots/upstream-hardikpandya-stop-slop/SKILL.source.md`（上游 `SKILL.md`，68 行 / 2629 字节）
  - `merges/maybe-humanizer/snapshots/upstream-hardikpandya-stop-slop/references/phrases.md`（128 行 / 2915 字节）
  - `merges/maybe-humanizer/snapshots/upstream-hardikpandya-stop-slop/references/structures.md`（134 行 / 5255 字节）
  - `merges/maybe-humanizer/snapshots/upstream-hardikpandya-stop-slop/references/examples.md`（59 行 / 1686 字节）
- 上游仓库：`hardikpandya/stop-slop`，分支 `main`
- commit（取自 sources.lock.json 的 last_seen_commit）：`8da1f030185bdfe8471220585162991eaeb970e9`
- 许可证：MIT，snapshot_policy 为 full-text，可引原文并标"引自上游"
- sources.yaml 的 tracking_revision：2（首轮拆规则时 paths 只有 `SKILL.md`，三份 references 于 2026-09-06 补进追踪范围，理由记在 sources.yaml 的 baseline_reset_reason）
- 上游自述的定位：frontmatter 的 description 写 "Remove AI writing patterns from prose. Use when drafting, editing, or reviewing text to eliminate predictable AI tells."，正文首句 "Eliminate predictable AI writing patterns from prose."。作者是 Hardik Pandya（frontmatter 的 metadata.author）。
- 四份文件的分工：`SKILL.md` 是索引，八条 Core Rules 每条一句祈使句，十二条交付前的 Quick Checks，一张五维 1-10 分的自评表加一个 35/50 的门槛；`references/phrases.md` 是词表（八个小节的短语和词条清单加一张企业黑话替换表）；`references/structures.md` 是结构清单（十一个小节的模式表，每条给 "Pattern | Problem" 或 "Pattern | Fix" 两列）；`references/examples.md` 是五组 before/after 改写示例，每组附一行 Changes 说明。
- 本轮补拆的范围：SKILL.md 里只给了模式名的单元，由 phrases.md 和 structures.md 补全触发词表、模式表和修法；references 里有、SKILL.md 没提到的规则新增为 U-ssl-025 至 U-ssl-035；examples.md 只用来补正反例，只反推出一条单元（U-ssl-026）。
- 总单元数：35（U-ssl-001 至 U-ssl-035）
- 按 category 计数：
  - pattern：21
  - style-opinion：11
  - process：1
  - measurement：2
  - protection：0
  - genre：0
- 按 language 计数：
  - en：32
  - both：3（U-ssl-022、U-ssl-023、U-ssl-024，判定逻辑不依赖具体语言）
  - zh：0

**本来源一条 protection 规则都没有。**补进三份 references 之后这个结论不变：全文没有任何"不得编造事实""保留引语和代码""保留原文数字"一类的约束，也没有"原文本来就好就不要改"的例外。这一点在归并时要单独考虑：它的删改主张（尤其 U-ssl-003 删所有副词、U-ssl-010 禁所有被动、U-ssl-017 禁所有破折号、U-ssl-026 删所有保留语）在没有任何保护条款的情况下是无上限的。

以下所有单元的 `source` 字段中这三项相同：

```
type: upstream
source_id: upstream-hardikpandya-stop-slop
commit: 8da1f030185bdfe8471220585162991eaeb970e9
```

`path` 和 `anchor` 逐条写出：`path` 是上游仓库内路径（`SKILL.md` 或 `references/*.md`），`anchor` 是该文件里的小节标题；多条规则共用一个小节时，标题后加各自那一行的行首原文。

---

## 2 单元清单

### U-ssl-001
category: pattern
language: en
rule_summary: 删掉清嗓子式开场（throat-clearing openers）——先宣告自己要说什么、再说的开头，直接从内容本身开始；上游给出的完整词表为 "Here's the thing:"、"Here's what [X]"、"Here's this [X]"、"Here's that [X]"、"Here's why [X]"、"The uncomfortable truth is"、"It turns out"、"The real [X] is"、"Let me be clear"、"The truth is,"、"I'll say it again:"、"I'm going to be honest"、"Can we talk about"、"Here's what I find interesting"、"Here's the problem though"，并规定任何 "here's what/this/that" 结构一律算清嗓子。
positive: The webpack dev server doesn't send the CORS header by default.
negative: Here's the thing: the webpack dev server doesn't send the CORS header. It turns out the fix is one flag. 违反点：`Here's the thing:` 和 `It turns out` 是词表里的两条，两句都只做预告、不承载信息。
path: references/phrases.md
anchor: `## Throat-Clearing Openers`
notes:
- 由 references 补全：首轮拆规则时本单元只有 SKILL.md 里的三个 "here's" 变体，完整的 15 条词表和"任何 here's what/this/that 结构一律算"这条兜底判据在 `references/phrases.md` 的 `## Throat-Clearing Openers` 一节。
- intent: 上游给了这一节的修法说明 "Remove these announcement phrases. State the content directly."——"announcement" 是理由本身：作者认为这些短语的共同点是宣告而不是陈述，与 Scoring 表 Directness 维度的问法 "Statements or announcements?" 是同一个判据。首轮记的"上游未说明、由评分表推断"在补进 references 后可以改成上游明说。
- existing: 疑似对应 EN-P-007（其词表已含 Here's the thing、Let me be clear、I'll be honest、The uncomfortable truth is、here's what you need to know）。上游词表里 "It turns out"、"The real [X] is"、"I'll say it again:"、"Can we talk about"、"Here's the problem though" 五条 EN-P-007 没有。
- 拆分判断：Core Rules 第 1 条一句话里并列了三件事（throat-clearing openers、emphasis crutches、all adverbs），三者判定逻辑不同，拆成 U-ssl-001、U-ssl-002、U-ssl-003；phrases.md 的小节划分与这个拆法一致。
- Quick Checks 里的 `Any "here's what/this/that" throat-clearing? Cut to the point.` 是这条的具体判据，共用本单元。

### U-ssl-002
category: pattern
language: en
rule_summary: 删掉强调拐杖（emphasis crutches）——只告诉读者"这里很重要"、本身不增加信息的短语；上游给出的词表为 "Full stop." 与 "Period."、"Let that sink in."、"This matters because"、"Make no mistake"、"Here's why that matters"，判据是删掉之后句子的信息一点不少。
positive: The migration dropped p99 latency from 400ms to 90ms.
negative: The migration dropped p99 latency. Let that sink in. Make no mistake, this matters because latency is the whole product. 违反点：`Let that sink in.`、`Make no mistake`、`this matters because` 是词表里的三条，删掉之后第一句的信息一点不少。
path: references/phrases.md
anchor: `## Emphasis Crutches`
notes:
- 由 references 补全：首轮只有模式名和我自己造的 truly / really 例子，完整词表在 `references/phrases.md` 的 `## Emphasis Crutches` 一节。补全后发现这一节收的不是副词而是整句式的强调短语，与首轮按"强调副词"理解的方向有出入，rule_summary 已按上游改写。
- intent: 上游给了这一节的判据 "These add no meaning. Delete them."。它防的是用一句话替论断撑场面：论断的分量应当由内容产生，不由一句"这很重要"宣布。
- existing: 疑似对应 EN-P-004（不增加信息的短语）与 EN-P-022（告诉读者该怎么理解的旁白）；五条词表条目现有词表里一条都没有。
- 与 U-ssl-003 的关系在补全后变了：phrases.md 把副词单列成 `## Adverbs` 一节，emphasis crutches 一节里没有一条是副词，两条不再是全集与子集的关系。
- 与 U-ssl-029 的边界：`This matters because` 在本节，`actually matters` 在 `## Telling Instead of Showing` 一节（U-ssl-029），两处词形接近但上游分在两节，本清单按上游的归属拆。

### U-ssl-003
category: style-opinion
language: en
rule_summary: 删掉全部副词，一个不留（"Kill all adverbs. No -ly words."、"Any adverbs? Kill them."），不区分这个副词有没有承担强调、不确定、对比或作者语感；上游点名的具体条目为 "really"、"just"、"literally"、"genuinely"、"honestly"、"simply"、"actually"、"deeply"、"truly"、"fundamentally"、"inherently"、"inevitably"、"interestingly"、"importantly"、"crucially"。
positive: The build failed.
negative: The build unfortunately failed again, and honestly it completely blocks the release. 违反点：`unfortunately`、`again`、`honestly`、`completely` 都是副词，按本条一律删除；其中 `honestly` 还在上游点名的十五条里。
path: references/phrases.md
anchor: `## Adverbs / Kill all adverbs. No -ly words.`
notes:
- 由 references 补全：首轮只有 SKILL.md 的 "Remove ... all adverbs" 和 "Any adverbs? Kill them."，十五条具体条目和 "No -ly words" 这个形式判据在 `references/phrases.md` 的 `## Adverbs` 一节。`references/structures.md` 的 `## Word Patterns` 一节还有一行 `| All adverbs (-ly words, "really," "just," "literally," "genuinely," "honestly," "simply," "actually") | Empty emphasis. See phrases.md for full list. |`，是同一条的第三次出现，覆盖表里指向本单元。
- intent: 上游在 structures.md 里给了理由 "Empty emphasis"——作者认为副词承担的是空的强调。他把判据写成 "No -ly words"（纯词形）而不是"不承担强调的副词"（需要判断），换来的是可判定性和执行成本，代价是误伤那些确实承担强调、不确定或对比的副词。首轮记的"上游未说明"在补进 references 后可以改成上游给了一个词组级的理由。
- existing: 疑似对应 EN-P-003，且与之直接冲突：EN-P-003 的判据是"不承担强调、不确定、对比或作者语感时删掉；承担时保留"，本条不留这个例外。EN-P-003 的词表与上游十五条重合十条（just、literally、honestly、simply、actually、truly、fundamentally、inherently、inevitably、importantly、crucially），上游多出 really、genuinely、deeply、interestingly。
- 强风格主张，按 criteria.md 第 4 条的判据（换一个作者、换一个体裁还成不成立）记 style-opinion，不因为与 EN-P-003 矛盾而弱化其表述。
- 与同一行的 U-ssl-026 拆开的理由：`Kill all adverbs. No -ly words. No softeners, no intensifiers, no hedges.` 这一行里，前半是词形判据（是不是副词），后半是功能判据（这个词是不是在软化、加强或保留），后半能命中不是副词的词（"most"、"some"），两条各自可判定。

### U-ssl-004
category: pattern
language: en
rule_summary: 拆掉二元对比（binary contrasts）——先否定一个说法再给出另一个说法的骨架，直接把后半陈述出来；上游给出的十一种形式为 "Not because X. Because Y." 与 "Not because X, but because Y."、"[X] isn't the problem. [Y] is."、"The answer isn't X. It's Y."、"It feels like X. It's actually Y."、"The question isn't X. It's Y."、"Not X. But Y." 与 "not X, it's Y" 与 "isn't X, it's Y"、"It's not this. It's that."、"stops being X and starts being Y"、"doesn't mean X, but actually Y"、"is about X but not Y"、"not just X but also Y"；修法是把否定整个丢掉，只留正面陈述。
positive: The bottleneck is disk I/O.
negative: The answer isn't CPU. It's disk I/O. The system stops being compute-bound and starts being I/O-bound. 违反点：`The answer isn't X. It's Y.` 与 `stops being X and starts being Y` 是模式表里的两条骨架，被否定的 X 在上下文里没人主张过。
path: references/structures.md
anchor: `## Binary Contrasts`
notes:
- 由 references 补全：首轮只有 SKILL.md 里的 "binary contrasts" 一个模式名和 Quick Checks 的一个例子，十一行模式表和修法 "State Y directly. 'The problem is Y.' 'Y matters here.' Drop the negation entirely." 在 `references/structures.md` 的 `## Binary Contrasts` 一节。
- intent: 上游给了这一节的理由 "These create false drama."，并给每一行标了各自的问题（Telegraphed reversal、Formulaic reframe、Predictable pivot、Setup/reveal cliche、Rhetorical misdirection、Mechanical contrast、False transformation arc、Negation-then-assertion crutch、False distinction、Additive hedge）。作者防的是用推翻一个没人主张的靶子来替代直接给出论断。
- existing: 疑似对应 EN-P-006（其词表已含 It's not X, it's Y、not only X but Y、The question isn't X. It's Y.）。上游多出 "stops being X and starts being Y"、"doesn't mean X, but actually Y"、"is about X but not Y" 三条，EN-P-006 没有。
- 十一行共用同一条判定逻辑（这个句子是不是先否定一个说法再给出另一个），合为一个单元，模式表放进正反例。
- 拆分判断：Core Rules 第 2 条一句话点名了五种结构，structures.md 把它们各自展成一个小节，本清单的 U-ssl-004 至 U-ssl-008 与那五个小节一一对应。

### U-ssl-005
category: pattern
language: en
rule_summary: 拆掉否定式排比（negative listing）——连续罗列"不是什么"、最后才给出"是什么"的结构，上游给出的两种形式为 "Not a X... Not a Y... A Z." 和 "It wasn't X. It wasn't Y. It was Z."；修法是直接给出最后那个 Z，不铺跑道。
positive: AlphaEvolve searched without favoring symmetry or human-looking designs.
negative: Not a heuristic. Not a prior. A search. 违反点：`Not a X... Not a Y... A Z.` 是模式表里的第一行，前两句只说不是什么。
path: references/structures.md
anchor: `## Negative Listing`
notes:
- 由 references 补全：首轮只有模式名，两行模式表、修法 "State Z. The reader doesn't need the runway." 和作者对这个结构的命名（"A rhetorical striptease."）在 `references/structures.md` 的 `## Negative Listing` 一节。
- intent: 上游写了理由 "Listing what something is *not* before revealing what it *is*. A rhetorical striptease."，并给两行各标了问题（Dramatic buildup through negation、Same structure, past tense）。作者防的是用推迟揭晓来制造分量。首轮记的"上游未说明"在补进 references 后可以改成上游明说。
- existing: 疑似对应 EN-P-006（其中的 `Not a X. Not a Y. A Z.` 变体，词形与上游第一行完全一致）。
- 与 U-ssl-004 的区别：U-ssl-004 是一个句子内的二元对比，本条是跨句的多项否定罗列；上游把两者分成两节，与首轮的拆法一致。

### U-ssl-006
category: pattern
language: en
rule_summary: 拆掉戏剧化碎片（dramatic fragmentation）——把话切成一串不完整的短句来制造节奏，写成完整句子；上游给出的三种形式为 "[Noun]. That's it. That's the [thing]."、"X. And Y. And Z."、"This unlocks something. [Word]."，并在 Rhythm Patterns 里补了一条 "Don't stack short punchy sentences"。
positive: The old assumptions stopped holding once the search ignored symmetry.
negative: Results. That's it. That's the trick. 违反点：`[Noun]. That's it. That's the [thing].` 是模式表里的第一行，三个片段靠断句制造重量。
path: references/structures.md
anchor: `## Dramatic Fragmentation`
notes:
- 由 references 补全：首轮只有模式名，三行模式表、理由 "Sentence fragments for emphasis read as manufactured profundity." 和修法 "Complete sentences. Trust content over presentation." 在 `references/structures.md` 的 `## Dramatic Fragmentation` 一节；同一文件 `## Rhythm Patterns` 的 `| Staccato fragmentation | Don't stack short punchy sentences |` 是同一条的第二次出现，覆盖表里指向本单元。
- intent: 上游写了理由 "manufactured profundity"——作者认为碎片化制造的是伪造的深刻感，修法 "Trust content over presentation" 点明了他的判据：分量该由内容承担，不由排版承担。这与 Scoring 表的 Authenticity 维度对应。
- existing: 疑似对应 EN-P-025（其例子 `That's it. That's the whole thing.`、`X. And Y. And Z.` 与上游模式表的第一、第二行词形几乎一致）。
- 注意：本条与 U-ssl-016（段尾不要都收在短促单句上）判定逻辑不同——本条看的是连续片段句，U-ssl-016 看的是段落收尾位置；上游把两者分别放在 `## Dramatic Fragmentation` 和 `## Rhythm Patterns` 两处，与首轮的拆法一致。

### U-ssl-007
category: pattern
language: en
rule_summary: 拆掉修辞性铺垫（rhetorical setups）——宣告洞见而不给出洞见的句子，上游给出的四种形式为 "What if [reframe]?"、"Here's what I mean:"、"Think about it:"、"And that's okay."；修法是直接给出论断，让读者自己下结论。
positive: Caching in Next.js happens at three layers: request memoization, the data cache, and the router cache.
negative: What if caching isn't one thing? Here's what I mean: it happens at three layers. Think about it. 违反点：`What if [reframe]?`、`Here's what I mean:`、`Think about it:` 是模式表里的三行，三句都不承载信息。
path: references/structures.md
anchor: `## Rhetorical Setups`
notes:
- 由 references 补全：首轮只有模式名和我自己造的例子，四行模式表、理由 "These announce insight rather than deliver it." 和修法 "Make the point. Let readers draw conclusions." 在 `references/structures.md` 的 `## Rhetorical Setups` 一节。补全后多出一条首轮没有的形式：`"And that's okay."`（上游标注的问题是 "Unnecessary permission"），它不是设问，是替读者发许可，已并入本单元。
- intent: 上游写了理由 "These announce insight rather than deliver it."，并给四行各标了问题（Socratic posturing、Redundant preview、Condescending prompt、Unnecessary permission）。这与 Scoring 表 Directness 维度的问法 "Statements or announcements?" 是同一个判据。
- existing: 疑似对应 EN-P-009（其词表含 What if I told you、Think about it 与自问自答式的"问题？答案。"）；`And that's okay.` 这条现有规则里没有，它与 EN-P-022（告诉读者该怎么理解的旁白）方向接近但不是同一条。
- 与 U-ssl-001 的区别：U-ssl-001 是段落开头的清嗓子，本条是任意位置的设问-揭晓骨架。与 U-ssl-034 的区别：本条看的是这个句子本身是不是铺垫，U-ssl-034 看的是问句和它的答案之间的距离。

### U-ssl-008
category: pattern
language: en
rule_summary: 不让无生命的事物做只有人能做的动作（false agency）：上游给出的七个例子为 "a complaint becomes a fix"、"a bet lives or dies in days"、"the decision emerges"、"the culture shifts"、"the conversation moves toward"、"the data tells us"、"the market rewards"；修法是找出真正做这件事的人放到主语位置，找不到具体的人时用 "you" 把读者放进那个位置。
positive: The on-call engineer turned that complaint into a fix that week.
negative: The complaint becomes a fix, the decision emerges, and the market rewards the team. 违反点：`complaint`、`decision`、`market` 是无生命的名词，`becomes a fix`、`emerges`、`rewards` 是把人的动作安到它们头上，三处都在模式表里，句子里没有施事者。
path: references/structures.md
anchor: `## False Agency`
notes:
- 由 references 补全：首轮只有 SKILL.md 里的两个例子（`the complaint becomes a fix`、`the decision emerges`），七行模式表、每行的逐条解释、以及 "If no specific person fits, use 'you' to put the reader in the seat." 这条兜底修法在 `references/structures.md` 的 `## False Agency` 一节。那条兜底修法把本单元与 U-ssl-013（把读者放进现场）连了起来，首轮没有这条线索。
- intent: 上游写明了理由——"A person does something to make those things happen. AI loves this because it avoids naming the actor."。作者防的是一种把责任主体抹掉的写法：事情"发生了"，没人做了它。他给每一行都写了同一形状的驳斥（"The complaint did nothing. Someone fixed it."、"Decisions don't emerge. Someone decides."、"Data sits there. Someone reads it and draws a conclusion."），说明他要的是把动作退回给人。首轮记的"上游未说明"在补进 references 后可以改成上游明说。
- existing: 疑似对应 ALL-P-004（其例子"市场奖励""数据告诉我们""决定浮现出来"与上游模式表的第七、第六、第三行完全对应）。
- 拆分判断：Core Rules 第 2 条把 "false agency" 列为套式结构之一，第 3 条写成 "No inanimate objects performing human actions"，Quick Checks 写成一条问句，structures.md 又单列一节——四处是同一条判定逻辑的四次出现，合并为一个单元，覆盖表里四处都指向这里。

### U-ssl-009
category: style-opinion
language: en
rule_summary: 每一个句子都要有一个"人"作主语并且在做一件事（"Every sentence needs a human subject doing something"）。
positive: The team ships the cache invalidation fix on Thursday.
negative: The cache invalidation fix ships on Thursday. 违反点：主语 `The cache invalidation fix` 不是人；句子是主动语态、也没有把人的动作安给死物，但仍然违反"每句都要有人做主语"。
path: SKILL.md
anchor: `## Core Rules / 3. **Use active voice.**`
notes:
- 本单元的规则文本只在 SKILL.md 里，path 保持 `SKILL.md`。`references/structures.md` 的 `## Passive Voice` 一节把同一句写成 "Every sentence needs a subject doing something."——**少了 "human" 这个限定**。两处口径不一致，这一点记在第 4 节。
- intent: 上游未说明。推断：这是作者对 Core Rule 5（"Put the reader in the room"）的语法层落实——他认为 AI 文本读起来悬空，根源是句子里没有人；要求每句都有人作主语是把这个直觉写成一条机器能执行的判据。推断依据是第 3 条与第 5 条主张方向一致、第 5 条写了 `"You" beats "People."`，以及 structures.md 的 `## False Agency` 一节把兜底修法写成"找不到具体的人就用 you"。
- existing: 疑似对应 ALL-P-004，但 ALL-P-004 只要求"指名动作的执行者、优先主动语态"，不要求执行者必须是人，本条比它强一档。
- 拆分判断：与 U-ssl-008、U-ssl-010 三者判定逻辑不同。"The cache stores results." 是主动语态、施事者明确、动词也不是人类专属，只违反本条；"The complaint becomes a fix." 只违反 U-ssl-008；"The configuration was updated." 只违反 U-ssl-010。三条各自可判定，故分立。
- 可判定性存疑：技术文档和百科文本里大量正确的句子没有人作主语，归并时按 criteria.md 第 4 条要考虑这条换个体裁还成不成立。

### U-ssl-010
category: style-opinion
language: en
rule_summary: 一处被动语态都不留（"No passive constructions"）；发现被动就找出施事者，把施事者放到句首。上游给出的四个例子和各自的修法为 "X was created"→点名是谁创建的、"It is believed that"→点名是谁相信、"Mistakes were made"→点名是谁犯的、"The decision was reached"→点名是谁决定的。
positive: The installer writes the config file on first run.
negative: The config file is written on first run, and it is believed that mistakes were made in the template. 违反点：`is written`、`it is believed that`、`mistakes were made` 是三处被动结构，后两处是模式表里的原样条目，句子没有说是谁写的、谁相信、谁犯的。
path: references/structures.md
anchor: `## Passive Voice`
notes:
- 由 references 补全：首轮只有 SKILL.md 的 "No passive constructions" 和 Quick Checks 的一句修法，四行模式表、逐条修法和 "Passive voice hides the actor and drains energy." 这句理由在 `references/structures.md` 的 `## Passive Voice` 一节。
- intent: 上游写了理由 "Passive voice hides the actor and drains energy."，修法一律是 "Find the actor. Put them at the front of the sentence."。这个修法假设每个被动句背后都有一个可以找出来的施事者，代价是误伤那些施事者不重要或不可知的正当被动句。首轮记的"上游未说明"在补进 references 后可以改成上游明说了前半（隐藏施事者），后半（drains energy）仍是无判据的主张。
- existing: 疑似对应 ALL-P-004，且与之冲突：ALL-P-004 写的是"优先主动语态"并禁止"隐藏施事者的无主句和被动式"，允许施事者明确或不重要时用被动；本条是无例外禁令。
- 强风格主张，按 criteria.md 第 4 条记 style-opinion。
- 归并时注意：本条与 blader §13 方向一致但强度不同——blader 写的是 "Use active voice when it makes the actor and action clearer."，带条件；本条不带条件。
- 与 U-ssl-009 共用 structures.md 同一节：那一节的开场句 "Every sentence needs a subject doing something." 归 U-ssl-009（口径差异见上），四行模式表和修法归本单元。

### U-ssl-011
category: pattern
language: en
rule_summary: 不用泛泛的断言句（vague declaratives）代替具体内容——宣布某件事重要、深刻或有结构，却不说出是哪一件；上游给出的五条为 "The reasons are structural"、"The implications are significant"、"This is the deepest problem"、"The stakes are high"、"The consequences are real"，并给了兜底判据：一句话说某件事 important / deep / structural 而没有给出那个具体的东西时，删掉它或换成那个具体的东西。
positive: Two teams own the same table, so every schema change needs a cross-team review.
negative: The reasons are structural. The stakes are high. The consequences are real. 违反点：三句都在词表里，都说了"有原因/有利害/有后果"却没有说出是哪一个。
path: references/phrases.md
anchor: `## Vague Declaratives`
notes:
- 由 references 补全：首轮只有 SKILL.md 里的两个例子，五条词表和兜底判据在 `references/phrases.md` 的 `## Vague Declaratives` 一节。补全后本条从"两个例子"变成了一条带兜底判据的可判定规则。
- intent: 上游给了这一节的定义 "Sentences that announce importance without naming the specific thing."。它针对的是一种特定的空转——句子在语法和语义上都成立，可以放进任何一篇文章而不出错，因此读者读完一无所获。修法给了两个选项（cut it or replace it with the specific thing），说明作者认为这个位置未必本该有内容。
- existing: 疑似对应 ALL-P-007（能给名字、数字、机制的地方不用抽象词）与 ALL-M-001（可移植性测试）；五条词表条目现有词表里没有。
- 拆分判断：Core Rules 第 4 条里 "No vague declaratives" 和 "No lazy extremes" 是两组不同的词/结构，拆成 U-ssl-011 和 U-ssl-012；phrases.md 和 structures.md 也把两者分在不同文件的不同小节。
- Core Rules 第 5 条末的 "Specifics beat abstractions." 是本条的重述，不另立单元。

### U-ssl-012
category: pattern
language: en
rule_summary: 不用全称量词做含糊的活（lazy extremes）——上游点名的六个词为 every、always、never、everyone、everybody、nobody，问题是 "False authority"：它们看着像论断，实际上没有划出任何真实范围；修法是给出具体范围而不是笼统主张。
positive: In the three incidents we reviewed, the retry loop fired before the health check.
negative: Everybody knows every incident always starts the same way, and nobody has ever seen the health check fire first. 违反点：`Everybody`、`every`、`always`、`nobody` 都在词表里，把一个没有统计过的范围说成全称，读者无法核对也无法反驳。
path: references/structures.md
anchor: `## Word Patterns / | Lazy extremes (every, always, never, everyone, everybody, nobody) |`
notes:
- 由 references 补全：首轮只有 SKILL.md 给的三个词（every、always、never），完整的六词清单、问题命名 "False authority" 和修法 "Use specifics instead of sweeping claims." 在 `references/structures.md` 的 `## Word Patterns` 一节。
- intent: 上游把问题命名为 "False authority"——全称词借来的是一种作者没有的权威。SKILL.md 里的措辞 "lazy extremes ... doing vague work" 补足了另一半：作者认为写作者用全称词是因为不想去查真实的范围。两处合起来是完整的理由。
- existing: 现有规则里没有。ALL-P-007 管的是抽象换具体，EN-P-039 管的是疑似捏造的统计数字，都不覆盖"全称量词当含糊用"这个判据。
- 六个词共用同一条判定逻辑（这个全称词有没有划出真实范围），合为一个单元，词表放进正反例。
- `## Word Patterns` 一节共两行，另一行（All adverbs）归 U-ssl-003，故本单元的 anchor 带行首原文。

### U-ssl-013
category: style-opinion
language: en
rule_summary: 不用悬在场景之上的旁白腔（narrator-from-a-distance），把读者放进现场；上游给出的四种形式为 "Nobody designed this."、"This happens because..."、"This is why..."、"People tend to..."，修法是改成第二人称的现场句（"You don't sit down one day and decide to..." 优于 "Nobody designed this."）。
positive: You open the dashboard and the numbers are already three hours stale.
negative: People tend to find that the numbers go stale. This happens because nobody designed the refresh path. 违反点：`People tend to`、`This happens because`、`nobody designed` 是模式表里的三条，读者不在场，叙述者在讲台上。
path: references/structures.md
anchor: `## Narrator-from-a-Distance`
notes:
- 由 references 补全：首轮只有 SKILL.md 的 `"You" beats "People."` 和 Quick Checks 的一个例子，四行模式表、每行的问题命名（Disembodied observation、Lecturer voice、Same、Armchair sociologist）和修法在 `references/structures.md` 的 `## Narrator-from-a-Distance` 一节。补全后多出两条首轮没有的形式：`"This happens because..."` 和 `"This is why..."`，上游把它们标为 "Lecturer voice"。
- intent: 上游写了理由 "Floating above the scene instead of putting the reader in it."，并用逐条的问题命名说清了他反对的是哪种姿态（无实体的观察、讲师腔、扶手椅社会学）。他把这件事定位成人称与视角选择问题，因为人称可判定，"疏离感"不可判定。
- existing: 疑似对应 EN-P-034（现有决定为 reference-only，其词表含 people tend to、nobody designed this，与上游第四、第一行对应）；`This happens because...`、`This is why...` 两条 EN-P-034 没有，而这两条的误伤面比另外两条大得多（技术文档里"这是因为"是正常写法）。
- 强风格主张（要求一种具体人称），按 criteria.md 第 4 条归并时要判断换个体裁是否还成立；技术文档和百科不适合用 you。
- 与 U-ssl-008 的连接：structures.md 的 `## False Agency` 一节把兜底修法写成"找不到具体的人就用 you 把读者放进那个位置"，两条在修法上是接力关系。

### U-ssl-014
category: pattern
language: en
rule_summary: 句子长度要有变化；连续三句长度相同即命中，必须把其中一句改掉。
positive: The cache warms on boot. Once it is warm, a cold request costs about four milliseconds, which is under the budget we set in March. Then it stays warm.
negative: The cache warms on boot. The index loads next. The workers then start. 违反点：连续三句词数相同、结构相同（主语+动词+时间副词），节奏是节拍器式的。
path: SKILL.md
anchor: `## Core Rules / 6. **Vary rhythm.**`
notes:
- 本条的规则文本和阈值只在 SKILL.md 里（Core Rules 第 6 条的 "Mix sentence lengths" 与 Quick Checks 的 `Three consecutive sentences match length? Break one.`）。`references/structures.md` 的 `## Rhythm Patterns` 一节收了六种节奏问题，**没有一条是句长**，path 保持 `SKILL.md`。
- intent: 上游未说明理由，但 Scoring 表的 Rhythm 维度写成 "Varied or metronomic?"，"metronomic"（节拍器式）就是作者对这个现象的命名。推断：作者认为语言模型逐词生成时会收敛到一个稳定的句长，人写东西不会，因此句长方差本身就是信号。推断依据是评分表的措辞。
- existing: 疑似对应 ALL-P-001。ALL-P-001 已经采纳了"连续三句以上落在同一档即命中"的判据，与本条的阈值一致。
- 拆分判断：Core Rules 第 6 条一句话里有四件事（mix sentence lengths、two items beat three、end paragraphs differently、no em dashes），拆成 U-ssl-014 至 U-ssl-017；structures.md 的 `## Rhythm Patterns` 一节把后三件各收成一行，与这个拆法一致。

### U-ssl-015
category: style-opinion
language: en
rule_summary: 并列项不用三项；SKILL.md 写成默认偏好（"Two items beat three"），structures.md 写成直接的修法（三项清单一律改成两项或一项）。
positive: The release covers caching and retries.
negative: The release covers caching, retries, and observability. 违反点：三项并列；按本条应当压成两项或一项。
path: references/structures.md
anchor: `## Rhythm Patterns / | Three-item lists | Use two items or one |`
notes:
- 由 references 补全：首轮只有 SKILL.md 的比较句 "Two items beat three"，structures.md 的 `## Rhythm Patterns` 把它写成 `| Three-item lists | Use two items or one |`——修法从"两项更好"变成了"改成两项或一项"，比首轮理解的更强。rule_summary 已按两处的合并口径改写。
- intent: 上游未说明理由。推断：这是把"AI 爱凑三项"这一观察反向写成了一条生成期的偏好——不是"发现三项排比就检查是不是凑出来的"，而是"直接改用两项"。作者选择在生成侧下手而不是在检测侧下手，代价是三项本来就成立的场合也会被压成两项。推断依据是 SKILL.md 用比较句式而 structures.md 用祈使式修法，两处都不带触发条件。
- existing: 疑似对应 ALL-P-005，且与之冲突：ALL-P-005 的判据是"该用几项就用几项"，本条要求默认取两项或一项。
- 强风格主张，按 criteria.md 第 4 条记 style-opinion。
- 与 blader §10（"Forced groups of three"）和 conorbronsdon 的 "Compulsive rule of three"（U-aaw-049）的区别值得归并时留意：那两条管的是"强行凑三"，本条管的是"有三项就改掉"，本条最强。

### U-ssl-016
category: pattern
language: en
rule_summary: 段落的收尾方式要有变化；每段都以一句短促有力的单句收尾（punchy one-liner）即命中。
positive: 一段以完整的解释句收尾，下一段以一个具体数字收尾，第三段以一个未解决的问题收尾。
negative: 连续三段分别以 `That's the whole trick.`、`It just works.`、`Nothing else changed.` 收尾。违反点：三段都用同一种收尾形状——一句短促的独立单句。
path: references/structures.md
anchor: `## Rhythm Patterns / | Every paragraph ends punchily | Vary endings |`
notes:
- 由 references 补全：首轮只有 SKILL.md 的 "End paragraphs differently" 和 Quick Checks 的一句问法，structures.md 的 `## Rhythm Patterns` 把它写成 `| Every paragraph ends punchily | Vary endings |`——判据仍是"每段都这样"（Every），不是"有一段这样"，与首轮的理解一致。
- intent: 上游未说明。推断：与 U-ssl-014 同属 Rhythm 维度，但管的是段落级而不是句子级——作者认为节拍器式的规律性会在段落收尾位置上重复出现，而这个位置读者印象最深，所以单独列一条。推断依据是它在 SKILL.md 和 structures.md 两处都被写成独立一项，且判据里带 "Every"。
- existing: 疑似对应 ALL-P-001（段落结构雷同）与 EN-P-024（故作深刻的收尾金句），但"每段都用同一种收尾形状"这个具体判据现有规则里没有——ALL-P-001 管的是段落长度和开头句式，EN-P-024 管的是收尾句的内容空洞与否。
- 与 U-ssl-019（cut quotables）的区别：本条看的是位置和重复，U-ssl-019 看的是单句本身像不像摘引金句。

### U-ssl-017
category: style-opinion
language: en
rule_summary: 全文一处破折号都不用（"No em dashes"、"Em-dash anywhere? Remove it."、"Remove. Use commas or periods. No em dashes at all."），不按篇幅、不按频率设上限；替代标点是逗号或句号。
positive: The policy was announced without warning, and it affects thousands of workers.
negative: The policy — announced without warning — affects thousands of workers. 违反点：两处 em dash（—）。
path: references/structures.md
anchor: `## Rhythm Patterns / | Em-dashes | Remove. Use commas or periods. No em dashes at all. |`
notes:
- 由 references 补全：首轮只有 SKILL.md 的两处禁令，structures.md 的 `## Rhythm Patterns` 给了第三次陈述并加上了替代标点和一句强调 "No em dashes at all."。**三处都没有频率或密度口径**，确认这是无条件禁令，不是上限。
- intent: 上游未说明。推断：作者把破折号归进 Rhythm 而不是标点或格式，说明他关注的不是排版而是破折号造成的停顿——他认为破折号是制造戏剧停顿最省力的手段。一刀切禁用与 U-ssl-003、U-ssl-010 是同一种取舍：换可判定性。推断依据是这条在 SKILL.md 和 structures.md 里都被归进节奏一类。
- existing: 疑似对应 EN-P-026，且与之冲突：EN-P-026 已经采纳的是按篇幅分界（200 词以下一处不用，200 词以上至多一到两处），本条是无条件禁令。
- 三个来源在这一点上三种口径：本条无条件禁；blader §14 禁但作者样本用破折号时按样本频率保留；conorbronsdon 设每千词一处的频率上限（U-aaw-035）。归并时是一处明确的三方冲突。
- **上游自己的示例违反了这一条**：`references/examples.md` 的 Example 4 的 After 文本写成 "Speed, quality, cost—pick two."，用了一处 em dash。这一点记在第 4 节。
- 强风格主张，按 criteria.md 第 4 条记 style-opinion。

### U-ssl-018
category: style-opinion
language: en
rule_summary: 直接把事实说出来，不加缓和语、不替读者预先辩解、不手把手解释（"Trust readers. State facts directly. Skip softening, justification, hand-holding."）。
positive: The migration will drop 40 rows that have no matching parent.
negative: It's worth noting that the migration may, in some cases, drop a small number of rows — this is expected behavior, and there's no need to worry. 违反点：`It's worth noting that`（预先辩解）、`may, in some cases`（缓和语）、`there's no need to worry`（手把手安抚）三件事叠在一句里。
path: SKILL.md
anchor: `## Core Rules / 7. **Trust readers.**`
notes:
- 本条的规则文本只在 SKILL.md 里，path 保持 `SKILL.md`。references 里与它最近的是 phrases.md 的 `## Adverbs` 一节那句 "No softeners, no intensifiers, no hedges."（U-ssl-026）和 structures.md 的 `| "Not always. Not perfectly." | Hedging disguised as reassurance |`（U-ssl-035），两条各自成单元，本条是它们共同的上位主张。
- intent: 上游未说明理由，但 Scoring 表把这条抽成一个独立维度 Trust（"Respects reader intelligence?"），说明作者认为它不是一个局部的措辞问题而是全篇的一种姿态。推断：作者防的是那种预设读者会误解、会不安、会需要被牵着走的写法，他认为这种预设本身就是 AI 文本的特征。推断依据是评分表里 Trust 维度的问法。
- existing: 疑似对应 EN-P-022（告诉读者该怎么理解的旁白）与 EN-P-029（堆叠保留语），但"不替读者预先辩解"这一层现有规则里没有对应。
- 拆分判断：softening、justification、hand-holding 三者共用同一条判定逻辑（这句话是不是在替读者垫话），合为一个单元，三种表现放进反例。
- category 归属勉强：三种表现里 softening 是可以指认的词，属 pattern；justification 和 hand-holding 更接近姿态判断。按整条的主张性质记 style-opinion，归并时可重判。

### U-ssl-019
category: pattern
language: en
rule_summary: 听起来像可以摘出来当引言的句子（pull-quote）要重写掉。
positive: Symmetric layouts feel more predictable to users because the eye can guess where the next element sits.
negative: Symmetry is the language of trust. 违反点：整句是一条脱离上下文也能独立成立的格言，形状就是为被摘引而造的。
path: SKILL.md
anchor: `## Core Rules / 8. **Cut quotables.**`
notes:
- 本条的规则文本只在 SKILL.md 里，path 保持 `SKILL.md`。**三份 references 里没有任何一节展开这条**：phrases.md 收的是短语，structures.md 收的是句法骨架，都没有"金句形状"这一类。这是补拆之后仍然只有一句话的两条之一（另一条是 U-ssl-009 的 "human" 限定）。
- intent: 上游未说明。推断：这条与 U-ssl-016 一起构成作者对"为传播而写"的排斥——他认为社交媒体优化过的写作会把每一句都造成可摘引的形状，而这个形状本身就是内容被掏空的信号。推断依据是它被单列为一条 Core Rule 而不是并进节奏或填充词那两条。
- existing: 疑似对应 EN-P-024。
- 可判定性存疑：判据是 "If it sounds like a pull-quote"，"sounds like" 需要判断，按 criteria.md 第 2 条归并时要考虑能不能圈出具体的词或结构。可用的形式判据：整句不依赖上下文、结构是 "X is the Y of Z" 或 "X is not A but B"。这个形式判据是我补的，不是上游写的，补进 references 之后仍然如此。

### U-ssl-020
category: style-opinion
language: en
rule_summary: 句子不以 Wh- 词开头，上游点名的七个词为 What、When、Where、Which、Who、Why、How；修法是重构这个句子，让主语或动词打头，"What makes this hard is..." 应改成 "The constraint is..."，更好的做法是直接说出那个具体的约束。
positive: Caching in Next.js works at three layers.
negative: What makes Next.js caching different is that it works at three layers. 违反点：句子以 `What` 开头，是 wh-分裂句，把论断推到了后半句。
path: references/structures.md
anchor: `## Sentence Starters to Avoid / | Sentences starting with What, When, Where, Which, Who, Why, How | Restructure. Lead with the subject or the verb. |`
notes:
- 由 references 补全：首轮只有 Quick Checks 的一句 "Sentence starts with a Wh- word? Restructure it."，七词清单、修法方向（Lead with the subject or the verb）、理由（"Wh- openers become a crutch."）和一个 before/after 例子在 `references/structures.md` 的 `## Sentence Starters to Avoid` 一节。
- intent: 上游给了理由 "Wh- openers become a crutch."，并用例子说明了他反对的具体形态：`"What makes this hard is..."` 这类 wh-分裂句把论断推迟到句子后半。他还给了两级修法（先重构，更好的是直接点名那个具体的东西），说明本条与 U-ssl-011（泛泛断言）指向同一个问题的两个面。首轮记的"上游未说明，连修法都只写了 Restructure it"在补进 references 后可以改成上游给了理由和两级修法。
- existing: 现有规则里没有。EN-P-032 管的是长文小标题不用问句，管不到正文句子；EN-P-009 管的是修辞性设问，管不到 wh-分裂句。
- 强风格主张且是纯形式判据，误伤面大（"Which team owns this table is unclear." 这类正常句子也会命中）。按 criteria.md 第 4 条记 style-opinion。
- `## Sentence Starters to Avoid` 一节共三行，另两行归 U-ssl-032 和 U-ssl-033，故本单元的 anchor 带行首原文。

### U-ssl-021
category: pattern
language: en
rule_summary: 删掉元评论（meta-commentary）——交代文章自身结构或对自己的写作发议论、不承载内容的句子；上游给出的词表为 "Hint:"、"Plot twist:" 与 "Spoiler:"、"You already know this, but"、"But that's another post"、"X is a feature, not a bug"、"Dressed up as"、"The rest of this essay explains..."、"Let me walk you through..."、"In this section, we'll..."、"As we'll see..."、"I want to explore..."。
positive: 直接进入下一节的内容。
negative: In this section, we'll walk through the three failure modes. Plot twist: they share a root cause. But that's another post. 违反点：`In this section, we'll`、`Plot twist:`、`But that's another post` 是词表里的三条，三句都只谈文章自身，没有关于失败模式的信息。
path: references/phrases.md
anchor: `## Meta-Commentary`
notes:
- 由 references 补全：首轮只有 Quick Checks 里的一条 `Meta-joiners ("The rest of this essay...")`，十一条词表在 `references/phrases.md` 的 `## Meta-Commentary` 一节。补全后本条的范围比首轮理解的宽：它不只是"交代结构的连接句"，还包括 `Plot twist:`、`X is a feature, not a bug`、`Dressed up as` 这类对自己的行文发议论的插话，rule_summary 已按上游改写。
- intent: 上游给了这一节的理由 "Remove self-referential asides. The essay should move, not announce its own structure."，Quick Checks 里的修法 "Delete. Let the essay move." 是同一句话的第二次出现。作者认为交代结构的句子把文章停住了，读者需要的是往前走而不是被告知路线。
- existing: 疑似对应 EN-P-007（其中 `in this article we will explore`、`let me walk you through` 与上游词表的第九、第八条对应）；但 EN-P-007 的定位是"清嗓子式开场"，本条管的是任意位置的自指插话，位置不同，且 `Plot twist:`、`Hint:`、`X is a feature, not a bug` 三条现有词表里没有。
- 与 U-ssl-001 的区别：U-ssl-001 是开头的清嗓子，本条可以出现在任何位置且明确指向"文章自身"。

### U-ssl-022
category: process
language: both
rule_summary: 交付任何文字之前，必须逐项跑完一份固定的检查清单（十二项 Quick Checks），不靠通读一遍的整体印象代替。
positive: 交付前逐项过一遍：副词、被动、无生命施事、Wh- 句首、清嗓子、二元对比、连续同长句、段尾单句、破折号、泛泛断言、疏离旁白、元连接句，每项给一个是或否。
negative: 改完通读一遍，觉得"读着挺顺"就交付。违反点：没有逐项核对清单，用整体印象代替了逐项判定。
path: SKILL.md
anchor: `## Quick Checks / Before delivering prose:`
notes:
- 本条的规则文本只在 SKILL.md 里，path 保持 `SKILL.md`。三份 references 里没有任何流程性内容——它们全是词表和模式表，不规定什么时候查、查几遍。
- intent: 上游未说明。推断：把八条 Core Rules 重新写成十二个可以回答是或否的问句，并冠以 "Before delivering prose:"，作者的意图是把规则从"写作时的心法"转成"交付前的检查表"——因为原则在生成过程中会被忘掉，检查表不会。推断依据是 Quick Checks 一节的内容与 Core Rules 大量重复，唯一的新增价值就是它的形式（问句）和位置（交付前）。
- existing: 疑似对应 ALL-PROC-014。
- 本单元管的是"必须跑清单"这件事；清单里每一项的具体判据各自归属对应的模式单元，见覆盖表。

### U-ssl-023
category: measurement
language: both
rule_summary: 交付前按五个维度各打 1 到 10 分自评：Directness（是陈述还是宣告）、Rhythm（有变化还是节拍器式）、Trust（尊不尊重读者的判断力）、Authenticity（听起来像不像人写的）、Density（还有没有可删的）。
positive: 给出 Directness 7 / Rhythm 5 / Trust 8 / Authenticity 6 / Density 7，合计 33。
negative: 只给一句"整体质量不错，大概 8 分"。违反点：没有按五个维度分别取值，用一个笼统的总印象代替了分维度评分。
path: SKILL.md
anchor: `## Scoring / Rate 1-10 on each dimension:`
notes:
- 本条的规则文本只在 SKILL.md 里，path 保持 `SKILL.md`；references 里没有评分相关内容。
- intent: 上游未说明。推断：五个维度是作者对"什么是 AI 味"的完整回答——他认为它可以拆成五个互相独立的失败方向，而不是一个整体感受；表里每个维度都配了一个问句而不是一个形容词，说明作者要的是可回答而不是可描述。推断依据是表格的两列结构（Dimension / Question）。
- existing: 疑似对应 ALL-M-006（现有决定为 reference-only）；与 ALL-M-005（rejected，反对给文本算一个总分）部分冲突——ALL-M-005 拒绝的是"算一个 0-100 的 AI 味分数并按分段给判语"，本条是五个分维度取值，不是单一总分，冲突落在 U-ssl-024 的合计门槛上而不是这里。
- 五个维度共用同一条判定逻辑（每个维度取一个 1-10 的值），合为一个单元，维度表放进正反例。

### U-ssl-024
category: measurement
language: both
rule_summary: 五维合计低于 35/50 时必须再改一轮，不得直接交付。
positive: 合计 33，低于门槛，重新改一轮再评。
negative: 合计 31，作者判断"够用了"，直接交付。违反点：合计低于 35 却没有再改一轮。
path: SKILL.md
anchor: `## Scoring / Below 35/50: revise.`
notes:
- 本条的规则文本只在 SKILL.md 里，path 保持 `SKILL.md`。
- intent: 上游未说明。推断：给出一个硬数字门槛而不是"分数偏低就改"，是为了让"要不要再改一轮"这件事不再依赖判断；35/50 等于每个维度平均 7 分，作者把及格线定在了"每一项都明显好于中等"。推断依据是门槛数值与维度数量的关系。
- existing: 疑似对应 ALL-M-005（rejected）与 ALL-PROC-019（最多三轮迭代）。ALL-M-005 拒绝的理由是"按公式给文本算一个分数并按分段给判语"，本条正是这种做法的一个实例，归并时大概率同样处理；但本条的分数不用于对外判语、只用于决定要不要再改一轮，这个区别值得在裁决理由里点明。
- 与 U-ssl-023 拆开的理由：U-ssl-023 是"怎么取值"，本条是"取到什么值该怎么办"，判定逻辑不同——一份稿子可以完成评分却不执行门槛。

### U-ssl-025
category: pattern
language: en
rule_summary: 企业黑话换成大白话，上游给出十一组替换：Navigate (challenges) 换成 handle 或 address、Unpack (analysis) 换成 explain 或 examine、Lean into 换成 accept 或 embrace、Landscape (context) 换成 situation 或 field、Game-changer 换成 significant 或 important、Double down 换成 commit 或 increase、Deep dive 换成 analysis 或 examination、Take a step back 换成 reconsider、Moving forward 换成 next 或 from now、Circle back 换成 return to 或 revisit、On the same page 换成 aligned 或 agreed。
positive: Next quarter we increase the retry budget, and both teams agree on the target.
negative: Moving forward, we'll double down on the retry budget and circle back once both teams are on the same page. 违反点：`Moving forward`、`double down`、`circle back`、`on the same page` 是替换表里的四条企业黑话，各自都有一个更短的日常说法。
path: references/phrases.md
anchor: `## Business Jargon`
notes:
- 新增单元：`references/phrases.md` 的 `## Business Jargon` 一节，SKILL.md 完全没有提到这一类。SKILL.md 的 Core Rules 第 1 条只点名了 throat-clearing openers、emphasis crutches 和 adverbs 三类，企业黑话不在其中。
- intent: 上游给了这一节的修法 "Replace with plain language."，并给每一条都配了一到两个平实的替代词。推断作者的理由：这些词的共同点是它们都有一个更短的日常说法，用长的那个不增加信息，只增加一层职场语域。推断依据是替换表的每一行右列都比左列短且更常见。
- existing: 疑似对应 EN-P-001（其词表含 game changer）与 EN-M-001（其第一档含 in today's landscape）；其余九条企业黑话现有词表里没有，其中 Circle back、On the same page、Take a step back、Double down、Moving forward 五条是英文职场用语，现有规则完全没有覆盖这一类。
- 十一行共用同一条判定逻辑（这个说法有没有一个更平实的等价说法），合为一个单元，替换表放进正反例。上游给了替换建议但没有给任何一行写例外，按 extraction.md 的判据不逐条拆。

### U-ssl-026
category: style-opinion
language: en
rule_summary: 除副词之外，软化语、强化语和保留语一律不留（"No softeners, no intensifiers, no hedges."）；判据是这个词在做软化、加强或保留的活，不看它是不是副词，因此像 "most"、"some" 这类限定词也在范围内。
positive: Teams struggle with alignment.
negative: Most teams struggle with alignment, at least to some extent. 违反点：`Most`、`to some extent` 都不是副词，但都在软化这句话的范围，按本条一并删掉。
path: references/phrases.md
anchor: `## Adverbs / No softeners, no intensifiers, no hedges.`
notes:
- 新增单元：`references/phrases.md` 的 `## Adverbs` 一节末句。这一句与 U-ssl-003 同在一行（`Kill all adverbs. No -ly words. No softeners, no intensifiers, no hedges.`），但判据不同：前半看词形（是不是副词），后半看功能（这个词在不在软化、加强、保留），后半能命中不是副词的词。因为共用一行，anchor 用的是该行的后半段原文而不是行首文本，这是本清单里唯一一处这样处理的 anchor，理由是行首文本已被 U-ssl-003 占用，两条必须分得开。
- 从示例反推：本条的判定边界是从 `references/examples.md` 的 Example 2 反推出来的——那一组的 Changes 一行写 "Cut hedging ('most')"，被删的 `most` 是限定词不是副词，说明 "No ... hedges" 这一句的适用范围确实超出副词。上游没有为这一句给过词表或例子，Example 2 是全部四份文件里唯一一处演示。
- intent: 上游未单独说明这一句的理由。推断：作者把三种功能词并列在副词禁令之后，是因为它们与副词共享同一个问题——都在替内容调音量而不增加内容。推断依据是这一句紧跟 "Kill all adverbs."，且 structures.md 给副词标的问题是 "Empty emphasis"。
- existing: 疑似对应 EN-P-003（副词）、EN-P-029（堆叠保留语）与 EN-P-030（与语气自相矛盾的保留语）；三条现有规则都保留"原文真实表达的不确定不动"这个例外，本条不留。**与 ALL-PROT-004（不得把原文表达的不确定说成确定）直接冲突**：删掉 "most"、"to some extent" 会把一个有范围的主张变成全称主张，这正是 ALL-PROT-004 禁止的。按 criteria.md 第 1 条，归并时 protection 优先。
- 强风格主张（无例外禁令），按 criteria.md 第 4 条记 style-opinion。

### U-ssl-027
category: pattern
language: en
rule_summary: 删掉七条固定的填充短语："At its core"、"In today's [X]"、"It's worth noting"、"At the end of the day"、"When it comes to"、"In a world where"、"The reality is"。
positive: The retry loop fires before the health check.
negative: At the end of the day, when it comes to reliability, the reality is that the retry loop fires first. 违反点：`At the end of the day`、`when it comes to`、`the reality is` 是词表里的三条，三处都不承载信息，删掉后句子完整。
path: references/phrases.md
anchor: `## Adverbs / Also cut these filler phrases:`
notes:
- 新增单元：`references/phrases.md` 的 `## Adverbs` 一节里 "Also cut these filler phrases:" 之下的七条。这七条既不是副词（U-ssl-003）也不是软化语（U-ssl-026），上游用 "Also" 把它们挂在副词一节下面，但它们是一份独立的短语表，判定逻辑是"这个短语整体不承载信息"。SKILL.md 里没有这份表。
- intent: 上游未说明理由，只给了 "Also cut these filler phrases:" 这一句引导。推断：这七条的共同点是它们都是可以放在任意句子前面而不改变句意的开场垫片。推断依据是七条里有六条都是从句式的句首状语。
- existing: **强对应 EN-P-004**：EN-P-004 的词表已含 it's worth noting、at the end of the day、when it comes to、at its core、in today's world、the reality is 六条，与上游七条重合六条；只有 "In a world where" 现有词表里没有（ZH-P-004 的"在当今……的时代"是中文的对应形式）。归并时本单元大概率作为 EN-P-004 的一条追加证据，不新立规则。
- 七条共用同一条判定逻辑，合为一个单元，词表放进正反例。
- `## Adverbs` 一节被三个单元共用（U-ssl-003、U-ssl-026、U-ssl-027），三条的 anchor 各带自己那一行的原文。

### U-ssl-028
category: pattern
language: en
rule_summary: 删掉表演式亲密（performative emphasis）——制造出来的真诚感和虚假的亲近，上游给出的三条为 "creeps in"、"I promise"、"They exist, I promise"。
positive: Three of the five services time out at 30 seconds.
negative: The bug creeps in around the third retry. These cases are real, I promise. 违反点：`creeps in`、`I promise` 是词表里的两条，前者给一个技术现象套上潜行的拟人姿态，后者用作者的人格担保替代证据。
path: references/phrases.md
anchor: `## Performative Emphasis`
notes:
- 新增单元：`references/phrases.md` 的 `## Performative Emphasis` 一节，SKILL.md 完全没有提到这一类。
- intent: 上游给了这一节的定义 "False intimacy or manufactured sincerity:"。推断作者的判据：这三条的共同点是它们都在用作者与读者的关系替代内容——"I promise" 拿人格作保，"creeps in" 拿拟人化制造在场感。推断依据是这一节的标题（Performative）和定义句里的两个形容词（False、manufactured）。
- existing: 现有规则里没有。EN-P-007 的词表里有 `I'll be honest`，方向接近（拿真诚作保），但 EN-P-007 管的是清嗓子式开场，管不到句中的 "I promise"；ALL-P-004 管的是无生命事物做人的动作，`creeps in` 属于这一类的边缘，但 ALL-P-004 的判据是"抹掉了施事者"，`creeps in` 的问题不是抹掉施事者而是加了拟人色彩。
- 三条共用同一条判定逻辑（这句话是不是在用作者的姿态替代内容），合为一个单元。
- 本单元是补拆之后最小的一个词表（三条），且其中两条是同一条的两种长度（"I promise" 与 "They exist, I promise"），实际只有两种形式。

### U-ssl-029
category: pattern
language: en
rule_summary: 不宣布难度或意义，把它演出来（telling instead of showing）；上游给出的四条为 "This is genuinely hard"、"This is what leadership actually looks like"、"This is what X actually looks like"、"actually matters"。
positive: The team rewrote the scheduler three times and still missed the deadline by six weeks.
negative: This is genuinely hard. This is what leadership actually looks like. 违反点：两句都在词表里，都在宣布一件事有难度或有意义，而没有给出任何让读者自己得出这个结论的材料。
path: references/phrases.md
anchor: `## Telling Instead of Showing`
notes:
- 新增单元：`references/phrases.md` 的 `## Telling Instead of Showing` 一节，SKILL.md 完全没有提到这一类。
- intent: 上游给了这一节的定义 "Announcing difficulty or significance rather than demonstrating it:"。判据写在定义句里：宣布（announce）与演示（demonstrate）的对立。这与 Scoring 表 Trust 维度（"Respects reader intelligence?"）方向一致——宣布意味着不相信读者能自己看出来。
- existing: 疑似对应 EN-P-022（不给内容贴"重要""惊人"的标签）与 EN-P-008（删掉故作洞见的铺垫）；四条具体词形现有词表里没有。
- 与 U-ssl-002 的边界：`This matters because` 在 `## Emphasis Crutches`（U-ssl-002），`actually matters` 在本节，两个短语词形接近但上游分在两节。本清单按上游的归属拆，这个划分在归并时可能需要合并，记在第 4 节。
- 四条共用同一条判定逻辑，合为一个单元；其中第二、第三条是同一个骨架的实例和模板（"This is what [X] actually looks like"）。

### U-ssl-030
category: pattern
language: en
rule_summary: 不用 "By the time X, I was Y." 这个叙事模板开场，上游标注的问题是 "Narrative template"。
positive: I joined the team in March; the scheduler had already been rewritten twice.
negative: By the time I joined the team, I was the third person to own the scheduler. 违反点：`By the time X, I was Y.` 是模式表里点名的叙事模板，它把一个普通的时间关系包装成一段个人史的开场。
path: references/structures.md
anchor: `## Formulaic Constructions / | "By the time X, I was Y." | Narrative template |`
notes:
- 新增单元：`references/structures.md` 的 `## Formulaic Constructions` 一节第一行，SKILL.md 完全没有提到这一类。这一节是 structures.md 十一个小节里唯一一个没有引导句和 "Instead:" 修法的，只有一张两行的表。
- intent: 上游只给了两个字的问题命名 "Narrative template"，没有解释。推断：作者反对的是这个句式的可预测性——它是个人叙事文章的固定开场，一旦用上，后面的内容读者已经能猜到形状。推断依据是这一节的标题（Formulaic Constructions）和这两个字的命名。
- existing: 现有规则里没有。EN-P-007 管的是清嗓子式开场，本条管的是一个具体的叙事骨架，两者不是同一条。
- 与同节 U-ssl-031 拆开的理由：这两行不共用判定逻辑——本行看的是一个时间从句加身份陈述的叙事骨架，U-ssl-031 看的是用否定给事物下定义，故一行一个单元。

### U-ssl-031
category: pattern
language: en
rule_summary: 不用 "X that isn't Y" 这种靠否定给事物下定义的说法（上游标注的问题是 "Indirect"），直接给出正面陈述，例如把它写成 "X is broken"。
positive: The retry loop is broken.
negative: We have a retry loop that isn't actually retrying. 违反点：`X that isn't Y` 是模式表里点名的间接说法，靠说明它不是什么来定义它，正面的说法（"the retry loop is broken"）更短也更清楚。
path: references/structures.md
anchor: `## Formulaic Constructions / | "X that isn't Y" | Indirect. Say "X is broken" |`
notes:
- 新增单元：`references/structures.md` 的 `## Formulaic Constructions` 一节第二行，SKILL.md 完全没有提到。
- intent: 上游给了问题命名 "Indirect" 和一个具体的替换示范（Say "X is broken"）。推断：作者反对的是用否定绕开正面判断——写作者知道这东西坏了，却写成"一个不工作的 X"，把判断藏进定语。推断依据是修法直接给出了那个被回避掉的正面判断。
- existing: 疑似对应 EN-P-006（二元对比）与 EN-P-024（其中的 not a X but a Y 骨架）；但 EN-P-006 管的是"先否定一个说法再给出另一个"的双句式，本条是单个名词短语内部的否定定语，判据不同。
- 与 U-ssl-004 的区别：U-ssl-004 的模式表里每一条都有 X 和 Y 两个并列的说法，本条只有一个 X 和一个被否定的属性，没有第二个说法。

### U-ssl-032
category: style-opinion
language: en
rule_summary: 段落不以 "So" 开头，改成从内容开始。
positive: The scheduler retries three times before it gives up.
negative: So the scheduler retries three times before it gives up. 违反点：段落以 `So` 开头，这个词不承载信息，只是把段落挂到上一段的语气上。
path: references/structures.md
anchor: `## Sentence Starters to Avoid / | Paragraphs starting with "So" | Start with content |`
notes:
- 新增单元：`references/structures.md` 的 `## Sentence Starters to Avoid` 一节第二行，SKILL.md 完全没有提到（SKILL.md 的 Quick Checks 只有 Wh- 词那一条）。
- intent: 上游只给了修法 "Start with content"，没有解释。推断：与同节的 Wh- 条同源——作者反对的是段落开头被一个不承载信息的词占掉。这一节的总结句 "Wh- openers become a crutch." 说的是 Wh- 词，但 "crutch"（拐杖）这个比喻同样解释了本条。推断依据是三行同在一节且修法方向一致（把开头让给内容）。
- existing: 现有规则里没有。EN-P-004 的词表里没有 So；EN-P-007 管的是成句的清嗓子式开场，管不到单个连接词。
- 强风格主张：段落开头的 "So" 在口语化写作和技术讲解里是正当的话题标记，换个体裁这条就不成立，按 criteria.md 第 4 条记 style-opinion。
- 限定范围是"段落"而不是"句子"（上游左列写的是 Paragraphs），与同节另两行的范围不同，这个限定要保留。

### U-ssl-033
category: style-opinion
language: en
rule_summary: 句子不以 "Look," 开头，直接删掉这个词。
positive: The benchmark only ran on one machine.
negative: Look, the benchmark only ran on one machine. 违反点：句子以 `Look,` 开头，这是一个招呼读者注意的口语标记，删掉后句子的信息一点不少。
path: references/structures.md
anchor: `## Sentence Starters to Avoid / | Sentences starting with "Look," | Remove |`
notes:
- 新增单元：`references/structures.md` 的 `## Sentence Starters to Avoid` 一节第三行，SKILL.md 完全没有提到。
- intent: 上游只给了修法 "Remove"，是这一节三行里唯一一个不给替代方案、直接删的。推断：作者认为这个词没有可替代的功能——它既不是连接词也不是限定词，只是一个把读者拽过来的动作。推断依据是修法只有一个词。
- existing: 疑似对应 EN-P-007（清嗓子式开场），但现有词表里没有 `Look,`。conorbronsdon 的 `### Infomercial engagement hooks` 一节把 "Look," 列为伪坦白语域的开场标记之一，两个来源在这一条上重合。
- 强风格主张：`Look,` 在对话体和意见文章里是作者真实的语气，换个体裁这条就不成立，按 criteria.md 第 4 条记 style-opinion。

### U-ssl-034
category: pattern
language: en
rule_summary: 不把问句和它的答案紧挨着放（questions answered immediately）；修法是让问句留出空间，或者把问句整个删掉。
positive: Caching in Next.js works at three layers.
negative: So how does caching work in Next.js? It works at three layers. 违反点：问句后面紧跟自己的答案，问句没有起到任何作用，属于模式表里的 `Questions answered immediately`。
path: references/structures.md
anchor: `## Rhythm Patterns / | Questions answered immediately | Let questions breathe or cut them |`
notes:
- 新增单元：`references/structures.md` 的 `## Rhythm Patterns` 一节第二行，SKILL.md 完全没有提到。
- intent: 上游只给了修法 "Let questions breathe or cut them"，没有解释。推断：修法给了两个选项，说明作者不反对问句本身，只反对问句与答案之间没有距离——问句的作用是让读者停一下，紧跟答案就取消了这个作用。推断依据是修法里 "breathe" 这个词把问题定位成节奏问题（这一行也确实收在 Rhythm Patterns 一节而不是 Rhetorical Setups 一节）。
- existing: **强对应 EN-P-009**（其判据含"自问自答式的'问题？答案。'"）与 ZH-P-005（中文的"为什么……？因为……"）。两条现有规则都不带"让问句留出空间"这个替代选项，只写了删掉，本条比它们宽一档。
- 与 U-ssl-007 的区别：U-ssl-007 管的是这个句子本身是不是铺垫（"What if [reframe]?"、"Think about it:"），本条管的是问句与答案之间的距离；一个问句可以不是修辞性铺垫却仍然被立刻回答。上游把两者分在两个文件小节里，与这个拆法一致。

### U-ssl-035
category: pattern
language: en
rule_summary: 不用 "Not always. Not perfectly." 这类否定对偶充当坦诚（上游标注的问题是 "Hedging disguised as reassurance"）——它形式上是让步，实际上没有说出任何一个具体的失败场合。
positive: The cache misses on the first request after a deploy, and on any key written in the last 200ms.
negative: The cache works. Not always. Not perfectly. 违反点：`Not always. Not perfectly.` 是模式表里点名的否定对偶，两句都是保留语，没有指出任何一处真实的例外。
path: references/structures.md
anchor: `## Rhythm Patterns / | "Not always. Not perfectly." | Hedging disguised as reassurance |`
notes:
- 新增单元：`references/structures.md` 的 `## Rhythm Patterns` 一节第六行，SKILL.md 完全没有提到。
- intent: 上游给了问题命名 "Hedging disguised as reassurance"，判据写在命名里：形式是让步（看起来在承认局限），实际是保留语（没有承认任何具体的局限）。推断作者反对的原因：这种写法让作者显得诚实而不必付出诚实的代价。推断依据是 "disguised" 这个词。
- existing: 疑似对应 EN-P-030（删掉与句子实际语气自相矛盾的保留语），但 EN-P-030 的判据是"保留语与句子语气矛盾"，本条的判据是"否定对偶充当具体让步"，两者不同；"以否定对偶表演坦诚"这个判据现有规则里没有。conorbronsdon 的 `- **Repeated empty concessions:**` 用的正是同一个例句 "Not always. Not perfectly."，两个来源在这一条上重合，但 conorbronsdon 带 pass condition（孤立出现一次不算），本条不带。
- 与 U-ssl-005（否定式排比）的区别：U-ssl-005 是"罗列不是什么、最后给出是什么"，最后必有一个正面的 Z；本条只有否定，没有那个 Z。
- 与 U-ssl-018（Trust readers）的关系：本条是那条主张里 softening 一项的一个具体形式，上游把它单列为一行模式，故单立单元。

---

## 3 覆盖表

### 3.1 `SKILL.md`

| 小节 / 行 | 归属单元 / 说明 |
|---|---|
| frontmatter（name / description / metadata.trigger / metadata.author） | 非规则内容：技能名称、触发描述、作者署名，供 skill 加载机制使用 |
| `# Stop Slop` 标题与 "Eliminate predictable AI writing patterns from prose." | 非规则内容：总纲一句话，内容被下文各条覆盖 |
| `## Core Rules` 小节标题本身 | 非规则内容：仅为分节标题 |
| 1. **Cut filler phrases.** — throat-clearing openers | U-ssl-001 |
| 1. **Cut filler phrases.** — emphasis crutches | U-ssl-002 |
| 1. **Cut filler phrases.** — all adverbs | U-ssl-003 |
| 1. **Cut filler phrases.** — `See [references/phrases.md]` | 非规则内容：指向本轮已纳入追踪的 `references/phrases.md`，该文件的覆盖见 3.2 |
| 2. **Break formulaic structures.** — binary contrasts | U-ssl-004 |
| 2. **Break formulaic structures.** — negative listings | U-ssl-005 |
| 2. **Break formulaic structures.** — dramatic fragmentation | U-ssl-006 |
| 2. **Break formulaic structures.** — rhetorical setups | U-ssl-007 |
| 2. **Break formulaic structures.** — false agency | U-ssl-008 |
| 2. **Break formulaic structures.** — `See [references/structures.md]` | 非规则内容：指向本轮已纳入追踪的 `references/structures.md`，该文件的覆盖见 3.3 |
| 3. **Use active voice.** — "Every sentence needs a human subject doing something" | U-ssl-009 |
| 3. **Use active voice.** — "No passive constructions" | U-ssl-010 |
| 3. **Use active voice.** — "No inanimate objects performing human actions" | U-ssl-008 |
| 4. **Be specific.** — vague declaratives | U-ssl-011 |
| 4. **Be specific.** — lazy extremes | U-ssl-012 |
| 5. **Put the reader in the room.** — narrator-from-a-distance / "You" beats "People" | U-ssl-013 |
| 5. **Put the reader in the room.** — "Specifics beat abstractions" | U-ssl-011（第 4 条的重述，不另立单元） |
| 6. **Vary rhythm.** — mix sentence lengths | U-ssl-014 |
| 6. **Vary rhythm.** — two items beat three | U-ssl-015 |
| 6. **Vary rhythm.** — end paragraphs differently | U-ssl-016 |
| 6. **Vary rhythm.** — no em dashes | U-ssl-017 |
| 7. **Trust readers.** | U-ssl-018 |
| 8. **Cut quotables.** | U-ssl-019 |
| `## Quick Checks` 小节标题本身 | 非规则内容：仅为分节标题 |
| `Before delivering prose:` | U-ssl-022 |
| - Any adverbs? Kill them. | U-ssl-003 |
| - Any passive voice? Find the actor, make them the subject. | U-ssl-010 |
| - Inanimate thing doing a human verb? Name the person. | U-ssl-008 |
| - Sentence starts with a Wh- word? Restructure it. | U-ssl-020 |
| - Any "here's what/this/that" throat-clearing? Cut to the point. | U-ssl-001 |
| - Any "not X, it's Y" contrasts? State Y directly. | U-ssl-004 |
| - Three consecutive sentences match length? Break one. | U-ssl-014 |
| - Paragraph ends with punchy one-liner? Vary it. | U-ssl-016 |
| - Em-dash anywhere? Remove it. | U-ssl-017 |
| - Vague declarative? Name the specific implication. | U-ssl-011 |
| - Narrator-from-a-distance? Put the reader in the scene. | U-ssl-013 |
| - Meta-joiners? Delete. Let the essay move. | U-ssl-021 |
| `## Scoring` 小节标题本身 | 非规则内容：仅为分节标题 |
| `Rate 1-10 on each dimension:` 与五行维度表 | U-ssl-023 |
| `Below 35/50: revise.` | U-ssl-024 |
| `## Examples` 与 `See [references/examples.md]` | 非规则内容：指向本轮已纳入追踪的 `references/examples.md`，该文件的覆盖见 3.4 |
| `## License` / `MIT` | 非规则内容：许可证声明 |

### 3.2 `references/phrases.md`

| 小节 / 行 | 归属单元 / 说明 |
|---|---|
| `# Phrases to Remove` 标题 | 非规则内容：文件标题 |
| `## Throat-Clearing Openers` 引导句、15 条词表、兜底判据 | U-ssl-001 |
| `## Emphasis Crutches` 引导句与 5 条词表 | U-ssl-002 |
| `## Business Jargon` 引导句与 11 行替换表 | U-ssl-025 |
| `## Adverbs` — "Kill all adverbs. No -ly words." 与 "Specific offenders:" 下的 15 条 | U-ssl-003 |
| `## Adverbs` — "No softeners, no intensifiers, no hedges." | U-ssl-026 |
| `## Adverbs` — "Also cut these filler phrases:" 下的 7 条 | U-ssl-027 |
| `## Meta-Commentary` 引导句与 11 条词表 | U-ssl-021 |
| `## Performative Emphasis` 引导句与 3 条词表 | U-ssl-028 |
| `## Telling Instead of Showing` 引导句与 4 条词表 | U-ssl-029 |
| `## Vague Declaratives` 引导句、5 条词表、兜底判据 | U-ssl-011 |

### 3.3 `references/structures.md`

| 小节 / 行 | 归属单元 / 说明 |
|---|---|
| `# Structures to Avoid` 标题 | 非规则内容：文件标题 |
| `## Binary Contrasts` 引导句、11 行模式表、`**Instead:**` | U-ssl-004 |
| `## Negative Listing` 引导句、2 行模式表、`**Instead:**` | U-ssl-005 |
| `## Dramatic Fragmentation` 引导句、3 行模式表、`**Instead:**` | U-ssl-006 |
| `## Rhetorical Setups` 引导句、4 行模式表、`**Instead:**` | U-ssl-007 |
| `## Formulaic Constructions` — 第 1 行（By the time X, I was Y.） | U-ssl-030 |
| `## Formulaic Constructions` — 第 2 行（X that isn't Y） | U-ssl-031 |
| `## False Agency` 引导段、7 行模式表、`**Instead:**`（含"找不到人就用 you"） | U-ssl-008 |
| `## Narrator-from-a-Distance` 引导句、4 行模式表、`**Instead:**` | U-ssl-013 |
| `## Passive Voice` — 引导句 "Every sentence needs a subject doing something." | U-ssl-009（口径与 SKILL.md 的 "human subject" 不一致，见第 4 节） |
| `## Passive Voice` — "Passive voice hides the actor and drains energy."、4 行模式表、`**Instead:**` | U-ssl-010 |
| `## Sentence Starters to Avoid` — Wh- 词一行与末尾的 "Wh- openers become a crutch." 说明 | U-ssl-020 |
| `## Sentence Starters to Avoid` — Paragraphs starting with "So" 一行 | U-ssl-032 |
| `## Sentence Starters to Avoid` — Sentences starting with "Look," 一行 | U-ssl-033 |
| `## Rhythm Patterns` — Three-item lists 一行 | U-ssl-015 |
| `## Rhythm Patterns` — Questions answered immediately 一行 | U-ssl-034 |
| `## Rhythm Patterns` — Every paragraph ends punchily 一行 | U-ssl-016 |
| `## Rhythm Patterns` — Em-dashes 一行 | U-ssl-017 |
| `## Rhythm Patterns` — Staccato fragmentation 一行 | U-ssl-006 |
| `## Rhythm Patterns` — "Not always. Not perfectly." 一行 | U-ssl-035 |
| `## Word Patterns` — Lazy extremes 一行 | U-ssl-012 |
| `## Word Patterns` — All adverbs 一行 | U-ssl-003 |

### 3.4 `references/examples.md`

| 小节 / 行 | 归属单元 / 说明 |
|---|---|
| `# Before/After Examples` 标题 | 非规则内容：文件标题 |
| `## Example 1: Throat-Clearing + Binary Contrast`（Before / After / Changes） | 示例，不是规则：Before 里的 `Here's the thing:` 演示 U-ssl-001，`Not because X. Because Y.` 演示 U-ssl-004，`Let that sink in.` 演示 U-ssl-002 |
| `## Example 2: Filler + Unnecessary Reassurance`（Before / After / Changes） | 示例：`It turns out`、`The uncomfortable truth is` 演示 U-ssl-001，`And that's okay.` 演示 U-ssl-007；Changes 一行的 "Cut hedging ('most')" 是 **U-ssl-026 的唯一演示**，该单元由此反推 |
| `## Example 3: Business Jargon Stack`（Before / After / Changes） | 示例：`In today's fast-paced landscape`、`lean into`、`navigate` 演示 U-ssl-025，`This matters because` 演示 U-ssl-002 |
| `## Example 4: Dramatic Fragmentation`（Before / After / Changes） | 示例：`That's it. That's the tradeoff.` 演示 U-ssl-006；**该组的 After 文本自身违反 U-ssl-017（用了一处 em dash）并保留了三项并列（U-ssl-015），见第 4 节** |
| `## Example 5: Rhetorical Setup`（Before / After / Changes） | 示例：`What if I told you`、`Here's what I mean:`、`Think about it.` 演示 U-ssl-007；**该组的 After 文本保留了一处 "X, not Y" 的对比结构（U-ssl-004），见第 4 节** |

四份文件的每个小节和每一行模式表都有归属，没有未归属的段落。

---

## 4 拆分时拿不准的地方

1. **三份 references 里没有任何密度或频率判据。**本轮补拆前预期 `structures.md` 会给出"每百字几处"一类的密度口径，实际没有：`## Rhythm Patterns` 一节的六行全是无条件修法（`Em-dashes | Remove. ... No em dashes at all.`、`Three-item lists | Use two items or one`），`phrases.md` 的词表也不带频率。四份文件里唯一的数量判据是 SKILL.md 的 `Three consecutive sentences match length? Break one.`（U-ssl-014）和 `Below 35/50: revise.`（U-ssl-024）。归并时凡是需要频率口径的条目（尤其破折号 U-ssl-017），本来源给不出，只能拿另外两个英文来源的口径比对。

2. **上游自己的示例违反自己的规则，共三处。**（一）`examples.md` Example 4 的 After 是 "Speed, quality, cost—pick two."，用了一处 em dash，直接违反 U-ssl-017 的无条件禁令；（二）同一句保留了三项并列，与 U-ssl-015 的"改成两项或一项"冲突；（三）Example 5 的 After 是 "The best teams optimize for learning, not productivity."，保留了 "X, not Y" 的对比结构，与 U-ssl-004 的"把否定整个丢掉"冲突。三处都在作者自己标为"正确改法"的文本里。这说明作者的实际执行强度低于他写下的规则强度，归并时若采纳 U-ssl-015 或 U-ssl-017 的无条件口径，要在裁决理由里点出上游自己没有执行它。

3. **SKILL.md 与 structures.md 在"主语必须是人"上口径不一致。**SKILL.md 第 3 条写 "Every sentence needs a **human** subject doing something"，`structures.md` 的 `## Passive Voice` 一节写 "Every sentence needs a subject doing something."，少了 human。前者禁止 "The cache stores results."，后者不禁。我按 SKILL.md 的强口径保留了 U-ssl-009，并在该单元 notes 里记了这处差异。归并时如果按 structures.md 的弱口径理解，U-ssl-009 就与 ALL-P-004 完全重合，不构成新规则。

4. **`## Adverbs` 一节里混了三类东西，一行被两个单元共用。**`Kill all adverbs. No -ly words. No softeners, no intensifiers, no hedges.` 这一行前半是词形判据、后半是功能判据，我拆成 U-ssl-003 和 U-ssl-026；同一节下面的 "Also cut these filler phrases:" 又是第三份表（U-ssl-027）。因为一行被两条规则共用，U-ssl-026 的 anchor 用的是该行的后半段原文而不是行首文本，这是本清单里唯一一处这样处理的 anchor。如果归并阶段认为 anchor 必须是行首文本，U-ssl-026 只能与 U-ssl-003 合并，代价是丢掉"软化语和保留语不限于副词"这一层，而那一层正是与 ALL-PROT-004 冲突的地方。

5. **词表条目跨小节、跨来源重复，重复项的归属是我定的。**`It's worth noting` 同时是 `## Adverbs` 的填充短语（U-ssl-027）和 conorbronsdon 的 hollow intensifier；`deep dive`、`unpack`、`landscape`、`game-changer` 在 `## Business Jargon`（U-ssl-025）里，同样出现在 conorbronsdon 的 Tier 1A 表里；`This matters because`（U-ssl-002）与 `actually matters`（U-ssl-029）词形接近但上游分在两节。跨来源的重复归归并处理，本来源内部的两处（U-ssl-002 / U-ssl-029）我按上游的小节归属拆开，如果归并阶段认为它们是同一条，合并时要点明上游把它们分在两节。

6. **category 里 pattern 与 style-opinion 的边界，补拆后仍然按同一个划法。**能指着一个具体的词或句法结构说"这里违反了"的记 pattern，要求一种腔调或人称、换个体裁就不成立的记 style-opinion。按这个划法，U-ssl-003（删所有副词）、U-ssl-010（禁所有被动）、U-ssl-017（禁所有破折号）、U-ssl-026（删所有保留语）、U-ssl-032（段落不以 So 开头）、U-ssl-033（句子不以 Look, 开头）落在 style-opinion，虽然它们的判据比很多 pattern 单元还要形式化。理由是 criteria.md 第 4 条的判据"换一个作者、换一个体裁，这条规则还成立吗"，而不是"能不能圈出来"。这个划法如果归并时不认同，这六条要改成 pattern。

7. **U-ssl-009（每句都要有人作主语）是不是应该并进 U-ssl-008。**两条来自同一条 Core Rule 的同一句话，且在大多数实际文本上会同时命中。我按"能不能构造一个只违反其中一条的例子"分开了（例子写在两条的 notes 里）。补进 structures.md 之后这个问题更突出：那个文件把 false agency 和 passive voice 分成两节，却没有单列"主语必须是人"这一节。如果归并阶段认为这个区分在实际改稿里用不上，可以合并。

8. **U-ssl-019（cut quotables）补拆之后仍然只有一句话。**三份 references 里没有任何一节展开 pull-quote 这一类。上游的判据仍然是 "If it sounds like a pull-quote"，圈不出具体的词或结构，按 criteria.md 第 2 条应记 rejected。我在 notes 里补的形式判据（整句不依赖上下文、结构是 "X is the Y of Z" 或 "X is not A but B"）是我补的，不是上游写的。归并时如果按上游原样裁决，这条应当 rejected；如果按补出来的形式判据裁决，它就与 EN-P-024 重合。

9. **language 全部标 en 是否合适。**新增的十一条全部依赖英文词表或英文句法（企业黑话、Wh- 词、So / Look, 开头、"X that isn't Y"），标 en 没有疑问。但补拆前就存在的问题没变：U-ssl-011（泛泛断言）、U-ssl-012（全称量词）、U-ssl-014（句长变化）、U-ssl-016（段尾形状）、U-ssl-034（问句紧跟答案）的判定逻辑在中文里同样成立。我按"本来源整体是英文散文 skill、且例句全是英文"统一标了 en，只把不含任何语言特征的三条（U-ssl-022 至 U-ssl-024）标 both。如果归并阶段认为后面几条应当标 both，需要为它们补一组中文正反例（extraction.md 禁止把英文例子直译）。

10. **本来源仍然没有任何 protection 规则，补进三份 references 后确认。**四份文件通读两遍：没有"不得编造事实""保留引语代码表格""原文本来就好就别改""先问再改"这类约束，也没有任何模式设定或输出格式要求。按 criteria.md 第 1 条，它的一批 style-opinion 强主张在归并后必须受已有的 protection 规则约束，这一点归并时要显式写进裁决理由，因为本来源自己不带这层约束。**U-ssl-026 是补拆新增的一处直接冲突**：它要求删掉全部保留语，而 ALL-PROT-004 要求保留原文表达的不确定。

11. **U-ssl-028（performative emphasis）的词表只有三条，其中两条是同一句的长短两版。**`"I promise"` 和 `"They exist, I promise"` 实际是同一个形式。这个单元的证据基础比本清单里其他词表单元薄得多，归并时按 criteria.md 第 3 条第 2 项（这条规则说的现象是否真实存在）要单独看。

---

## 5 疑似与现有规则或别的来源重合的单元

### 与现有 144 条规则明确冲突的（归并时按 criteria.md 第 8 条两条都要留痕）

| 单元 | 现有规则 | 冲突点 |
|---|---|---|
| U-ssl-003 | EN-P-003 | 本条删所有副词；EN-P-003 只删不承担强调、不确定、对比或作者语感的副词 |
| U-ssl-010 | ALL-P-004 | 本条禁所有被动；ALL-P-004 只禁隐藏施事者的被动，优先主动语态而非禁止被动 |
| U-ssl-015 | ALL-P-005 | 本条把三项清单改成两项或一项；ALL-P-005 的判据是"该用几项就用几项" |
| U-ssl-017 | EN-P-026 | 本条无条件禁破折号；EN-P-026 按篇幅允许长文留一到两处 |
| U-ssl-024 | ALL-M-005 | 本条按合计分数决定要不要再改；ALL-M-005 已 rejected 了"按公式算分并按分段给判语"的做法 |
| U-ssl-026（新增） | ALL-PROT-004 | 本条删掉全部软化语和保留语（含 most、to some extent）；ALL-PROT-004 要求保留原文表达的不确定。按 criteria.md 第 1 条 protection 优先 |

### 现有规则里没有对应的单元

- U-ssl-012（every / always / never / everyone / everybody / nobody 当含糊用）
- U-ssl-016（每段都以短促单句收尾这个具体判据）
- U-ssl-020（句子不以 Wh- 词开头）
- U-ssl-025（新增，企业黑话替换表里除 game-changer 外的十条）
- U-ssl-028（新增，表演式亲密）
- U-ssl-030（新增，"By the time X, I was Y." 叙事模板）
- U-ssl-032（新增，段落不以 So 开头）
- U-ssl-035（新增，以否定对偶表演坦诚）

### 补拆后确认与现有规则强对应、大概率不新立规则的单元

- U-ssl-027（七条填充短语）与 EN-P-004 重合六条
- U-ssl-034（问句紧跟答案）与 EN-P-009、ZH-P-005 判据一致
- U-ssl-005（否定式排比）的两行模式与 EN-P-006 的 `Not a X. Not a Y. A Z.` 词形一致
- U-ssl-006（戏剧化碎片）的两行模式与 EN-P-025 的两个例子词形一致
- U-ssl-008（false agency）的模式表第三、六、七行与 ALL-P-004 的三个例子一一对应

### 与本轮另两个英文来源大概率聚成一类的单元

- U-ssl-001 / U-ssl-021 ↔ blader §28（announcing the next point）、conorbronsdon 的 "Let's" transition openers 与 formulaic openings
- U-ssl-004 / U-ssl-005 ↔ blader §9、conorbronsdon 的 `"It's not X — it's Y"` 一节（补拆后可比的模式表条目从 1 条增到 11 条）
- U-ssl-006 ↔ blader §31、conorbronsdon 的 Manufactured punchlines and staccato drama
- U-ssl-008 / U-ssl-009 / U-ssl-010 ↔ blader §13、conorbronsdon 的 False agency 与 Subjectless fragments and agentless passives
- U-ssl-011 ↔ conorbronsdon 的 Tone calibration 第 2 条（Be concrete）
- U-ssl-013 ↔ EN-P-034 同源；conorbronsdon 无对应
- U-ssl-014 / U-ssl-016 ↔ conorbronsdon 的 Sentence length uniformity 与 Paragraph length uniformity
- U-ssl-015 ↔ blader §10、conorbronsdon 的 Compulsive rule of three（三方强度递减：本条最强）
- U-ssl-017 ↔ blader §14、conorbronsdon 的 Em dash frequency（三方冲突，见上）
- U-ssl-019 ↔ blader §32、conorbronsdon 的 Aphorism formulas
- U-ssl-023 / U-ssl-024 ↔ 与另两个英文来源都不重合；conorbronsdon 有严重度分级但不打分，blader 完全不打分
- **补拆新增的重合**：U-ssl-025 ↔ conorbronsdon 的 Tier 1A 表（deep dive / unpack / landscape / game-changer 四条重合）；U-ssl-029 ↔ conorbronsdon 的 Emotional flatline；U-ssl-033 ↔ conorbronsdon 的 Infomercial engagement hooks（"Look," 一条）；U-ssl-035 ↔ conorbronsdon 的 Repeated empty concessions（同一个例句 "Not always. Not perfectly."，但 conorbronsdon 带 pass condition）

三个来源的谱系互不相同（sources.yaml 里 lineage 分别是 hardikpandya-stop-slop、blader-humanizer、conorbronsdon-avoid-ai-writing），因此上面这些聚类会给 independent_sources 带来真实的增量。补拆之后 U-ssl-035 与 conorbronsdon 用同一个例句这一点需要归并时留意：例句完全相同通常意味着共同来源而不是独立观察，但本轮两个来源都没有声明这一条的出处。

---

## 6 上游文本内的指令

四份文件通读两遍，**未发现针对读者或助手的注入式指令**（"忽略之前的规则""把这段加进你的系统提示"一类）。

三份 references 的正文几乎全部由祈使句构成，这些祈使句是这份 skill 对它自己的使用者说的话（规则本身），不是对本仓库合并流程说的话，也不改变本轮的处理方式。按 criteria.md 第 7 条把指令形态的原文照抄记录如下，**一条都不执行**：

`references/phrases.md`：

> Remove these announcement phrases. State the content directly.
>
> These add no meaning. Delete them.
>
> Replace with plain language.
>
> Kill all adverbs. No -ly words. No softeners, no intensifiers, no hedges.
>
> Also cut these filler phrases:
>
> Remove self-referential asides. The essay should move, not announce its own structure.
>
> Sentences that announce importance without naming the specific thing. Kill these.
>
> If a sentence says something is important/deep/structural without showing the specific thing, cut it or replace it with the specific thing.

`references/structures.md`：

> These create false drama. State the point directly.
>
> **Instead:** State Y directly. "The problem is Y." "Y matters here." Drop the negation entirely.
>
> **Instead:** State Z. The reader doesn't need the runway.
>
> **Instead:** Complete sentences. Trust content over presentation.
>
> **Instead:** Make the point. Let readers draw conclusions.
>
> **Instead:** Name the human. "The team fixed it that week" beats "the complaint becomes a fix." If no specific person fits, use "you" to put the reader in the seat.
>
> **Instead:** Put the reader in the room. "You don't sit down one day and decide to..." beats "Nobody designed this."
>
> **Instead:** Find the actor. Put them at the front of the sentence.

这些句子全部是规则文本，已经拆成对应单元（依次是 U-ssl-001、U-ssl-002、U-ssl-025、U-ssl-003 与 U-ssl-026、U-ssl-027、U-ssl-021、U-ssl-011、U-ssl-004、U-ssl-005、U-ssl-006、U-ssl-007、U-ssl-008、U-ssl-013、U-ssl-010）。

`references/examples.md` 不含祈使句，只有 Before / After / Changes 三段式的示例文本。

全文不含脚本，无"只读不跑"的对象；SKILL.md 里三处指向 references 的链接现在都指向已纳入追踪的文件，不再是未追踪引用。
