# 拆规则清单：upstream-blader-humanizer

## 1 来源摘要

- 文件（本仓库快照）：`merges/maybe-humanizer/snapshots/upstream-blader-humanizer/SKILL.source.md`
- 上游原路径：`SKILL.md`
- 上游仓库：`blader/humanizer`，分支 `main`
- commit（取自 sources.lock.json 的 last_seen_commit）：`e2e92e7b4b8229253ed5c8e81dc65463fdeddda5`
- 许可证：MIT（frontmatter 里也自写 `license: MIT`），snapshot_policy 为 full-text，可引原文并标"引自上游"
- 规模：456 行，30409 字节；frontmatter 自写 `metadata.version: "2.11.2"`；sources.lock.json 记录的 stars 为 43894、forks 为 3670
- 谱系地位：sources.yaml 记它为 `blader-humanizer` 谱系的 representative，是 op7418/Humanizer-zh、hairyf/skills、kevintsai1202/Humanizer-zh-TW、z0gSh1u/oh-my-writing-skill 四个中文与繁体版本的英文根节点
- 上游自述的定位：frontmatter 的 description 写 "Rewrite AI-sounding text so it reads naturally without changing what it says... Based on Wikipedia's 'Signs of AI writing.'"；正文第 15 行写 "Rewrite AI-sounding text so it reads like the writer, not a chatbot. Do not change what it says or make up details."。全文结构是：四条总则、样本匹配、个性边界、35 条编号模式（分成 Content / Language and grammar / Style / Chatbot / Filler and hedging 五组）、一节假阳性防护（What not to flag 与 Human details to keep）、三种返回方式、四步改写流程、出处声明。
- 上游的出处自述：第 17 行和第 452 至 456 行两次声明模式来自 [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)（由 WikiProject AI Cleanup 维护），并引用了 Wikipedia 的主要论点："LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."
- 总单元数：77（U-bld-001 至 U-bld-077）
- 按 category 计数与 language 计数：见第 1.2 节
- 未追踪内容：本来源只有一个文件，没有 references、没有脚本，追踪范围完整。

### 1.1 哪些模式是 Wikipedia 原有的，哪些是作者补的

任务要求点出这一区分（blader 与 upstream-aboudjem-humanizer-skill 都自述基于同一篇 Wikipedia 文章，归并判断 independent_sources 时要用）。

**判断依据**：本仓库快照 `merges/maybe-humanizer/snapshots/upstream-aboudjem-humanizer-skill/skills/humanizer/references/patterns.md` 里有一节 `## Coverage against Wikipedia: Signs of AI writing`，逐条列出了 Wikipedia 指南记载的每个信号对应 aboudjem 的哪个模式编号；同一份文件的 `## The craft and forensic set (P44-P55)` 一节明确写了 P44 至 P55 这十二条是 "novel relative to the P1-P43 set"，即不来自 Wikipedia。我用这两处作为判断基准，把 blader 的 35 条模式逐条对上去。**我没有读 Wikipedia 原文**，因此下面的划分是基于第三方（aboudjem）的对照表作出的推断，不是对 Wikipedia 的直接核对。有疑问的条目单独标出。

**来自 Wikipedia 的（21 条模式，对应 24 个单元）**：

| blader 小节 | 单元 | Wikipedia 侧的对应信号（据 aboudjem 覆盖表） |
|---|---|---|
| §1 Inflated claims | U-bld-015 | significance inflation |
| §2 Name-dropping | U-bld-016、U-bld-017 | notability over-attribution |
| §3 Shallow -ing phrases | U-bld-018 | superficial -ing |
| §4 Sales language | U-bld-019 | promotional tone |
| §5 Vague sources | U-bld-020、U-bld-021 | weasel / vague attribution；exaggerated source quantity |
| §6 Formulaic challenges | U-bld-022、U-bld-023 | formulaic "challenges" |
| §7 Overused AI words | U-bld-024 | AI vocabulary |
| §8 Avoiding is and are | U-bld-025 | copula avoidance |
| §9 Not X but Y | U-bld-026 | negative parallelisms（覆盖表写"all three variants"） |
| §10 Forced groups of three | U-bld-028 | rule of three |
| §11 前半 Changing names | U-bld-029 | elegant variation |
| §14 Em and en dashes | U-bld-034、U-bld-035 | em dashes |
| §15 Too much bold | U-bld-036 | boldface overuse |
| §16 Lists with bold mini-headings | U-bld-037 | inline-header lists |
| §17 Title case in headings | U-bld-038 | title case headings |
| §18 Emojis | U-bld-039 | emoji-as-formatting |
| §19 Curly quotation marks | U-bld-040 | curly quotes |
| §20 Chatbot text left in the answer | U-bld-041 | collaborative / conversational language |
| §21 前半 Knowledge-limit disclaimers | U-bld-042 | knowledge-cutoff disclaimers |
| `### What not to flag` | U-bld-060、U-bld-064 | "detectors are unreliable, do not judge on one tell" caution |
| `### Human details to keep` | U-bld-065、U-bld-066 | human-writing positive indicators（含 predating Nov 2022） |

**作者补的（14 条模式，对应 25 个单元）**：§11 后半 repeating sentence openings（U-bld-030、U-bld-031）、§12 False from X to Y ranges（U-bld-032）、§13 Passive voice and missing subjects（U-bld-033）、§23 Filler phrases（U-bld-045）、§24 Too many qualifiers（U-bld-046）、§25 Generic positive endings（U-bld-047）、§26 Too many hyphenated word pairs（U-bld-048）、§27 Pretending to reveal a deeper truth（U-bld-049）、§28 Announcing the next point（U-bld-050）、§29 A heading repeated in the first sentence（U-bld-051）、§30 Writing about the previous version（U-bld-052）、§31 Forced punchlines and dramatic fragments（U-bld-053）、§32 Formulaic sayings（U-bld-054）、§33 Fake-candid openings（U-bld-055）、§34 Answering objections no one raised（U-bld-056、U-bld-057）、§35 Rejecting fake alternatives（U-bld-058、U-bld-059、U-bld-063）。

其中 §13、§24、§26、§30、§32、§34、§35 在 aboudjem 的编号体系里分别落在 P50、P55、P47、P46、P48、P54、P54/P55，全部属于 aboudjem 自述 "novel relative to the P1-P43 set" 的 craft set，这是它们不来自 Wikipedia 的正面证据；其余几条（§12、§23、§25、§27、§28、§29、§31、§33）是因为不出现在覆盖表里而判为作者补的，属于反面证据，强度较弱。

**归属存疑的三条**：

- §9 后半 clipped negative endings（U-bld-027）：覆盖表写 negative parallelisms 有 "all three variants"，但没有列出是哪三个变体，句尾截断式否定（"no guessing"）是否算其中之一无法确定。
- §21 后半 speculative gap-fill（U-bld-043）：覆盖表只映射了 knowledge-cutoff disclaimers，没有提"找不到来源就用猜测填空"。可能属于 Wikipedia 的同一节，也可能是作者补的。
- §22 Overly agreeable tone（U-bld-044）：覆盖表把 "collaborative/conversational language" 映射到 aboudjem 的 P19、P32，谄媚（"Great question!"）是否包含在内无法确定。

**归并时的用法**：blader 与 aboudjem 在上面第一张表里的条目上不构成两个独立来源——它们各自从同一篇 Wikipedia 文章抄下来，independent_sources 应当只算一个 Wikipedia 谱系；第二张表里的 14 条模式，blader 与 aboudjem 是各自独立提出的（aboudjem 的 craft set 自述为独立撰写），可以算两个独立来源。

### 1.2 计数

- 按 category 计数：
  - pattern：37
  - protection：16
  - process：15
  - measurement：5
  - style-opinion：2
  - genre：2
- 按 language 计数：
  - en：53
  - both：24
  - zh：0

以下所有单元的 `source` 字段均为：

```
type: upstream
source_id: upstream-blader-humanizer
path: SKILL.md
commit: e2e92e7b4b8229253ed5c8e81dc65463fdeddda5
```

下面每条只写 anchor，其余 source 字段不再重复。

---

## 2 单元清单

### 2.1 四条总则（`## What to do`）

### U-bld-001
category: process
language: both
rule_summary: 拿到要改的文字，先拿全文对照模式表逐条检查一遍，找出命中的模式，再动手改。
positive: 先通读全文，逐条对照 35 条模式标出命中的位置，再开始改写。
negative: 一边读一边随手改，改完也没有对照过模式表。违反点：跳过了"先找模式"这一步，改动依据是随手的语感而不是模式表。
anchor: `## What to do / 1. **Find AI patterns.**`
notes:
- intent: 上游未单独说明这一步的理由。推断：把"找"和"改"拆成两个动作，是为了让改动有一个可以复查的依据——找出来的模式是一份清单，随手改出来的东西没有清单。推断依据是 `## Rewrite process` 一节把同一件事又写了一遍（第一步"读原文并标出每一处 AI 模式"），且这两处都把标记放在改写之前。
- existing: 疑似对应 ALL-PROC-009（先通读全文再动手）与 ALL-PROC-028（判断算不算命中以 references 为准）。
- Wikipedia 归属：不适用（这是流程，不是模式）。

### U-bld-002
category: protection
language: both
rule_summary: 每一条主张都要保住：可以缩短乏味的部分、扩展有用的部分、合并或拆分段落，但结构改了之后信息一条都不能少。
positive: 把三段合成一段，原来三段里的每个事实在新段落里都还在。
negative: 为了让文字更紧凑，把一段里的两个次要事实一起删了。违反点：改结构的同时丢掉了原文的信息，而本条允许改结构、不允许丢信息。
anchor: `## What to do / 2. **Keep every claim.**`
notes:
- intent: 上游把授权和约束写在同一条里——"You may shorten dull parts, expand useful parts, and merge or split paragraphs. Keep the information even when you change the structure."。它防的是一种常见的混淆：把"允许重排"理解成"允许取舍"。作者的立场是结构可以动，内容不可以。
- existing: 疑似对应 ALL-PROT-003（不得默认做摘要式压缩）。
- Wikipedia 归属：不适用（总则，不是模式）。

### U-bld-003
category: protection
language: both
rule_summary: 不得添加事实、名字、数字、日期、引语或引用，除非它来自原文或用户。
positive: 原文没有给出成立年份，改写稿也不写年份。
negative: 原文写 "founded in the 1990s"，改写稿写成 "founded in 1994"。违反点：新增了一个原文没有的具体年份。
anchor: `## What to do / 3. **Do not invent facts.**`
notes:
- intent: 作者把这条放在四条总则的第三位，并在正文第 15 行的总纲里就先写了一遍（"Do not change what it says or make up details."）。它防的是这类工具最容易造成的实质损害：改写读起来更好了，但里面多了一件原文没说过的事。同一条禁令在 §2、§5、§6 和 `## Rewrite process` 第三步共出现五次，是全文重复次数最多的规则。
- existing: 疑似对应 ALL-PROT-001。
- Wikipedia 归属：不适用（总则）。

### U-bld-004
category: process
language: both
rule_summary: 一句话需要一个原文没有的细节时，要么去向用户要这个细节，要么改用一句不需要这个细节的更简单的句子。
positive: "这句需要一个具体日期，原文没有，你能补一个吗？"或者直接改写成不含日期的说法。
negative: 原文没有日期，改写稿写了一个看着合理的日期。违反点：既没有去问，也没有改用不需要日期的说法，而是自己填了一个。
anchor: `## What to do / 3. **Do not invent facts.**`
notes:
- intent: 上游把这一句紧接在禁令之后——"If a sentence needs a missing detail, ask for it or use a simpler sentence."。它的作用是给禁令配一个出路：只写"不许编"，遇到确实缺细节的句子就会卡住，所以作者明确给了两个合法动作。
- existing: 疑似对应 ALL-PROC-004（缺失部分影响事实时先问用户）与 ALL-PROT-001。
- 与 U-bld-003 拆开的理由：U-bld-003 是禁令，本条是禁令触发时的处置方式，一份改写可以遵守禁令却在遇到缺口时直接卡住不做处理。

### U-bld-005
category: protection
language: both
rule_summary: 作者的声口需要时可以加入一个观点或一句反应，但不得加入事实主张。
positive: 原文语气本来就带情绪，改写时保留或补上一句反应，但不添加任何新的事实。
negative: 改写时加了一句 "This is the fastest approach available today."。违反点：这是一个可以为真为假的事实主张，不是观点或反应。
anchor: `## What to do / 3. **Do not invent facts.**`
notes:
- intent: 作者在禁令里划了一条界线——"You may add an opinion or reaction when the writer's voice calls for one, but you may not add a factual claim."。他区分的是能不能被核对：观点不可核对，因此加进去不会让文本失真；事实主张可核对，加进去就是引入了一个没有出处的断言。
- existing: **与 ALL-PROT-001 冲突**：现有规则明确禁止新增"观点"（"不得新增原文没有的事实、数字、日期、例子、论据、观点或来源"），本条允许在声口需要时新增观点。这是一处需要在归并时留痕的实质分歧。同时可参照 upstream-conorbronsdon-avoid-ai-writing 的 U-aaw-087（原文没有 I，改写稿就没有 I），那一条站在现有规则一边。
- Wikipedia 归属：不适用（总则）。

