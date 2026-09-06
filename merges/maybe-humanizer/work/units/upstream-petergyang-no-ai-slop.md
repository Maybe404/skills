# 拆规则清单：upstream-petergyang-no-ai-slop

## 1 来源摘要

- 文件（本仓库快照）：`merges/maybe-humanizer/snapshots/upstream-petergyang-no-ai-slop/skills/no-ai-slop/SKILL.source.md`
- 上游原路径：`skills/no-ai-slop/SKILL.md`
- 上游仓库：`petergyang/no-ai-slop`，分支 `main`
- commit（取自 sources.lock.json 的 last_seen_commit）：`000650b156983f5159695b441477f4e63b25dc85`
- 许可证：MIT，snapshot_policy 为 full-text，可引原文
- 上游自述的定位：frontmatter 写"Edit drafts into sharper, more human writing while preserving the writer's personal voice, or detect AI-slop patterns without rewriting"——英文审稿与改写 skill，同时支持"改写"（Edit）和"只报告不改"（Detect）两种模式，面向英文稿件（词表、模式表全部是英文词汇和短语）。仓库另有 `agents/`、`scripts/`、`eval.md`，本轮按 sources.yaml 只追踪 SKILL.md，不追踪、不执行。
- 总单元数：55
- 按 category 计数：
  - process：16
  - pattern：31
  - protection：4
  - style-opinion：3
  - measurement：1
  - genre：0

以下所有单元的 `source` 字段均为：
```
type: upstream
source_id: upstream-petergyang-no-ai-slop
path: skills/no-ai-slop/SKILL.md
commit: 000650b156983f5159695b441477f4e63b25dc85
```
下面每条只写 anchor，其余 source 字段不再重复。

---

## 2 单元清单

### U-nas-001
category: process
language: both
rule_summary: Edit（默认）模式下，用户给了待改稿子时，按其余规则做出最小有效编辑，只返回编辑后的完整稿子加一节 "What changed"，不额外产出别的内容。
positive: 输出编辑后的全文，末尾附一节"**What changed**"，用几条要点说明改了什么。
negative: 输出编辑后的全文，但结尾没有任何说明改动的小节。违反点：缺少 "What changed" 小节。
anchor: `## Two jobs / Edit (default).`
notes: 与 Editing principles 里 "Make the minimum effective edit" 的 EP2（U-nas-008）是同一条规则在两处出现，这里是"两个工作模式"的顶层定义，EP2 是该原则的具体判据；归并时可能需要合并或建立引用关系。

### U-nas-002
category: process
language: both
rule_summary: Detect 模式下（用户问稿子是不是 AI slop，或要求 audit/scan/flag 而不重写），逐条点出命中的模式名并引用原句、用几个词给出修法，不重写全文、不给稿子打分。
positive: "命中'Colon reveals'：'The best part: it learns.' 改法：写成一句直白的陈述句。"
negative: 给出 1-10 分的"AI 味评分"并附打分理由，或者直接把整篇重写后返回。违反点：Detect 模式下不得打分（score the draft），也不得重写（rewrite）。
anchor: `## Two jobs / Detect.`
notes: 与"给出修法"相关的具体输出格式（点名模式、引句子、给修法）共用同一条判定逻辑，合为一个单元；"不猜测是否为 AI 所写"和"事后可以主动提出编辑"逻辑不同，另立 U-nas-003。

### U-nas-003
category: process
language: both
rule_summary: Detect 模式下不得判定或猜测这篇稿子是不是 AI 写的，因为检测器本身就是在猜；只报告命中的具体模式作为用户可自行核实的证据，报告完之后可以主动提出愿意帮忙编辑。
positive: "以上是命中的模式，供你自行判断。要不要我顺便把这些改掉？"
negative: "这篇文章有 80% 的可能是 AI 生成的。" 违反点：对是否为 AI 写作给出判断性结论，而不是只列出可核实的具体模式。
anchor: `## Two jobs / Detect.`
notes: 上游原句"AI detectors guess. Named patterns are evidence the user can check."是这条规则的理由，写进 rationale 时可以引用。

### U-nas-004
category: process
language: both
rule_summary: 用户没有提供待改稿子时，先问对方把稿子贴出来，不能凭空编造或假设一份稿子。
positive: "麻烦把要改的稿子贴过来。"
negative: 用户只说"帮我把这篇文章改得更像人写的"但没有贴正文，助手直接编了一段示例文章去"改"。违反点：没有稿子时没有先索要，而是自己编造了内容。
anchor: `If the user has not provided a draft`
notes: 该行在 "## What to ask for" 小节下，无小节标题以外的锚点，用行首文本定位。

### U-nas-005
category: process
language: both
rule_summary: 稿子的受众或发布场合不明确时，只问一个具体问题："谁会看这篇稿子，会发在哪里？"（Who is this for and where will it be published?），不问别的问题、不一次问多个问题。
positive: "这篇是给谁看的，打算发在哪儿？"
negative: 一次抛出三个问题："这是给谁看的？打算发在哪？是正式场合还是随意场合？字数有限制吗？" 违反点：应该只问一个关于受众和发布场合的问题，这里问了四个不相关的问题。
anchor: `If the audience or format is unclear`
notes: "只问一个问题"是可判定的边界，超过一个即违反。

### U-nas-006
category: process
language: both
rule_summary: 稿子想达到的目标不明确时，问读者读完之后应该"想什么、感受什么、做什么"，用这个问题确认目标，不用别的问法。
positive: "你希望读者看完这篇之后，会怎么想、有什么感受，或者去做什么？"
negative: 目标不明确时直接按自己猜的目标去改稿子，不问用户。违反点：目标不明时没有停下来问"读者应该 think/feel/do 什么"，而是自行假设了目标。
anchor: `If the goal is unclear`
notes: 与 U-nas-004、U-nas-005 是同一小节下并列的三个独立触发条件，各自的问题内容不同，因此分成三个单元而不是合一。