### U-bld-006
category: genre
language: both
rule_summary: 虚构文本不受"不得编造细节"这条约束，因为编造细节本来就是虚构写作任务的一部分。
positive: 改一段小说时，按情节需要补一个场景细节。
negative: 改一份技术文档时，按"虚构豁免"补了一个不存在的接口字段。违反点：这不是虚构文本，豁免不适用。
anchor: `## What to do / 3. **Do not invent facts.**`
notes:
- intent: 上游只写了一句 "Fiction is exempt because invented details are part of the task."，理由就在句子里。它防的是把一条为非虚构写的红线套到虚构上，那会让这个 skill 在小说上完全不可用。
- existing: 疑似对应 ALL-G-003，但方向不同：ALL-G-003 是"小说和创意写作不适用本 skill 的模式表，遇到虚构文本先说明再问用户"，本条是"虚构文本豁免不得编造这一条，其余照常"。两条对虚构文本的处置不一样，归并时要对齐。

### U-bld-007
category: style-opinion
language: both
rule_summary: 语体要与文本相符（正式、随意、技术），只有文本本身和作者需要时才加个性。
positive: 一份技术文档改写后仍然是技术语体，不加口语和第一人称。
negative: 把一份法律条款改写成轻快的博客腔。违反点：换掉了与文本不符的语体。
anchor: `## What to do / 4. **Match the voice.**`
notes:
- intent: 上游未展开说明，它在 `## Add personality only when it fits` 一节把同一主张写全了。推断：作者把"匹配语体"和"加个性"分成两件事，是因为前者是所有文本都要做的，后者只有部分体裁要做。推断依据是这两处的措辞差别（Match the voice 无条件，Add personality 带条件）。
- existing: 疑似对应 ALL-G-002 与 ALL-PROC-001。

### 2.2 匹配写作样本（`## Match the writer's voice`）

### U-bld-008
category: process
language: both
rule_summary: 用户提供了写作样本（作者自己以前写的东西）时，改写之前先分析这份样本：句长、用词、段落开头、标点、反复出现的短语、过渡方式。
positive: 先读样本，记下它平均句长偏短、爱用破折号、段落常以疑问句开头，再动手改。
negative: 用户给了一份样本，助手直接开始改稿，没有读样本。违反点：跳过了改写前的样本分析。
anchor: `## Match the writer's voice`
notes:
- intent: 上游未直接说明理由。推断：作者把"像人写的"操作化成了"像这个人写的"——没有样本时只能按通用规则改，有样本时就有了一个具体的目标，而且这个目标可以从六个可观察的维度上读出来。推断依据是他列出的六项全是可以数、可以对照的特征（句长、用词、段落开头、标点、重复短语、过渡）。
- existing: 现有规则里没有。ALL-PROC-025 规定用户提供的词表优先，但没有"分析写作样本"这个机制。**这是现有规则里没有的一条，且是 blader 谱系向多个中文版本传播的特色机制之一。**

### U-bld-009
category: protection
language: both
rule_summary: 按样本的习惯改：不把随意的词换成正式的词，不删掉作者刻意的怪癖。
positive: 样本里反复用一个不标准但作者惯用的说法，改写稿保留它。
negative: 把样本里惯用的口语词统一换成书面词。违反点：把随意的词换成了正式的词。
anchor: `## Match the writer's voice / 2. Match those habits.`
notes:
- intent: 上游写了两条具体禁令（"Do not replace casual words with formal ones or remove deliberate quirks."）而不是一句"要贴近样本"，说明作者知道改写工具的默认漂移方向是往正式、往标准走，因此他直接把这两个方向堵上。
- existing: 疑似对应 ALL-PROT-017。

### U-bld-010
category: process
language: both
rule_summary: 写作样本优先于本 skill 的风格规则；样本用破折号就按样本的频率保留破折号，§14 不作为禁令执行。
positive: 样本里每两百词有一处破折号，改写稿也保持这个频率，不执行 §14 的禁令。
negative: 样本里大量使用破折号，改写稿仍按 §14 把破折号全删了。违反点：让 skill 的风格规则压过了作者的样本。
anchor: `A writing sample takes priority over these style rules.`
notes:
- intent: 上游把它写成一条明确的优先级（"takes priority"），并且指名了一条会被压过去的规则（§14）。它防的是一个具体的冲突：作者本人惯用破折号，而 skill 有一条全局的破折号禁令，如果不写这条优先级，这个 skill 会把作者的标点习惯当成 AI 痕迹清掉。
- existing: 疑似对应 ALL-PROC-025（用户或项目提供的词表优先于本 skill 的默认词表），但"写作样本优先于风格规则、并按样本频率保留标点"这个具体机制现有规则里没有。
- 与 U-bld-034 的关系：本条是那条禁令的唯一例外，两条必须一起读。

### 2.3 个性的边界（`## Add personality only when it fits`）

### U-bld-011
category: process
language: both
rule_summary: 去掉 AI 模式只完成了一半的活，改完的结果仍然要读起来像一个人写的。
positive: 清完模式之后再通读一遍，判断这稿子读起来还像不像一个人写的。
negative: 清完全部命中就交付，改写稿读起来平整、无人称、无起伏。违反点：把"清掉模式"当成了完成标准。
anchor: `## Add personality only when it fits`
notes:
- intent: 上游写了 "Removing AI patterns is only half the job. The result should still sound like a person."。它防的是一个可测量指标的失真：命中数可以清零，而清零之后的文字仍然一眼是机器写的。
- existing: 疑似对应 ALL-PROC-018。
- **来源关系**：upstream-conorbronsdon-avoid-ai-writing 的 U-aaw-082 自述改编自本条（原文标注 `Adapted from blader/humanizer ("Personality and soul")`），两者不构成两个独立来源。

### U-bld-012
category: genre
language: both
rule_summary: 博客、随笔、观点和个人写作里，按作者本人的样子加个性；参考、技术、法律和事实性文本保持中性，不加观点、不加第一人称。
positive: 给一篇个人随笔保留作者的判断和第一人称；给一份 API 参考保持中性。
negative: 给一份法律条款的改写稿加上作者的第一人称评价。违反点：给不该有个性的体裁加了观点和第一人称。
anchor: `Use personality in blog posts, essays, opinions, and personal writing`
notes:
- intent: 上游未直接说明理由，但把体裁分成两组并各给一句处置。推断：作者知道"要像人写的"这条指令如果不带体裁限制，会被套到百科和法律文本上，而那些体裁的正确人类声口本来就是中性的。推断依据是他把两组体裁并列写出并各给一个相反的处置。
- existing: 疑似对应 ALL-G-002 与 ALL-PROC-018。

### U-bld-013
category: protection
language: both
rule_summary: 个性合适的时候，保留作者的观点、不确定、复杂心情、幽默、跑题和不齐整的节奏。
positive: 原文里一句"我也说不清为什么这让我不舒服"原样保留。
negative: 把原文里作者表达犹疑和复杂心情的那一句改写成一个明确的结论。违反点：抹掉了作者原本表达的不确定和复杂心情。
anchor: `When personality fits, keep the writer's opinions`
notes:
- intent: 上游列出的六项（opinions、uncertainty、mixed feelings、humor、asides、uneven rhythm）都是改写工具倾向于抹平的东西——它们在形式上看起来像缺陷（不确定、跑题、节奏不齐），实际上是作者在场的证据。作者用一条明确的保留清单挡住这种抹平。
- existing: 疑似对应 ALL-PROT-017。
- 六项共用同一条判定逻辑（这些属于作者的东西不得因为"看起来不齐整"被改掉），合为一个单元，清单放进正反例。

### U-bld-014
category: protection
language: both
rule_summary: 绝不为了让文字显得有人味而编造事实。
positive: 想让一段读起来更有人味时，只调整节奏和用词，不加任何新的事实。
negative: 为了让一段个人叙述更可信，补了一个具体的地点和时间。违反点：为了追求人味而新增了原文没有的事实。
anchor: `Never invent facts to make the text feel personal.`
notes:
- intent: 上游把这一句单独放在"加个性"那一节的末尾，是因为这一节本身就是最容易诱发编造的地方：要让文字有人味，最省力的办法就是编一个细节。作者在给出"加个性"的许可的同一段里立刻把这个出口堵上。
- existing: 疑似对应 ALL-PROT-018 与 ALL-PROT-001。
- 与 U-bld-003 是同一条禁令在不同场景下的第二次出现，归并时算同一来源内部的重复，不构成 evidence 的增量。

### 2.4 内容类模式（`## Content patterns`，§1 至 §6）

### U-bld-015
category: pattern
language: en
rule_summary: 不把一件普通的事说成标志着重大转变、证明了某种遗产或反映了某个大趋势。触发词：stands/serves as、is a testament/reminder、a vital/significant/crucial/pivotal/key role/moment、underscores/highlights its importance/significance、reflects broader、symbolizing its ongoing/enduring/lasting、contributing to the、setting the stage for、marking/shaping the、represents/marks a shift、key turning point、evolving landscape、focal point、indelible mark、deeply rooted。
positive: The Statistical Institute of Catalonia was established in 1989, part of a wider decentralization of administrative functions in Spain.（引自上游）
negative: The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain.（引自上游）违反点：`marking a pivotal moment in the evolution of` 把一次机构设立说成了转折点。
anchor: `### 1. Inflated claims about importance and legacy`
notes:
- intent: 上游给了理由——"AI writing often claims that ordinary details mark a major change, prove a legacy, or reflect a broad trend."。作者防的是一种没有出处的评价：这些短语给事实加上了一层"它意味着什么"的判断，而这个判断在原文里没有依据。
- existing: 疑似对应 EN-P-014。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 significance inflation）。
- 词表共用同一条判定逻辑，合为一个单元；词表照录自上游，说明文字为重写。

### U-bld-016
category: pattern
language: en
rule_summary: 不靠罗列知名媒体或粉丝数来证明一个人重要。触发词：independent coverage、local/regional/national media outlets、written by a leading expert、active social media presence。
positive: Her views have been cited in The New York Times and the BBC.（引自上游）
negative: Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.（引自上游）违反点：四家媒体的罗列加粉丝数，都没有说出报道的内容。
anchor: `### 2. Name-dropping to prove importance`
notes:
- intent: 上游给了理由——"The list usually gives no useful context."。作者的判据是这份清单有没有说出内容：说了"在哪里被报道"而没说"报道了什么"，这份清单就只是在借别人的名号撑分量。
- existing: 疑似对应 EN-P-018。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 notability over-attribution）。

### U-bld-017
category: protection
language: en
rule_summary: 原文说清了这个人说了什么、在哪里说的，就保留这条有用的引用；不得为了让句子更短而编造语境。
positive: 原文写明她在 2024 年的一次访谈里主张监管应当针对结果，改写稿保留这个内容。
negative: 为了压缩篇幅，把"她在某次访谈里说了什么"改写成"她在多家媒体上表达过类似看法"。违反点：把原文给出的具体语境换成了一个原文没有的概括说法。
anchor: `If the source explains what the person said and where`
notes:
- intent: 上游把这一句紧接在 §2 的模式之后（"Do not invent context for a shorter version."），作用是划出上一条的边界：不是所有的引用都要删，删的是没有内容的清单，有内容的引用要留，而且压缩不能靠编。
- existing: 疑似对应 ALL-PROT-010（引用标识必须紧跟它实际支持的陈述）与 ALL-PROT-008。
- Wikipedia 归属：与 U-bld-016 同属 Wikipedia 的 notability over-attribution 条目下的例外说明。

### U-bld-018
category: pattern
language: en
rule_summary: 不用现在分词从句把一个简单事实包装得更有深度。触发词：highlighting / underscoring / emphasizing…、ensuring…、reflecting / symbolizing…、contributing to…、cultivating / fostering…、encompassing…、showcasing…。
positive: The temple is painted blue, green, and gold, colors meant to evoke Texas bluebonnets and the Gulf of Mexico.（引自上游）
negative: The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.（引自上游）违反点：`symbolizing…`、`reflecting…` 两个分词从句都在替读者解释这件事意味着什么。
anchor: `### 3. Shallow analysis with -ing phrases`
notes:
- intent: 上游给了理由——"AI writing often adds an -ing phrase to make a simple fact sound deeper than it is."。作者盯的是这个句法位置本身：句尾挂一个分词从句，是给事实追加一层解读最省力的方式，而这层解读通常没有出处。
- existing: 疑似对应 EN-P-013。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 superficial -ing）。