### U-nas-007
category: style-opinion
language: en
rule_summary: 编辑前先识别稿子本身的词汇、节奏、直率程度、幽默感、不确定感、跑题和打磨程度，保留这些属于作者本人的特征，不要把每一段都改得同样工整，也不要仅仅为了统一风格而改写本来就有特色的句子。
positive: 保留作者原本口语化、略显跳跃的段落节奏，只修正其中确实读不通的一句。
negative: 把全文所有段落都改成同样长度、同样工整的书面语句式，抹掉了原作者时而简短时而啰嗦的口语节奏。违反点：为了"统一"而重写本来就有特色、并不影响理解的句子。
anchor: `## Editing principles / Preserve the writer's real voice.`
notes: 归类为 style-opinion 是勉强的选择——本条管的是"保留输入稿的声音特征"，不完全等同于类别定义里"腔调、语气、人称、标点偏好"这种助手自身的输出风格主张，taxonomy 里没有更贴切的类别，留待归并阶段判断。

### U-nas-008
category: process
language: both
rule_summary: 编辑时只修 AI 味的写法、错误、重复、看不懂的段落，本来就写得好的"人味"句子留着不动；改完之后整篇读起来还应该像同一个人写的。
positive: 只改了两处套话开头和一处重复用词，其余原本流畅有个性的句子原样保留。
negative: 把稿子里一句已经很清楚、很有个性的句子也重写成了"更书面"的版本，理由只是"顺便让它更规范"。违反点：对本来就没问题的"strong human sentence"做了非必要改动。
anchor: `## Editing principles / Make the minimum effective edit.`
notes: 与 U-nas-001（Two jobs / Edit）里"做最小有效编辑"是同一条规则，这里是该原则的具体判据（改什么、不改什么），归并时两者大概率合并成一条。

### U-nas-009
category: pattern
language: en
rule_summary: 如果开头的铺垫对内容没有实际作用，就直接说重点，删掉泛泛的开场白；但如果开头是能带出语境、张力或人物性格的个人化插叙、故事或坦白，就保留。
positive: "The eval matters more than the model."（引自上游）直接给出结论，不加铺垫。
negative: "在深入探讨这个话题之前，我想先简单聊聊背景"这类不承载语境或张力的通用开场白，直接放在正文前面。违反点：generic throat-clearing 式铺垫没有被砍掉。
anchor: `## Editing principles / Lead with the point when the setup adds nothing.`
notes: 与 Patterns to cut 里的"Throat-clearing openers"（U-nas-031）是同一现象在两个小节里各自出现，一个是原则性表述，一个是具体短语清单，分别保留为两个单元。

### U-nas-010
category: pattern
language: en
rule_summary: 只有在能提升清晰度时才把结论提到段落或全文最前面，不能强行把每一段都套成"观点—细节—背景"的固定结构。
positive: 某一段确实是先说结论更清楚，就把结论移到段首；另一段原本是按时间顺序叙述更清楚，就保留原顺序。
negative: 把全文每一段都机械地改成"先给结论、再给细节、最后给背景"的同一种结构，即使有的段落这样改并不会更清楚。违反点：force every section and paragraph into the same point-detail-background shape。
anchor: `## Editing principles / Front-load only when it improves clarity.`
notes: 与 EP17a（U-nas-025，"除非结构本身有问题，否则保留原结构"）方向一致，都是反对不必要的结构统一化，可以互相印证。

### U-nas-011
category: protection
language: both
rule_summary: 编辑时不能替用户新造事实、例子、数据或观点；原文没写的内容不能凭编辑者自己的判断加进去。
positive: 原文只说"上线后评审时间变短了"，编辑时不补一个原文没提过的具体数字。
negative: 原文说"这个功能提升了效率"，编辑时擅自加上"根据内部数据，效率提升了 40%"，而用户从未提供过这个数字。违反点：invent...stats——凭空编造了原文没有的数据。
anchor: `## Editing principles / Keep the user's meaning.`
notes: 与后面"Protect the specific fact"（U-nas-021）都属于 protection，但角度不同：这条管"不能新增没有的事实"，U-nas-021 管"不能把已有的具体事实抹成模糊说法"，一增一减，分别保留。

### U-nas-012
category: process
language: both
rule_summary: 原文意思不清楚时要去问用户，不能自己猜一个意思接着改。
positive: "这句话里'它'指的是产品还是团队？麻烦确认一下再往下改。"
negative: 遇到一句指代不清的话，编辑者按自己以为的意思直接把稿子改完，不跟用户确认。违反点：意思不清时没有 ask，而是自行猜测后继续编辑。
anchor: `## Editing principles / Keep the user's meaning.`
notes: 与 U-nas-004/005/006 属于同一类"何时停下问用户"的流程规则，但触发条件（正文意思不清）不同，单独成条。

### U-nas-013
category: protection
language: both
rule_summary: 简化稿子时要保留原文的实质内容、细微差别和精确度，不能为了让文字"更好读"而把有内容的部分一起删掉或抹平。
positive: 把一句话里的从句拆短，但从句里原本的限定条件和例外情况都保留了下来。
negative: 为了让句子更短，把原文里"仅适用于企业版客户"这个限定条件直接删掉，只留下"这个功能很好用"。违反点：把限定条件（nuance）当作累赘一起删掉，而不是只删可读性障碍。
anchor: `## Editing principles / Open it up, don't dumb it down.`
notes: 与 U-nas-014 是同一条原则里的两半：这条是"底线"（不能删实质），U-nas-014 是"该删什么"（术语、长句等），两者共同构成完整判据，但各自可独立判定，故拆开。

### U-nas-014
category: pattern
language: en
rule_summary: 简化时只处理让人读不下去的表层问题：黑话术语、过长的句子、抽象名词、纠缠不清的结构，除此之外不动内容。
positive: 把一句塞满专业黑话、长达五行的句子拆成两句大白话，但信息量不变。
negative: 遇到一句读起来吃力的句子，编辑者不是拆句子、换掉抽象名词，而是直接删掉整句里的一半信息来"让它变短"。违反点：用删内容的方式而不是处理 jargon/long sentences/abstract nouns/tangled structure 来简化。
anchor: `## Editing principles / Open it up, don't dumb it down.`
notes: 见 U-nas-013 notes。

### U-nas-015
category: pattern
language: en
rule_summary: 优先用主动语态，不能让没有生命的事物去做本该由人做的动作。
positive: "The team shipped it Tuesday."（引自上游）
negative: "the decision emerged"（引自上游，作为反例）。违反点：让"决定"（无生命的抽象名词）充当了"emerge"这个动作的主语，掩盖了真正做出决定的人。
anchor: `## Editing principles / Use active voice.`
notes: 无。

### U-nas-016
category: pattern
language: en
rule_summary: 空洞的限定语和铺垫词要删；但如果这些词表达的是真实的不确定、自我意识或作者本人说话的语感（比如 "I think"、"maybe"、"to be honest"），就保留。
positive: "I think this approach might backfire" 中的 "I think" 表达了真实的不确定，予以保留。
negative: 一句陈述句里随手加了一个 "honestly" 但既不表达强调也不表达不确定，纯属口头禅式填充。违反点：empty qualifier 没有承担任何语义功能，却没有被删掉。
anchor: `## Editing principles / Make every sentence earn its place.`
notes: 与 Words to cut 里的"Often-empty adverbs"（U-nas-028）是同一逻辑在不同小节的表述，一个是原则性说明，一个是具体词表，分别保留，归并时可能合并。

### U-nas-017
category: pattern
language: en
rule_summary: 只在句子确实难以理解时才拆分句子和段落；如果长句、片段句或节奏变化本身清楚、并且是作者特有的语感，就保留，不要为了"整齐"而拉平节奏。
positive: 保留一句作者特意写的长长的、带转折的口语化句子，因为它读起来是清楚的。
negative: 把一句虽然长但完全说得通、且带有作者个人语感的句子拆成三个短句，理由只是"长句不好"。违反点：flattening the cadence——句子本身不难懂，却被拆短抹平了节奏。
anchor: `## Editing principles / Untangle sentences without flattening the cadence.`
notes: 无。

### U-nas-018
category: pattern
language: en
rule_summary: 写得具体、有细节，不要停留在抽象概括；能用名字、数字、日期、机制、例子说清楚的，就不要用抽象词代替。
positive: "The integration cut deploy time from 40 minutes to 4."（引自上游）
negative: "The integration improved efficiency."（引自上游，作为反例）。违反点：用"improved efficiency"这个抽象说法代替了本可以给出的具体数字（40 分钟到 4 分钟）。
anchor: `## Editing principles / Be concrete and specific.`
notes: 无。

### U-nas-019
category: measurement
language: both
rule_summary: 用"可移植性测试"判断一句话是不是废话：如果这句话原封不动搬到别的人、公司、国家或产品身上依然成立，它多半是填充句，要么删掉，要么换成针对这个主题的具体事实、例子、机制、后果或判断。
positive: 把一句可以套用在任何公司身上的话，改成只针对这家公司具体情况的一句话（加入这家公司特有的数字或机制）。
negative: 保留一句"在当今快速变化的市场环境中，企业需要不断创新"，这句话换成任何公司、任何行业都成立。违反点：这句话能通过"搬到别的公司还成立"的可移植性测试，说明是填充句，却没有被删除或替换成具体内容。
anchor: `## Editing principles / Use the portability test.`
notes: 归为 measurement 是因为它本身就是一条可操作的验证方法（"能不能搬到别处"），而不是某个具体的写法模式；也可以理解为 pattern，归并时可以按 criteria.md 再核对。

### U-nas-020
category: pattern
language: en
rule_summary: 用事实、动作、例子和后果本身去承载重点，不要额外加评论去给一个点贴"重要""令人惊讶""微妙""明显"这类标签；如果前面的内容已经能体现这一点，就把这句评论删掉。
positive: 直接描述"这个功能把审核时间从两周压缩到两天"，让读者自己判断这是不是重要的。
negative: 在陈述完一个事实后又加一句"这一点非常重要，值得读者特别注意"。违反点：用评论去标注重要性（label a point important），而不是靠事实本身体现。
anchor: `## Editing principles / Always show, don't tell the reader what to think.`
notes: 与 Patterns to cut 里的"Interpretive metadiscourse"（U-nas-037）是近似的现象，一个是原则性说明，一个是具体短语清单，分别保留。

### U-nas-021
category: protection
language: both
rule_summary: 不能把一个已经很具体的细节磨成笼统的"重要性"说法；有具体数字或事实的地方要保留具体数字或事实。
positive: "The tool cut review time from 30 minutes to 8."（引自上游）
negative: "The tool significantly improves engineering productivity."（引自上游，作为反例）。违反点：把原本可以是"30 分钟到 8 分钟"这样的具体事实，抹平成了"significantly improves productivity"这种空泛说法。
anchor: `## Editing principles / Protect the specific fact.`
notes: 与 U-nas-011 同属 protection，见 U-nas-011 notes 的区分说明。

### U-nas-022
category: pattern
language: en
rule_summary: 用直接、有力的动词代替绕弯子的动词短语。
positive: "decided"（引自上游，"Made a decision" 的修正）
negative: "Made a decision"（引自上游）。违反点：用"make a decision"这种弱动词短语代替了本可以直接用的"decide"。
anchor: `## Editing principles / Make verbs do the work.`
notes: 无。

### U-nas-023
category: process
language: both
rule_summary: 动手改结构或改用词之前，先搞清楚这篇稿子想做什么、是写给谁看的。
positive: 编辑前先确认这是一篇给内部团队看的进度更新，再决定用什么语气和结构。
negative: 不了解稿子的目的和读者是谁，直接按通用的"专业文章"标准开始调整结构和措辞。违反点：跳过了"know the job"这一步，在不清楚目标和受众的情况下就动手改结构、改用词。
anchor: `## Editing principles / Know the job.`
notes: 与 U-nas-005、U-nas-006（受众/目标不明时要问用户）是同一关切的两个层面：那两条是"外部触发、要不要停下来问"，这条是"内部原则、动手前要先明确"，保留为独立单元。