### U-bld-019
category: pattern
language: en
rule_summary: 不用广告腔描述地方、文化、产品或机构。触发词：boasts a、vibrant、rich（比喻义）、profound、enhancing its、showcasing、exemplifies、commitment to、natural beauty、nestled、in the heart of、groundbreaking（比喻义）、renowned、breathtaking、must-visit、stunning。
positive: Alamata Raya Kobo is a town in the Gonder region of Ethiopia.（引自上游）
negative: Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.（引自上游）违反点：`Nestled`、`breathtaking`、`vibrant`、`rich cultural heritage`、`stunning natural beauty` 五处广告腔堆在一句里，全句没有一条事实。
anchor: `### 4. Sales language`
notes:
- intent: 上游给了理由和适用场景——"AI writing often sounds like an advertisement, especially when it describes places, culture, products, or organizations."。这条与 §1 的区别在方向：§1 是给事实追加历史意义，本条是给事实追加吸引力，两者都是在没有新信息的情况下加分量。
- existing: 疑似对应 EN-P-002。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 promotional tone）。

### U-bld-020
category: pattern
language: en
rule_summary: 不把一个论断挂在不具名的专家、评论者、报告或观察者身上。触发词：Industry reports、Observers have cited、Experts argue、Some critics argue、several sources / publications（在实际只引了很少几个来源时）。
positive: Researchers and conservationists study the Haolai River for its unusual characteristics.（引自上游）
negative: Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.（引自上游）违反点：`Experts believe` 把一个生态学论断挂在了一个查不到的主体上。
anchor: `### 5. Vague sources`
notes:
- intent: 上游给了理由——"AI writing often assigns a claim to unnamed experts, critics, reports, or observers."。作者盯的是归因的可核查性：一个查不到的归因等于一个没有出处的事实主张。
- existing: 疑似对应 EN-P-017。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 weasel / vague attribution，以及 exaggerated source quantity 对应 "several sources"）。

### U-bld-021
category: protection
language: en
rule_summary: 原文给了真实来源就点名它；原文没有给，就删掉这个没有支撑的论断；绝不编造来源。
positive: 原文给了 2024 年 EPA 报告，改写稿点名它；原文没有出处的那句删掉。
negative: 原文写 "Experts believe…"，改写稿改成 "A 2023 study found…"。违反点：编造了一个原文没有的来源。
anchor: `Name a real source when the source text provides one.`
notes:
- intent: 上游把三种处置写全了（点名、删掉、绝不编造），是因为上一条只说了"不要用模糊归因"，如果不写清替代动作，最省力的修法恰恰是编一个具体来源顶上——那比模糊归因更糟。
- existing: 疑似对应 ALL-PROT-001 与 EN-P-017。
- 与 U-bld-003 是同一条禁令在具体场景下的第三次出现。

### U-bld-022
category: pattern
language: en
rule_summary: 不加套路化的"挑战与展望"小节。触发词：Despite its… faces several challenges…、Despite these challenges、Challenges and Legacy、Future Outlook。
positive: Korattur has recurring traffic congestion and water shortages.（引自上游）
negative: Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.（引自上游）违反点：`Despite its…`、`Despite these challenges…` 两句构成一个不含新事实的套路小节。
anchor: `### 6. Formulaic challenges and outlook sections`
notes:
- intent: 上游给了理由——"These sections usually repeat vague claims instead of adding facts."。作者盯的不是"挑战"这个话题，而是这个话题在生成文本里固定出现、固定用同一个转折句式、固定不带具体内容。
- existing: 疑似对应 EN-P-031。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 formulaic "challenges"）。

### U-bld-023
category: protection
language: en
rule_summary: 日期、公开行动这类细节只有来自原文或用户时才能补进去。
positive: 把套路小节改写成具体问题时，只用原文已经给出的信息。
negative: 把 "faces challenges" 改写成 "the city council approved a water plan in 2023"。违反点：为了让句子具体，补了一个原文没有的公开行动和年份。
anchor: `Add details such as dates or public actions only when they come from the source or the user.`
notes:
- intent: 与 U-bld-021 同一设计：上一条要求把空洞的套路小节换成具体问题，而"换成具体"这个动作最容易诱发编造，所以作者在紧邻的位置再堵一次。
- existing: 疑似对应 ALL-PROT-001。
- 与 U-bld-003 是同一条禁令在具体场景下的第四次出现。

### 2.5 语言与语法类模式（`## Language and grammar patterns`，§7 至 §13）

### U-bld-024
category: pattern
language: en
rule_summary: 不用这批高频 AI 词，尤其不成组出现：Actually、additionally、align with、crucial、delve、emphasizing、enduring、enhance、fostering、garner、gate / gated / gating（比喻义，已确立的技术用法保留）、highlight（动词）、interplay、intricate / intricacies、key（形容词）、landscape（抽象义）、pivotal、quietly、showcase、tapestry（抽象义）、testament、underscore（动词）、valuable、vibrant。
positive: Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.（引自上游）
negative: Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.（引自上游）违反点：`Additionally`、`enduring`、`testament`、`landscape`、`showcasing` 五个词表词聚在两句里。
anchor: `### 7. Overused AI words`
notes:
- intent: 上游给了理由——"AI writing uses these words much more often than most people do, especially in groups."。"especially in groups" 是判据的一部分：单个词不构成证据，成组出现才构成。词表里 `gate/gated/gating` 一项还带了自己的例外（保留已确立的技术用法），说明作者知道词表会误伤专业语境。
- existing: 疑似对应 EN-P-001 与 EN-M-001。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 AI vocabulary）。
- 词表照录自上游，说明文字为重写。

### U-bld-025
category: pattern
language: en
rule_summary: 不用更长的短语替代 is、are、has 这类简单动词。触发词：serves as / stands as / marks / represents [a]、boasts / features / offers [a]。
positive: Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.（引自上游）
negative: Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.（引自上游）违反点：`serves as`、`features`、`boasts` 三处各自替代了 is 和 has。
anchor: `### 8. Avoiding is and are`
notes:
- intent: 上游给的理由是 "AI writing often replaces simple verbs such as *is*, *are*, and *has* with longer phrases."。推断作者盯的是这个替换背后的动机：这些替代词让一个等同或所属关系看起来像一个动作，句子因此显得更"有内容"，实际信息量不变。这个推断依据是上游给出的 before/after 对照——改写后信息完全相同，只是变短了。
- existing: 疑似对应 EN-P-015。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 copula avoidance）。

### U-bld-026
category: pattern
language: en
rule_summary: 不用 "Not only… but…"、"It's not just X, it's Y" 这类否定式对比句式。
positive: The heavy beat adds to the aggressive tone.（引自上游）
negative: It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.（引自上游）违反点：`It's not just X, it's Y`、`It's not merely X, it's Y` 连用两次。
anchor: `### 9. Not X but Y and clipped negative endings`
notes:
- intent: 上游只写了 "AI writing overuses forms such as…"，理由是频率。推断作者盯的还有一层：这个句式先立一个没人主张的说法再推翻它，读者拿到的是一个反转动作而不是一个论断。推断依据是上游给的 after 版本直接把 Y 陈述出来，把否定的那半整个去掉了。
- existing: 疑似对应 EN-P-006。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 negative parallelisms）。

### U-bld-027
category: pattern
language: en
rule_summary: 不用句尾截断式否定（"…, no guessing"）代替把话说完整的从句。
positive: The options come from the selected item without forcing the user to guess.（引自上游）
negative: The options come from the selected item, no guessing.（引自上游）违反点：句尾的 `no guessing` 是一个截断的否定短语，替代了一个完整的说明从句。
anchor: `### 9. Not X but Y and clipped negative endings`
notes:
- intent: 上游写了 "It also adds clipped endings such as 'no guessing' instead of writing a clear clause."。作者盯的是省略本身：这个位置本该有一个说明为什么、怎么样的从句，截断之后句子显得干脆，但读者要自己补出被省掉的意思。
- existing: 现有规则里没有。EN-P-006 的四个例子（It's not X, it's Y、not only X but Y、The question isn't X. It's Y.、Not a X. Not a Y. A Z.）都是句首或整句的否定对比，不含句尾截断式否定。
- Wikipedia 归属：**存疑**。aboudjem 的覆盖表把 negative parallelisms 写成"all three variants"但没有列出是哪三个，本条是否属于其中一个变体无法确定。
- 与 U-bld-026 拆开的理由：一句 "The options come from the selected item, no guessing." 只违反本条不违反 U-bld-026，两条各自可判定。

### U-bld-028
category: pattern
language: en
rule_summary: 不为了听起来完整而把想法硬凑成三项。
positive: The event includes talks and panels. There's also time for informal networking between sessions.（引自上游）
negative: The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.（引自上游）违反点：连续两句都是三项并列，第二句的三项还全是抽象名词。
anchor: `### 10. Forced groups of three`
notes:
- intent: 上游给了理由——"AI writing often forces ideas into groups of three to sound complete."。"forces" 和 "to sound complete" 是判据：三项本身不是问题，为了让句子听起来收得住而凑出第三项才是。
- existing: 疑似对应 ALL-P-005。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 rule of three）。
- 与 upstream-hardikpandya-stop-slop 的 U-ssl-015（"Two items beat three"，默认取两项）强度不同：本条只管"凑出来的"三项。

### U-bld-029
category: pattern
language: en
rule_summary: 指代同一个人或同一件事时用一个固定的名称，不为了避免重复而不停换称呼。
positive: The protagonist faces many challenges but eventually triumphs and returns home.（引自上游）
negative: The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.（引自上游）违反点：`protagonist`、`main character`、`central figure`、`hero` 四个称呼指同一个人。
anchor: `### 11. Changing names and repeating sentence openings`
notes:
- intent: 上游给了理由——"AI writing handles repetition by rule instead of by ear."。这句话是本条和 U-bld-030 共同的解释：模型有一条"不要重复"的规则，于是在不该避免重复的地方也照做。作者的判断是重复该不该避免要用耳朵听，不能按规则一律避免。
- existing: 疑似对应 EN-P-019 与 EN-P-020。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 elegant variation）。

### U-bld-030
category: pattern
language: en
rule_summary: 不连续几句用同一个主语开头（尤其是 she、he）；修法是合并句子、换一个主语，或者从动作开始写。
positive: She noted the door and its lock, then filed both away.（引自上游）
negative: She noted the door. She noted the lock on it. She filed both away.（引自上游）违反点：连续三句都以 `She` 开头。
anchor: `### 11. Changing names and repeating sentence openings`
notes:
- intent: 与 U-bld-029 共用同一句解释（"handles repetition by rule instead of by ear"）。这两条是同一个成因的两个相反表现：模型该重复的地方不重复（换称呼），不该重复的地方重复（同一句首）。作者把它们放进同一节，是在说明它们是一个问题。
- existing: 疑似对应 ALL-P-001（整篇不得段落长度、开头句式雷同）。
- Wikipedia 归属：**作者补的**（不在 aboudjem 的覆盖表里；覆盖表只映射了 elegant variation）。
- 与 U-bld-029 拆开的理由：判定逻辑相反（一个数称呼有几种，一个数句首重复几次）。

### U-bld-031
category: protection
language: en
rule_summary: 修重复句首时不要禁掉那个重复的词，要修的是重复的句式；改完之后剩下的那一句仍然可以用 She 开头。
positive: 把三句合成一句，新句子仍以 `She` 开头。
negative: 为了不重复，把三句里的 `She` 分别换成 `The woman`、`The visitor`、`She`。违反点：把句式问题当成用词问题修，结果制造出了 U-bld-029 禁止的换称呼。
anchor: `Do not ban the repeated word. Fix the repeated sentence pattern.`
notes:
- intent: 上游把这一句写成一条独立的告诫，是因为 U-bld-029 和 U-bld-030 放在同一节里会诱发一个具体的错误修法：读者看到"不要重复句首"，最省力的做法是把重复的词换掉，而那正好触发上一条禁止的换称呼。作者用这一句把两条规则的互动锁死。
- existing: 疑似对应 ALL-PROT-009（不得为避免重复而换称）。
- **这一条是全文最能说明作者判断力的地方之一：它规定的不是文本，而是两条规则同时生效时的正确修法。**

### U-bld-032
category: pattern
language: en
rule_summary: 不用 "from X to Y" 制造并不存在的跨度——X 和 Y 不在同一个维度上时，直接列出具体的项。
positive: The book covers the Big Bang, star formation, and current theories about dark matter.（引自上游）
negative: Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.（引自上游）违反点：两组 `from X to Y` 里的四项不构成任何一条连续的轴，跨度是修辞造出来的。
anchor: `### 12. False from X to Y ranges`
notes:
- intent: 上游给了理由——"AI writing often uses 'from X to Y' when X and Y do not form a real range."。作者盯的是这个句式带来的暗示：它让读者以为中间还有很多没列出来的东西，而实际上作者只有这两项。
- existing: 疑似对应 EN-P-021。
- Wikipedia 归属：**作者补的**（不在 aboudjem 的覆盖表里）。