### U-nas-024
category: style-opinion
language: en
rule_summary: 保留属于作者本人的强烈观点、直率的语言、幽默、脏话和坦率的自我承认，不要把它们换成更安全或更"专业"的措辞。
positive: 保留原文里一句带脏话的吐槽，因为这是作者本人说话的方式。
negative: 把原文里一句带脏话、语气强烈的吐槽改写成温和、正式的表达。违反点：replace them with safer or more professional wording——把本属于作者的直率语言替换成了更安全的说法。
anchor: `## Editing principles / Preserve useful edge and character.`
notes: 与 U-nas-007 主题相近（都是保留作者特征），但触发对象不同：U-nas-007 管"节奏和打磨程度"这类整体声音，这条专门管"观点、脏话、坦白"这类容易被过度净化的内容，分别保留。

### U-nas-025
category: style-opinion
language: both
rule_summary: 保留作者原本的行文顺序和跳跃，除非这个结构本身在损害内容的表达。
positive: 一篇稿子里作者先讲了一个题外话再回到主题，这个安排本身没有损害表达，予以保留。
negative: 没有理由地把作者原本"先讲故事再讲结论"的顺序，重新调整成标准的"结论先行"结构。违反点：结构本身并没有 hurting the piece，却被重新组织了。
anchor: `## Editing principles / Keep structure unless it's hurting the piece.`
notes: 与 U-nas-010（不要强行统一段落结构）方向一致，互相印证。

### U-nas-026
category: process
language: both
rule_summary: 如果确实对稿子做了结构性重组，要在 "What changed" 小节里说明重组的理由。
positive: "What changed" 里写"把结论段落挪到了最前面，因为原来的顺序让读者要看完全文才知道结论"。
negative: 把稿子的段落顺序整体调换了，但 "What changed" 只字未提这处改动或没有说明原因。违反点：reorganize 之后没有 say why——重组了结构却没有在 What changed 里说明理由。
anchor: `## Editing principles / Keep structure unless it's hurting the piece.`
notes: 与 U-nas-001/U-nas-055 里"要有 What changed 小节"的要求相关但更具体：这条管的是"重组结构时 What changed 必须写什么"，不是"要不要有这一节"。

### U-nas-027
category: pattern
language: en
rule_summary: 以下词一律不用，无例外：delve、foster、leverage、utilize、facilitate、empower、streamline、robust、cutting-edge、paradigm shift、game changer、this is huge、this changes everything、tapestry、realm、beacon、multifaceted、meticulous、intricate、paramount、transformative、elevate、embark、supercharge、harness、ever-evolving。
positive: "This update makes review faster."
negative: "This update will supercharge your workflow and truly transform how your team collaborates."（自造）违反点：使用了清单内的禁用词 "supercharge" 和 "transform"（transformative 的同类用法）。
anchor: `## Words to cut / Banned outright`
notes: 这份词表共用同一条判定逻辑（一律不用、无例外），按 extraction.md 的判据合为一个单元，词表整体放进正例反例范围内。

### U-nas-028
category: pattern
language: en
rule_summary: just、literally、honestly、simply、actually、truly、fundamentally、importantly、crucially、inherently、inevitably 这类副词，不承担强调、不确定、对比或作者语感时要删；承担这些功能时保留。
positive: "I actually think this will work"——"actually"在这里表达了带一点意外的强调，予以保留。
negative: "This is just a simple bug fix that we simply need to ship." 违反点：两个"just/simply"都没有承担强调、不确定或对比功能，纯属填充，却没有删掉。
anchor: `## Words to cut / Often-empty adverbs`
notes: 与 U-nas-016（EP8）逻辑一致但词表不同、来源小节不同，各自保留为独立单元；判据是"是否承担语义功能"，与"often-empty phrases"（U-nas-029）的判据措辞不同，不合并。

### U-nas-029
category: pattern
language: en
rule_summary: it's worth noting、it's important to note、at the end of the day、when it comes to、at its core、in today's world、in the age of、in the world of、the reality is、the truth is、in terms of、with regard to、in order to、going forward、in this article、let's dive in 这类短语，在拖延重点时要删；只有当这个短语确实是作者辨识度很高的语言习惯、且句子仍然有内容时才保留。
positive: 直接说"这个功能下个月上线"，不加"going forward, we plan to..."这类铺垫。
negative: "At the end of the day, when it comes to shipping fast, the reality is that speed matters."（自造）违反点：连续堆叠了"at the end of the day""when it comes to""the reality is"三个空洞短语，只为拖延到"speed matters"这一个真正的意思。
anchor: `## Words to cut / Often-empty phrases`
notes: 与 U-nas-028 的区别见该条 notes。

### U-nas-030
category: pattern
language: en
rule_summary: "这不是 X，是 Y"、"问题不在 X，而在 Y"、"不只是 X，而是 Y" 这类二元对比句式要拆掉，直接陈述 Y。
positive: "The eval matters more than the model."（引自上游，即 "The question isn't the model. It's the eval." 的修正）
negative: "The question isn't the model. It's the eval."（引自上游，原句作为反例）。违反点：用"不是 X，是 Y"的二元对比句式代替了直接陈述 Y。
anchor: `## Patterns to cut / Binary contrasts.`
notes: 无。

### U-nas-031
category: pattern
language: en
rule_summary: "Here's the thing,"、"Here's what I mean,"、"Let me be clear,"、"I'll be honest,"、"The uncomfortable truth is" 这类开场铺垫要删，直接说重点。
positive: 直接陈述观点，不加任何开场白。
negative: "Here's the thing: this approach doesn't scale."（引自上游模式名对应的典型结构，短语为自造示例）违反点：用"Here's the thing"这个铺垫开头，而不是直接说"this approach doesn't scale"。
anchor: `## Patterns to cut / Throat-clearing openers.`
notes: 与 U-nas-009（Editing principles 里的"Lead with the point"）是同一现象的原则版和短语清单版，分别保留。