### U-bld-033
category: pattern
language: en
rule_summary: 不隐藏谁在做这件事，也不丢掉主语；用主动语态，当它能让施事者和动作更清楚时。
positive: You do not need a configuration file. The system preserves the results automatically.（引自上游）
negative: No configuration file needed. The results are preserved automatically.（引自上游）违反点：第一句是无主句，第二句是被动式，两句都没说谁不需要、谁保存。
anchor: `### 13. Passive voice and missing subjects`
notes:
- intent: 上游写了 "AI writing often hides who acts or drops the subject. Use active voice when it makes the actor and action clearer."。第二句的条件从句（"when it makes… clearer"）是本条的关键：作者要的不是消灭被动语态，而是让施事者可见；被动语态在施事者不重要时不算问题。
- existing: 疑似对应 ALL-P-004。
- Wikipedia 归属：**作者补的**（aboudjem 把 Passive / Subjectless 编为 P50，属于它自述 "novel relative to the P1-P43 set" 的 craft set）。
- **三个英文来源在这一点上的强度差别值得归并时留意**：本条带条件（"when it makes the actor and action clearer"），upstream-hardikpandya-stop-slop 的 U-ssl-010 是无条件禁令，现有 ALL-P-004 介于两者之间。

### 2.6 样式类模式（`## Style patterns`，§14 至 §19）

### U-bld-034
category: style-opinion
language: en
rule_summary: 最终稿里不得出现 em dash（—）和 en dash（–），除非作者的写作样本用它们；替换成句号、逗号、冒号、括号，或者重写句子。
positive: The new policy, announced without warning, affects thousands of workers.（引自上游）
negative: The new policy — announced without warning — affects thousands of workers.（引自上游）违反点：两处 em dash。
anchor: `### 14. Em and en dashes`
notes:
- intent: 上游只给了规则和例句，没有写为什么破折号是 AI 痕迹。推断：这条被放进 "Style patterns" 而不是内容类，说明作者把它当成排版层的信号而不是写作层的问题；而它被写成禁令加一个明确例外（作者样本），说明作者知道破折号本身是正当标点，问题在于模型的使用频率。这个推断的依据是 U-bld-010 里对本条的显式豁免。
- existing: 疑似对应 EN-P-026，**且与之冲突**：EN-P-026 按篇幅分界（200 词以下一处不用，200 词以上至多留一到两处），本条是禁令加样本例外。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 em dashes）。
- 三个来源三种口径：本条禁令加样本例外；upstream-hardikpandya-stop-slop 的 U-ssl-017 无条件禁；upstream-conorbronsdon-avoid-ai-writing 的 U-aaw-035 是每千词一处的频率上限。归并时是一处明确的三方冲突。
- category 记 style-opinion 的理由：它规定的是一种标点偏好，且换个作者（样本用破折号的作者）就不成立——上游自己也承认了这一点。

### U-bld-035
category: process
language: en
rule_summary: 交付改写稿之前，必须逐字符搜索 `—` 和 `–` 并逐个处理；同时要查用空格包起来的破折号（` — `）和当破折号用的双连字符（` -- `）。
positive: 交付前跑一遍字符搜索，四种形式各查一次。
negative: 交付前只凭通读判断"应该没有破折号了"。违反点：没有做字符搜索，通读会漏掉空格包围的破折号和双连字符。
anchor: `Before returning the rewrite, search for`
notes:
- intent: 上游未说明理由。推断：作者把一条写作规则配了一个机械步骤，是因为破折号在通读时最容易被漏掉——它不影响句子的可读性，读者的眼睛会滑过去。四种变体（—、–、` — `、` -- `）都被点名，说明作者遇到过靠通读漏掉的情形。推断依据是这一步被写成"搜索"这个不需要判断的动作，且列了四种形式。
- existing: 疑似对应 ALL-PROC-014（交付前逐项自查）；"对特定字符做机械搜索"这一层现有规则里没有。
- 与 U-bld-034 拆开的理由：一份改写可以遵守禁令却不做交付前搜索，两条各自可判定。

### U-bld-036
category: pattern
language: en
rule_summary: 不在没有明确理由的情况下给词和短语加粗。
positive: It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.（引自上游）
negative: It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.（引自上游）违反点：四处加粗覆盖了句子里的每一个专有名词，没有一条能说出来的规则决定为什么是这四处。
anchor: `### 15. Too much bold text`
notes:
- intent: 上游给了理由——"AI chatbots often bold words and phrases without a clear reason."。判据在 "without a clear reason"：加粗不是禁令，无理由的加粗才是；如果说不出为什么加粗这几处而不是别处，就是命中。
- existing: 疑似对应 ALL-P-002。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 boldface overuse）。

### U-bld-037
category: pattern
language: en
rule_summary: 不用"每项以加粗小标题加冒号开头"的竖排列表把本可以连着说的内容拆开。
positive: The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.（引自上游）
negative: - **User Experience:** The user experience has been significantly improved with a new interface.（引自上游，另有两项同构）违反点：每项都是"加粗标签＋冒号＋一句复述标签的话"，三项拼起来还不如一句话说得清楚。
anchor: `### 16. Lists with bold mini-headings`
notes:
- intent: 上游给了现象描述——"AI writing often uses vertical lists in which every item starts with a bold label and a colon."。推断作者盯的是这个结构造成的信息稀释：加粗标签重复了后面那句话的内容，三项里真正的信息只有"新界面、算法优化、端到端加密"三个词。推断依据是上游给的 after 版本把三项压成了一句话且信息没有丢。
- existing: 疑似对应 ALL-P-002。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 inline-header lists）。
- 与 U-bld-036 拆开的理由：加粗滥用可以出现在正文里不涉及列表，本条专指列表结构，两条各自可判定。

### U-bld-038
category: pattern
language: en
rule_summary: 标题用句子大小写，不把每个实词都首字母大写。
positive: `## Strategic negotiations and global partnerships`（引自上游）
negative: `## Strategic Negotiations And Global Partnerships`（引自上游）违反点：`Negotiations`、`And`、`Global`、`Partnerships` 全部首字母大写，连虚词 `And` 也大写了。
anchor: `### 17. Title case in headings`
notes:
- intent: 上游给了现象描述——"AI chatbots often capitalize every main word in a heading."。推断：这是一个纯排版层的信号，与写作质量无关，价值在于它极易辨认且模型极稳定地产生它。推断依据是这条被放在 Style patterns 组、且上游只给了一行 before/after 没有别的说明。
- existing: 疑似对应 EN-P-012。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 title case headings）。

### U-bld-039
category: pattern
language: en
rule_summary: 不在标题和列表项上加装饰性的 emoji。
positive: The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.（引自上游）
negative: 🚀 **Launch Phase:** The product launches in Q3（引自上游，另有两项同构）违反点：`🚀` 是纯装饰，不承载任何信息。
anchor: `### 18. Emojis`
notes:
- intent: 上游给了现象描述——"AI chatbots often add emojis to headings and list items as decoration."。判据在 "as decoration"：emoji 本身不是禁令，作为装饰加在结构位置上才是。
- existing: 疑似对应 ALL-P-002。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 emoji-as-formatting）。

### U-bld-040
category: pattern
language: en
rule_summary: 作者或目标格式用直引号（"…"）时，不要用弯引号（“…”）。
positive: He said "the project is on track" but others disagreed.（引自上游）
negative: He said “the project is on track” but others disagreed.（引自上游）违反点：一对弯引号，而作者和目标格式用的是直引号。
anchor: `### 19. Curly quotation marks`
notes:
- intent: 上游给了成因——"ChatGPT often uses curly quotes where the writer or target format uses straight quotes."。判据里的条件从句是关键：命中条件不是"用了弯引号"，而是"用了弯引号而作者或目标格式用的是直引号"。作者自己在 `### What not to flag` 一节又补了一条（弯引号单独出现不算证据，因为 macOS、Word、Google Docs 和多数 CMS 默认会自动转弯）。
- existing: 疑似对应 EN-P-037，**方向不同**：EN-P-037 是"原稿用哪种就保持哪种，不统一改成另一种"，本条是"作者用直引号时把弯引号改成直引号"。两者在原稿用弯引号的情形下处置一致，在原稿混用的情形下处置不同。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 curly quotes）。

### 2.7 聊天机器人类模式（`## Chatbot patterns`，§20 至 §22）

### U-bld-041
category: pattern
language: en
rule_summary: 删掉留在正文里的助手问候、提议和结语。触发词：I hope this helps、Of course!、Certainly!、You're absolutely right!、Would you like…、Want me to…?、Want me to give examples?、Should I continue?、let me know、here is a…。
positive: The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.（引自上游）
negative: Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.（引自上游）违反点：`Here is an overview of`、`I hope this helps!`、`Let me know if…` 三处都是对话框架的残留，正文里没有对话对象。
anchor: `### 20. Chatbot text left in the answer`
notes:
- intent: 上游给了理由——"A chatbot's greeting, offer, or closing sometimes remains in text that should stand on its own."。判据在 "should stand on its own"：这些句子在对话里是正当的，被复制进一篇独立的文章里就成了残留物。
- existing: 疑似对应 EN-P-028。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 collaborative / conversational language）。

### U-bld-042
category: pattern
language: en
rule_summary: 删掉知识截止免责声明与"找不到资料"的说明。触发词：as of [date]、Up to my last training update、While specific details are limited / scarce…、based on available information、not publicly available。处理方式是说明原文没有这项信息，或者删掉整句。
positive: The company's founding date is not documented in the available sources.（引自上游）
negative: While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.（引自上游）违反点：`While specific details… are not extensively documented in readily available sources` 是模型在说明自己的检索边界，与文章内容无关。
anchor: `### 21. Knowledge-limit disclaimers and guesses`
notes:
- intent: 上游给了成因——"Older models may mention the date when their knowledge ends."。作者把它排进 Chatbot patterns 而不是内容类，说明他认为这类句子的问题在于它谈的是生成过程而不是主题。
- existing: 疑似对应 EN-P-028。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表 knowledge-cutoff disclaimers）。

### U-bld-043
category: pattern
language: en
rule_summary: 不把找不到资料时的猜测当成事实写出来。触发词：maintains a low profile、keeps personal details private、prefers to stay out of the spotlight、likely [grew up / studied / began]、it is believed that。应当写明原文没有这项信息，或者整节略去。
positive: Her early life is not documented in the available sources.（引自上游）
negative: Information about her early life is not publicly available, suggesting she maintains a low profile and keeps personal details private. She likely grew up in a middle-class household, which shaped her later interest in education reform.（引自上游）违反点：`suggesting she maintains a low profile`、`She likely grew up in a middle-class household` 把"查不到"当成了推理的前提，编出了两条关于这个人的断言。
anchor: `### 21. Knowledge-limit disclaimers and guesses`
notes:
- intent: 上游写了 "A model may also explain that it could not find a source, then fill the gap with a plausible guess... Do not present a guess as a fact."。作者盯的是一个特定的推理错误：把"没有记录"当成"这个人低调"的证据，再从这个虚构的性格推出更多细节。这是全文里对编造机制描述得最具体的一条。
- existing: 疑似对应 EN-P-039（疑似捏造的痕迹要标出来交给作者确认）与 ALL-PROT-001。
- Wikipedia 归属：**存疑**。覆盖表只映射了 knowledge-cutoff disclaimers，没有提"猜测填空"。
- 与 U-bld-042 拆开的理由：一段文字可以只有截止声明没有猜测，也可以只有猜测没有截止声明，两条各自可判定。

### U-bld-044
category: pattern
language: en
rule_summary: 删掉先夸用户或先表示同意再进入正题的句子。
positive: The economic factors you mentioned are relevant here.（引自上游）
negative: Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.（引自上游）违反点：`Great question!`、`You're absolutely right`、`That's an excellent point` 三句都是先给评价再说事，且三句加起来没有任何内容。
anchor: `### 22. Overly agreeable tone`
notes:
- intent: 上游给了现象描述——"AI assistants often praise the user or agree before giving the answer."。推断作者盯的是这类句子的位置：它们出现在回答之前，占据了本该给出内容的位置，且它们的存在只与对话关系有关、与主题无关。推断依据是上游的 after 版本把三句压成了一句实质回答。
- existing: 疑似对应 EN-P-028。
- Wikipedia 归属：**存疑**。覆盖表把 collaborative / conversational language 映射到 aboudjem 的 P19、P32，谄媚是否包含在内无法确定。

### 2.8 填充与保留语（`## Filler and hedging`，§23 至 §35）

### U-bld-045
category: pattern
language: en
rule_summary: 把填充短语换成它的最短说法：In order to achieve this goal → To achieve this；Due to the fact that → Because；At this point in time → Now；In the event that → If；has the ability to → can；It is important to note that the data shows → The data shows。
positive: Because it was raining, the system can process the request now.
negative: Due to the fact that it was raining, the system has the ability to process the request at this point in time. 违反点：`Due to the fact that`、`has the ability to`、`at this point in time` 三处都可以换成一个更短的说法而不损失任何意思。
anchor: `### 23. Filler phrases`
notes:
- intent: 上游只给了一张 before → after 对照表，没有写理由。推断：这六对的共同特征是右边一列的意思与左边完全相同、字数只有一半，因此判据不是"这个短语不好"而是"这个短语可以无损压缩"。推断依据是这一节的形式——只有对照表，没有 Problem 段落，与前面 22 条的写法都不同。
- existing: 疑似对应 EN-P-004。
- Wikipedia 归属：**作者补的**（不在 aboudjem 的覆盖表里；aboudjem 的 P22 sentence-level filler 不在 Wikipedia 映射中）。
- 六对短语共用同一条判定逻辑，合为一个单元；对照表照录自上游，说明文字为重写。