### U-nas-032
category: pattern
language: en
rule_summary: "这是大多数人会跳过的部分"、"大多数人搞错的地方"、"这里是没人告诉你的"、"大家都忽略的部分" 这类"故作洞见"的铺垫要删，让论断本身站得住，不靠把作者包装成"孤独的行家"来加分。
positive: "Distribution is the moat."（引自上游）
negative: "The part everyone misses: distribution is the real moat."（引自上游，原句作为反例）。违反点：用"The part everyone misses"这种自我拔高的铺垫，代替了直接陈述"Distribution is the moat"。
anchor: `## Patterns to cut / Faux-insight setups.`
notes: 无。

### U-nas-033
category: pattern
language: en
rule_summary: "名词短语 + 冒号 + 小写的戏剧化揭晓"这种结构（比如"The best part: it learns."）要改写成一句平实的陈述句；冒号只用于列表、标签和引语，不用来制造假悬念。
positive: "A separate agent does the grading, which is what makes it work."（引自上游，改写后的版本）
negative: "The detail that makes it work: a separate agent grades it."（引自上游，原句作为反例）。违反点：用冒号加小写戏剧化揭晓的结构（colon reveal），而不是写成一句平铺直叙的陈述句。
anchor: `## Patterns to cut / Colon reveals.`
notes: 与 U-nas-034 同一条 bullet，但判定逻辑不同（这条管"要不要用冒号制造悬念"，U-nas-034 管"冒号后面是否该大写"），拆成两个单元。

### U-nas-034
category: pattern
language: en
rule_summary: 冒号后面的内容默认用小写句式（sentence case），除非语法要求、专有名词、标题或代码另有规定才大写。
positive: "The launch adds one thing: faster search."——冒号后小写，因为没有语法或专有名词方面的理由要求大写。
negative: "The launch adds one thing: Faster search."（自造）违反点：冒号后的"Faster"没有语法、专有名词、标题或代码方面的理由却大写了首字母。
anchor: `## Patterns to cut / Colon reveals.`
notes: 与 U-nas-033 拆分说明见该条 notes；这是一条独立的标点/大小写惯例，和"要不要用冒号制造戏剧化揭晓"是两件事。

### U-nas-035
category: pattern
language: en
rule_summary: highlighting、underscoring、reflecting、showcasing 这类假装在解释意义的现在分词从句要删，换成真正说明原因或后果的内容。
positive: "The launch adds file search, so users can find old drafts without leaving the editor."（引自上游）
negative: "The launch adds file search, highlighting the team's commitment to better workflows."（引自上游，原句作为反例）。违反点：用"highlighting..."这个假装解释意义的 -ing 从句，代替了真正说明后果的内容。
anchor: `## Patterns to cut / Superficial analysis.`
notes: 无。

### U-nas-036
category: pattern
language: en
rule_summary: "stands as a testament"、"marks a pivotal moment"、"plays a vital role"、"solidifies its position"、"underscores its significance" 这类"重要性吹捧"短语要删，陈述事实，让读者自己判断是否重要。
positive: "The launch is the company's first paid product."（引自上游）
negative: "The launch marks a pivotal moment for the company."（引自上游，原句作为反例）。违反点：用"marks a pivotal moment"这种重要性吹捧短语代替了具体事实。
anchor: `## Patterns to cut / Importance puffery.`
notes: 无。

### U-nas-037
category: pattern
language: en
rule_summary: "That last part matters more than it sounds,"、"The key point is,"、"As you can see,"、"This distinction matters,"、多余的"In other words" 这类跳出内容本身、告诉读者该怎么理解或该给多少权重的旁白句要删；如果意思已经清楚就直接删掉，不清楚就换成正文里已有的支撑事实。
positive: 删掉一句"这一点很重要"的旁白，让前面的事实自己说明重要性。
negative: 在陈述完一个事实后又加一句"As you can see, this shows..."。违反点：用了跳出内容本身的解读性旁白（interpretive metadiscourse），而不是让事实本身承担说明作用。
anchor: `## Patterns to cut / Interpretive metadiscourse.`
notes: 与 U-nas-020（"show don't tell"原则）是同一关切的原则版和短语清单版，分别保留。

### U-nas-038
category: pattern
language: en
rule_summary: "Experts agree,"、"industry reports suggest,"、"many argue,"、"widely regarded as,"、"studies show" 这类模糊归因短语要点明具体来源，或者干脆删掉这个论断。
positive: "Anthropic's 2026 usage report shows..."——点明了具体来源。
negative: "Studies show that this approach works better."（引自上游）违反点：用"Studies show"这种模糊归因（weasel attribution）代替了点名具体来源。
anchor: `## Patterns to cut / Weasel attribution.`
notes: 该 bullet 还有一句"If the user has no source, ask instead of inventing one"，判定逻辑不同（不是"怎么处理模糊归因短语"而是"没有来源时该怎么办"），拆到 U-nas-039。

### U-nas-039
category: protection
language: both
rule_summary: 遇到用户没有给出来源的论断时，要去问用户有没有来源，不能替用户编一个来源。
positive: "这句话需要一个来源，你有具体的报告或数据可以引用吗？"
negative: 用户的稿子里有一句"industry reports suggest"却没给出具体报告，编辑者直接编了一个看起来真实的报告名字填进去。违反点：instead of inventing one——在没有来源时凭空编造了一个来源，而不是去问用户。
anchor: `## Patterns to cut / Weasel attribution.`
notes: 与 U-nas-011（不能凭空编造事实、数据）方向一致，是"编造来源"这个更具体场景下的同类规则；拆分理由见 U-nas-038 notes。

### U-nas-040
category: pattern
language: en
rule_summary: 用 "is"、"has" 这类清楚的动词代替假装有力的动词短语（比如 "serves as"）。
positive: "The app tracks sponsors, drafts, due dates, and approvals in one place."（引自上游）
negative: "The app serves as a centralized hub for sponsor management."（引自上游，原句作为反例）。违反点：用"serves as a centralized hub"这种假装有力的动词短语（fake-strong verb），代替了更清楚的"tracks"。
anchor: `## Patterns to cut / Fake-strong verbs.`
notes: 无。