### U-bld-046
category: pattern
language: en
rule_summary: 不堆叠保留语。触发词：to be fair、it's also possible、could potentially、might arguably、in some cases it may、this is an inference。只有原文支持且意义确实需要时才留一个；只用来补救前面说过头的话的保留语要删掉。
positive: The policy may affect outcomes.（引自上游）
negative: It could potentially possibly be argued that the policy might have some effect on outcomes.（引自上游）违反点：`could`、`potentially`、`possibly`、`be argued that`、`might`、`some` 六层保留语叠在一句里，句子最后什么都没主张。
anchor: `### 24. Too many qualifiers`
notes:
- intent: 上游给了成因——"Repeated editing can add one qualifier after another until every claim sounds uncertain."。这个成因很具体：保留语堆叠不是一次生成的产物，是多轮编辑的积累，每一轮都为上一轮的过头说法打一个补丁。作者据此给了删除判据："Remove caveats that only repair an earlier overstatement."
- existing: 疑似对应 EN-P-029 与 EN-P-030。
- Wikipedia 归属：**作者补的**（aboudjem 把 Leftover Hedge Debris 编为 P55，属 craft set）。
- 例外条件（原文支持且意义需要时保留一个）与主规则共用同一条判定逻辑，合进本单元。

### U-bld-047
category: pattern
language: en
rule_summary: 不用空洞的乐观收尾；结尾停在最后一个具体事实上，原文有真实计划就写那个计划。
positive: 结尾停在最后一个具体事实上，或者写出原文给出的真实计划。
negative: The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.（引自上游）违反点：三句都是不可核实的乐观表述，没有一条事实。
anchor: `### 25. Generic positive endings`
notes:
- intent: 上游给了理由——"AI writing often ends with vague optimism instead of the last useful fact."。作者的修法值得注意：他给的 after 是"删掉这一段"，不是"改写这一段"，说明他认为这个位置本来就不需要内容。
- existing: 疑似对应 EN-P-023。
- Wikipedia 归属：**作者补的**（不在 aboudjem 的覆盖表里）。

### U-bld-048
category: pattern
language: en
rule_summary: 复合修饰语在名词前保留连字符（a high-quality report），跟在名词后作表语时去掉连字符（the report is high quality）。触发词：third-party、cross-functional、client-facing、data-driven、decision-making、well-known、high-quality、real-time、long-term、end-to-end。
positive: The cross-functional team delivered a high-quality, data-driven report. The team is cross functional, the report is high quality, and the methodology is data driven.（引自上游）
negative: The team is cross-functional, the report is high-quality, and the methodology is data-driven. 违反点：三处复合词都在系动词之后作表语，此处不该保留连字符。
anchor: `### 26. Too many hyphenated word pairs`
notes:
- intent: 上游给了现象和规则——"AI writing often hyphenates these pairs everywhere."。判据不是"这些词不能用"，而是"位置决定加不加连字符"，而模型的做法是不分位置一律加。作者给的 before/after 里前半句两版完全相同，只有后半句不同，正是为了把这个位置判据演示清楚。
- existing: 疑似对应 EN-P-036。
- Wikipedia 归属：**作者补的**（aboudjem 把 Hyphenated-Pair Overuse 编为 P47，属 craft set）。

### U-bld-049
category: pattern
language: en
rule_summary: 不用"揭示更深真相"的短语把一个普通论点包装得像隐藏的洞见。触发词：The real question is、at its core、in reality、what really matters、fundamentally、the deeper issue、the heart of the matter。
positive: The question is whether teams can adapt. That mostly depends on whether the organization is ready to change its habits.（引自上游）
negative: The real question is whether teams can adapt. At its core, what really matters is organizational readiness.（引自上游）违反点：`The real question is`、`At its core`、`what really matters` 三处都在宣称"这才是真正重要的"，而句子本身的论点没有变。
anchor: `### 27. Pretending to reveal a deeper truth`
notes:
- intent: 上游给了理由——"AI writing uses these phrases to make an ordinary point sound like a hidden truth."。作者盯的是这些短语的共同动作：它们暗示前面说的都是表面，接下来才是实质，而实际上接下来说的和前面是一回事。
- existing: 疑似对应 EN-P-008；其中 `at its core` 也在 EN-P-004 的短语表里。
- Wikipedia 归属：**作者补的**（不在 aboudjem 的覆盖表里）。

### U-bld-050
category: pattern
language: en
rule_summary: 不预告下一个点，直接把它说出来；随意语域的同类表达（"one thing that bit me hard, so pay attention to this part"）同样要删——删的是预告这个动作，不是它的正式腔。触发词：Let's dive in、let's explore、let's break this down、here's what you need to know、now let's look at、without further ado、heads up、quick note、before I forget。
positive: Next.js caches data at multiple layers, including request memoization, the data cache, and the router cache.（引自上游）
negative: Let's dive into how caching works in Next.js. Here's what you need to know.（引自上游）违反点：两句都在预告接下来要讲什么，没有一句在讲。
anchor: `### 28. Announcing the next point`
notes:
- intent: 上游写了一条容易被忽略的判据——"A casual phrase such as 'one thing that bit me' can have the same problem. Remove the announcement, not just its formal tone."。作者要防的是一个具体的错误修法：把 "Let's dive in" 改成 "one thing that bit me hard" 看起来是去掉了 AI 腔，实际上预告这个动作还在，只是换了语域。
- existing: 疑似对应 EN-P-007。
- Wikipedia 归属：**作者补的**（不在 aboudjem 的覆盖表里；aboudjem 的 P41 Infomercial Engagement Hooks 标注出处为 Writewithai Substack，不是 Wikipedia）。
- 正式与随意两种语域的例子共用同一条判定逻辑（这句话是不是只在预告），合为一个单元。

### U-bld-051
category: pattern
language: en
rule_summary: 标题后面不跟一句只是复述标题的话；删掉这句，直接进正文。
positive: `## Performance` 之后直接写 "When users hit a slow page, they leave."（引自上游）
negative: `## Performance` 之后先写一句 "Speed matters."，再写正文。（引自上游）违反点：`Speed matters.` 只是把标题 `Performance` 换个说法重复了一遍。
anchor: `### 29. A heading repeated in the first sentence`
notes:
- intent: 上游给了识别信号——"A heading followed by a one-line paragraph that simply restates the heading before the real content begins."。作者盯的是这个位置的一个固定动作：模型在标题之后需要一个过渡，而最省力的过渡就是把标题再说一遍。
- existing: 疑似对应 EN-P-033。
- Wikipedia 归属：**作者补的**（不在 aboudjem 的覆盖表里）。

### U-bld-052
category: pattern
language: en
rule_summary: 文档和注释描述当前的行为，不叙述改动过程；只有变更日志、发布说明、迁移指南这类以变化为主题的文档才提上一个版本。
positive: This function uses a hash map for O(1) lookups, avoiding the O(n²) cost of naive iteration.（引自上游）
negative: This function was added to replace the previous approach of iterating through all items, which caused O(n²) performance.（引自上游）违反点：`was added to replace the previous approach of` 讲的是改动过程，读者要的是这个函数现在做什么。
anchor: `### 30. Writing about the previous version`
notes:
- intent: 上游写了适用范围和例外——"Documentation and comments should describe the current behavior. Mention the previous version only in change logs, release notes, migration guides, and other documents about change."。作者盯的是一种写作视角的错位：写文档的人刚做完改动，脑子里是"我改了什么"，而读文档的人不知道有过改动。
- existing: 疑似对应 EN-P-035。
- Wikipedia 归属：**作者补的**（aboudjem 把 Diff-Anchored Writing 编为 P46，属 craft set）。
- 例外条件与主规则共用同一条判定逻辑（这份文档的主题是不是变化本身），合进本单元。

### U-bld-053
category: pattern
language: en
rule_summary: 不把每一句都写成戏剧化的收尾句；一句短句可以强调，一串短句片段连排通常是硬凑的。
positive: AlphaEvolve changed the search because it did not favor symmetry or human-looking designs. That made some of the older assumptions less useful.（引自上游）
negative: Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.（引自上游）违反点：`No aesthetic prior.`、`No nostalgia for human taste.` 是两个不成句的片段，加上前后共五句连排制造重量。
anchor: `### 31. Forced punchlines and dramatic fragments`
notes:
- intent: 上游给了判据——"One short sentence can add emphasis. A row of short fragments usually feels forced."。作者明确保留了单个短句的正当性，命中条件是连排。这条与 `### What not to flag` 里的 "One short sentence for emphasis"（U-bld-060）是同一个判据的两次表述。
- existing: 疑似对应 EN-P-025。
- Wikipedia 归属：**作者补的**（不在 aboudjem 的覆盖表里）。

### U-bld-054
category: pattern
language: en
rule_summary: 不把一个普通论断改写成听起来深刻、实际不含细节的格言。触发词：X is the Y of Z、X becomes a trap、X is not a tool but a mirror、the language of、the currency of、the architecture of。修法是把格言换回那个具体的论断。
positive: Symmetric layouts often feel more predictable to users. Teams can over-optimize workflows and miss how people actually use them.（引自上游）
negative: Symmetry is the language of trust. Efficiency becomes a trap when teams forget the human layer.（引自上游）违反点：`is the language of`、`becomes a trap` 两个格言模板各自把一个可以说清楚的观察换成了一句听着有分量、无法核对的话。
anchor: `### 32. Formulaic sayings`
notes:
- intent: 上游给了理由和修法——"AI writing often turns an ordinary claim into a saying that sounds deep but adds no detail. Replace the saying with the specific claim."。作者的判据是"adds no detail"：格言的形式本身不是问题，问题是套进这个形式之后原本的细节丢了。
- existing: 疑似对应 EN-P-024。
- Wikipedia 归属：**作者补的**（aboudjem 把 Aphorism Formulas 编为 P48，属 craft set）。

### U-bld-055
category: pattern
language: en
rule_summary: 不用假坦白式开场制造停顿。触发词（作为独立的钩子或普通论点前的假坦白停顿时）：Honestly?、Look、Here's the thing、The thing is、Let's be honest、Real talk。
positive: Whether it's worth the price depends on how often you'll use it.（引自上游）
negative: Is it worth the price? Honestly? It depends on how often you'll use it.（引自上游）违反点：`Honestly?` 单独成句作停顿，暗示接下来是一句难说出口的实话，而接下来的是一句普通判断。
anchor: `### 33. Fake-candid openings`
notes:
- intent: 上游给了理由——"AI writing often starts with a staged pause or claim of honesty before making a routine point."。判据里的 "routine point" 是关键：假坦白的问题不在于坦白，而在于它铺垫的那个点根本不需要坦白。作者在 `### What not to flag` 里补了边界（U-bld-060：句中的 honestly 和 look 是日常用法，命中的是独立成句的戏剧化开场）。
- existing: 疑似对应 EN-P-007（其中含 `Here's the thing`、`I'll be honest`）。
- Wikipedia 归属：**作者补的**（不在 aboudjem 的覆盖表里）。

### U-bld-056
category: pattern
language: en
rule_summary: 不反驳原文里没人提出过的反对意见。触发词：This isn't (mainly/really) about、I'm not saying / arguing / trying to、To be clear、Don't get me wrong、This is not to say、You could argue / frame this differently but、Some might say… but。一个直接的论断（"the API is not thread-safe"）不算这个模式。
positive: The issue is whether the agent can use the instruction when it acts.（引自上游）
negative: This isn't mainly about prompt length, and I'm not arguing that documentation doesn't matter. You could categorize the problem another way, but the issue is whether the agent can use the instruction when it acts.（引自上游）违反点：`This isn't mainly about prompt length`、`I'm not arguing that documentation doesn't matter`、`You could categorize the problem another way` 三处都在回应原文里没有出现过的说法。
anchor: `### 34. Answering objections no one raised`
notes:
- intent: 上游给了识别信号——"Watch for an unattributed statement about what the writer does not mean, especially when the topic appears nowhere else."。判据是可查的：被否定的那个话题在文章别处出不出现。作者还专门排除了一个假阳性（直接论断里的否定不算），说明他知道这条规则容易误伤。
- existing: 疑似对应 EN-P-041。
- Wikipedia 归属：**作者补的**（aboudjem 把 Argument Residue 编为 P54，属 craft set，且自述与其他项目的术语无关地独立写成）。

### U-bld-057
category: protection
language: en
rule_summary: 只删掉没有支撑的那部分辩解；辩解里如果含有一个真实的主张，就把那个主张直接陈述出来；原文点了名或完整回应了的反对意见要保留。
positive: 把 "I'm not arguing that documentation doesn't matter, but the agent has to be able to act on it." 改成 "The agent has to be able to act on the documentation."，保住后半的主张。
negative: 看到 `I'm not saying` 就把整句删掉，连同句子后半的真实主张一起删了。违反点：删掉了含有真实主张的部分，本条只允许删没有支撑的辩解。
anchor: `Remove only the unsupported defense.`
notes:
- intent: 上游把三种处置写全了（只删没支撑的、含真主张的要陈述出来、点了名的反对意见要留）。它防的是把一条模式规则当成关键词删除器用：这些触发词后面常常挂着真正的内容，按词删会把内容一起删掉。
- existing: 疑似对应 ALL-PROT-020（删掉无功能的连接词和元叙述时，原文真实存在的逻辑关系要保留下来）。
- 与 U-bld-056 拆开的理由：一份改写可以正确识别这个模式却用错误的方式修它，两条各自可判定。

### U-bld-058
category: pattern
language: en
rule_summary: 不引入一个没有读者会考虑的备选方案、在一个从句里否掉它、然后再也不提。触发词：A tempting option / approach would be、One might be tempted to、An obvious approach would be、You might think… but、It would be easy to just、Some would suggest。修法是删掉这个假选项，直接说出真正的约束。
positive: Session tokens are rotated every 24 hours, in place, and clients refresh transparently.（引自上游）
negative: Session tokens are rotated every 24 hours. A tempting approach would be to rotate them by restarting the auth service on a cron job, but that would drop every active session. Rotation happens in place, and clients refresh transparently.（引自上游）违反点：`A tempting approach would be to…, but…` 引入并否掉了一个没人会提的方案，之后再没提过。
anchor: `### 35. Rejecting fake alternatives`
notes:
- intent: 上游给了一个很具体的成因——"This often leaves an old drafting idea in the final text."。作者认为这类句子是起草过程的残留：写的人考虑过这个方案、否掉了，但把这个思考过程留在了成稿里。这个成因解释了为什么修法是删掉而不是改写。
- existing: 疑似对应 EN-P-041，但判据不同：EN-P-041 管的是"没人提出过的反对意见"，本条管的是"没人会考虑的备选方案"。一段文字可以只有其中一种。可能属于现有规则里没有覆盖的那一半。
- Wikipedia 归属：**作者补的**（aboudjem 把 Argument Residue / Leftover Hedge Debris 编为 P54、P55，属 craft set）。

### U-bld-059
category: measurement
language: en
rule_summary: 判定门槛：一个被否掉的方案可能是正当的；几个简短、互不相关的否定才是更强的信号。逐句问它增加了什么新信息；如果一句话只是记录了一次早先的编辑，就围绕这一段的主旨重写整段。
positive: 全文只有一处被否掉的方案且它交代了一条真实约束，不标记。
negative: 一段里有三处简短、互不相关的"某某做法行不通"，助手只把其中一处标了。违反点：多个简短不相关的否定聚集时信号更强，应当整段处理而不是逐处点掉。
anchor: `One rejected option may be valid.`
notes:
- intent: 上游把单次和多次分开处理（"One rejected option may be valid. Several short, unrelated rejections are a stronger sign."），并给了一个通用的判据 "Ask what new information each sentence adds."。它防的是把一条模式规则用成一次命中就改：这个模式的证据强度依赖出现次数。
- existing: 疑似对应 ALL-M-002（多种痕迹聚集才构成信号）。
- 与 U-bld-058 拆开的理由：一份改写可以识别出这个模式却按单次处理，判定逻辑不同。

### 2.9 假阳性防护（`## Check for false positives`）

### U-bld-060
category: measurement
language: en
rule_summary: 以下十一项单独出现时都不构成 AI 的证据，不得据此标记或改写：语法和风格完美；随意与正式混用；平淡或机械的文风（没有具体痕迹的干燥就只是干燥）；正式或学术用词（§7 只列了特定的词，不是让你简化每一个正式词）；评论里的书信式开头或结尾；孤立出现的常见过渡词（一个 however 不是痕迹）；孤立的弯引号（macOS、Word、Google Docs 和多数 CMS 默认自动转弯）；孤立的破折号（破折号只有与套路化的推销节奏同时出现才算证据）；单独一句用于强调的短句（只有连排才标记）；作者刻意重复的句首（"She came. She saw. She conquered." 这类为了制造节奏或压迫感的重复，只有在重复不带来任何东西时才改）；缺少引用（网上大部分内容都没有引用）；正确而复杂的排版（可视化编辑器和模板不用 AI 也能产出干净的输出）。
positive: 一篇语法完美、句长一致、用了一处弯引号的文章，没有其他痕迹，不标记。
negative: 因为一篇文章语法完美、用了一个 however 和一处弯引号，就判定它有 AI 味并改写。违反点：三项都属于单独出现不算证据的项目。
anchor: `### What not to flag`
notes:
- intent: 上游写了这一节的总纲——"A person may use some of these patterns. Do not treat any item below as proof by itself."。作者的立场是模式表会误伤真人写作，因此必须配一份等长的免责清单；十一项里有五项（弯引号、破折号、短句、重复句首、正式用词）直接指向他自己在前面立的规则，是对那些规则的自我限制。
- existing: 疑似对应 ALL-M-002。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表把 "detectors are unreliable, do not judge on one tell" caution 映射到 aboudjem 的 Guardrails 一节）。
- 十一项共用同一条判定逻辑（单独出现不算证据），合为一个单元；另外三项（Useful limits and disclaimers、Real alternatives、Secondhand text）不是"不算证据"而是改写保护，分别拆成 U-bld-061、U-bld-062、U-bld-063。

### U-bld-061
category: protection
language: en
rule_summary: 保留有用的限定和声明：适用范围声明、法律与安全提示、真实的更正、点了名的反对意见、答复，以及 FAQ 的答案。
positive: 一段"本文只讨论 v3 及以上版本"的范围声明原样保留。
negative: 把一段安全提示当成"保留语堆叠"删掉了。违反点：安全提示属于必须保留的限定，不是要清理的保留语。
anchor: `- **Useful limits and disclaimers.**`
notes:
- intent: 上游把这一项混在 "What not to flag" 清单里，但它的措辞是 "Keep…" 而不是 "Do not treat as proof"，处置方式与其余十一项不同。推断作者的意图：§24（保留语堆叠）和 §34（回应没人提的反对）这两条规则最容易误伤的正是这几类内容，因为它们在形式上就是限定和辩解。推断依据是这一项的措辞与同一清单里其余项目不一致。
- existing: 疑似对应 ALL-PROT-020 与 ALL-PROT-014。
- 拆分判断：与 U-bld-060 拆开，因为判定逻辑不同——那条是"不算证据"，本条是"必须保留"。

### U-bld-062
category: protection
language: en
rule_summary: 不改写出现在引语、标题、专有名词里的被盯上的短语，也不改写那些在讨论这个短语而不是在使用它的例子。
positive: 一篇讲 AI 味的文章里引用了 "delve into" 作为例子，原样保留。
negative: 把一本书名里的 `Vibrant Landscapes` 按 §4 和 §7 的词表改掉了。违反点：这是专有名词，不是作者在使用这些词。
anchor: `- **Secondhand text.**`
notes:
- intent: 上游写了判据——"where the phrase is being discussed rather than used"。这是使用与提及的区分：同一个词组出现在文本里可能是作者在用它，也可能是作者在谈它，后者不受词表约束。它防的是一个自指的失败：讨论 AI 写作的文章必然要引用 AI 写作的例子。
- existing: 疑似对应 ALL-PROT-008。
- 与 upstream-conorbronsdon-avoid-ai-writing 的 U-aaw-055（Self-reference escape hatch）是同一条规则，两个来源谱系不同，构成独立证据。

### U-bld-063
category: measurement
language: en
rule_summary: 保留读者在设计文档、教程或论证里可能真的会考虑的选项；只删掉那个不太可能被考虑、被文中否掉且再没用到的选项。
positive: 一份设计文档里列出了两个真实的技术选型并说明为什么选了其中一个，两个都保留。
negative: 因为句子里出现了"另一个做法是…"，就把一份设计文档里真实的选型比较删了。违反点：这是读者会真的考虑的选项，不是 §35 说的假备选方案。
anchor: `- **Real alternatives.**`
notes:
- intent: 上游把这一项放在假阳性清单里，是为了给 §35 划边界：§35 要删的是起草残留，而设计文档和教程里讨论备选方案是这些体裁的正当内容。它防的是把一条为随笔写的规则套到技术文档上。
- existing: 现有规则里没有。EN-P-041 没有这条体裁例外。
- 与 U-bld-059 的关系：U-bld-059 给的是数量判据（几个简短不相关的否定才是强信号），本条给的是体裁判据（这个选项读者会不会真的考虑），两条都限制 §35 但判据不同。

### U-bld-064
category: measurement
language: en
rule_summary: 拿不准的时候看有没有几个模式同时出现：一处破折号什么都证明不了，同一段里出现几个套路化模式才是更强的证据。
positive: 一段里同时出现广告腔、意义充值和三项排比，判为有信号。
negative: 一篇文章里只有一处破折号，据此判定它是 AI 写的。违反点：单个模式不构成证据，本条要求看聚集。
anchor: `When unsure, look for several patterns together.`
notes:
- intent: 上游用这一句收束整节假阳性防护，把前面十一项的道理提炼成一条可执行的规则。它与 U-bld-060 的关系是：那条列出了哪些东西单独出现不算数，本条给出了正面的判据（要几个一起看）。
- existing: 疑似对应 ALL-M-002。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表的 "do not judge on one tell" caution）。

### U-bld-065
category: protection
language: en
rule_summary: 以下承载作者声口的细节要保留，除非它们损害了意思：具体而不寻常的细节（一个真实地址、一句奇怪的引语、"the lawyer who used to work upstairs from my dentist" 这样的说法）；复杂心情和没有解决的张力；有年代印记的指涉（能对应到某一年某个圈子的俚语、梗、内部笑话，模型要滞后一年以上）；作者能说出理由的第一人称选择；句长的长短变化；真实的插话、括注和自我纠正（"(I keep wanting to say 'almost' here, but it really was certain.)"，模型很少这样打断自己）。
positive: 一句括号里的自我纠正原样保留。
negative: 把一句带年代印记的俚语换成一个通用说法。违反点：有年代印记的指涉属于必须保留的作者声口细节。
anchor: `### Human details to keep`
notes:
- intent: 上游给这一节的说明是 "These details often carry the writer's voice."。这六项的共同点是它们在形式上都像缺陷（不寻常、没解决、过时、不齐整、打断自己），因此正是改写工具最想抹平的东西；作者把它们列成一份保留清单，是在给改写工具的默认倾向设一道闸。其中"模型滞后一年以上"和"模型很少这样打断自己"是他给出的两条依据。
- existing: 疑似对应 ALL-PROT-017 与 ALL-PROT-013。
- Wikipedia 归属：**Wikipedia 原有**（覆盖表的 human-writing positive indicators）。
- 六项共用同一条判定逻辑，合为一个单元；第七项（2022 年 11 月 30 日之前的编辑）判定逻辑不同，拆成 U-bld-066。

### U-bld-066
category: measurement
language: en
rule_summary: 2022 年 11 月 30 日（ChatGPT 公开发布日）之前写下的文字，除极少数例外，不是 AI 写的。
positive: 一段有确切时间戳、写于 2019 年的文字，不按 AI 痕迹处理。
negative: 一段 2015 年的博客文章因为句长一致、用了 delve，被判定有 AI 味。违反点：写作时间早于 2022 年 11 月 30 日，这条判据优先。
anchor: `- **Edits made before November 30, 2022.**`
notes:
- intent: 上游给了这个日期的含义（ChatGPT 的公开发布日）和结论（"Anything older than that is, with very rare exceptions, not AI-written."）。这是全文唯一一条不看文本本身、只看元数据的判据，而且它的判定力强于任何模式——它防的是把 2022 年之前的人类写作当成 AI 输出。
- existing: 疑似对应 ALL-PROT-013（原文标明或可推知的写作年代属于事实），但那条管的是"不得改掉时代特征"，本条管的是"时间可以直接排除 AI 嫌疑"，判据不同。**这条具体判据现有规则里没有。**
- Wikipedia 归属：**Wikipedia 原有**（覆盖表的 human-writing positive indicators 明确写了 "predating Nov 2022"）。
- 注意这条判据依赖 Wikipedia 编辑历史这个特定语境（编辑有时间戳）；用在一般散文上时需要一个可信的写作时间，上游没有说明这个时间从哪里来。

### 2.10 返回方式（`## How to return the result`）