### U-nas-041
category: pattern
language: en
rule_summary: 指代同一件事时，如果一个清楚的词就够用，就重复用这个词，不要为了显得有文采而不断换用同义词。
positive: "The agent reviews the draft, scores it, and suggests fixes."（引自上游）
negative: "The agent reviews the draft. The assistant scores the piece. The tool suggests fixes."（引自上游，原句作为反例）。违反点：agent/assistant/tool 三个词指代同一个东西，纯粹为了文采而换用同义词（synonym cycling）。
anchor: `## Patterns to cut / Synonym cycling.`
notes: 无。

### U-nas-042
category: pattern
language: en
rule_summary: "不是 X。不是 Y。是 Z。"这种否定式罗列，直接说 Z 就够了。
positive: 直接说"Z"。
negative: "Not a feature. Not a gimmick. A platform."（自造，套用上游模式名对应结构）违反点：用连续的否定式罗列（negative listing）铺垫，而不是直接说"A platform"。
anchor: `## Patterns to cut / Negative listing.`
notes: 无。

### U-nas-043
category: pattern
language: en
rule_summary: "X。而且 Y。而且 Z。"或者"就是这样。就是这么回事。"这种戏剧化的碎片化句子，要写成完整句子。
positive: 把碎片化的短句合写成一句完整、通顺的陈述句。
negative: "That's it. That's the whole thing."（引自上游）违反点：用戏剧化的碎片句（dramatic fragmentation）代替完整句子。
anchor: `## Patterns to cut / Dramatic fragmentation.`
notes: 无。

### U-nas-044
category: pattern
language: both
rule_summary: 避免重复的句式结构、雷同的段落结构和堆叠的短促断句；只有在确实有助于表达重点时才特意改变句式。
positive: 一篇稿子里句式长短、结构错落有致，只在需要强调时才用短句。
negative: 全文每一段都用"主语+动词+宾语"的同一种短句结构，读起来像敲鼓点。违反点：repeated sentence shapes 和 identical paragraph structures 没有服务于表达重点，只是机械重复（robotic rhythm）。
anchor: `## Patterns to cut / Robotic rhythm.`
notes: 归为语言 both，因为这是关于句式/段落结构重复的现象，不依赖具体英文词汇，中文写作里同样会出现这种机械重复。

### U-nas-045
category: pattern
language: en
rule_summary: "如果我告诉你……"、"想一想："、"神转折："，以及自问自答式的"问题？答案。"这类修辞性铺垫要去掉，直接给出论点。
positive: 直接陈述论点，不设修辞性悬念。
negative: "What if I told you this approach could double your output?"（自造，套用上游模式名对应结构）违反点：用"What if I told you..."这种修辞性设问铺垫（rhetorical setup），而不是直接给出论点。
anchor: `## Patterns to cut / Rhetorical setups.`
notes: 无。

### U-nas-046
category: pattern
language: en
rule_summary: 结尾那种把论点包装成花哨隐喻、格言或"金句收尾"的"故作深刻"句子要直接删掉，不要把它改写成一个更好的隐喻，也不要为了保留节奏感而留着；删掉之后用稿子里已有的、最清楚的具体句子收尾，如果结尾因此显得意犹未尽，就补一句朴素的收获或下一步行动。
positive: 删掉结尾那句隐喻式金句，直接用前一句具体的事实或结论收尾。
negative: 把结尾那句"故作深刻"的隐喻句改写成另一个更精致的隐喻，试图保留原来的收尾节奏感。违反点：Do not rewrite it into a better metaphor. Do not preserve the rhythm——规则明确要求删掉而不是换一个更好的版本，这里却只是替换了隐喻本身。
anchor: `## Patterns to cut / Fake-profound kickers.`
notes: 这条的"不能改写成更好的隐喻"是一个容易被忽略但明确写出的例外情况，判定逻辑独立，值得单独强调。

### U-nas-047
category: pattern
language: en
rule_summary: "总之"、"归根结底"、"总的来说"这类总结句，或者复述全文内容的结尾段，要去掉；用最后一个具体的重点、收获或下一步行动来结尾。
positive: 结尾直接停在最后一个具体的行动建议上，不加总结段。
negative: 结尾又写了一段"总之，本文讨论了……"，把前面讲过的内容复述了一遍。违反点：summary-recap ending 复述了读者刚刚看过的内容，而不是停在最后一个具体点上。
anchor: `## Patterns to cut / Summary-recap endings.`
notes: 无。

### U-nas-048
category: pattern
language: both
rule_summary: 标题里加表情符号、句子中间随手加粗强调、用列表代替本来两句话就能说清楚的内容、给两句话的小节硬加标题，这些都是"用格式装饰"而不是"格式服务于内容"，应当避免；格式要跟着内容走，不是反过来。
positive: 一段两三句就能说清的内容，直接写成一段散文，不拆成列表、不加标题。
negative: 给一个只有两句话的小节加了一个大标题，标题里还带一个表情符号。违反点：headers over two-sentence sections 和 emoji in headings——用格式装饰掩盖了内容本身信息量不足。
anchor: `## Patterns to cut / Formatting slop.`
notes: 这条包含表情符号、加粗、列表、标题四种具体表现，共用"格式服务于内容，不是装饰"这一条判定逻辑，按词表合一的先例保留为一个单元；归为 both 是因为这是格式/排版层面的问题，不依赖具体语言。

### U-nas-049
category: pattern
language: en
rule_summary: 不要把破折号当成默认的节奏拐杖；短文里一个都不用，长文里如果确实比逗号、句号或括号更合适，可以用一到两个，但要去掉成串出现和纯装饰性的破折号。
positive: 一篇较长的稿子里只保留一处确实比逗号更清楚的破折号，其余去掉。
negative: 一段短文里连续用了三处破折号来制造停顿感。违反点：破折号成串出现（remove clusters），且在短文里本应"一个都不用"却用了不止一个。
anchor: `## Patterns to cut / Em dashes.`
notes: 无。

### U-nas-050
category: process
language: both
rule_summary: 动手编辑前先完整读一遍全文，不能只看片段就开始改。
positive: 先通读全文，再开始逐段编辑。
negative: 只看了稿子的开头几段就开始改，没读完全文就动手。违反点：没有 "read the full draft before editing"，在没通读全文的情况下就开始编辑。
anchor: `## Workflow / 1. Read the full draft before editing.`
notes: 无。

### U-nas-051
category: process
language: both
rule_summary: 通读之后要识别核心论点，以及要保留的声音特征（词汇、节奏、直率程度、幽默、不确定感、跑题）；如果确实无法识别出核心论点，就去问用户。
positive: 读完稿子后先写下"核心论点是 X，作者的声音特征是直率、带自嘲"，再动手编辑。
negative: 读完一篇论点模糊、自己也判断不出核心论点的稿子，既不去问用户，也直接按自己猜的重点开始改。违反点：cannot identify the core point 时没有 ask the user，而是自行假设了核心论点。
anchor: `## Workflow / 2. Identify the core point`
notes: 与 U-nas-023（Know the job）关切相近，这条是工作流步骤版本，带有更具体的"识别不出就问用户"的触发条件，保留为独立单元。

### U-nas-052
category: process
language: both
rule_summary: 收到 Detect 请求时，按"两个工作模式"里描述的方式返回发现报告，然后停下，不继续往编辑方向推进。
positive: 给出命中模式的报告后停在这里，等用户决定要不要继续编辑。
negative: 给完 Detect 报告后，没有征得同意就自动接着把全文重写了一遍。违反点：Detect 流程应该在给出报告后 stop，这里却继续往下做了编辑。
anchor: `## Workflow / 3. For a detect request`
notes: 这条是对 U-nas-002/U-nas-003（Detect 模式定义）的工作流层复述，新增信息是明确写了"stop"；归并时大概率与 U-nas-002/003 合并为一条，这里为覆盖 Workflow 小节单独保留。

### U-nas-053
category: process
language: both
rule_summary: 收到 Edit 请求时，做出最小有效改动之后，要按 `eval.md` 里的清单自己检查一遍编辑后的稿子。
positive: 编辑完成后，对照 eval.md 里的检查项逐条自查一遍。
negative: 编辑完成后直接把结果返回给用户，没有做 eval.md 里描述的自查。违反点：跳过了"check the edited draft against eval.md yourself"这一步。
anchor: `## Workflow / 4. For an edit`
notes: `eval.md` 本身不在本次追踪的 paths 内（sources.yaml 只追踪 `skills/no-ai-slop/SKILL.md`），无法核实其具体检查项内容，只记录"有自查这一步"这件事本身。

### U-nas-054
category: process
language: both
rule_summary: 自查如果发现问题，就修改稿子，然后重新检查一遍，直到通过为止。
positive: 自查发现一处遗漏的禁用词，改掉之后重新走一遍检查清单，确认通过。
negative: 自查发现了问题但没有回头修改，直接带着已知问题把稿子交出去。违反点：跳过了"if any check fails, fix the draft and run the checks again"这一步，发现问题后没有修正并复查。
anchor: `## Workflow / 5. If any check fails`
notes: 与 CLAUDE.md 里"先看到测试失败再修"的方法论不是一回事——这条是稿子自查失败后的修正循环，不是测试驱动开发流程，两者只是形式上相似。

### U-nas-055
category: process
language: both
rule_summary: 最终交付编辑后的完整稿子，加一段简短的 "What changed" 小节。
positive: 输出完整编辑稿，末尾附几条要点组成的 "What changed"。
negative: 只输出改动的几个片段，不给完整稿子，也没有 "What changed" 小节。违反点：应输出 full edited draft 加 short "What changed" section，这里两者都缺。
anchor: `## Workflow / 6. Output the full edited draft`
notes: 与 U-nas-001 是同一要求在 Workflow 小节的复述，归并时大概率合并。

---

## 3 覆盖表

| 小节 | 归属单元 / 说明 |
|---|---|
| frontmatter（name/description） | 非规则内容：技能名称与触发描述，供 skill 加载机制使用，不构成可判定规则 |
| `# No AI slop` 正文首段（"You are a sharp human editor..."） | 非规则内容：总纲性表述，把下文各条原则概括了一遍，内容已被 U-nas-007、U-nas-008、U-nas-024 等具体单元覆盖，不单独立条 |
| `## Two jobs` 小节标题本身 | 非规则内容：仅为分节标题 |
| `## Two jobs / Edit (default).` | U-nas-001 |
| `## Two jobs / Detect.` | U-nas-002、U-nas-003 |
| `## What to ask for` 小节标题本身 | 非规则内容：仅为分节标题 |
| `If the user has not provided a draft...` | U-nas-004 |
| `If the audience or format is unclear...` | U-nas-005 |
| `If the goal is unclear...` | U-nas-006 |
| `## Editing principles` 小节标题本身 | 非规则内容：仅为分节标题 |
| Preserve the writer's real voice. | U-nas-007 |
| Make the minimum effective edit. | U-nas-008 |
| Lead with the point when the setup adds nothing. | U-nas-009 |
| Front-load only when it improves clarity. | U-nas-010 |
| Keep the user's meaning. | U-nas-011、U-nas-012 |
| Open it up, don't dumb it down. | U-nas-013、U-nas-014 |
| Use active voice. | U-nas-015 |
| Make every sentence earn its place. | U-nas-016 |
| Untangle sentences without flattening the cadence. | U-nas-017 |
| Be concrete and specific. | U-nas-018 |
| Use the portability test. | U-nas-019 |
| Always show, don't tell the reader what to think. | U-nas-020 |
| Protect the specific fact. | U-nas-021 |
| Make verbs do the work. | U-nas-022 |
| Know the job. | U-nas-023 |
| Preserve useful edge and character. | U-nas-024 |
| Keep structure unless it's hurting the piece. | U-nas-025、U-nas-026 |
| `## Words to cut` 小节标题本身 | 非规则内容：仅为分节标题 |
| Banned outright: ... | U-nas-027 |
| Often-empty adverbs: ... | U-nas-028 |
| Often-empty phrases: ... | U-nas-029 |
| `## Patterns to cut` 小节标题本身 | 非规则内容：仅为分节标题 |
| Binary contrasts. | U-nas-030 |
| Throat-clearing openers. | U-nas-031 |
| Faux-insight setups. | U-nas-032 |
| Colon reveals. | U-nas-033、U-nas-034 |
| Superficial analysis. | U-nas-035 |
| Importance puffery. | U-nas-036 |
| Interpretive metadiscourse. | U-nas-037 |
| Weasel attribution. | U-nas-038、U-nas-039 |
| Fake-strong verbs. | U-nas-040 |
| Synonym cycling. | U-nas-041 |
| Negative listing. | U-nas-042 |
| Dramatic fragmentation. | U-nas-043 |
| Robotic rhythm. | U-nas-044 |
| Rhetorical setups. | U-nas-045 |
| Fake-profound kickers. | U-nas-046 |
| Summary-recap endings. | U-nas-047 |
| Formatting slop. | U-nas-048 |
| Em dashes. | U-nas-049 |
| `## Workflow` 小节标题本身 | 非规则内容：仅为分节标题 |
| 1. Read the full draft before editing. | U-nas-050 |
| 2. Identify the core point and the voice traits to preserve... | U-nas-051 |
| 3. For a detect request... | U-nas-052 |
| 4. For an edit, make the minimum effective changes... | U-nas-053 |
| 5. If any check fails, fix the draft and run the checks again. | U-nas-054 |
| 6. Output the full edited draft and a short **What changed** section. | U-nas-055 |