### U-bld-067
category: process
language: both
rule_summary: 默认（用户粘贴文本）时返回三样东西：草稿、一份还剩哪些 AI 模式的简短清单、最终改写。
positive: 输出依次给出草稿、剩余模式清单、最终稿。
negative: 只返回最终稿。违反点：缺少草稿和剩余模式清单两项。
anchor: `**Pasted text (default).**`
notes:
- intent: 上游未说明理由。推断：这三样对应改写流程的三个阶段（第二步的草稿、第三步的自查、第四步的终稿），把它们全部交给用户，等于把中间过程公开。推断依据是 `## Rewrite process` 四步与这三样输出一一对应。
- existing: 疑似对应 ALL-PROC-007 与 ALL-PROC-008；"把草稿一起交出去"这一层现有规则里没有。

### U-bld-068
category: process
language: both
rule_summary: 用户点名一个文件时，照常跑完整的改写流程，但只把最终文本写进文件，然后给用户一段简短总结。
positive: 文件里只写最终文本，对话里给一段简短总结。
negative: 把草稿和剩余模式清单也写进了文件。违反点：文件模式下只应写最终文本。
anchor: `**File mode.**`
notes:
- intent: 上游未说明。推断：文件是产物，中间过程不该进产物；但流程本身不能因为输出形式变了就缩水，所以作者特意写了"跑完整的改写流程"。推断依据是这一句的措辞（"run the full rewrite process but write only the final text"）。
- existing: 疑似对应 ALL-PROC-021。

### U-bld-069
category: protection
language: both
rule_summary: 文件模式下只改散文；代码块、YAML 元数据、数据和链接目标保持不变。
positive: 改写一份带 frontmatter 和代码块的 markdown 文件，只动散文段落。
negative: 顺手把代码块里的注释也改得更自然了。违反点：代码块属于保持不变的范围。
anchor: `**File mode.**`
notes:
- intent: 上游只写了 "Change prose only. Keep code blocks, YAML metadata, data, and link targets unchanged."。推断：这四类内容的共同点是改动会产生功能后果而不只是阅读后果——代码会跑不通、元数据会解析失败、链接会失效。推断依据是四类的选取，它们不是按"重要性"选的，是按"改了会坏"选的。
- existing: 疑似对应 ALL-PROC-016 与 ALL-PROT-008；"链接目标"这一项现有规则里没有明确列出。
- 与 U-bld-068 拆开的理由：一份文件模式的改写可以只写最终文本却改坏了代码块，两条各自可判定。

### U-bld-070
category: process
language: both
rule_summary: 另一个任务把这个 skill 用于拉取请求、提交信息或文档时（内嵌模式），只返回最终文本。
positive: 被当成流程的一步调用时，只返回改好的提交信息正文。
negative: 被当成流程的一步调用时，仍然返回草稿加剩余模式清单加终稿三段。违反点：内嵌模式只应返回最终文本。
anchor: `**Embedded mode.**`
notes:
- intent: 上游未说明。推断：内嵌调用的消费者是另一个程序或流程，不是人，中间过程对它没有用且会污染输出。推断依据是这一条列举的三个场景（PR、提交信息、文档）都是输出会被直接使用的地方。
- existing: 疑似对应 ALL-PROC-021。

### 2.11 改写流程（`## Rewrite process`）

### U-bld-071
category: process
language: both
rule_summary: 第一步：读原文，标出每一处 AI 模式。
positive: 读完原文后先把每一处命中标出来，再写草稿。
negative: 读一段改一段，没有先做整体标记。违反点：跳过了先通读标记这一步。
anchor: `## Rewrite process / 1. Read the source and mark each AI pattern.`
notes:
- intent: 与 U-bld-001（`## What to do` 第 1 条）是同一条规则在两个位置的重复。推断：作者把它写进流程，是为了让"先标记"成为一个有序步骤而不只是一条原则。
- existing: 疑似对应 ALL-PROC-009。
- 与 U-bld-001 归并时算同一来源内部的重复，不构成 evidence 的增量。

### U-bld-072
category: process
language: both
rule_summary: 第二步：写一版草稿，把它读出声，检查节奏、细节、is 和 has 这类简单动词，以及正式程度是否合适。
positive: 写完草稿念一遍，发现有两句读起来拗口，标出来。
negative: 写完草稿直接进入自查问题，没有朗读检查。违反点：跳过了朗读这一步。
anchor: `## Rewrite process / 2. Write a draft. Read it aloud.`
notes:
- intent: 上游未说明为什么要读出声。推断：朗读是检查节奏的唯一可靠方式——句长变化、拗口的从句、机械的重复在默读时容易被跳过。上游列出的四项检查里，"节奏"排第一，而它正是靠听才能发现的那一项。推断依据是这四项检查的顺序和"读出声"这个动作的搭配。
- existing: 现有规则里没有。ALL-PROC-014 规定了交付前的自查清单，但没有"朗读"这个动作，也没有"检查 is / has 这类简单动词有没有回来"这一项。

### U-bld-073
category: process
language: both
rule_summary: 第三步的第一个问题：还有哪里听起来像 AI 生成的？
positive: 写完草稿后明确问自己这个问题并列出还剩的几处。
negative: 自查时只核对了事实清单，没有问这一句。违反点：漏了第三步的两个问题之一。
anchor: `## Rewrite process / 3. Ask two questions:`
notes:
- intent: 上游未说明。推断：这个问题的作用是让改写者用读者的视角再看一遍，而不是用"我改过哪几处"的视角；后者只会确认自己改过的地方，前者会发现改写本身引入的新痕迹。推断依据是这个问题被写成一个开放式提问而不是一份清单。
- existing: 疑似对应 ALL-PROC-014（"再问自己一句'这稿子哪里还像 AI 写的'，诚实列出两三点"）。

### U-bld-074
category: protection
language: both
rule_summary: 第三步的第二个问题：这次改写有没有增加或去掉任何事实、名字、数字、日期、引语、引用、排名或其他主张？任何没有支撑的新增或丢失的主张都算错误。
positive: 逐项对照原文的事实清单，确认改写稿一条没多、一条没少。
negative: 自查时只看了文风，没有核对事实的增删。违反点：漏了这个问题，而它是本 skill 唯一一条把结果直接判为"错误"的检查。
anchor: `## Rewrite process / 3. Ask two questions:`
notes:
- intent: 上游用了全文最重的措辞——"Treat any unsupported addition or lost claim as an error."。别处的规则说的是"不要这样写"，这一条说的是"这样就是错的"。作者把八类内容（事实、名字、数字、日期、引语、引用、排名、其他主张）逐一列出，是为了让这个核对能逐项做而不是凭印象做。
- existing: 疑似对应 ALL-PROT-019（改前列两份清单、改后逐项核对）。
- 与 U-bld-073 拆开的理由：两个问题的判定对象不同（一个看文风、一个看事实），一份自查可以只做其中一个。

### U-bld-075
category: process
language: both
rule_summary: 第四步：写最终版时把每个点自然地说出来，不要一个一个地给被标记的短语打补丁。
positive: 把整段按它真正要说的意思重写一遍。
negative: 逐个把命中的短语换成同义的替代词，句子结构一动不动。违反点：这是逐处打补丁，不是重新把话说出来。
anchor: `## Rewrite process / 4. Write the final version.`
notes:
- intent: 上游写了 "State each point naturally instead of patching one flagged phrase at a time."。它防的是一种可以骗过模式表却骗不过读者的改写：每一处命中都被替换掉了，但句子的骨架还是生成时的那个骨架，读起来仍然是机器写的。
- existing: 疑似对应 ALL-PROC-012（只做局部换词不算完成改写）。

### U-bld-076
category: process
language: both
rule_summary: 一句话怎么改都别扭时，围绕这一段的主旨把整段重写。
positive: 一句话改了三遍还是拗口，就把整段按它的主旨重写。
negative: 一句话改不顺就把它删了。违反点：本条给的处置是重写整段，不是删句。
anchor: `## Rewrite process / 4. Write the final version.`
notes:
- intent: 上游写了 "If a sentence stays awkward, rewrite the paragraph around its main point."。推断作者的判断：一句话反复改不顺，问题通常不在这句话，而在它在段落里承担的位置不对；在句子层面继续改是在错的层面用力。推断依据是修法给的是提高一层（段落），不是换一个说法。
- existing: 疑似对应 ALL-P-006 与 ALL-PROC-012。

### U-bld-077
category: process
language: en
rule_summary: 最终版要再执行一次 §14 的破折号规则。
positive: 终稿写完后再跑一次破折号检查。
negative: 第二步的草稿检查过破折号，终稿就没再查。违反点：终稿必须再执行一次 §14。
anchor: `## Rewrite process / 4. Write the final version.`
notes:
- intent: 上游未说明。推断：破折号是改写过程本身会引入的东西——重写句子时最容易顺手加一个破折号，所以草稿阶段的检查不够，终稿要再查一次。推断依据是这条被专门挂在第四步（写终稿）而不是第三步（自查）上，且它是全文唯一一条被要求执行两次的模式规则。
- existing: 疑似对应 EN-P-026 与 ALL-PROC-014。
- 与 U-bld-035（交付前搜索破折号字符）的关系：那条给的是搜索动作，本条给的是执行时机，两条一起构成破折号规则的完整执行方式。

---

## 3 覆盖表

| 小节 / 行 | 归属单元 / 说明 |
|---|---|
| frontmatter（name / description / license / metadata.version） | 非规则内容：技能名称、触发描述、许可证、版本；description 里的 "Based on Wikipedia's 'Signs of AI writing.'" 是出处声明 |
| `# Humanizer: remove AI writing patterns` 与第 15 行总纲 | 非规则内容：一句话总纲，内容由 U-bld-002、U-bld-003 覆盖 |
| 第 17 行（Wikipedia 出处与链接） | 非规则内容：出处声明；用于本清单第 1.1 节的谱系判断 |
| `## What to do` 引导句 | 非规则内容：分节引导 |
| 1. **Find AI patterns.** | U-bld-001 |
| 2. **Keep every claim.** | U-bld-002 |
| 3. **Do not invent facts.** | U-bld-003、U-bld-004、U-bld-005、U-bld-006 |
| 4. **Match the voice.** | U-bld-007 |
| 第 28 行（输入类型决定返回方式） | 非规则内容：指向 `## How to return the result` 的交叉引用 |
| `## Match the writer's voice` 1. Read the sample first. | U-bld-008 |
| `## Match the writer's voice` 2. Match those habits. | U-bld-009 |
| `## Match the writer's voice` 3. If there is no sample… | 非规则内容：说明无样本时回落到下文的通用指引 |
| `A writing sample takes priority over these style rules.` | U-bld-010 |
| `## Add personality only when it fits` 第 42 行 | U-bld-011 |
| `Use personality in blog posts, essays…` | U-bld-012 |
| `When personality fits, keep the writer's opinions…` | U-bld-013 |
| `Never invent facts to make the text feel personal.` | U-bld-014 |
| `## Content patterns` 小节标题 | 非规则内容：仅为分组标题 |
| `### 1. Inflated claims about importance and legacy` | U-bld-015 |
| `### 2. Name-dropping to prove importance` | U-bld-016 |
| `If the source explains what the person said and where` | U-bld-017 |
| `### 3. Shallow analysis with -ing phrases` | U-bld-018 |
| `### 4. Sales language` | U-bld-019 |
| `### 5. Vague sources` | U-bld-020 |
| `Name a real source when the source text provides one.` | U-bld-021 |
| `### 6. Formulaic challenges and outlook sections` | U-bld-022 |
| `Add details such as dates or public actions only when…` | U-bld-023 |
| `## Language and grammar patterns` 小节标题 | 非规则内容：仅为分组标题 |
| `### 7. Overused AI words` | U-bld-024 |
| `### 8. Avoiding is and are` | U-bld-025 |
| `### 9. Not X but Y and clipped negative endings`（Not X but Y 部分） | U-bld-026 |
| `### 9`（clipped negative endings 部分） | U-bld-027 |
| `### 10. Forced groups of three` | U-bld-028 |
| `### 11`（Changing names 部分） | U-bld-029 |
| `### 11`（repeating sentence openings 部分） | U-bld-030 |
| `Do not ban the repeated word.` | U-bld-031 |
| `### 12. False from X to Y ranges` | U-bld-032 |
| `### 13. Passive voice and missing subjects` | U-bld-033 |
| `## Style patterns` 小节标题 | 非规则内容：仅为分组标题 |
| `### 14. Em and en dashes`（Rule 与两组例句） | U-bld-034 |
| `Before returning the rewrite, search for` | U-bld-035 |
| `### 15. Too much bold text` | U-bld-036 |
| `### 16. Lists with bold mini-headings` | U-bld-037 |
| `### 17. Title case in headings` | U-bld-038 |
| `### 18. Emojis` | U-bld-039 |
| `### 19. Curly quotation marks` | U-bld-040 |
| `## Chatbot patterns` 小节标题 | 非规则内容：仅为分组标题 |
| `### 20. Chatbot text left in the answer` | U-bld-041 |
| `### 21`（cutoff disclaimer 部分） | U-bld-042 |
| `### 21`（speculative gap-fill 部分） | U-bld-043 |
| `### 22. Overly agreeable tone` | U-bld-044 |
| `## Filler and hedging` 小节标题 | 非规则内容：仅为分组标题 |
| `### 23. Filler phrases` | U-bld-045 |
| `### 24. Too many qualifiers` | U-bld-046 |
| `### 25. Generic positive endings` | U-bld-047 |
| `### 26. Too many hyphenated word pairs` | U-bld-048 |
| `### 27. Pretending to reveal a deeper truth` | U-bld-049 |
| `### 28. Announcing the next point`（含随意语域例句） | U-bld-050 |
| `### 29. A heading repeated in the first sentence` | U-bld-051 |
| `### 30. Writing about the previous version` | U-bld-052 |
| `### 31. Forced punchlines and dramatic fragments` | U-bld-053 |
| `### 32. Formulaic sayings` | U-bld-054 |
| `### 33. Fake-candid openings` | U-bld-055 |
| `### 34. Answering objections no one raised` | U-bld-056 |
| `Remove only the unsupported defense.` | U-bld-057 |
| `### 35. Rejecting fake alternatives` | U-bld-058 |
| `One rejected option may be valid.` | U-bld-059 |
| `## Check for false positives` 小节标题 | 非规则内容：仅为分组标题 |
| `### What not to flag` 与其中十一项 | U-bld-060 |
| `- **Useful limits and disclaimers.**` | U-bld-061 |
| `- **Real alternatives.**` | U-bld-063 |
| `- **Secondhand text.**` | U-bld-062 |
| `When unsure, look for several patterns together.` | U-bld-064 |
| `### Human details to keep` 与其中六项 | U-bld-065 |
| `- **Edits made before November 30, 2022.**` | U-bld-066 |
| `## How to return the result` 小节标题 | 非规则内容：仅为分节标题 |
| `**Pasted text (default).**` | U-bld-067 |
| `**File mode.**` | U-bld-068、U-bld-069 |
| `**Embedded mode.**` | U-bld-070 |
| `## Rewrite process` 1. Read the source and mark each AI pattern. | U-bld-071 |
| `## Rewrite process` 2. Write a draft. Read it aloud. | U-bld-072 |
| `## Rewrite process` 3. 第一个问题 | U-bld-073 |
| `## Rewrite process` 3. 第二个问题与 "Treat any unsupported addition or lost claim as an error." | U-bld-074 |
| `## Rewrite process` 4. State each point naturally… | U-bld-075 |
| `## Rewrite process` 4. If a sentence stays awkward… | U-bld-076 |
| `## Rewrite process` 4. Apply the dash rule in §14. | U-bld-077 |
| 第 450 行（返回本文要求的结果） | 非规则内容：指向 `## How to return the result` 的交叉引用 |
| `## Source` 与第 456 行的 Wikipedia 引文 | 非规则内容：出处声明与被引用的 Wikipedia 论点；用于本清单第 1.1 节和各单元 intent 的依据 |

覆盖表的每一行都有归属，SKILL.md 里没有未归属的段落。

---

## 4 拆分时拿不准的地方

1. **Wikipedia 归属的判断是间接的。**第 1.1 节的划分依据是 upstream-aboudjem-humanizer-skill 快照里那份 `Coverage against Wikipedia` 对照表，不是 Wikipedia 原文。这带来两类误差：一是 aboudjem 的对照表本身可能不完整（它是为 aboudjem 自己的 55 条模式写的，不是为 blader 的 35 条写的）；二是对于不出现在对照表里的条目，我判为"作者补的"用的是反面证据（没提到就当作没有），强度弱于 §13、§24、§26、§30、§32、§34、§35 那几条——那几条有 aboudjem 明确自述 craft set 为独立撰写的正面证据。三条存疑条目（U-bld-027、U-bld-043、U-bld-044）已在第 1.1 节单列。如果归并阶段要把 independent_sources 的判断建立在这个划分上，建议先直接核对 Wikipedia 原文。

2. **U-bld-005（可以加观点、不可以加事实主张）与现有 ALL-PROT-001 的冲突是实质性的，不是措辞差异。**现有规则的禁止清单里明确含"观点"，blader 明确允许。这不是我拆错了，上游原文写得很清楚。归并时按 criteria.md 第 1 条（事实保护优先）和第 8 条（冲突要留痕）处理，两条都要进 decisions.yaml。upstream-conorbronsdon-avoid-ai-writing 的 U-aaw-087（原文没有 I，改写稿就没有 I）站在现有规则一边，可以作为裁决的参考。

3. **§9 拆成两条、§11 拆成两条、§21 拆成两条，粒度与其他小节不一致。**这三节各自把两个判定逻辑不同的现象写在了同一个编号下。我按判定逻辑拆开了，代价是这三节的单元数与"一个编号一个单元"的直觉不符。反过来，§23（六对填充短语）、§24（含例外条件）、§26（含位置判据）、§30（含体裁例外）、§50（正式与随意两种语域）我都合成了一个单元，因为它们共用同一条判定逻辑。这两类处理的判据是一致的（看判定逻辑而不是看编号），但结果看起来不齐整，归并时如果需要与编号一一对应，可以按覆盖表回溯。

4. **`### What not to flag` 的十四项里，三项被我拆了出来。**十一项写成 "Do not treat as proof"（不算证据），三项（Useful limits and disclaimers、Real alternatives、Secondhand text）写成 "Keep…" / "Do not rewrite…"（必须保留、不得改写）。前者是 measurement，后者是 protection，处置方式不同，因此我没有把十四项合成一个单元。上游把它们混在同一份清单里，可能是无意的，也可能是作者认为"不算证据"和"不要改"是一件事——我按前一种理解拆的，这是我的判断。

5. **language 的划分。**流程类（U-bld-001 至 U-bld-014 的大部分、U-bld-067 至 U-bld-077）标 both，因为判定逻辑不依赖具体语言；模式类和假阳性清单标 en，因为触发词、例句和判据（Title Case、弯引号、连字符、句首 Wh- 结构、is/are）都依赖英文。边界上有几条我拿不准：U-bld-028（凑三项）、U-bld-030（重复句首）、U-bld-032（假跨度）、U-bld-051（标题复述）、U-bld-053（碎片句连排）的判定逻辑在中文里同样成立，本仓库也确实有对应的中文规则（ZH-P-002、ZH-P-003 等）。我按"上游的触发词和例句全是英文"标了 en。如果归并阶段要标 both，需要为它们各补一组中文正反例（extraction.md 禁止把英文例子直译）。

6. **U-bld-066（2022 年 11 月 30 日之前的文字不是 AI 写的）在一般散文上怎么用，上游没有说。**这条判据依赖一个可信的写作时间，而 Wikipedia 的编辑有时间戳、一般粘贴进来的文本没有。上游把这条直接搬过来，没有处理这个差异。归并时如果采纳，需要补一句"时间从哪里来"。

7. **U-bld-072 里的"读出声"这个动作，助手无法真的执行。**上游写的是给人看的流程（"Read it aloud"），落到助手身上只能变成"按朗读会发现的那几类问题再查一遍"。我在 rule_summary 里保留了原文的动作，没有替它改写成助手可执行的形式，因为改写会丢掉上游的原意。归并时需要决定是照录还是转译。

---

## 5 疑似与现有规则或别的来源重合的单元

### 与现有 144 条规则明确冲突的（归并时按 criteria.md 第 8 条两条都要留痕）

| 单元 | 现有规则 | 冲突点 |
|---|---|---|
| U-bld-005 | ALL-PROT-001 | 本条允许在声口需要时新增观点；ALL-PROT-001 明确把"观点"列进禁止新增的清单 |
| U-bld-006 | ALL-G-003 | 本条给虚构文本一个"可以编造细节"的豁免、其余规则照常；ALL-G-003 的处置是模式表整体不适用、先说明再问用户 |
| U-bld-034 | EN-P-026 | 本条是禁令加作者样本例外；EN-P-026 是按篇幅允许长文留一到两处 |
| U-bld-040 | EN-P-037 | 本条在作者用直引号时把弯引号改成直引号；EN-P-037 是"原稿用哪种就保持哪种，不统一改成另一种"，原稿混用时两者处置不同 |

### 现有规则里没有对应的单元（8 条）

- U-bld-008（分析用户提供的写作样本，六个维度）
- U-bld-010（写作样本优先于风格规则，破折号按样本频率保留）
- U-bld-027（句尾截断式否定，"…, no guessing"）
- U-bld-035（交付前对破折号字符做机械搜索，含四种变体）
- U-bld-058（否掉一个没人会考虑的假备选方案；与 EN-P-041 管的"没人提出的反对意见"判据不同）
- U-bld-063（设计文档、教程、论证里的真实备选方案要保留）
- U-bld-066（2022 年 11 月 30 日之前的文字不是 AI 写的）
- U-bld-072（朗读检查，含"is / has 这类简单动词有没有回来"这一项）

### 与本轮另两个英文来源的对照

| blader 单元 | hardikpandya | conorbronsdon | 关系 |
|---|---|---|---|
| U-bld-015 | 无 | U-aaw-027 | 同一模式；conorbronsdon 排 P0 |
| U-bld-016 | 无 | 无 | blader 独有（Wikipedia 原有） |
| U-bld-019 | 无 | 无 | blader 独有（Wikipedia 原有） |
| U-bld-020 | 无 | U-aaw-026 | 同一模式；conorbronsdon 排 P0 |
| U-bld-024 | 无 | U-aaw-029 | 同一模式（均可追溯到 Wikipedia） |
| U-bld-025 | 无 | U-aaw-051 | 同一模式（均可追溯到 Wikipedia，不构成独立证据） |
| U-bld-026 / U-bld-027 | U-ssl-004 / U-ssl-005 | U-aaw-043 | 三方都有，判据各不相同 |
| U-bld-028 | U-ssl-015 | U-aaw-049 | 三方都有；强度从弱到强为 blader < conorbronsdon < hardikpandya |
| U-bld-029 | 无 | U-aaw-032 | 同一模式（均可追溯到 Wikipedia） |
| U-bld-030 | 无 | 无 | blader 独有（作者补的） |
| U-bld-033 | U-ssl-008 / U-ssl-009 / U-ssl-010 | U-aaw-048 的 false agency | 三方都有；blader 带条件、hardikpandya 无条件、conorbronsdon 归为判断型检查 |
| U-bld-034 / U-bld-035 | U-ssl-017 | U-aaw-035 / U-aaw-091 | **三方冲突**：禁令加样本例外 / 无条件禁 / 每千词一处上限 |
| U-bld-036 / U-bld-037 / U-bld-039 | 无 | U-aaw-034 | 部分重合（bold overuse） |
| U-bld-041 / U-bld-042 / U-bld-044 | 无 | U-aaw-024 / U-aaw-025 | 同一组模式（均可追溯到 Wikipedia） |
| U-bld-046 | 无 | U-aaw-040 | 同一模式（均为作者补的，构成独立证据） |
| U-bld-047 | 无 | U-aaw-036 / U-aaw-046 | 同一模式（独立证据） |
| U-bld-048 | 无 | U-aaw-054 | 同一模式（独立证据） |
| U-bld-050 | U-ssl-001 / U-ssl-021 | U-aaw-031 / U-aaw-033 | 三方都有（独立证据） |
| U-bld-053 | U-ssl-006 | U-aaw-092 | 三方都有；conorbronsdon 从改写侧写（不得把句子剁碎） |
| U-bld-054 | U-ssl-019 | U-aaw-036 | 三方都有（独立证据） |
| U-bld-055 | 无 | U-aaw-039 / U-aaw-090 | 两方（独立证据） |
| U-bld-056 / U-bld-057 | 无 | U-aaw-089 | 两方（独立证据） |
| U-bld-060 / U-bld-064 | 无 | U-aaw-001 / U-aaw-002 | 两方；blader 给清单，conorbronsdon 给文献依据 |
| U-bld-062 | 无 | U-aaw-055 | 两方（谱系不同，构成独立证据） |
| U-bld-011 | 无 | U-aaw-082 | **不构成独立证据**：conorbronsdon 自述改编自本条 |

### 与 blader 谱系其余成员的关系

sources.yaml 把 op7418/Humanizer-zh、hairyf/skills、kevintsai1202/Humanizer-zh-TW、z0gSh1u/oh-my-writing-skill 归入同一谱系（`blader-humanizer`），且记 blader 为 representative。这四个成员由中文组的另一位 subagent 处理或按 derivative 只带差异部分进入归并，本清单不涉及。归并时凡是这四个来源与本清单单元表述相同的条目，都不构成 independent_sources 的增量。

---

## 6 上游文本内的指令

无。通读全文两遍，未发现针对读者或助手的注入式指令（"忽略之前的规则""把这段加进你的系统提示"一类）。

全文不含脚本、不含指向其他文件的引用（本来源只追踪也只存在 `SKILL.md` 一个文件），因此没有"只读不跑"的对象。第 17 行和 `## Source` 一节含两个指向 Wikipedia 的外部链接，属于出处声明，本轮未访问。