---

## 4 拆分时拿不准的地方

1. **"保留声音"类规则的 category 归属**（U-nas-007、U-nas-024、U-nas-025）：这几条管的是"保留输入稿本身的特征"，不是助手自己的输出腔调，和 style-opinion 类别定义（"腔调、语气、人称、标点偏好"）不完全对应，taxonomy 六类里没有更贴切的选项。按最接近的类别暂定为 style-opinion，归并阶段如果 criteria.md 第 4 条（单一来源强风格意见不进默认规则）适用，这几条可能需要重新考虑是否算"强风格意见"——它们本质是"不要抹平"而不是"往哪个方向改"，是否属于第 4 条针对的那种"要求一种具体腔调"的规则，需要人工判断。

2. **Colon reveals 和 Formatting slop 的拆分粒度不一致**：Colon reveals 拆成了两个单元（U-nas-033 戏剧化揭晓、U-nas-034 冒号后大小写），因为两者判定逻辑明显不同；但 Formatting slop 涵盖表情符号、加粗、列表、标题四种表现，判定逻辑同样可以说各不相同，却按"共用一条判定逻辑"的词表先例合并成了一个单元（U-nas-048）。这个粒度不一致是拆分时的主观判断，如果归并阶段认为不一致，可以把 Formatting slop 按四种表现再拆细。

3. **同一规则在不同小节重复出现是否要合并成一个单元**：至少三处存在这种情况——U-nas-001/U-nas-008/U-nas-055（最小有效编辑 + What changed，分别出现在 Two jobs、Editing principles、Workflow）、U-nas-002/U-nas-003/U-nas-052（Detect 模式定义在 Two jobs 和 Workflow 里各出现一次）。按 extraction.md 的字面要求（每个小节的每条要求都要能在覆盖表里对应上），本次按小节位置各自保留成独立单元；但这些本质是同一条规则，归并阶段大概率会合并，届时 evidence_count 会因为"同一来源内部重复"而虚高，需要在归并时注意这不是三个独立来源、只是同一来源内部的三次重复。

4. **language 字段默认值的判断**：本来源整体是英文改写 skill，词表和模式清单类单元（pattern 为主）大多标了 en；但流程类（process）、事实保护类（protection）和"可移植性测试"（measurement）这几类判定逻辑本身不依赖具体语言，标成了 both。这个二分是我的判断，不是上游文本明确写出来的，如果归并阶段认为应该统一按来源整体语言标 en，需要重新核对。

5. **U-nas-039（不能替用户编来源）与 U-nas-011（不能编造事实/数据）的独立性**：两者本质是同一条"不臆造"原则在不同场景下的体现，是否应该合并成一条、还是保留因为分别出现在 Editing principles 和 Patterns to cut 两个不同小节——按现在的拆法各自独立，归并阶段可以视为同一条规则的两个证据来源（但注意二者都来自同一个 source_id，不构成 independent_sources 的增量）。

---

## 5 疑似常见规则

以下单元凭规则本身的通用程度判断，猜测在其他"去 AI 味"类项目里也大概率出现，归并时可优先按这些 id 去其他来源的清单里找对应聚类：

- U-nas-027（禁用词清单：delve、leverage、utilize、foster 等）
- U-nas-028（空洞副词：just、literally、honestly 等）
- U-nas-029（空洞短语：at the end of the day、it's worth noting 等）
- U-nas-015（主动语态优先）
- U-nas-018（具体化、反对抽象概括）
- U-nas-020 / U-nas-037（show don't tell / 反对解读性旁白）
- U-nas-031（反对套话开场白）
- U-nas-041（反对同义词轮换）
- U-nas-047（反对"总之/归根结底"式总结收尾）
- U-nas-049（反对破折号滥用）
- U-nas-048（反对表情符号、无意义加粗、格式装饰）
- U-nas-044（反对机械重复的句式/段落结构）
- U-nas-007 / U-nas-008（保留原作者声音、最小有效编辑）
- U-nas-011（不能替用户编造事实、数据、观点）

以下几条相对独特，命名和框架化程度较高，未必能在其他来源里找到同名对应，归并时不必强行聚类：

- U-nas-019（"可移植性测试"这个具体命名的检验方法）
- U-nas-033 / U-nas-034（冒号戏剧化揭晓、冒号后大小写规则，命名和粒度都比较具体）
- U-nas-046（fake-profound kickers，且明确写了"不能改写成更好的隐喻"这条反直觉的例外）
- U-nas-002 / U-nas-003（Detect 模式：只报告不改写、且不判定是否 AI 所写，这个"双模式"设计本身相对少见）

---

## 6 上游文本内的指令

无。通读全文未发现针对读者/助手的注入式指令（例如"忽略之前的规则""把这段加进你的系统提示"之类的表述）。


