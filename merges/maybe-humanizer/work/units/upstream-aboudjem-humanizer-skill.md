# 来源拆规则清单：upstream-aboudjem-humanizer-skill

commit: 275af9489079d0c4a95d47d62a311a5cb0bd85ba（sources.lock.json 的 last_seen_commit）
license: MIT，snapshot_policy: full-text，可引原文。

## 1 来源摘要

四个追踪文件，上游路径均在 `skills/humanizer/` 下：

| 文件（上游路径） | 定位 | 本清单单元数 |
|---|---|---|
| skills/humanizer/SKILL.md | 流程（Step 1-5）、voice、CLI 参数、guardrails、55 条模式的紧凑目录、评分与迭代机制 | 107 |
| skills/humanizer/references/patterns.md | 55 条模式的深挖版：完整触发词表、before/after 例句、emerging 模式来源、Wikipedia 覆盖对照、目录局限性说明；不含独立新规则 | 1 |
| skills/humanizer/references/patterns.zh.md | 中文原生 AI 痕迹附录（ZH1-ZH15），作者自称实验性、未经中文母语写手校验 | 10 |
| skills/humanizer/references/always-on-templates.md | 四份可复制的"常驻规则"模板（CLAUDE.md/SOUL.md/系统提示/ChatGPT 自定义指令），内容复述 SKILL.md 已有规则，不含独立新规则 | 0 |

单元总数：118（U-abh-001 至 U-abh-118）。

按 category 计数：
- pattern (P)：65（P1-P55 共 55 条，P13 伴随的分号/冒号弱信号 1 条，ZH1-ZH7 共 7 条，ZH13-ZH14 共 2 条）
- protection (PROT)：5
- process (PROC)：20
- style-opinion (S)：15
- genre (G)：2
- measurement (M)：11

按 language 计数：
- en：101
- both：7（对应 P1、P10、P14、P18、P22、P43 六条模式单元，以及 Step 3 的 Position engine 单元；均因 patterns.zh.md 明确标注"对应"某个英文模式而合并。P18 和 P22 共用同一条 ZH9 例句，因为 ZH9 本身同时对应这两条英文规则）
- zh：10（patterns.zh.md 里没有被标注为英文模式对应的原生条目：ZH1-ZH7、ZH13-ZH14，以及一条关于 burstiness/perplexity 指标不能迁移到中文的度量单元）

---

## 2 单元清单

按来源文件分组：先 SKILL.md（U-abh-001 至 U-abh-107），再 patterns.md（U-abh-108），再 patterns.zh.md（U-abh-109 至 U-abh-118）。patterns.md 和 always-on-templates.md 的其余内容不产生新单元，理由见"覆盖表"。

所有单元的 source.type 均为 upstream，source.source_id 均为 upstream-aboudjem-humanizer-skill，source.commit 均为 275af9489079d0c4a95d47d62a311a5cb0bd85ba，下文每条只写 path 和 anchor。

### 2.1 来自 SKILL.md（path: skills/humanizer/SKILL.md）

#### U-abh-001
category: process | language: en
rule_summary: `--mode` 决定输出形态：`detect` 只扫描输出报告不改文本，`rewrite`（默认）做完整改写，`edit` 读文件并用 Edit 工具原地改。
positive: 用户传 `--mode detect` 时，输出只有模式报告，原文一字未改。
negative: 用户传 `--mode detect`，输出却直接给出了改写后的整段文字。违反点：detect 模式下不应输出改写结果。
source: path: skills/humanizer/SKILL.md; anchor: `## Quick reference / Modes`
notes: Step 1 的 `--mode` 说明与此重复，视为同一规则的第二个锚点，见 anchor 附加说明；Step 4 的三个模式执行细节拆成独立的 process 单元（U-abh-097、U-abh-099、U-abh-101、U-abh-102），本条只管"选哪个模式意味着做什么"这一层。

#### U-abh-002
category: process | language: en
rule_summary: `--voice` 未显式指定时，按输入文本的语域推断使用哪个 voice profile，而不是套用固定默认值。
positive: 输入文本本身就轻松随意（大量缩写、第一人称），未传 `--voice` 时按 casual 处理。
negative: 未传 `--voice`，不看输入文本语域，一律套用 professional。违反点：跳过了"从输入文本语域推断"这一步。
source: path: skills/humanizer/SKILL.md; anchor: `## Step 1: Parse Arguments / --voice`
notes: 与 `## Quick reference / Voices` 表格描述的"Best for"一栏共用同一条规则，此处取更明确的 Step 1 措辞为主锚点。

#### U-abh-003
category: style-opinion | language: en
rule_summary: casual voice 要求：一律用缩写形式，行文可用第一人称，允许口语化过渡词（So/Anyway/Look）与不完整句，允许用 And/But 开头。
positive: "So I tried this for a week and honestly? Still not sold."
negative: "One should note that this approach has not yet demonstrated sufficient merit." 违反点：无缩写、无第一人称、无口语过渡词，通篇书面语。
source: path: skills/humanizer/SKILL.md; anchor: `### Voice Profiles / casual`
notes: `## Quick reference / Voices` 表格里的"casual"行是同一规则的重复锚点。

#### U-abh-004
category: style-opinion | language: en
rule_summary: professional voice 要求：有选择地使用缩写，默认第三人称、表达观点时才用第一人称，用干燥的机智而非玩笑，举具体例子，段落短（3-5 句）。
positive: "The migration took longer than planned. Three weeks, not the estimated one. Worth it: query latency dropped 60%."
negative: 一段十句以上、不举任何具体例子、通篇第三人称却毫无观点的段落。违反点：段落长度超出 3-5 句且没有具体例子。
source: path: skills/humanizer/SKILL.md; anchor: `### Voice Profiles / professional`
notes: 与 `## Quick reference / Voices` 表格"professional"行重复。

#### U-abh-005
category: style-opinion | language: en
rule_summary: technical voice 要求：用精确术语而非更简单的替代词，一句话只讲一个点，"Note:"/"Important:"节制使用，允许冷静的旁观式评论，数字优先于模糊量词，不用比喻除非确实能澄清。
positive: "The function retries three times with exponential backoff before failing."
negative: "This robust and seamless solution handles retries gracefully like a well-oiled machine." 违反点：用比喻（well-oiled machine）且用模糊词（robust, seamless）代替具体机制描述。
source: path: skills/humanizer/SKILL.md; anchor: `### Voice Profiles / technical`
notes: 与 `## Quick reference / Voices` 表格"technical"行重复。

#### U-abh-006
category: style-opinion | language: en
rule_summary: warm voice 要求：一律用缩写，多用"we"/"our"营造共同经历感，承认困难之处，鼓励但不谄媚，段落更短、留白更多。
positive: "This part's tricky, we know. Take it slow. You've got this."
negative: "Users must complete configuration prior to proceeding." 违反点：无缩写、无"we/our"、不承认任何难度，语气疏远。
source: path: skills/humanizer/SKILL.md; anchor: `### Voice Profiles / warm`
notes: 与 `## Quick reference / Voices` 表格"warm"行重复。

#### U-abh-007
category: style-opinion | language: en
rule_summary: blunt voice 要求：句子尽量短，不加保留语，用"X is bad. Here's why."式的直接判断，观点当事实讲，去掉所有客套，只用主动语态。
positive: "This design is bad. It leaks state across requests."
negative: "It could perhaps be argued that this design might benefit from some reconsideration, though reasonable people may disagree." 违反点：堆叠保留语（could perhaps/might/though reasonable people may disagree），无直接判断。
source: path: skills/humanizer/SKILL.md; anchor: `### Voice Profiles / blunt`
notes: 与 `## Quick reference / Voices` 表格"blunt"行重复。

#### U-abh-008
category: measurement | language: en
rule_summary: 设置 `--score` 时，在输出最前面加一行 `[Score: NN/100]` 的分数头，所有模式都适用。
positive: 输出以 `[Score: 34/100]` 开头，后面跟改写结果。
negative: 传了 `--score`，输出里完全没有分数头。违反点：漏掉了 `[Score: NN/100]` 前缀。
source: path: skills/humanizer/SKILL.md; anchor: `## Quick reference / Flags / --score`
notes: 分数具体怎么算是 U-abh-105（评分公式）的内容，本条只管"要不要显示、显示在哪"这个格式规则，两者判定逻辑不同不合并。

#### U-abh-009
category: process | language: en
rule_summary: `--aggressive` 时改写力度更大：句子更短、个性更强、彻底去掉所有保留语；默认是均衡改写。
positive: 传 `--aggressive` 后输出句子明显变短、态度更鲜明、找不到任何"perhaps/maybe"类保留语。
negative: 传了 `--aggressive`，输出和不传时几乎一样，仍保留大量保留语。违反点：没有体现"更重的改写力度"和"去掉所有保留语"。
source: path: skills/humanizer/SKILL.md; anchor: `## Step 1: Parse Arguments / --aggressive`
notes: -

#### U-abh-010
category: genre | language: en
rule_summary: `--purpose` 在 voice 之上叠加体裁规则：`essay` 不用缩写、标题正式、论证要结构化；`email` 允许问候语和落款、不用 markdown；`marketing` 段落短、给具体利益点、结尾只放一个 CTA；`technical` 保留代码块、术语精确、数字优先于形容词；`general` 不叠加任何规则（默认）。
positive: `--purpose email` 的输出以"Hi Sam,"开头、以签名结尾，不含任何 `**bold**` markdown。
negative: `--purpose essay` 的输出里大量使用缩写（don't/it's）且没有结构化论证。违反点：essay 体裁不该用缩写。
source: path: skills/humanizer/SKILL.md; anchor: `## Step 1: Parse Arguments / --purpose`
notes: 五个取值判定逻辑相同（"按体裁叠加规则"），只是词表/要求不同，按 extraction.md 的合并判据合成一个单元；`## Quick reference` 表格未单列 `--purpose` 行，只在 Step 1 出现。

#### U-abh-011
category: process | language: en
rule_summary: 设置 `--ignore-code` 时先把围栏代码块（三反引号或缩进代码）替换成占位符再扫描/打分；设置 `--ignore-quotes` 时对 Markdown 引用块（`>` 开头）做同样处理；输出前把被掩蔽的内容原样还原。
positive: 输入里的代码块含有 `delve`，设 `--ignore-code` 后该代码块未被标记也未被改写，且原样出现在最终输出里。
negative: 设了 `--ignore-quotes`，输出里引用块的内容却被重写了。违反点：掩蔽/还原流程没有生效，引用块被当成正文改写。
source: path: skills/humanizer/SKILL.md; anchor: `## Quick reference / Flags / --ignore-code`
notes: `## Step 4: Execute Based on Mode / Masking first (all modes)` 是同一规则的重复锚点；两个标志(`--ignore-code`、`--ignore-quotes`)判定逻辑完全相同（掩蔽→跳过→还原），只是作用对象不同，合并为一个单元。

#### U-abh-012
category: process | language: en
rule_summary: 开始解析参数前，先检查当前工作目录下是否存在 `humanizer-context.md`；存在就加载为额外的 voice 指引（品牌样例、禁用词、偏好用词），不存在则默默继续，不报错。
positive: 项目根目录有 `humanizer-context.md` 列出了禁用词"synergy"，改写结果里没有出现这个词。
negative: 项目根目录存在 `humanizer-context.md`，但改写时完全没有读取它，仍然用了文件里明确禁止的词。违反点：跳过了自动加载步骤。
source: path: skills/humanizer/SKILL.md; anchor: `## Step 1: Parse Arguments / Auto-load brand context`
notes: `## When to use this skill` 段末尾一句是同一规则的重复提及。

#### U-abh-013
category: process | language: en
rule_summary: 只有当多个 AI 写作痕迹在同一段落里同时出现时才标记为问题；单独出现一次的破折号、一次"crucial"、一个三项列表本身不构成证据。
positive: 一段话里同时出现三个 em dash、两个"crucial"、一个刻意的三项排比——足够密集，可以标记。
negative: 只把一整篇文章里唯一出现一次的 em dash 单独标记为"AI 痕迹"。违反点：孤例不构成聚类，不该单独标记。
source: path: skills/humanizer/SKILL.md; anchor: `## Guardrails: what NOT to flag, and what to preserve / A single em dash, curly quote, or tidy sentence alone means nothing.`
notes: 合并了该小节的第一条（"Flag clusters, not isolated tells"）和第三条（"A single em dash, curly quote, or tidy sentence alone means nothing"）两条 bullet，二者判定逻辑相同（孤例不算，聚类才算），只是举例不同。

#### U-abh-014
category: process | language: en
rule_summary: 干净的拼写、正确的标点、统一的牛津逗号本身不是 AI 的证据，可能只是细心的作者或经过校对；不能单凭语法完美就标记为 AI。
positive: 一段语法完美、无错别字的文字，但没有其他聚类信号时不被标记为 AI。
negative: 仅因为一段文字"语法太干净、一个错都没有"就判定为 AI 生成。违反点：把语法质量本身当成了 AI 证据。
source: path: skills/humanizer/SKILL.md; anchor: `## Guardrails: what NOT to flag, and what to preserve / Perfect grammar is not AI.`
notes: 上游第二条 bullet（Perfect grammar is not AI），与 U-abh-013 判定的对象不同（一个管"孤例聚类"，一个管"语法质量"），不合并。

#### U-abh-015
category: protection | language: en
rule_summary: 引号、块引用、标题、标题文字、代码、示例里出现的被监控词（如"delve"）一律不改写，即使它是直接引语、书名、变量名或作者正在批评的一段 AI 文本样本，改写会破坏原意和引用关系。
positive: 原文引用了一句话"as the report states, 'the initiative delves into...'"，改写时这句引语原样保留，包括其中的"delve"。
negative: 把一句直接引语里的"delve"换成了"explore"。违反点：改写了引号内的内容，改变了引语原文。
source: path: skills/humanizer/SKILL.md; anchor: `## Guardrails: what NOT to flag, and what to preserve / What NOT to flag (false positives)`
notes: 这是本节里唯一一条明确落在 protection 定义（必须保留的原文/引用）而非 process 判定方法上的规则，因此单独归为 protection 而不是并入 U-abh-013。与 U-abh-011（`--ignore-code`/`--ignore-quotes` 的掩蔽机制）关系密切：U-abh-011 是可选标志触发的机制，本条是不论是否设置标志都必须遵守的默认原则。

#### U-abh-016
category: protection | language: en
rule_summary: 技术写作里反复出现同一个术语（如 `useEffect`）是正确用法，不能为了"优雅"而替换成别的说法；参考类/百科类文字的平实、中性语域本身就是人类声音，不是缺陷。
positive: 一篇 React 文档里连续三次使用"useEffect"这个准确术语。
negative: 把连续出现的"useEffect"分别改写成"the effect hook"、"this hook"、"the side-effect mechanism"以避免重复。违反点：对精确技术术语做了不该做的同义替换。
source: path: skills/humanizer/SKILL.md; anchor: `## Guardrails: what NOT to flag, and what to preserve / What NOT to flag (false positives)`
notes: 这条限定了 P11（Synonym Cycling）和 P31（Elegant Variation）不适用的场景：精确技术术语的重复不算"优雅变体"问题，与已 adopted 的 P11/P31 规则要在裁决阶段一并看，写明"技术术语重复"是例外。

#### U-abh-017
category: measurement | language: en
rule_summary: 40 词以下的样本信号不足，不足以打分；遇到过短样本应明确说明信号不足，而不是硬给一个分数。
positive: 输入只有 25 个词，输出回应"样本太短，无法可靠打分"而不是给出具体数字。
negative: 输入只有 20 个词，仍输出"[Score: 62/100]"。违反点：样本长度不足以支撑打分，却给出了确定的分数。
source: path: skills/humanizer/SKILL.md; anchor: `## Guardrails: what NOT to flag, and what to preserve / What NOT to flag (false positives)`
notes: -

#### U-abh-018
category: measurement | language: en
rule_summary: 句长一致、结构规整本身不能单独作为 AI 证据：自闭症/多动症写作者天然会产出精确、低方差、格式一致的文字，burstiness 类指标无法区分"天生低方差的人类风格"和"机器生成的低方差"；只有同时出现词汇/内容类痕迹才该提高分数。
positive: 一段句长高度一致但没有任何 P7 词汇或内容类痕迹的文字，不因为句长一致本身被判定为高分。
negative: 仅因为句子长度方差低就把分数拉高，不检查是否同时存在词汇或内容类痕迹。违反点：把 burstiness 低单独当成了充分证据。
source: path: skills/humanizer/SKILL.md; anchor: `## Guardrails: what NOT to flag, and what to preserve / Consistent, formulaic structure alone is not proof of AI.`
notes: 与 U-abh-084（Burstiness Principle 的数值目标）互补：那条是"改写时该怎么做"，本条是"检测/打分时不该怎么判"。

#### U-abh-019
category: measurement | language: en
rule_summary: 正式或非母语英语的文风不是 AI 的证据；面向非母语写作者训练的检测器本身存在系统性偏差（引 Liang et al., arXiv:2304.02819），僵硬的教科书式正式语域可能是第二语言写作者真实的声音。
positive: 一段用词正式、句式偏教科书化但明显是母语非英语作者真实写作习惯的文字，不因语域正式被判定为 AI。
negative: 仅因为一段英文"读起来很正式、不够地道"就标记为 AI 生成。违反点：把正式/非母语语域本身当成了 AI 证据。
source: path: skills/humanizer/SKILL.md; anchor: `## Guardrails: what NOT to flag, and what to preserve / Formal or non-native-English prose is not proof of AI either.`
notes: 引用的论文 arXiv:2304.02819 是可以照抄的原文证据（MIT 来源，full-text 允许引用）。

#### U-abh-020
category: protection | language: en
rule_summary: 必须保留难以捏造的具体信息：真实日期、金额、文件路径、真实姓名、精确测量数字（如"从 900ms 降到 40ms"），这些是人类写作的强信号，不能被泛化改写抹掉。
positive: 保留原文中的"dropped from 900ms to 40ms"这一具体数字，不改写成"significantly improved performance"。
negative: 把"revenue grew from $2.3M to $4.1M in Q3"改写成"revenue saw substantial growth"。违反点：删掉了具体数字，换成了模糊的泛化表述。
source: path: skills/humanizer/SKILL.md; anchor: `## Guardrails: what NOT to flag, and what to preserve / Signs of human writing (preserve these)`
notes: -

#### U-abh-021
category: process | language: en
rule_summary: 识别以下人类写作信号后应减少改写而非强行加工：矛盾/未解决的情绪表达、有感官细节的第一人称亲历描述、与特定时代/圈子绑定的俚语或梗、刻意的不完美（片段句、跑题、自我纠正、戛然而止的结尾）；这些信号出现时，正确的编辑往往是不编辑。
positive: 原文写"I still can't decide if I love it or if it makes me uneasy"，保留这句矛盾表达，不把它"修顺"成一个明确立场。
negative: 把"I still can't decide if I love it"改写成"I love it"，抹掉了原有的矛盾感。违反点：把已经存在的真实矛盾情绪改写没了。
source: path: skills/humanizer/SKILL.md; anchor: `## Guardrails: what NOT to flag, and what to preserve / Signs of human writing (preserve these)`
notes: 合并了该小节里除"难以捏造的具体信息"（已单列为 U-abh-020，因为更贴近 protection 定义）和"2022 年前内容"（已单列为 U-abh-022，因为判定逻辑是时间线而非风格识别）之外的四条 bullet：矛盾情绪、感官细节、时代/圈子声音、刻意不完美；四者共用同一条判定逻辑（识别到这类信号就减少改写）。

#### U-abh-022
category: protection | language: en
rule_summary: 2022 年底之前写成或编辑过的内容不应被"修得更新"；它本来就早于要检测的这类 AI 痕迹，不能因为读起来"旧"就强行改成看起来更新的风格。
positive: 一篇写于 2019 年的博客文章保留其本来的写作风格，不因为"读起来不够现代"而重写。
negative: 把一篇标注写于 2019 年的文章改写成更符合 2025 年常见网文腔调的样子。违反点：不该因内容早于检测窗口就修改其真实的时间背景/风格。
source: path: skills/humanizer/SKILL.md; anchor: `## Guardrails: what NOT to flag, and what to preserve / Signs of human writing (preserve these)`
notes: 归为 protection 是因为它保护的是内容的真实时间属性/事实背景不被篡改，判定逻辑（按时间线判断）与 U-abh-021（按风格信号判断）不同，故单列。

#### U-abh-023
category: protection | language: en
rule_summary: 改写可以削尖、删减、重组，但不能编造原文没有的事实、人名、日期、数字或引语；Concretizer 环节只能用原文已暗示或明确给出的具体细节替换抽象表述，找不到具体细节时要标出缺口或询问作者，绝不能凭空发明。
positive: 原文说"the process is complex"，且原文其他地方提到了具体步骤，改写时用那些已有步骤替换抽象说法。
negative: 原文只说"improves performance"，改写时编出一个原文完全没提过的具体数字"cuts latency by 73%"。违反点：编造了原文不存在的数字。
source: path: skills/humanizer/SKILL.md; anchor: `## Operating principles / No fabrication`
notes: 这是本文件里最核心的一条 protection 规则，与 U-abh-089（Concretizer pass 的操作步骤）是同一原则的两面：本条是"不能做什么"的红线，U-abh-089 是"该怎么做"的操作步骤，二者不合并因为一个是边界约束、一个是执行流程。

#### U-abh-024
category: style-opinion | language: en
rule_summary: 北极星原则：LLM 会回归统计均值，人类是怪异、具体、不一致的；写作应该像人类一样怪异、具体、不一致。
positive: -（这条本身是价值主张，不针对具体句子举例）
negative: -（同上）
source: path: skills/humanizer/SKILL.md; anchor: `## Operating principles`
notes: 拿不准是否可判定：这条更像是贯穿全文其他具体规则（Position engine、Concretizer、Burstiness、Perplexity）的统领性口号，本身给不出"违反点：具体的词或结构"，按 criteria.md 第 2 条大概率会被判"不可判定"而 rejected，或按第 4 条作为 reference-only。收录是为了在归并阶段能追溯这条口号和下游具体规则的关系；正反例留空，因为它不满足"能拿一句具体文本判定"的要求。文件末尾"Write like a human. Be weird, specific, inconsistent."是同一条规则的重复表述。

#### U-abh-025
category: process | language: en
rule_summary: 既没有提供文本也没有提供 `--file` 时，应提示用户"Paste the text you want me to humanize, or pass `--file path/to/file.md`."，而不是猜测或报错退出。
positive: 用户只输入了 `--voice casual`，没有正文也没有 `--file`，系统回复固定的提示语要求补充输入。
negative: 用户没给正文也没给 `--file`，系统直接报错终止或凭空编一段文本来处理。违反点：没有按规定的提示语请求补充输入。
source: path: skills/humanizer/SKILL.md; anchor: `## Step 1: Parse Arguments / Text`
notes: -

#### U-abh-026
category: process | language: en
rule_summary: 设置 `--openings N` 时，生成 N 个尽量互不相同的开头钩子（例如：直白断言、具体场景、先问后答的问题），挑出最强的一个并用一句话说明为什么它更强。
positive: `--openings 3` 生成了一个直白断言开头、一个具体场景开头、一个设问开头，并说明选中场景开头的理由是"更快建立画面感"。
negative: 设了 `--openings 3`，但三个候选开头几乎是同一句话的轻微变体，且没有说明选择理由。违反点：候选开头不够"maximally different"，且缺少选择理由。
source: path: skills/humanizer/SKILL.md; anchor: `## Step 1: Parse Arguments / --openings N`
notes: `## Step 3: Rewrite Craft / Opening tournament` 是同一规则的重复锚点，取更详细的 Step 1 描述为主。

#### U-abh-027
category: pattern | language: both
rule_summary: 不用"stands/serves as""is a testament/reminder""pivotal/vital/crucial moment""underscores importance""evolving landscape""indelible mark""deeply rooted"这类词把一件普通事实吹成"有时代意义"；应直接说这东西是什么、做了什么，删掉"这代表了什么"的评论。
positive (en): "established in 1989 to collect regional statistics"（引自上游）
negative (en): "established in 1989, marking a pivotal moment in the evolution of regional statistics"（引自上游）。违反点："marking a pivotal moment in the evolution of"这类意义拔高措辞。
positive (zh): "这次更新修了那个登录会掉线的 bug，另外把加载调快了一点。"
negative (zh): "这次更新彰显了团队精益求精的工匠精神，标志着产品迈入了全新的时代。" 违反点："彰显""标志着...全新的时代"把一次普通更新拔高成时代性事件。
source: path: skills/humanizer/SKILL.md; anchor: `### CONTENT PATTERNS / P1: Significance Inflation`
notes: 中文示例来自 patterns.zh.md 的 ZH8（该文件明确标注"对应 P1 / P40"），故本单元 language 定为 both，中文正反例引自 patterns.zh.md 附加锚点 `## 英文模式的中文对应 · Analogs of English patterns (ZH8–ZH12) / ZH8`。ZH8 同时也对应 P40（Symbolic Gloss），但 P40 的"讲意义"和 P1 的"拔高重要性"是上游明确区分的两条规则（P40 说明写"distinct from P1 framing"），故不把 P40 也标为 both，只在 P40（U-abh-066）的 notes 里提示这层关系。触发词对比：英文触发词是 stands/serves as、testament、pivotal 等；中文触发词是"标志着、彰显、体现了、象征着、折射出、具有里程碑意义"，词表完全不同、不是逐词翻译。英文完整触发词表见 patterns.md 锚点 `## Full trigger lists / P1 Significance Inflation`；英文 before/after 见 patterns.md 锚点 `## Before and after examples / P1 Significance Inflation`。

#### U-abh-028
category: pattern | language: en
rule_summary: 不用"featured in X, Y, Z""profiled in""independent coverage""active social media presence"这类"报道过谁"的清单来证明重要性；应挑一个来源说清楚它具体报道了什么，或者直接删掉。
positive: "In a 2024 NYT interview, she argued that regulation should focus on outcomes"（引自上游）
negative: "cited in NYT, BBC, FT, and The Hindu"（引自上游）。违反点：只堆砌媒体名单，没说任何一家具体报道了什么内容。
source: path: skills/humanizer/SKILL.md; anchor: `### CONTENT PATTERNS / P2: Notability Name-Dropping`
notes: 与 P37（Overattribution）判定对象几乎一致，但上游在 patterns.md 明确写"distinct from P2 famous-name dropping"，二者的侧重不同（P2 是"报过大牌媒体"，P37 是"用来源数量本身当证据，不管媒体大小"），不合并，仅在两条的 notes 互相点名。

#### U-abh-029
category: pattern | language: en
rule_summary: 不用现在分词短语（highlighting/underscoring/emphasizing/ensuring/reflecting/symbolizing/fostering/showcasing）伪装深度；应删掉这个分词从句，或者把它里面真正的信息提升成一句有来源的独立句子。
positive: "The architect chose blue and gold to reference local bluebonnets"（引自上游）
negative: "The color palette resonates with the region's beauty, symbolizing bluebonnets, reflecting the community's deep connection to the land"（引自上游）。违反点：三个连续的分词短语（symbolizing、reflecting）堆砌评论，没有一个具体事实。
source: path: skills/humanizer/SKILL.md; anchor: `### CONTENT PATTERNS / P3: Superficial -ing Phrases`
notes: -

#### U-abh-030
category: pattern | language: en
rule_summary: 不用旅游宣传册式形容词（nestled、in the heart of、vibrant、breathtaking、must-visit、cutting-edge、seamless、robust、world-class、state-of-the-art、figurative rich、renowned）代替事实；应换成"具体是什么让它值得一提"。
positive: "A town in the Gonder region, known for its weekly market and 18th-century church"（引自上游）
negative: "Nestled within the breathtaking region of Gonder, a vibrant town with rich cultural heritage"（引自上游）。违反点：nestled、breathtaking、vibrant、rich 四个宣传语式形容词，没有一条具体事实。
source: path: skills/humanizer/SKILL.md; anchor: `### CONTENT PATTERNS / P4: Promotional Language`
notes: 完整触发词表见 patterns.md 锚点 `## Full trigger lists / P4 Promotional Language`；`seamless`、`robust` 两个词在 always-on-templates.md 的示例模板里被归进了"AI 词汇"清单（与 P7 混在一起），但上游权威定义里它们属于 P4 而非 P7，见"拆分时拿不准的地方"一节。

#### U-abh-031
category: pattern | language: en
rule_summary: 不用"experts argue""research suggests""observers have cited""several sources""it is widely believed""industry reports"这类没有具体所指的权威来源撑腰；应指名具体的专家、论文或报告，否则删掉这个说法。
positive: "A 2019 Chinese Academy of Sciences survey found 12 endemic fish species"（引自上游）
negative: "Experts believe it plays a crucial role in the regional ecosystem"（引自上游）。违反点："Experts believe"没有指名任何具体专家或研究。
source: path: skills/humanizer/SKILL.md; anchor: `### CONTENT PATTERNS / P5: Vague Attributions`
notes: -

#### U-abh-032
category: pattern | language: en
rule_summary: 不用"Despite [好的一面]，[模糊的问题]。Despite these, [空话]。"这种"挑战小节"套路；应写清楚具体问题（带日期和数据），或者直接删掉这一段。
positive: "Traffic worsened after 2015 when three IT parks opened. A stormwater project started in 2022"（引自上游）
negative: "Despite its prosperity, faces challenges typical of urban areas. Despite these challenges, continues to thrive"（引自上游）。违反点：两次"Despite"套路，问题和结论都是空泛的套话，没有一条具体信息。
source: path: skills/humanizer/SKILL.md; anchor: `### CONTENT PATTERNS / P6: Formulaic Challenges Sections`
notes: -

#### U-abh-033
category: pattern | language: en
rule_summary: delve、leverage、multifaceted、tapestry、testament、underscore、interplay、realm、pivotal、crucial、vibrant、foster、garner、bolster、notably、moreover、furthermore、"it's worth noting"、"in today's landscape"这批 2023 年后暴增 3-10 倍的词应删掉或换成大白话。
positive: "Also, this launch adds three new integrations."
negative: "Additionally, it's worth noting that this pivotal development underscores the vibrant landscape."（引自上游，出自 Tiered-confidence vocabulary 小节的聚类示例）违反点：一句话里聚集了 additionally、it's worth noting、pivotal、underscores、vibrant landscape 五个 AI 高频词。
source: path: skills/humanizer/SKILL.md; anchor: `### CONTENT PATTERNS / P7: AI Vocabulary Words`
notes: 完整触发词表和分级见 patterns.md 锚点 `## Full trigger lists / P7 AI Vocabulary Words`，以及本文件的 `### Tiered-confidence vocabulary (refines P7)`（拆成独立的度量单元 U-abh-083，因为它改变的是打分权重而非"该不该删词"这条基础判定）。

#### U-abh-034
category: pattern | language: en
rule_summary: 不用"serves as""stands as""marks""represents""boasts""features""offers"这类花哨动词代替简单的 is/are/has/was；简单系动词是清楚，不是无聊。
positive: "Gallery 825 is the exhibition space"（引自上游）
negative: "Gallery 825 serves as the exhibition space"（引自上游）。违反点："serves as"可以直接换成"is"却没换。
source: path: skills/humanizer/SKILL.md; anchor: `### CONTENT PATTERNS / P8: Copula Avoidance`
notes: -

#### U-abh-035
category: pattern | language: en
rule_summary: "not only X but Y""it's not just X, it's Y""it's not merely X, it's Y"这类否定式排比，用一次是修辞，用两次是套路，用三次就是聊天机器人；应直接把意思说出来，不搞戏剧化铺垫。
positive: "The heavy beat adds to the aggressive tone"（引自上游）
negative: "It's not just a song, it's a statement"（引自上游）。违反点："not just...it's..."否定式排比铺垫，绕了一圈才说出本来能直说的意思。
source: path: skills/humanizer/SKILL.md; anchor: `### LANGUAGE & STYLE PATTERNS / P9: Negative Parallelisms`
notes: -

#### U-abh-036
category: pattern | language: both
rule_summary: 不为了显得权威而硬凑三项抽象名词排比；该用几个就用几个，两项和四项被低估了但同样自然。
positive (en): "talks and panels, plus time for networking"（引自上游）
negative (en): "innovation, inspiration, and industry insights"（引自上游）。违反点：三个抽象名词的强行排比，内容空洞。
positive (zh): "它够快，也够稳。优不优雅我不好说，反正没再半夜被叫起来过。"
negative (zh): "它不仅高效，而且稳定，更兼具优雅、简洁与可扩展性。" 违反点："不仅……而且……更"三连对仗，凑气势而非讲内容。
source: path: skills/humanizer/SKILL.md; anchor: `### LANGUAGE & STYLE PATTERNS / P10: Rule of Three`
notes: 中文示例来自 patterns.zh.md 的 ZH10（明确标注"对应 P10"），故本单元定为 both。中文触发词（"不仅……而且……更""既……又……还""三个结构相同的短句连排"）比英文触发词（三项抽象名词列表）覆盖面更宽，还包含并列谓语结构，notes 里提示归并阶段注意这层差异。

#### U-abh-037
category: pattern | language: en
rule_summary: 同一个实体在连续句子里不能没有理由地换着说法称呼（"protagonist"换成"main character"再换成"central figure"）；应选定一个说法反复用。
positive: 连续三句都用"the API"指代同一个接口，不做无理由的换称。
negative: 连续三句分别用"the API""this interface""the service layer"指代同一个东西。违反点：无理由地对同一实体换用三种不同称呼。
source: path: skills/humanizer/SKILL.md; anchor: `### LANGUAGE & STYLE PATTERNS / P11: Synonym Cycling (Elegant Variation)`
notes: 与 P31（Elegant Variation, Noun-Phrase Cycling）判定对象相关，但上游明确写"distinct from P11 (Synonym Cycling), which is word-level"——P11 管单个词的替换，P31 管整个名词短语的替换，不合并，互相在 notes 点名。本单元没有上游给的 before/after 例句（不在 patterns.md 的 34 条清单内），正反例为自撰。

#### U-abh-038
category: pattern | language: en
rule_summary: 不用"from X to Y"这种表面上像跨度实则 X 和 Y 根本不在同一光谱上的强行范围表述；应直接说出具体的项目。
positive: "the plan covers three cities: Austin, Denver, and Raleigh"
negative: "the plan ranges from grassroots outreach to enterprise partnerships"，把两个不在同一维度上的东西硬凑成一个"from...to..."跨度。违反点：X 和 Y 不构成真实的光谱，是硬凑的"从……到……"。
source: path: skills/humanizer/SKILL.md; anchor: `### LANGUAGE & STYLE PATTERNS / P12: False Ranges`
notes: 不在 patterns.md 的 34 条 before/after 清单内，正反例为自撰。

#### U-abh-039
category: pattern | language: en
rule_summary: 破折号（U+2014）零容忍，一律不用，改用逗号、冒号或连字符；这是最常见的单一格式痕迹。
positive: "The fix was simple: cache the response."
negative: "The fix was simple—cache the response." 违反点：使用了破折号（U+2014）。
source: path: skills/humanizer/SKILL.md; anchor: `### LANGUAGE & STYLE PATTERNS / P13: Em Dash Ban`
notes: 这条是"零容忍"，与紧随其后的分号/冒号聚类弱信号（U-abh-082）判定强度不同（一个零容忍、一个只在聚类且置信度低时才算信号），不合并，但共享同一段锚点。patterns.zh.md 明确把中文改写排除在这条零容忍之外（见 U-abh-113 的 notes），本单元的 language 因此保持 en，不升级为 both——中文场景走的是判定逻辑不同的 ZH5（U-abh-113），这是一处需要在归并阶段留痕的范围冲突，详见"拆分时拿不准的地方"。

#### U-abh-040
category: pattern | language: both
rule_summary: 不用机械式的加粗、emoji 装饰标题、跳级标题、每个标题前加分割线、本该用散文的地方硬用表格、非 Markdown 场合出现 Markdown 记号；加粗应节制使用，每节最多一次。
positive (en): 一篇邮件正文没有任何 `**bold**` 记号，标题层级连续（H2 后直接接 H3），没有 emoji 装饰的小标题。
negative (en): 邮件正文里几乎每隔一个短语就加粗一次，标题前每次都插入一条分割线。违反点：加粗过度使用、每个标题前加分割线。
positive (zh): "核心优势就一条：冷启动比上一版快了三倍。"
negative (zh): "🚀 **核心优势**：我们的**产品**拥有**强大**的**性能**和**卓越**的**体验**！" 违反点：emoji 开头的小标题、几乎每个名词都加粗。
source: path: skills/humanizer/SKILL.md; anchor: `### LANGUAGE & STYLE PATTERNS / P14: Boldface/Formatting Overuse`
notes: 中文示例来自 patterns.zh.md 的 ZH12（明确标注"对应 P14 / P28"），故定为 both。ZH12 同时对应 P28（Markdown Bleeding），但上游把"系统性加粗过度"（P14）和"纯文本渠道漏出 Markdown 记号"（P28）当成两条不同规则，本单元只承接 P14 那一半，P28（U-abh-054）的 notes 里另外点名 ZH12。触发词对比：英文触发词偏向标题层级、分割线、表格滥用；中文触发词偏向 emoji 小标题和逐词加粗，覆盖范围不完全一致。

#### U-abh-041
category: pattern | language: en
rule_summary: 不用"**粗体小标题：** 描述"这种项目符号列表代替本该写成散文的内容；内容如果本来就是流畅的论述，应该写成段落而不是列表。
positive: 一段关于产品决策权衡的论述写成了三句连贯的段落，而不是拆成项目符号。
negative: 把一段本该是连贯论述的内容拆成"**优点：** 速度快 **缺点：** 成本高 **建议：** 采用"这种项目符号列表。违反点：内容本可以写成连贯段落，却拆成了机械的加粗项目符号列表。
source: path: skills/humanizer/SKILL.md; anchor: `### LANGUAGE & STYLE PATTERNS / P15: Structured List Syndrome`
notes: -

#### U-abh-042
category: pattern | language: en
rule_summary: 标题应该用句子大小写（只有句首和专有名词大写），不应该用标题大小写（Title Case，每个实词首字母都大写）。
positive: "Strategic negotiations and global partnerships"（引自上游）
negative: "Strategic Negotiations And Global Partnerships"（引自上游）。违反点：每个实词首字母大写（Title Case）。
source: path: skills/humanizer/SKILL.md; anchor: `### LANGUAGE & STYLE PATTERNS / P16: Title Case in Headings`
notes: -

#### U-abh-043
category: pattern | language: en
rule_summary: ChatGPT 常用弯引号（curly quotes），Claude 常用直引号；改写应匹配作者原有的排版习惯，不能自作主张统一成弯引号；牛津逗号如果整篇文章刚性统一使用也是一个提示信号。
positive: 全文统一使用直引号"like this"，与作者原有排版一致。
negative: 把作者原本用的直引号全部换成弯引号"like this"。违反点：改变了作者原有的引号排版风格。
source: path: skills/humanizer/SKILL.md; anchor: `### LANGUAGE & STYLE PATTERNS / P17: Curly Quotes and Typographic Tells`
notes: -

#### U-abh-044
category: pattern | language: both
rule_summary: 在读者期待大白话的场合不用官僚式正式语域；"it should be noted that""it is essential to""in the context of""the implementation of"这类词应降到语境需要的语域。
positive (en): "Set the timeout to 30 seconds."
negative (en): "It should be noted that it is essential to configure the implementation of the timeout parameter."（引自上游触发词组合而成）。违反点：It should be noted that / it is essential to / the implementation of 三个官僚式短语堆砌，本可以一句话说清。
positive (zh): "这个功能让结账少点一次。转化率涨了 4%。"
negative (zh): "值得注意的是，在一定程度上，这个功能从某种意义上说提升了用户体验。" 违反点："值得注意的是""在一定程度上""从某种意义上说"三个书面腔填充短语，删掉不影响意思。
source: path: skills/humanizer/SKILL.md; anchor: `### LANGUAGE & STYLE PATTERNS / P18: Formal Register Overuse`
notes: 中文示例来自 patterns.zh.md 的 ZH9（明确标注"对应 P18 / P22"），故定为 both；本单元承接 P18 那一半（书面腔正式语域），ZH9 同时对应的 P22（Filler Phrases，冗余连接词）见 U-abh-048 的 notes。英文本身没有上游给的 before/after 例句（不在 34 条清单内），本单元英文例句为自撰，用了上游列出的触发词。

#### U-abh-045
category: pattern | language: en
rule_summary: 删掉助手式寒暄，如"I hope this helps""Of course!""Certainly!""You're absolutely right!""Would you like me to""Let me know if""Here is a"。
positive: 直接给出答案，不加任何寒暄前缀或结尾。
negative: "Of course! Here is a summary of the changes. I hope this helps! Let me know if you have any questions." 违反点：整句话由四个助手式寒暄短语拼成，没有实质内容。
source: path: skills/humanizer/SKILL.md; anchor: `### COMMUNICATION PATTERNS / P19: Chatbot Artifacts`
notes: -

#### U-abh-046
category: pattern | language: en
rule_summary: 删掉知识截止日期式的免责声明，如"As of [date]""up to my last training update""while specific details are limited""based on available information"；要么直接说清楚事实，要么删掉这个保留。
positive: "The library's latest release is 4.2, published in March."
negative: "As of my last training update, while specific details are limited, the library's version may have changed." 违反点：知识截止日期免责声明代替了应有的具体事实。
source: path: skills/humanizer/SKILL.md; anchor: `### COMMUNICATION PATTERNS / P20: Knowledge-Cutoff Disclaimers`
notes: -

#### U-abh-047
category: pattern | language: en
rule_summary: 删掉谄媚语气，如"Great question!""That's an excellent point!""You raise a very important issue""Absolutely!"；直接回答，不加奉承。
positive: 直接回答问题本身，不加任何夸赞式开场白。
negative: "Great question! That's an excellent point you raise. Absolutely, let's dive in." 违反点：三句话全是谄媚式开场白，没有进入实质回答。
source: path: skills/humanizer/SKILL.md; anchor: `### COMMUNICATION PATTERNS / P21: Sycophantic Tone`
notes: -

#### U-abh-048
category: pattern | language: both
rule_summary: 删掉或缩短不增加信息的冗长连接词，如"in order to""due to the fact that""at this point in time""it's worth noting""when it comes to""in connection with""connected with/to""in association with""associated with"。
positive (en): "We upgraded the server to handle more traffic."
negative (en): "Due to the fact that we needed to handle more traffic, and in connection with our scaling plans, we upgraded the server at this point in time."（触发词组合，自撰）违反点：due to the fact that / in connection with / at this point in time 三个冗余连接词，删掉不影响意思。
positive (zh): "这个功能让结账少点一次。转化率涨了 4%。"
negative (zh): "值得注意的是，在一定程度上，这个功能从某种意义上说提升了用户体验。" 违反点：同 U-abh-044 的中文反例，"值得注意的是"类填充短语属于此条覆盖范围。
source: path: skills/humanizer/SKILL.md; anchor: `### FILLER & HEDGING PATTERNS / P22: Filler Phrases`
notes: 中文例句与 U-abh-044（P18）共用同一句 ZH9 例句，因为 ZH9 本身同时对应 P18 和 P22（中文里"书面语套话"和"冗余虚词"在同一批触发词里不分家）；本单元 language 因此也定为 both，并在此处提示归并阶段：ZH9 的中文触发词在英文侧被上游拆成了两条规则（P18 语域、P22 填充词），裁决时需要决定是否也拆成两条中文规则，还是保留一条覆盖两者的中文规则。

#### U-abh-049
category: pattern | language: en
rule_summary: 不堆叠多层保留语（如"could potentially possibly""it might perhaps be argued"）；应表态，或者只说出那一个真正的不确定点。
positive: "This might not scale past 10k users; I haven't tested it."
negative: "It could potentially possibly be argued that this might perhaps not scale." 违反点：could potentially possibly、might perhaps 两处保留语堆叠。
source: path: skills/humanizer/SKILL.md; anchor: `### FILLER & HEDGING PATTERNS / P23: Excessive Hedging`
notes: -

#### U-abh-050
category: pattern | language: en
rule_summary: 不用"the future looks bright""exciting times lie ahead""poised for growth""a step in the right direction"这类空泛乐观的结尾；应以一个具体事实或一个开放问题收尾。
positive: 以"下一步要解决冷启动的延迟问题"这类具体待办收尾。
negative: "The future looks bright, and exciting times lie ahead as we're poised for growth." 违反点：整句是空泛乐观套话，没有任何具体内容。
source: path: skills/humanizer/SKILL.md; anchor: `### FILLER & HEDGING PATTERNS / P24: Generic Positive Conclusions`
notes: -

#### U-abh-051
category: pattern | language: en
rule_summary: 过于具体却像是编造的日期或数字、归到不存在来源的引用、对冷门事实的自信断言而没有引用，这些是幻觉标记；应核实或删除。
positive: 一个具体统计数字附带真实可查的来源引用。
negative: "According to a 2019 internal Gartner memo, 73.4% of enterprises had adopted this by Q2."，来源无法核实且过于精确。违反点：引用了无法核实、疑似编造的来源和精确数字。
source: path: skills/humanizer/SKILL.md; anchor: `### FILLER & HEDGING PATTERNS / P25: Hallucination Markers`
notes: 与 U-abh-023（No fabrication protection）密切相关：U-abh-023 是"改写不能编造"的红线，本条是"检测阶段识别疑似编造痕迹"的信号，一个管改写行为、一个管检测判断，不合并。

#### U-abh-052
category: pattern | language: en
rule_summary: 整段文字里语法完美的部分和明显有基础错误的部分交替出现，提示这是"部分人工编辑过的 AI 输出"；应统一保持同一质量水平。
positive: 全篇语法和用词质量一致。
negative: 一段语法无懈可击的文字后面紧跟一句明显有基础拼写错误的话，风格反差极大。违反点：完美和粗糙交替出现，质量不统一。
source: path: skills/humanizer/SKILL.md; anchor: `### FILLER & HEDGING PATTERNS / P26: Perfect/Error Alternation`
notes: 与 P36（Sudden Style/Register Shift）判定对象接近（都是"文风突变"），但 P26 特指"完美与错误交替"，P36 特指"正式与随意语域突变"，上游把两者列为不同编号，不合并，互相在 notes 点名。

#### U-abh-053
category: pattern | language: en
rule_summary: 长文里不用问句做小标题（如"What makes X unique?""Why is Y important?""How does Z work?"）；应改用陈述句标题。
positive: "How the cache invalidation logic works"改成陈述式标题"Cache invalidation checks the config hash on every request"。
negative: 小标题写成"What Makes This Approach Unique?"。违反点：用问句做长文小标题。
source: path: skills/humanizer/SKILL.md; anchor: `### FILLER & HEDGING PATTERNS / P27: Question-Format Section Titles`
notes: 与 ZH6（设问-回答套路，U-abh-114）判定对象部分重叠，但上游在 patterns.zh.md 里明确写 ZH6"区别于英文 P27 的疑问句标题"——P27 管标题层面用问句，ZH6 管正文里反复自问自答的节奏，二者判定逻辑不同，不合并，仅互相点名。

#### U-abh-054
category: pattern | language: en
rule_summary: 在邮件、社交媒体帖子或 Word 文档这类不渲染 Markdown 的场合，不该出现 `**bold**` 这类 Markdown 记号；应在这些场合去掉 Markdown 语法。
positive: 一封邮件正文没有任何 `**` 或 `##` 记号。
negative: 一封邮件正文里出现"Please review the **updated policy** before Friday."，`**` 未被渲染，原样显示。违反点：在不支持 Markdown 的渠道里保留了 Markdown 记号。
source: path: skills/humanizer/SKILL.md; anchor: `### FILLER & HEDGING PATTERNS / P28: Markdown Bleeding`
notes: patterns.zh.md 的 ZH12（U-abh-040 的中文部分）同时标注对应 P14 和 P28，本单元承接"纯文本渠道漏出 Markdown 记号"这一半；ZH12 的例句"发到不支持 Markdown 的地方就把 `**` 去掉"更贴近本条而非 P14，归并阶段可以考虑本条也升级为 both，此处先按上游归类的主标注（P14 排在前）处理，留在 U-abh-040 的 notes 里提示这个待确认点。

#### U-abh-055
category: pattern | language: en
rule_summary: 不用"this comprehensive guide/overview covers""in this article, we will explore""let's dive into"这类"全面概览"式开场；应直接从实际内容开始。
positive: 文章开头直接是"The auth system uses JWTs."
negative: "This comprehensive guide delves into the intricacies of our authentication system." 违反点："This comprehensive guide delves into"是典型的全面概览式开场，没有任何实质内容。
source: path: skills/humanizer/SKILL.md; anchor: `### FILLER & HEDGING PATTERNS / P29: The "Comprehensive Overview" Opening`
notes: 与 P32（Collaborative Communication Leaking）触发词高度重叠（"in this article, we will explore"两条都列了），上游把 P29 归为"全面概览开场"、P32 归为"对话框架泄漏进已发布内容"，说的是同一句触发词但强调的成因不同（P29 强调空洞开场，P32 强调聊天语境泄漏），不合并，互相在 notes 点名；与 ZH3（套话开头，U-abh-111）语义接近但触发词完全不同（中文用"在当今……的时代"类），不合并。

#### U-abh-056
category: pattern | language: en
rule_summary: 句子长度统计学上均匀、没有变化，是 AI 痕迹；应混合短促和绵长的句子。
positive: "The system answers in 40ms at p99, about 20x faster than the tool it replaced."（长短句混合，引自上游）
negative: 连续多句都是 15-25 词、没有任何明显偏短或偏长的句子。违反点：句长高度一致，没有短句或长句的异常值。
source: path: skills/humanizer/SKILL.md; anchor: `### FILLER & HEDGING PATTERNS / P30: Uniform Sentence Length`
notes: 与 U-abh-084（Burstiness Principle 的具体数值目标：短 3-8 词/中 12-20 词/长 25-40 词，不超过 3 句连续同长度）是同一现象的"检测判据"和"改写目标"两面，判定内容不完全相同（P30 只给方向不给数字，Burstiness Principle 给了具体数字），故不合并，互相点名。

#### U-abh-057
category: pattern | language: en
rule_summary: 不因为重复语言模型的重复惩罚机制而给同一个实体换用一整个名词短语（"the artist"→"the visionary creator"→"the non-conformist painter"）；应选定最清楚的说法反复用。
positive: "Yankilevsky and other non-conformist artists faced obstacles. His work continued."（引自上游）
negative: "Yankilevsky, alongside other non-conformist artists, faced obstacles. The visionary creator's distinctive artistic journey continued."（引自上游）。违反点：同一个人被换称为"the visionary creator"这个整个名词短语。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P31: Elegant Variation (Noun-Phrase Cycling)`
notes: 与 P11（Synonym Cycling）互相点名，见 U-abh-037 的 notes。

#### U-abh-058
category: pattern | language: en
rule_summary: 不把面向用户的对话式框架（"in this article, we will explore""let me walk you through""here's what you need to know"）原样粘贴进已发布的文章；应删掉这类元评论，直接从内容开始。
positive: "This framework solves three problems that React Router doesn't."（引自上游）
negative: "In this article, we will explore the unique characteristics that make this framework worth using."（引自上游）。违反点：整句是对话式的"我们将探讨"框架语，没有进入实质内容。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P32: Collaborative Communication Leaking`
notes: 与 P19（Chatbot Artifacts）互相点名（"distinct from P19 identity disclosure"）；触发词与 P29 重叠，见 U-abh-055 的 notes。

#### U-abh-059
category: pattern | language: en
rule_summary: 不留下未填写的填空模板（如 `[Your Name]`、`[INSERT SOURCE URL]`、`2025-XX-XX`、方括号占位说明）；应填好或删掉。
positive: "Dear Alex, I am writing regarding the Q3 renewal."
negative: "Dear [Recipient], I am writing regarding [Topic]."（引自上游）。违反点：`[Recipient]`、`[Topic]`两处占位符未填写。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P33: Placeholder Text / Mad Libs`
notes: -

#### U-abh-060
category: pattern | language: en
rule_summary: 不保留复制粘贴时残留的工具内部引用标记（ChatGPT 的 `citeturn0search0`、`contentReference[oaicite:0]{index=0}`、`oai_citation`；Gemini 的 `[cite: 1]`、`[span_1](start_span)`；Grok 的 `grok_card`、`grok_render_citation_card_json`；DeepSeek 的透镜括号、剑号；Perplexity 的 `attached_file`、`ppl-ai-file-upload`；RAG 的 `attribution`/`attributableIndex` 标签；孤立的脚注字符）；应删掉这些标记，如果确实有价值再补一个真实引用。
positive: "The school has been recognized as an International Fellowship Centre."（引自上游）
negative: "The school has been recognized as an International Fellowship Centre. citeturn0search1"（引自上游）。违反点：句末残留了 ChatGPT 的内部引用标记 `citeturn0search1`。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P34: Chatbot Reference Markup Leaking`
notes: -

#### U-abh-061
category: pattern | language: en
rule_summary: 不保留 AI 工具在生成链接时附带的 UTM 追踪参数（`utm_source=chatgpt.com`、`utm_source=openai`、`utm_source=copilot.com`、`referrer=grok.com`）；应从 URL 里去掉这些参数。
positive: "`https://example.com/article`"（引自上游）
negative: "`https://example.com/article?utm_source=chatgpt.com`"（引自上游）。违反点：URL 带有 `utm_source=chatgpt.com`追踪参数。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P35: UTM Source Parameters from AI Tools`
notes: -

#### U-abh-062
category: pattern | language: en
rule_summary: 同一篇文字里不应出现突然的语域/口吻切换（正式英语段落突然接上带错别字的随意段落，或拼写风格中途从美式切到英式）；应统一同一个语域，把 AI 段落改写到匹配作者原有的声音。
positive: "yeah so the bug is in line 42. The loop allocates on every iteration instead of reusing the buffer."（引自上游，全文统一随意口吻）
negative: "yeah so the bug is in line 42 lol. The aforementioned implementation exhibits suboptimal performance characteristics."（引自上游）。违反点：前一句随意口语，后一句突然切换成正式书面语，语域断裂。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P36: Sudden Style/Register Shift`
notes: 与 P26（Perfect/Error Alternation）互相点名，见 U-abh-052 的 notes。

#### U-abh-063
category: pattern | language: en
rule_summary: 不用"被哪些媒体报道过"这份来源清单本身当作重要性的证明；应挑一个来源，说清楚它具体报道了什么。
positive: "Wired profiled her 2024 research on algorithmic bias in hiring software."（引自上游）
negative: "Her insights have been featured in Wired, Refinery29, and other prominent media outlets."（引自上游）。违反点：只列来源名单，不说任何一家具体报道了什么。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P37: Overattribution / Source-Listing as Content`
notes: 与 P2（Notability Name-Dropping）互相点名，见 U-abh-028 的 notes。

#### U-abh-064
category: pattern | language: en
rule_summary: 段落之间如果可以互换顺序而不破坏论证，说明这是并列的自足小论点堆砌而非展开的论证；每段应依赖上一段才能成立，可互换的段落应合并或删除。
positive: "Remote work's flexibility is the obvious sell. The harder question is what you lose..."（引自上游，段落顺序不可互换）
negative: "Remote work improves balance. Many workers prefer it. Studies show productivity rises. Commuting costs drop. Office costs decline too."（引自上游）。违反点：五句话互相独立，任意打乱顺序都不影响理解，说明论证没有真正展开。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P38: Paragraph-Reshuffling Immunity`
notes: 与 ZH15（立场缺失，见 U-abh-088 的 notes）在方法论上相关：patterns.zh.md 把 ZH15 标注为"对应 P38 段落可打乱性 + 英文版 North Star"，但 ZH15 的修正方式（逼出一个鲜明立场）更贴近 Step 3 的 Position engine（U-abh-088），故本单元不升级为 both，只在此处点名这层关系。

#### U-abh-065
category: pattern | language: en
rule_summary: 不用"Whether you prefer X or Y..."这类段末总结、"In summary,""To sum up,""Overall,"这类节末总结做 SEO 式的收束；应以最有信息量的具体点收尾。
positive: "Tokyo's best ramen counter doesn't have a phone, doesn't take reservations, and hasn't changed the broth recipe since 1987."（引自上游）
negative: "Tokyo offers everything from Michelin-starred restaurants to humble ramen stalls. Whether you prefer fine dining or street food, Tokyo has something for every palate."（引自上游）。违反点："Whether you prefer...has something for every palate"是典型的段末 SEO 式总结，没有任何具体信息。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P39: Paragraph-Closing "Whether" Summaries`
notes: -

#### U-abh-066
category: pattern | language: en
rule_summary: 不用"represents""symbolizes""speaks to""embodies""reflects broader"把一件平常小事解读出象征意义；应陈述事实本身，让读者自己解读。
positive: "The factory closed in 2009. Three hundred jobs. The town's high school dropped football the following year."（引自上游）
negative: "The closed factory represents the decline of American manufacturing and speaks to broader anxieties about post-industrial identity."（引自上游）。违反点："represents...speaks to broader anxieties"把一个具体事件强行解读成象征意义。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P40: Symbolic Gloss / Meaning-Telling`
notes: 与 P1（Significance Inflation）互相点名，见 U-abh-027 的 notes；ZH8 同时对应 P1 和 P40，本单元不升级为 both（已在 P1 承接），此处只做交叉引用。

#### U-abh-067
category: pattern | language: en
rule_summary: 不用"The catch?""The kicker?""Here's the thing.""The brutal truth?""Sound familiar?"这类社媒式假戏剧停顿；应删掉这句钩子，让下一句直接把话说完。
positive: "Most people abandon goals in week three. The ones who don't usually make the failure threshold explicit before they start."（引自上游）
negative: "Most people abandon goals in week three. The brutal truth? They lack a clear failure threshold."（引自上游）。违反点："The brutal truth?"是假戏剧停顿，没有实质作用。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P41: Infomercial Engagement Hooks`
notes: -

#### U-abh-068
category: pattern | language: en
rule_summary: 不在段落中随机加粗 1-4 个词、没有统一的加粗规则；应去掉这类随意加粗，只给术语表词条和 UI 标签保留加粗。
positive: "Remote work has fundamentally changed how companies operate. Most employees now want flexible arrangements."（引自上游，无随意加粗）
negative: "Remote work has **fundamentally changed** the way companies operate, with **many employees** now preferring **flexible arrangements**."（引自上游）。违反点：三处加粗没有共同的规则，纯属随意点缀。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P42: Erratic Inline Bolding`
notes: 与 P14（Boldface/Formatting Overuse）互相点名（"distinct from P14 systematic overuse"）：P14 管系统性、机械式的过度加粗，P42 管无规则、随机的零星加粗，不合并。

#### U-abh-069
category: pattern | language: both
rule_summary: 长段落反复用"In other words,""Put simply,""Essentially,""That is to say,"把同一个意思绕好几圈重复；应保留最清楚的一版，删掉重复的转述。
positive (en): "The system answers in 40ms at p99, about 20x faster than the tool it replaced."（引自上游）
negative (en): "The system is fast. In other words, it performs well. Put simply, speed is one of its strengths."（引自上游）。违反点：三句话用"In other words""Put simply"重复表达同一个意思。
positive (zh): "它把导出报表的时间从十分钟压到了一分钟。"
negative (zh): "它能提升效率。换句话说，它让工作更快。也就是说，它节省了时间。" 违反点："换句话说""也就是说"把同一个意思重复绕了三遍。
source: path: skills/humanizer/SKILL.md; anchor: `### EMERGING PATTERNS / P43: The Treadmill Effect (Low Information Density)`
notes: 中文示例来自 patterns.zh.md 的 ZH11（明确标注"对应 P43"），故定为 both。与 P22（sentence-level filler）、P30（uniform length）互相点名（"distinct from P22...and P30"）。

#### U-abh-070
category: pattern | language: en
rule_summary: 不让无生命的抽象事物做出人类才能做的动作（"the data tells us""the market rewards""the decision emerges"）；应指名具体的人，或者用"you"直接称呼读者。
positive: "Customers spend more with companies that answer support tickets within an hour."（引自上游）
negative: "The market rewards companies that listen."（引自上游）。违反点："the market"作为无生命抽象主语做出"rewards"这个拟人动作。
source: path: skills/humanizer/SKILL.md; anchor: `### CRAFT AND FORENSIC PATTERNS / P44: False Agency`
notes: -

#### U-abh-071
category: pattern | language: en
rule_summary: 不用悬浮在场景之上的疏离第三人称叙述（"nobody designed this""people tend to""one might say""there is a sense that"）；应把读者放进场景里，用"you"而不是"people"。
positive: "You will underestimate how much testing matters, right up until a Friday deploy pages you at 2am."（引自上游）
negative: "People tend to underestimate how much testing matters."（引自上游）。违反点：用疏离的"people tend to"而不是把读者直接拉进场景。
source: path: skills/humanizer/SKILL.md; anchor: `### CRAFT AND FORENSIC PATTERNS / P45: Narrator-from-a-Distance`
notes: -

#### U-abh-072
category: pattern | language: en
rule_summary: 文档不该用叙述改动过程的方式描述现状（"was added to""now uses""has been updated to""replaces the old""previously"）；应直接描述这个东西现在是什么样，删掉编辑历史。
positive: "This function fetches the user and returns a promise."（引自上游）
negative: "This function was refactored to replace the old callback approach with async/await."（引自上游）。违反点：用"was refactored to replace the old"叙述改动历史，而不是直接描述现状。
source: path: skills/humanizer/SKILL.md; anchor: `### CRAFT AND FORENSIC PATTERNS / P46: Diff-Anchored Writing`
notes: -

#### U-abh-073
category: pattern | language: en
rule_summary: 复合修饰语在名词前应连字符连接，但跟在动词后面（作表语）时应去掉连字符；不能不分位置一律加连字符。
positive: "The results are high quality and the pipeline is genuinely new."（引自上游）
negative: "The results are high-quality and the pipeline is state-of-the-art."（引自上游）。违反点："high-quality"作表语时不该保留连字符。
source: path: skills/humanizer/SKILL.md; anchor: `### CRAFT AND FORENSIC PATTERNS / P47: Hyphenated-Pair Overuse`
notes: -

#### U-abh-074
category: pattern | language: en
rule_summary: 不用"X is the new Y""the currency of""not a X but a Y""X is where Y meets Z"这类假深刻的格言模板代替具体论点；应删掉格言，直接说出真正的论点。
positive: "Ad networks pay about $8 per thousand views, so publishers chase pageviews."（引自上游）
negative: "Data is the new oil, and attention is the currency of the modern web."（引自上游）。违反点：两个格言模板（"X is the new Y""the currency of"）叠加，没有一句具体论点。
source: path: skills/humanizer/SKILL.md; anchor: `### CRAFT AND FORENSIC PATTERNS / P48: Aphorism Formulas`
notes: -

#### U-abh-075
category: pattern | language: en
rule_summary: 标题后面不该紧跟一句只是复述标题的话（或"This section covers X."）；应删掉这句复述，或换成一个真正的事实。
positive: "## Performance / The dashboard renders 10,000 rows in 40ms because it virtualizes the list."（引自上游）
negative: "## Performance / Performance is important for a good user experience."（引自上游）。违反点：标题下面这句话只是复述标题本身，没有信息增量。
source: path: skills/humanizer/SKILL.md; anchor: `### CRAFT AND FORENSIC PATTERNS / P49: Fragmented Headers`
notes: -

#### U-abh-076
category: pattern | language: en
rule_summary: 不用隐藏施事者的无主句被动式（"no configuration is needed""the results are preserved automatically""it is recommended that""changes were made"）；应指名具体的行为主体，用主动语态。
positive: "The file watcher clears the cache whenever you edit the config."（引自上游）
negative: "The cache is invalidated automatically when the config is changed."（引自上游）。违反点：两处被动语态（is invalidated / is changed）隐藏了具体的行为主体（file watcher / you）。
source: path: skills/humanizer/SKILL.md; anchor: `### CRAFT AND FORENSIC PATTERNS / P50: Passive / Subjectless Constructions`
notes: -

#### U-abh-077
category: pattern | language: en
rule_summary: 不把内部推理链的脚手架（"Let me think""Step 1:""Breaking this down""First, I'll"、本该留在内部的编号式思考过程）泄漏进最终文本；应删掉这些脚手架，只保留作者声音里的结论。
positive: "Ops engineers hit this endpoint about 400 times a day. That is who we are designing for."（引自上游）
negative: "Let me break this down. First, we need to understand the users. Step 1: identify who hits this endpoint."（引自上游）。违反点：保留了"Let me break this down""Step 1:"这类内部推理脚手架。
source: path: skills/humanizer/SKILL.md; anchor: `### CRAFT AND FORENSIC PATTERNS / P51: Reasoning-Chain Artifacts`
notes: -

#### U-abh-078
category: pattern | language: en
rule_summary: 不插入零宽字符（U+200B）、零宽连接符（U+200D）、软连字符（U+00AD）、密集的不换行空格，或用西里尔/希腊字母冒充拉丁字母，来躲避检测器；应清除这些字符，规范化为纯 NFC 文本。
positive: 一段文字规范化为纯 NFC 文本，不含任何零宽或控制字符（引自上游）。
negative: "Text seeded with zero-width spaces between letters so a detector reads gibberish."（引自上游）。违反点：字母之间插入了零宽空格，目的是让检测器读出乱码。
source: path: skills/humanizer/SKILL.md; anchor: `### CRAFT AND FORENSIC PATTERNS / P52: Unicode Obfuscation`
notes: 这条描述的是"绕过检测器"的具体手法，需要在归并阶段对照 criteria.md 第 5 条第 1 款（声称能"降低 AI 检测率""绕过检测器"的规则一律 rejected）：本规则的方向是"检测并清除混淆字符"（防御方向），不是"如何混淆以绕过检测"（攻击方向），字面上不违反该条款；但正反例本身描述了具体的混淆手法（零宽字符插入），拆规则阶段照抄是为了让规则可判定，裁决时仍需确认是否要在 rationale 里弱化这类"如何构造混淆"的具体描述。

#### U-abh-079
category: pattern | language: en
rule_summary: 不用"There are several ways to""There are a few things to consider""In general,""It is generally a good idea to""Generally speaking,"这类模糊枚举开场宣布一个笼统列表；应先给出具体答案，再省掉这些清嗓子式的铺垫。
positive: "Add an index on user_id. That one change took the query from 900ms to 12ms."（引自上游）
negative: "There are several ways to speed up a slow query. In general, it is a good idea to consider indexing."（引自上游）。违反点："There are several ways to"和"In general, it is a good idea to"两处模糊枚举开场，没有先给出具体答案。
source: path: skills/humanizer/SKILL.md; anchor: `### CRAFT AND FORENSIC PATTERNS / P53: Hedged-Enumeration Openers`
notes: 由 HC3 语料库（Guo et al. 2023, arXiv:2301.07597）里的高判别力词汇归纳而来，见 patterns.md 锚点 `## The HC3 corpus (grounding for P53 and the science claims)`；该引用是可以照抄的原文证据（MIT，full-text 允许）。

#### U-abh-080
category: pattern | language: en
rule_summary: 不反驳一个原文里根本没人提出过的反对意见（"While some might argue...""It would be easy to dismiss this as...""One might object that... but"）；应直接陈述立场，或者只反驳原文里真实存在、点名的反对意见。
positive: "Remote work hasn't hurt our collaboration. Our incident response time actually improved after we went remote."（引自上游）
negative: "While some might argue that remote work hurts collaboration, the data tells a different story."（引自上游）。违反点：反驳了一个原文中从未有人提出过的假想反对意见（"some might argue"）。
source: path: skills/humanizer/SKILL.md; anchor: `### CRAFT AND FORENSIC PATTERNS / P54: Argument Residue`
notes: patterns.md 明确说明 P54/P55 是"独立描述、不借用其他项目的术语和文字"（见 anchor `## The craft and forensic set (P44-P55)` 的 provenance note），拆规则阶段照实记录这条 provenance 声明，供归并阶段核实原创性时参考。

#### U-abh-081
category: pattern | language: en
rule_summary: 不保留一个和最终确定的论断语气矛盾的过时保留语（"to some extent""in some ways""to a certain degree""arguably"）；应重读每个保留语和它所在的句子，删掉任何底气和句子实际自信程度对不上的保留语。
positive: "This approach solves the problem."（引自上游）
negative: "To some extent, this approach is arguably the best option, and it will definitely solve the problem."（引自上游）。违反点："To some extent""arguably"两处保留语和后半句"will definitely solve"的绝对自信语气自相矛盾。
source: path: skills/humanizer/SKILL.md; anchor: `### CRAFT AND FORENSIC PATTERNS / P55: Leftover Hedge Debris`
notes: 与 P54 共享同一条 provenance note（见 U-abh-080 的 notes）。

#### U-abh-082
category: pattern | language: en
rule_summary: 分号或冒号在连续 3 句以上密集出现是与破折号同类、但置信度更低的新兴信号（社区报告、无对照研究支撑）；孤立的一个分号或冒号不该被标记，只有聚类出现时才算一个弱信号。
positive: 一段文字里偶尔各出现一次分号和冒号，不被标记。
negative: 连续四句话都用分号或冒号连接从句。违反点：分号/冒号在连续多句里密集聚类出现。
source: path: skills/humanizer/SKILL.md; anchor: `### LANGUAGE & STYLE PATTERNS / P13: Em Dash Ban`（紧随其后的"Related, lower-confidence note"一段）
notes: 与 P13（U-abh-039，破折号零容忍）判定强度不同：P13 零容忍，本条只在聚类且低-中置信度时才算信号，不合并；上游没有给这条单独编号，本单元的临时 id 只在本清单内使用。

#### U-abh-083
category: measurement | language: en
rule_summary: P7 的 AI 高频词按证据强度分四档：Tier 1A（delve、tapestry、testament、multifaceted、realm、interplay、"in today's...landscape"）单独出现一次即可视为强证据；Tier 1B（underscore动词、leverage动词、"it's worth noting"、"it's important to note"）要标记但权重更低，单独一次不能和 Tier 1A 同等看待；Tier 2（crucial、pivotal、vibrant、robust、foster、enhance、showcase、notably、moreover、furthermore、garner、bolster、"align with"、utilize）只在同一段落出现 2 次以上才算证据；Tier 3（key、important、significant、various、effective、valuable、powerful、essential）单独出现从不算证据，只有和 Tier 1/2 聚类出现才算。
positive: 一段文字里出现一次"significant"（Tier 3），周围没有其他任何 Tier 1/2 词，不因此提高分数。
negative: 仅凭一次"significant"（Tier 3）或一次"crucial"（Tier 2，未聚类）就把文本判为高分。违反点：把低层级词的孤立出现当成了和 Tier 1A 同等的证据。
source: path: skills/humanizer/SKILL.md; anchor: `### Tiered-confidence vocabulary (refines P7)`
notes: 这条改变的是"这些词该怎么计入分数权重"，与 P7 本身"该不该删这些词"的判定逻辑不同（P7 是内容规则，本条是打分权重规则），故单独归为 measurement 而不并入 P7；与 J3（U-abh-105，评分公式里的 vocabulary_blacklist_ratio）直接相关，评分公式吃的正是这个分级后的比例。

#### U-abh-084
category: measurement | language: en
rule_summary: 每段应混合短句（3-8 词）、中句（12-20 词）、长句（25-40 词），不应连续 3 句以上长度相近；允许使用片段句和偶尔的单词句。
positive: 一段话里既有一句 5 词的短句，也有一句 30 词的长句，中间穿插中等长度的句子。
negative: 连续四句都在 15-20 词区间，没有任何短句或长句打断。违反点：连续超过 3 句长度相近，且句长范围没有覆盖短/中/长三档。
source: path: skills/humanizer/SKILL.md; anchor: `### The Burstiness Principle`
notes: 与 P30（U-abh-056）互相点名：P30 是检测层面的现象描述，本条是改写时的具体数值目标，见 P30 的 notes。评分公式（U-abh-105）里的 burstiness_normalized 项直接依赖这条描述的指标。

#### U-abh-085
category: style-opinion | language: en
rule_summary: 应选用第二或第三个想到的词而不是第一反应的最常见说法，使用领域黑话或俚语，做出源自个人经历的意外类比，偶尔用非正式过渡词（"Anyway,""So here's the thing:""Look,""Thing is,"），以此提高文字的"意外程度"（perplexity）。
positive: "Anyway, the real fix was two lines, not the refactor everyone was scared of."
negative: 通篇只用最直接、最常见的词汇和表达，没有任何意外的类比或非正式过渡。违反点：全篇用词都是统计学上最可预测的选择，没有体现"选第二三个想到的词"这条要求。
source: path: skills/humanizer/SKILL.md; anchor: `### The Perplexity Principle`
notes: 拿不准是否可判定：反例只能说明"没有体现"，但很难像其他规则一样从一句话里精确"圈出违反点"（"选了第一反应的词"这件事本身无法从最终文本里逆向验证），按 criteria.md 第 2 条大概率会在裁决阶段被判"不可判定"，收录是为了保留这个思路供归并阶段讨论。

#### U-abh-086
category: process | language: en
rule_summary: 开始改写前先输出一行"Reading this as: <kind> for <audience>, register <formal / neutral / casual>."，为后续所有改写决策定调；只有在 edit 模式下处理一个已经有稳定声音的文件时才跳过这一步。
positive: 改写正文前先输出"Reading this as: a technical README for backend engineers, register: neutral."
negative: 直接开始改写，完全不输出这行定调声明。违反点：跳过了 Voice Read 这一步。
source: path: skills/humanizer/SKILL.md; anchor: `## Step 3: Rewrite Craft / Voice Read`
notes: -

#### U-abh-087
category: process | language: en
rule_summary: 改写时应主动点名并拒绝以下反射性默认动作：机械性的三项排比、每段结尾都加一句工整的总结句、各打五十大板的两边论调、"In conclusion"式收尾、开头复述一遍原始指令；给本该保持平实的文字硬注入个性同样是一种"AI 味"。
positive: 一篇技术说明的每一段都以具体信息结尾，没有一段以工整的总结句收尾。
negative: 每一段末尾都补一句"总的来说，这体现了……的重要性"式的总结。违反点：反射性地在每段结尾添加了工整总结句。
source: path: skills/humanizer/SKILL.md; anchor: `## Step 3: Rewrite Craft / Anti-Default Discipline`
notes: 这是一条汇总性规则，判定逻辑一致（"改写时不要反射性地做这些默认动作"），但具体对象和已有单元有重叠，归并阶段应参考：机械三项排比→P10（U-abh-036）；段末总结句→P39（U-abh-065）；各打五十大板→P54（U-abh-080）/ZH15（见 U-abh-088）；"In conclusion"收尾→P24（U-abh-050）/P39；复述指令开头→P29（U-abh-055）/P32（U-abh-058）。也吸收了 Soul Injection Techniques 里"End without wrapping up"一条（不单独立条，见 notes 提示）。

#### U-abh-088
category: style-opinion | language: both
rule_summary: 对于任何观点或论证，应逼出一个站得住脚、足够鲜明的立场，并点名一个具体的反对对象；一个没人能反驳的观点不是观点。在中性、技术或参考类文本上应跳过这一步，那里立场就是事实本身。
positive (en): "Teams under ten people shouldn't run microservices. We tried it; maintaining the service mesh alone ate two engineers' time."（自撰，体现点名具体反方并给出代价）
negative (en): "There are pros and cons to both approaches, and the right choice depends on your specific context." 违反点：各打五十大板、不点名任何具体反方、读者猜不出作者站哪边。
positive (zh): "团队少于十个人就别上微服务。我们试过，光维护那套服务发现就吃掉了两个人。等你真被单体拖垮了再拆也不迟。"（引自 patterns.zh.md ZH15）
negative (zh): "关于是否采用微服务，业界看法不一。它既有优势，也有挑战，需要根据具体情况权衡，没有绝对的对错。"（引自 patterns.zh.md ZH15）违反点：全文没有一句可反驳的判断，两边都占理，读者不知道作者站哪边。
source: path: skills/humanizer/SKILL.md; anchor: `## Step 3: Rewrite Craft / Position engine (give it teeth)`
notes: patterns.zh.md 的 ZH15 明确标注"对应 P38 段落可打乱性 + 英文版 North Star"，其修正方式与本条（逼出一个站得住的立场、点名反方）几乎一一对应，故本单元定为 both，中文例句取自 ZH15，附加锚点 `## 最深层痕迹 · The deepest tell (ZH15)`。同时也和 U-abh-024（North Star）、U-abh-064（P38）语义相关，三者互相点名，不合并——North Star 太笼统不可判定，P38 是检测层面的可打乱性测试，本条是改写阶段的操作性要求，三者判定粒度不同。

#### U-abh-089
category: process | language: en
rule_summary: 改写时应把每个抽象表述换成原文已暗示或明确给出的具体形象、类比或动作（"The process is complex"变成实际的步骤，"Improves performance"变成"cuts p99 latency from 900ms to 40ms"）；一句话如果套用到任何事情上都成立，就等于什么也没说。
positive: 把"the API is easy to use"具体化为"you can fetch a user in one call: `GET /users/:id`"。
negative: 保留"the process is complex"这类抽象表述，不做任何具体化处理。违反点：没有把抽象表述换成原文已有的具体细节。
source: path: skills/humanizer/SKILL.md; anchor: `## Step 3: Rewrite Craft / Concretizer pass`
notes: 与 U-abh-023（No fabrication protection）是同一原则的两面，见该条 notes；Soul Injection Techniques 里"Use specific sensory/experiential details"一条与本条高度重叠，不单独立条，归并阶段可作为同一规则的额外证据。

#### U-abh-090
category: style-opinion | language: en
rule_summary: 应有真实的反应而不是只做报告；对一件事发表实际的观点比中立地陈述它的属性更有人味。
positive: "This API design is frustrating."（引自上游）
negative: "The API has certain limitations."（引自上游）。违反点：用中立、回避态度的措辞代替了本可以直接表达的真实反应。
source: path: skills/humanizer/SKILL.md; anchor: `### Soul Injection Techniques / Have actual opinions.`
notes: 与 U-abh-088（Position engine）方向一致但粒度更小（本条管"有没有反应"，Position engine 管"论证是否有立场"），不合并，互相点名。

#### U-abh-091
category: style-opinion | language: en
rule_summary: 确定性的用词应该对应真实的信念强度并形成一个光谱，而不是只会打折扣：高确信用"clearly""no question"，中等用"I think""in my experience"，真正的怀疑用"I'm not sure, but"；不应堆叠保留语，也不应通篇停留在扁平的中等确信度。
positive: 同一篇文字里对不同论点分别用了"clearly"（高确信）和"I'm not sure, but"（真正怀疑），确信度有真实的高低变化。
negative: 通篇所有论点都用"I think"这一种确信度表达，不管论点本身其实差异很大。违反点：确信度扁平，没有随论点强弱变化。
source: path: skills/humanizer/SKILL.md; anchor: `### Soul Injection Techniques / Calibrate certainty on a spectrum, don't just hedge.`
notes: 与 P23（Excessive Hedging，U-abh-049）相关但角度不同：P23 管"不要堆叠保留语"，本条额外要求"确信度要有真实的高低变化"，不合并。

#### U-abh-092
category: style-opinion | language: en
rule_summary: 应引用读者共有的经历来建立连接（"You know that feeling when..."这类表达）。
positive: "You know that feeling when a deploy goes out on Friday and you spend the weekend refreshing the dashboard?"
negative: 通篇没有任何一句尝试和读者的共同经历建立连接，全是抽象陈述。违反点：完全没有使用共有经历式表达。
source: path: skills/humanizer/SKILL.md; anchor: `### Soul Injection Techniques / Reference shared human experiences.`
notes: -

#### U-abh-093
category: style-opinion | language: en
rule_summary: 应允许简短的跑题和旁支话题，一段简短的离题能体现一个正在思考的头脑。
positive: 主线之外插入一句"（说句题外话，这个 bug 让我想起去年那次更离谱的事故）"再回到主线。
negative: 全文严格按照大纲逐条推进，没有任何一句离题或旁支。违反点：完全没有允许任何跑题，行文过于工整。
source: path: skills/humanizer/SKILL.md; anchor: `### Soul Injection Techniques / Allow tangents and asides.`
notes: -

#### U-abh-094
category: style-opinion | language: en
rule_summary: 可以用"不完美开头"技巧，从思路中途直接切入（"So I was looking at the logs and..."），而不是先给背景铺垫。
positive: "So I was looking at the logs and noticed the retry count kept climbing."（引自上游）
negative: "In this section, I will describe how I discovered an issue by examining the logs." 违反点：用了完整的背景铺垫式开头，而不是从思路中途直接切入。
source: path: skills/humanizer/SKILL.md; anchor: `### Soul Injection Techniques / Use the "imperfect start" technique.`
notes: -

#### U-abh-095
category: style-opinion | language: en
rule_summary: 应使用"回响"技巧，回指前文提到过的东西（"Remember that API I called frustrating? It gets worse."）。
positive: "Remember that API I called frustrating? It gets worse."（引自上游）
negative: 后文提到的每个话题都是全新的，从不回指前面已经说过的内容。违反点：完全没有使用任何回指前文的"回响"。
source: path: skills/humanizer/SKILL.md; anchor: `### Soul Injection Techniques / Use callbacks.`
notes: -

#### U-abh-096
category: style-opinion | language: en
rule_summary: 应允许行文中途自我纠正（"The system handles auth... well, authentication and authorization are separate, but you get the idea."），一次小的纠正能体现实时思考。
positive: "The system handles auth... well, authentication and authorization are separate, but you get the idea."（引自上游）
negative: 全文所有表述都一次性精确无误，没有任何一处自我纠正的痕迹。违反点：完全没有使用自我纠正，行文过于工整。
source: path: skills/humanizer/SKILL.md; anchor: `### Soul Injection Techniques / Self-correct.`
notes: -

#### U-abh-097
category: process | language: en
rule_summary: `detect` 模式只扫描全部 55 条模式、记录每条命中的模式编号和名称、原文引用、触发原因和建议修法，输出结构化报告，不做任何改写。
positive: `--mode detect`的输出是一份带 `# / Pattern / Text / Fix` 表格的报告，原文没有任何改动。
negative: `--mode detect`时直接输出了改写后的文本，没有输出报告表格。违反点：detect 模式下不应输出改写结果，应输出报告。
source: path: skills/humanizer/SKILL.md; anchor: ``### Mode: `detect` ``
notes: -

#### U-abh-098
category: measurement | language: en
rule_summary: detect 报告里的严重程度分级：命中 8 条以上模式记为 HIGH（"heavy AI smell"）。
positive: 命中 10 条模式的报告标注"Severity: HIGH"。
negative: 命中 10 条模式的报告标注为"Severity: LOW"。违反点：命中数超过 8 条却没有标为 HIGH。
source: path: skills/humanizer/SKILL.md; anchor: ``### Mode: `detect` / Severity: HIGH (8+ patterns = heavy AI smell)``
notes: 与 U-abh-105（0-100 评分表）是两套独立的量表（一个是"命中数量"阈值，一个是"综合分数"区间），不合并，但同一份 detect 报告里可能同时出现，归并阶段需要确认这两套量表是否需要统一。

#### U-abh-099
category: process | language: en
rule_summary: `rewrite`模式的执行顺序：内部跑一遍检测但不输出报告，为每个命中的模式打补丁，按 `--voice`做语气注入，最后核验并输出改写结果附带一段简短的变更摘要。
positive: `--mode rewrite`的输出只有改写后的文本和一段"Changes: Removed 12 AI patterns..."式摘要，没有单独的检测报告。
negative: `--mode rewrite`的输出里混入了一份完整的 detect 报告表格。违反点：rewrite 模式不应输出检测报告本身，只应输出改写结果和简短摘要。
source: path: skills/humanizer/SKILL.md; anchor: ``### Mode: `rewrite` ``
notes: -

#### U-abh-100
category: measurement | language: en
rule_summary: 改写结果在输出前需核验：不残留 AI 黑名单词（除非确实必要）、零破折号（U+2014）、句长方差超过 30%、不超过 2 句连续相似结构、没有孤立的格式残留。
positive: 改写结果句长方差超过 30%，没有破折号，也没有连续 3 句以上结构相似的句子。
negative: 改写结果里句长方差只有 10%，且有连续 3 句结构几乎相同（都是"X does Y."的模式）。违反点：句长方差没有达到 30%，且连续相似结构句超过 2 句上限。
source: path: skills/humanizer/SKILL.md; anchor: ``### Mode: `rewrite` / Verify the rewrite:``
notes: "零破折号"一项与 P13（U-abh-039）重复，此处作为 rewrite 模式输出前的核验清单一并记录；"句长方差超过 30%"和"不超过 2 句连续相似结构"是本文件里新出现的具体数值，与 Burstiness Principle（U-abh-084）的数值目标（3-8/12-20/25-40 词、不超过 3 句连续同长度）不完全一致（一个用方差百分比，一个用绝对词数区间；一个是"不超过 2 句"，一个是"不超过 3 句"），这是同一来源内部两处数值表述不一致，留在"拆分时拿不准的地方"一节。

#### U-abh-101
category: process | language: en
rule_summary: `edit`模式遇到源代码、配置或结构化数据（`.js`、`.ts`、`.py`、`.go`、`.rs`、`.json`、`.yaml`、`.yml`、`.toml`、`.env`、`.csv`、`.lock`等扩展名，或内容明显不是散文），应停止并说明"This looks like code or structured data, not prose..."，不做任何编辑；Markdown、纯文本等散文格式才继续往下走。
positive: `--file config.yaml --mode edit`时输出拒绝编辑的说明，文件未被改动。
negative: `--file config.yaml --mode edit`时直接对 YAML 文件做了改写。违反点：对非散文的结构化数据文件做了编辑，应该拒绝。
source: path: skills/humanizer/SKILL.md; anchor: ``### Mode: `edit` / Refuse non-prose targets.``
notes: -

#### U-abh-102
category: process | language: en
rule_summary: `edit`模式在确认是散文文件后：先对文件内容跑检测；如果 0 条命中，回复"This file reads clean. No AI patterns detected."；如果有命中，用 Edit 工具做针对性的局部改动（不是整篇重写），保留作者已有的人类声音，改完后重新读取并核验问题已解决，最后输出改动摘要。
positive: 对一个命中 3 条模式的 Markdown 文件，只用 Edit 工具改动了那 3 处，其余原文一字未动，并输出了改动摘要。
negative: 对一个只命中 1 条模式的 Markdown 文件做了整篇重写，而不是针对那一处做局部编辑。违反点：edit 模式应做针对性的局部改动，而不是整篇重写。
source: path: skills/humanizer/SKILL.md; anchor: ``### Mode: `edit` / If patterns found: apply fixes with the Edit tool``
notes: -

#### U-abh-103
category: process | language: en
rule_summary: 输出前的最终检查清单：检查开头是否是无聊的概览句（对应 P29）、检查结尾是否是空泛乐观收尾（对应 P24）、清点是否还残留 AI 黑名单词（对应 P7）、检查是否零破折号（对应 P13）、检查是否有 3 句以上连续相似长度的句子（对应 Burstiness）；"读出声音判断像不像press release"和"能不能想象出一个具体的人写了这个"这两项本身是定性提示，给不出可判定的具体违反点。
positive: 输出前逐项核对，确认开头不是概览句、结尾不是空泛乐观、无残留黑名单词、零破折号、无连续相似长句。
negative: 输出前跳过核对步骤，直接把改写结果交出去，结果里仍残留一个"delve"和一处破折号。违反点：跳过最终核验，导致已知问题（黑名单词、破折号）没有被清除。
source: path: skills/humanizer/SKILL.md; anchor: `## Step 5: Final Quality Check`
notes: 这是一条汇总性的复核清单，7 项里 5 项分别对应已有单元（P29/U-abh-055、P24/U-abh-050、P7/U-abh-033、P13/U-abh-039、Burstiness/U-abh-084），另外 2 项（"读出声音判断"、"谁写了这个"测试）按 criteria.md 第 2 条大概率不可判定，只保留描述，不单独拆出可判定的正反例。

#### U-abh-104
category: process | language: en
rule_summary: 完成第一版改写后，应对着自己的草稿问一句"What still makes this read as AI?"，诚实地列出两三点，再针对这几点做一轮修正；这个元认知步骤比完整跑一次 `--iterate`更省成本，且能抓到清单查不出来的痕迹，与 `--iterate`互补而非替代。
positive: 第一版改写后自问自答列出两点残留问题，针对性修正后再输出最终版本。
negative: 第一版改写完直接输出，跳过自我审查这一步。违反点：没有做"What still makes this read as AI?"这一轮自审。
source: path: skills/humanizer/SKILL.md; anchor: ``### Draft, self-audit, final (cheap quality pass, distinct from `--iterate`)``
notes: -

#### U-abh-105
category: measurement | language: en
rule_summary: 设置 `--score`时，按 `score = 4 × patterns_hit + 25 × (1 - burstiness_normalized) + 15 × (vocabulary_blacklist_ratio)`计算 0-100 分并夹在 0-100 区间内，分数越低越像人写；区间含义：0-20 pristine（读起来像具体的人写的，不该被任何检测器标记）、21-40 mostly human（一两个小痕迹，容易清理）、41-60 mixed（半人半 AI，可能是部分编辑过）、61-80 AI-leaning（多处结构性痕迹，检测器大概率会抓到）、81-100 pure AI smell（整段是未经编辑的聊天机器人输出）。分数显示在输出的第一行，改写内容之前。
positive: 命中 3 条模式、burstiness_normalized 为 0.8、vocabulary_blacklist_ratio 为 0.1 的文本，按公式算出的分数落在 21-40 区间，输出标注"Mostly human"。
negative: 按公式算出分数是 75，却在输出里标注"Pristine"。违反点：分数区间和标注的verdict不匹配。
source: path: skills/humanizer/SKILL.md; anchor: ``### Scoring rubric (used when `--score` is set)``
notes: 与 U-abh-083（Tiered vocabulary confidence）直接相关：公式里的 vocabulary_blacklist_ratio 就是分级后的比例。

#### U-abh-106
category: measurement | language: en
rule_summary: 模型给自己的输出打分容易虚高；`--score`只应被当作一个信号，不是定论，真正的验收应该是独立的一遍检查或人类读者。
positive: 报告里注明"该分数由本次改写的同一次会话生成，仅供参考，建议再找独立的一遍检查或人工复核"。
negative: 把 `--score`给出的分数直接当作最终验收标准，不做任何独立复核。违反点：把自评分数当成了定论而非信号。
source: path: skills/humanizer/SKILL.md; anchor: ``### Scoring rubric (used when `--score` is set) / A model grading its own output in the same session``
notes: cli/ 目录提供的确定性版本指标（burstiness、type-token ratio、Flesch-Kincaid 等）不在追踪路径内，不读不跑，此处只记录 SKILL.md 正文里提到"有这么个工具"这一事实，不展开其内容。

#### U-abh-107
category: process | language: en
rule_summary: 设置 `--iterate N`（N≤3）时，产出改写后在输出上重新跑一遍检测；如果命中数大于 0 且迭代次数小于 N，就把这次改写结果作为新输入递归；命中数为 0 或达到 N 次时停止，并在最终变更摘要里注明总共迭代了几次。
positive: 第一次改写后检测仍命中 2 条模式，且迭代次数 1<3，于是用改写结果作为新输入再跑一轮，最终摘要注明"Converged in 2 iterations"。
negative: 设置了 `--iterate 3`，但只跑了一次改写就直接输出，也没有在摘要里说明迭代次数。违反点：没有按命中数和迭代次数的条件判断是否继续递归。
source: path: skills/humanizer/SKILL.md; anchor: ``### Iterate handling (used when `--iterate N` is set)``
notes: `## Quick reference / Flags / --iterate N`是同一规则的重复锚点，取本处更详细的描述为主，Quick reference 表格行不再单独立条。

### 2.2 来自 references/patterns.md（path: skills/humanizer/references/patterns.md）

这个文件是 55 条模式的深挖版：完整触发词表、before/after 例句、emerging 模式的来源引用、Wikipedia 覆盖对照表、目录局限性说明。除下面一条外，全部内容都是对 SKILL.md 已有模式的补充说明（完整触发词表、例句、出处），已经在 2.1 节对应单元的 notes 里逐条标注了补充锚点，不再重复拆成新单元。

#### U-abh-108
category: genre | language: en
rule_summary: 本目录（P1-P55）不覆盖虚构/创意类文本；StoryScope（arXiv:2604.03136）的研究发现，区分人类和 AI 小说更可靠的信号是叙事结构特征（未解决的支线、人物选择的模糊性、非线性结构），而不是本目录依赖的用词和标点，虚构文本需要专门的模式和 guardrails，不能直接套用本目录。
positive: 面对一篇小说手稿，先确认是否需要单独的虚构文本模式，而不是直接套用 P1-P55 检测。
negative: 直接用 P1-P55 的用词/标点类触发词去审查一篇小说，把叙事上合理的重复用词判定为"AI 痕迹"。违反点：对虚构文本套用了不适用的通用散文检测标准。
source: path: skills/humanizer/references/patterns.md; anchor: `## Honest limits of this catalog`（"Fiction and creative prose sit outside this catalog's current scope"段）
notes: 这是 patterns.md 里唯一一条产生新判定内容的规则（本目录的适用边界），其余"Honest limits"小节的内容（目录会随对齐方式漂移过时、P7/P13/P17 最容易过时、结构性模式更耐久、人类评委辨识准确率接近抛硬币）是评估目录可靠性的元评论，不是可以从一句具体文本判定"违反"或"没违反"的规则，归为非规则内容，仅在"疑似常见规则"和"拿不准的地方"两节里提及。

### 2.3 来自 references/patterns.zh.md（path: skills/humanizer/references/patterns.zh.md）

作者自述这是实验性草稿（ZH1-ZH15），未经中文母语写手校验，且明确说明英文的 burstiness/perplexity 指标不能直接迁移到以字为单位的中文。ZH8-ZH12、ZH15 在原文里被明确标注"对应"某条英文模式，按任务要求已在 2.1 节合并进对应的英文单元（分别是 P1/U-abh-027、P18/U-abh-044（含 P22/U-abh-048）、P10/U-abh-036、P43/U-abh-069、P14/U-abh-040、Position engine/U-abh-088），不在本节重复。本节只收 ZH1-ZH7（原文自称"核心原生模式"，未标注对应哪条英文模式）、ZH13-ZH14（原文自称"未验证假设"），以及一条关于中文场景下 burstiness/perplexity 指标本身不适用的度量单元。

#### U-abh-109
category: pattern | language: zh
rule_summary: 不用一连串四字成语、对仗短语堆出"文学感"，也不写听起来能摘抄、实则没有信息量的空心金句；应删掉这类堆砌，只保留有具体场景、有代价权衡、有明确态度的压缩句。
positive: "过去三年，我们把部署时间从两小时压到了九分钟。代价是每次发布都得盯着监控，怕它崩。"（引自上游）
negative: "在这个日新月异、瞬息万变的时代，技术的浪潮波澜壮阔、势不可挡，深刻地改变着我们的生活方式。"（引自上游）。违反点：连续四字成语和对仗排比堆砌（日新月异、瞬息万变、波澜壮阔、势不可挡），没有任何具体信息。
source: path: skills/humanizer/references/patterns.zh.md; anchor: `## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH1`
notes: 原文标题为"ZH1：四字词语堆砌 / 空心金句"，未标注对应哪条英文模式，保持 zh-only，不并入任何 P 单元。

#### U-abh-110
category: pattern | language: zh
rule_summary: 不机械地用"首先……其次……再次……最后……"搭骨架；应删掉这些连接词，让内容本身的逻辑决定顺序，或者分点但不加套话式序词。
positive: "它快了三倍，服务器账单少了一半。用户没抱怨，这是头一回。"（引自上游）
negative: "首先，它提升了效率。其次，它降低了成本。最后，它改善了体验。"（引自上游）。违反点："首先……其次……最后……"机械化的序词脚手架，内容本身空泛。
source: path: skills/humanizer/references/patterns.zh.md; anchor: `## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH2`
notes: 与英文"first, second, finally"脚手架同源但没有被上游标注为某条 P 编号的直接对应，保持 zh-only；归并阶段可参考是否与英文任何一条模式合并，暂不预设。

#### U-abh-111
category: pattern | language: zh
rule_summary: 不用换个主语就能套到任何文章上的万能空话开场；应直接从最具体的那句话开始——一个数字、一个场景、一个判断。
positive: "上周我用 AI 重写了一份 API 文档，母语审稿人五秒就退回来了，说'一股机翻味'。"（引自上游）
negative: "随着人工智能的飞速发展，各行各业正在经历前所未有的深刻变革。"（引自上游）。违反点："随着……的飞速发展""前所未有的深刻变革"是可以套用到任何主题的万能空话开场。
source: path: skills/humanizer/references/patterns.zh.md; anchor: `## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH3`
notes: 与 P29（Comprehensive Overview Opening）、P53（Hedged-Enumeration Openers）语义接近但触发词完全不同，未被上游标注为对应关系，保持 zh-only，仅在此处提示与 U-abh-055、U-abh-079 的相似性。

#### U-abh-112
category: pattern | language: zh
rule_summary: 不用一批中文 AI 文本高频出现的书面腔、外来语翻译腔、企业黑话词汇，如"此外、值得注意的是、至关重要、深入探讨、赋能、抓手、闭环、底层逻辑、颗粒度、打法、格局、生态、织锦、挂毯、相互作用、凸显、彰显、标志着、令人叹为观止、坐落于、不可或缺、保驾护航、量身打造"；应换成日常说法，或直接删。
positive: "我们把三个系统的数据接到了一起，这样退款不用再手动对账了。"（引自上游）
negative: "此外，构建数据闭环、打通底层逻辑，对于赋能业务增长至关重要。"（引自上游）。违反点："此外""闭环""底层逻辑""赋能""至关重要"五个中文 AI 黑名单词聚集在一句话里。
source: path: skills/humanizer/references/patterns.zh.md; anchor: `## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH4`
notes: 概念上和 P7（AI Vocabulary Words）平行——都是"AI 高频词黑名单，该删或换"——但词表完全不是逐词翻译（"抓手""颗粒度""闭环"这类企业黑话在英文清单里没有对应词），上游把它放进"核心原生模式"而非"英文模式的中文对应"一节，说明作者自己也认为这不是 P7 的翻译版而是独立的中文现象，故不并入 P7（U-abh-033），保持 zh-only，只在两条的 notes 里互相点名这层"概念平行但非同一规则"的关系。原文特别注明"织锦/挂毯"是 tapestry 的翻译腔、"格局/生态"是 landscape/ecosystem 的对译，这两个词条本身可以看作 P7 词表的中文借词现象，归并阶段可留意。

#### U-abh-113
category: pattern | language: zh
rule_summary: 中文改写里破折号不受"零容忍"约束，可以在真正需要解释、转折或停顿时用一次；但不能当万能连接符到处滥用，也不能让中文正文混入英文式逗号、括号、引号或全角半角标点乱套。应统一用中文全角标点，破折号只用一次。
positive: "这个方案能省一半时间。代价是前期要重写数据层，大概两周。"（引自上游）
negative: "这个方案——非常创新——它将——从根本上——改变行业(尤其是效率方面)."（引自上游）。违反点：一句话里出现四处破折号滥用，且括号和句号用了英文半角标点(半角括号、"."）。
source: path: skills/humanizer/references/patterns.zh.md; anchor: `## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH5`
notes: 这条与 P13（em dash 零容忍，U-abh-039）在同一话题上给出了不同的判定标准：patterns.zh.md 开头明确写"中文改写里可以使用破折号，这份文件不受仓库禁破折号 CI 的约束"。这是同一来源内部按语言分域的范围声明，不是矛盾的两条规则要"二选一"，而是 P13 的适用范围本来就限定在英文、ZH5 是中文场景下判定逻辑不同的替代规则（P13 零容忍单次出现；ZH5 允许单次、只惩罚滥用聚类+标点混用）。已在 U-abh-039 的 notes 里同步记录这层关系，归并阶段裁决 P13 时需要连带确认其 language 范围是否明确限定为 en，避免被误用到中文改写上。

#### U-abh-114
category: pattern | language: zh
rule_summary: 不反复用"为什么……？因为……""是什么让它与众不同？答案是……"这种自问自答的机械节奏；偶尔一次是修辞，通篇就是套路，应把问句改成直接陈述。
positive: "它高效，是因为绕过了那一层缓存。安全性我还没压测过，别在生产上用。"（引自上游）
negative: "为什么它如此高效？因为它采用了先进的架构。那么，它安全吗？答案是肯定的。"（引自上游）。违反点：连续两组自问自答，通篇都是这个节奏，没有一句直接陈述。
source: path: skills/humanizer/references/patterns.zh.md; anchor: `## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH6`
notes: 原文写"区别于英文 P27 的疑问句标题"——P27（U-abh-053）管长文小标题用问句，本条管正文里反复的自问自答节奏，对象不同，不合并，仅互相点名。

#### U-abh-115
category: pattern | language: zh
rule_summary: 不把结尾一律拉高到空洞的乐观（"让我们拭目以待、未来一片光明、必将产生深远影响、前景无限、值得期待、共同书写新篇章"）；应用一个具体的下一步、一个待解问题或一句真实的判断收尾。
positive: "下一步要解决冷启动那 800 毫秒的延迟。搞不定的话这套方案就得推倒重来。"（引自上游）
negative: "我们有理由相信，在各方的共同努力下，未来必将一片光明，让我们拭目以待。"（引自上游）。违反点：整句是空洞乐观口号，没有任何具体的下一步或判断。
source: path: skills/humanizer/references/patterns.zh.md; anchor: `## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH7`
notes: 与 P24（Generic Positive Conclusions，U-abh-050）语义高度平行，但原文没有把 ZH7 标注为"对应 P24"（不在 ZH8-ZH12 那批被明确标注的条目里），触发词也完全不同（中文的"拭目以待""共同书写新篇章"不是"the future looks bright"的翻译），尊重上游自己的分类边界，保持 zh-only，只在两条 notes 里互相点名。

#### U-abh-116
category: pattern | language: zh
rule_summary: 【未验证假设，原文自称推测、无竞品验证】假设 AI 中文倾向堆叠"的"字定语（一个名词前挂三层以上"的"）、句末机械加"了"；若成立，应拆掉多层"的……的……的"定语改成短句，删掉不必要的"了"。
positive: "这方案用了新的检索层，专门解决搜索慢的问题。"（引自上游）
negative: "这是一个基于最新技术的、经过精心设计的、能够满足用户需求的解决方案了。"（引自上游）。违反点：一个名词（解决方案）前堆叠了三层"的"定语，句末又加了不必要的"了"。
source: path: skills/humanizer/references/patterns.zh.md; anchor: `## 未验证假设 · Unverified hypotheses (ZH13–ZH14) / ZH13`
notes: 原文明确标注这条是"UNVERIFIED"、"没有任何竞品会显式检测它们"，作者自己也说"可能是伪模式"。裁决时应对照 criteria.md 第 9 条（证据不足时记 unverified/deferred），不应径直 adopted；本单元的 notes 就是为了把这条自我声明的不确定性带进归并阶段。

#### U-abh-117
category: pattern | language: zh
rule_summary: 【未验证假设，原文自称推测、仅间接触及】假设 AI 中文常带英文语法痕迹——被动句过多、从句套从句的长句、"一个……"滥用（英文"a/an"直译）、"进行+动词"代替直接动词（"make a decision"→"进行决策"）；若成立，应拆长句为短句、被动改主动、删掉冗余的"一个"和"进行"。
positive: "我们做了个处理数据的系统，用户反馈还挺信得过。"（引自上游）
negative: "一个能够被用户所信赖的、对数据进行有效处理的系统被我们所构建了出来。"（引自上游）。违反点："被……所……"被动句式、"对数据进行有效处理"的"进行+动词"翻译腔、"一个"的滥用堆叠在同一句里。
source: path: skills/humanizer/references/patterns.zh.md; anchor: `## 未验证假设 · Unverified hypotheses (ZH13–ZH14) / ZH14`
notes: 原文明确标注"UNVERIFIED"，且说明现有工具只通过 ZH4 的外来语词黑名单间接触及这个现象，没有工具专门检测句法层面的翻译腔。同 U-abh-116，裁决时应参照 criteria.md 第 9 条，不宜直接 adopted。

#### U-abh-118
category: measurement | language: zh
rule_summary: 英文用来打分的 burstiness（句长波动）和 perplexity（用词可预测性）指标不能直接迁移到以字为单位、不分词间空格的中文；在中文里，四字成语的密度和句读节奏通常比句长方差更能反映 AI 痕迹，这两个指标本身也未经中文母语写手校验。
positive: 对中文文本打分时，不直接套用英文的句长方差公式，而是额外参考四字成语密度和句读节奏。
negative: 对一段中文文本直接套用英文的 burstiness_normalized 公式来计算 AI 味分数，不做任何中文场景的调整。违反点：把只在英文里验证过的指标未经调整直接套用到中文文本上。
source: path: skills/humanizer/references/patterns.zh.md; anchor: `## ⚠️ 实验性 · PROVISIONAL — 请先读这里`
notes: 原文这条声明本身就是一条元规则（"不要把这套指标直接套到中文上"），且原文用大写强调"NOT been validated"，裁决时应留意这不是一条"证明有效"的规则，而是一条"警示不适用"的规则，与 U-abh-105（评分公式）的适用范围直接相关：如果 skill 要支持中文改写打分，这条决定了 U-abh-105 的公式不能原样套用到中文。

### 2.4 来自 references/always-on-templates.md（path: skills/humanizer/references/always-on-templates.md）

不产生新单元。这个文件是四份可复制的"常驻规则"模板（分别给 CLAUDE.md/AGENTS.md、SOUL.md、系统提示、ChatGPT 自定义指令），四份内容彼此措辞不同但要求完全一致，且全部是对 SKILL.md 里已经拆出的规则的压缩重述，没有引入任何新的判定内容。四份模板压缩重述的规则依次对应：不用破折号（P13/U-abh-039）、句长要有变化（Burstiness/U-abh-084）、删除 AI 词汇黑名单（P7/U-abh-033，但四份模板里把"seamless""robust"也混进了这份黑名单，这两个词在上游权威定义里属于 P4/U-abh-030，不属于 P7——同一来源内部的用词不一致，记入"拿不准的地方"）、不反射性三项排比（P10/U-abh-036）、不做段末总结（P39/U-abh-065）、不写"In conclusion"收尾（U-abh-087 Anti-Default Discipline）、陈述事实而非讲意义（P1/P40，U-abh-027/U-abh-066）、用主动语态和具名主体（P50/U-abh-076）、对论点要有立场（Position engine/U-abh-088）、用具体数字代替抽象表述（Concretizer/U-abh-089）、不改写引号或代码块内的文字（U-abh-015）。

---

## 3 覆盖表

### 3.1 P1-P55 逐条归属

| 模式 | 单元 id | 备注 |
|---|---|---|
| P1 | U-abh-027 | language: both（含 ZH8） |
| P2 | U-abh-028 | |
| P3 | U-abh-029 | |
| P4 | U-abh-030 | |
| P5 | U-abh-031 | |
| P6 | U-abh-032 | |
| P7 | U-abh-033 | 分级规则见 U-abh-083 |
| P8 | U-abh-034 | |
| P9 | U-abh-035 | |
| P10 | U-abh-036 | language: both（含 ZH10） |
| P11 | U-abh-037 | |
| P12 | U-abh-038 | |
| P13 | U-abh-039 | 分号/冒号弱信号见 U-abh-082；与 ZH5(U-abh-113) 存在语言范围划分 |
| P14 | U-abh-040 | language: both（含 ZH12 的一半） |
| P15 | U-abh-041 | |
| P16 | U-abh-042 | |
| P17 | U-abh-043 | |
| P18 | U-abh-044 | language: both（含 ZH9 的一半） |
| P19 | U-abh-045 | |
| P20 | U-abh-046 | |
| P21 | U-abh-047 | |
| P22 | U-abh-048 | language: both（含 ZH9 的另一半） |
| P23 | U-abh-049 | |
| P24 | U-abh-050 | |
| P25 | U-abh-051 | |
| P26 | U-abh-052 | |
| P27 | U-abh-053 | |
| P28 | U-abh-054 | 与 ZH12(U-abh-040) 有交叉，见 notes |
| P29 | U-abh-055 | |
| P30 | U-abh-056 | 数值目标见 U-abh-084 |
| P31 | U-abh-057 | |
| P32 | U-abh-058 | |
| P33 | U-abh-059 | |
| P34 | U-abh-060 | |
| P35 | U-abh-061 | |
| P36 | U-abh-062 | |
| P37 | U-abh-063 | |
| P38 | U-abh-064 | |
| P39 | U-abh-065 | |
| P40 | U-abh-066 | |
| P41 | U-abh-067 | |
| P42 | U-abh-068 | |
| P43 | U-abh-069 | language: both（含 ZH11） |
| P44 | U-abh-070 | |
| P45 | U-abh-071 | |
| P46 | U-abh-072 | |
| P47 | U-abh-073 | |
| P48 | U-abh-074 | |
| P49 | U-abh-075 | |
| P50 | U-abh-076 | |
| P51 | U-abh-077 | |
| P52 | U-abh-078 | |
| P53 | U-abh-079 | |
| P54 | U-abh-080 | |
| P55 | U-abh-081 | |

### 3.2 SKILL.md 逐节归属

| 小节 | 单元 id / 归属 |
|---|---|
| frontmatter（name/description/allowed-tools 等） | 非规则内容 |
| `# Humanizer: Make Text Sound Like a Human Wrote It`（引言段） | 非规则内容（不可判定的总体描述） |
| `## Quick reference / Modes` | U-abh-001 |
| `## Quick reference / Voices` | U-abh-003 至 U-abh-007 |
| `## Quick reference / Pattern catalog (55 total)` | 非规则内容（统计表，指向 3.1 全部） |
| `## Quick reference / Flags` | U-abh-008、U-abh-009、U-abh-010、U-abh-011、U-abh-026、U-abh-107（对应各行） |
| `## Quick reference`（Deep dives 指引句） | 非规则内容（文件间指引） |
| `## When to use this skill`（触发条件列表） | 非规则内容（何时调用本 skill，非文本内容判定规则） |
| `## When to use this skill`（Auto-loads 一句） | U-abh-012 |
| `## Guardrails.../ What NOT to flag (false positives)` | U-abh-013、U-abh-014、U-abh-015、U-abh-016、U-abh-017、U-abh-018、U-abh-019 |
| `## Guardrails.../ Signs of human writing (preserve these)` | U-abh-020、U-abh-021、U-abh-022 |
| `## Operating principles`（前两段，未点名 No fabrication 的部分） | 非规则内容（不可判定，见 U-abh-024 的收录说明） |
| `## Operating principles / No fabrication` | U-abh-023 |
| `Arguments received: $ARGUMENTS` | 非规则内容（模板占位符） |
| `## Step 1: Parse Arguments`（Text） | U-abh-025 |
| `## Step 1: Parse Arguments`（--mode/--voice/--file/--aggressive/--iterate/--score/--purpose/--openings/--ignore-code/--ignore-quotes） | U-abh-001、U-abh-002、U-abh-009、U-abh-107、U-abh-008、U-abh-010、U-abh-026、U-abh-011（对应各条） |
| `## Step 1: Parse Arguments / Auto-load brand context` | U-abh-012 |
| `## Step 2: Detect AI Patterns`（P1-P55） | 见 3.1 |
| `### Tiered-confidence vocabulary (refines P7)` | U-abh-083 |
| `### The Burstiness Principle` | U-abh-084 |
| `### The Perplexity Principle` | U-abh-085 |
| `## Step 3: Rewrite Craft / Voice Read` | U-abh-086 |
| `## Step 3: Rewrite Craft / Anti-Default Discipline` | U-abh-087 |
| `## Step 3: Rewrite Craft / Position engine` | U-abh-088 |
| `## Step 3: Rewrite Craft / Concretizer pass` | U-abh-089 |
| `## Step 3: Rewrite Craft / Opening tournament` | U-abh-026（重复锚点） |
| `### Voice Profiles` | U-abh-003 至 U-abh-007（重复锚点） |
| `### Soul Injection Techniques` | U-abh-090 至 U-abh-096（第 3、6、8、11 项并入 U-abh-089/U-abh-084/U-abh-036/U-abh-087 的 notes，不单独立条，见各自 notes） |
| `## Step 4: Execute Based on Mode / Masking first` | U-abh-011（重复锚点） |
| ``### Mode: `detect` `` | U-abh-097、U-abh-098 |
| ``### Mode: `rewrite` `` | U-abh-099、U-abh-100 |
| ``### Mode: `edit` `` | U-abh-101、U-abh-102 |
| `## Step 5: Final Quality Check` | U-abh-103 |
| `### Draft, self-audit, final` | U-abh-104 |
| `### Scoring rubric` | U-abh-105、U-abh-106 |
| `### Iterate handling` | U-abh-107（重复锚点） |
| `## Always-On Mode`（指引句） | 非规则内容（文件间指引） |
| 末行"Write like a human. Be weird, specific, inconsistent." | U-abh-024（重复锚点） |

### 3.3 references/patterns.md 逐节归属

| 小节 | 归属 |
|---|---|
| 引言、Contents | 非规则内容 |
| `## The craft and forensic set (P44-P55)`（含 P54/P55 provenance note） | 非规则内容（补充 U-abh-070 至 U-abh-081 的出处说明，已并入 U-abh-080/U-abh-081 的 notes） |
| `## Emerging patterns (P31-P43): extended notes` | 非规则内容（补充 U-abh-057 至 U-abh-069 的说明，未引入新判定内容） |
| `## The HC3 corpus` | 非规则内容（支撑 U-abh-079、U-abh-085 的引用证据） |
| `## Coverage against Wikipedia: Signs of AI writing` | 非规则内容（模式与 Wikipedia 指南的对照表） |
| `## Honest limits of this catalog`（漂移、人类评委准确率等段落） | 非规则内容（评估性元评论，见"拿不准的地方"） |
| `## Honest limits of this catalog`（Fiction and creative prose 段） | U-abh-108 |
| `## Full trigger lists` | 非规则内容（补充 U-abh-027、U-abh-030、U-abh-033 的完整触发词表） |
| `## Before and after examples` | 非规则内容（补充相应模式单元的例句） |
| `## Worked examples` | 非规则内容（综合示例，不单独判定） |

### 3.4 references/patterns.zh.md 逐节归属

| 小节 | 归属 |
|---|---|
| `## ⚠️ 实验性 · PROVISIONAL — 请先读这里`（免责声明） | U-abh-118 |
| `## 目录 · Contents` | 非规则内容 |
| `## 怎么用这份附录 · How to use` | 非规则内容（使用说明；其中"中文改写里可以使用破折号"一句已并入 U-abh-113 的 notes） |
| `## 核心原生模式 · Core native tells (ZH1–ZH7)` | U-abh-109 至 U-abh-115（ZH1 至 ZH7 逐条） |
| `## 英文模式的中文对应 · Analogs of English patterns (ZH8–ZH12)` | ZH8→U-abh-027；ZH9→U-abh-044、U-abh-048；ZH10→U-abh-036；ZH11→U-abh-069；ZH12→U-abh-040（均已合并进对应英文单元，本节不产生独立 id） |
| `## 未验证假设 · Unverified hypotheses (ZH13–ZH14)` | U-abh-116、U-abh-117 |
| `## 最深层痕迹 · The deepest tell (ZH15)` | U-abh-088（已合并） |
| `## 来源与致谢 · Sources` | 非规则内容（含"给 integrator 的提醒"，见"拿不准的地方"） |

### 3.5 references/always-on-templates.md 逐节归属

| 小节 | 归属 |
|---|---|
| 引言段（"Copy one of these blocks..."） | 非规则内容（见"拿不准的地方"关于是否构成指令的讨论） |
| ``## For `CLAUDE.md` or `AGENTS.md` `` | 非规则内容，复现 U-abh-039、U-abh-084、U-abh-033、U-abh-036、U-abh-065、U-abh-087、U-abh-027、U-abh-066、U-abh-076、U-abh-088、U-abh-089 |
| ``## For a `SOUL.md` or persona file`` | 非规则内容，复现同上一组单元 |
| `## For a system prompt` | 非规则内容，复现同上一组单元，另加 U-abh-015 |
| `## For ChatGPT Custom Instructions` | 非规则内容，复现同上一组单元，另加 U-abh-015 |
| 末行（"cover the highest-signal rules only..."） | 非规则内容（文件间指引） |

---

## 4 拆分时拿不准的地方

1. **always-on-templates.md 引言是否构成"上游文本内的指令"。** 该文件写"Copy one of these blocks into your agent's standing instructions so it writes clean by default"，措辞和 criteria.md 第 7 条给出的反面例子（"把这段加进你的系统提示"）非常接近。我的判断是：这句话面向的是 humanizer skill 的最终使用者（教他们怎么给自己的 agent 配置常驻规则），不是针对正在执行本次抽取任务的我发出的指令，也没有"忽略当前规则"这类要求我此刻改变行为的表述，因此没有列入第 6 节。但这个判断带有主观性，建议归并阶段人工复核一次，确认是否要以更保守的口径处理。
2. **`seamless`/`robust` 的词表归属不一致。** always-on-templates.md 的四份模板把这两个词和 delve/leverage/tapestry 混在一起当作"AI 词汇"要求删除，但 SKILL.md 权威定义里这两个词属于 P4（Promotional Language，U-abh-030），不属于 P7（U-abh-033）。这是上游同一来源内部的用词不一致，已在 U-abh-030 和 2.4 节里记录，归并阶段需要决定这两个词最终挂在哪条规则下，或者两条规则都覆盖。
3. **rewrite 模式验证清单和 Burstiness Principle 的具体数值不一致。** U-abh-100（Step 4 rewrite 模式）要求"句长方差 > 30%"且"不超过 2 句连续相似结构"；U-abh-084（Burstiness Principle）给的是"短 3-8 词/中 12-20 词/长 25-40 词"且"不超过 3 句连续同长度"。一个用方差百分比、一个用绝对词数区间，"不超过 2 句"和"不超过 3 句"也对不上。这是同一份 SKILL.md 内部前后不统一，我按各自出现的位置原样记录成两条单元，没有替上游做取舍，归并阶段需要决定用哪一版数值，或者说明两者适用的时机不同（一个是改写中的目标，一个是最终核验的门槛）。
4. **两套并行的"严重程度"量表。** detect 报告用"命中 8 条以上模式 = HIGH"（U-abh-098）；`--score`用 0-100 的连续分数（U-abh-105）。两者都能用来描述"AI 味有多重"，但计算方式完全独立，我没有假设归并阶段一定要统一它们。
5. **ZH2、ZH3、ZH7 是否应该和对应的英文模式合并为 both。** 这三条概念上分别接近"first/second/finally 脚手架"、P29/P53（套话开头）、P24（空洞乐观结尾），但 patterns.zh.md 只在 ZH8-ZH12 和 ZH15 明确写了"对应 P_"，没有给 ZH1-ZH7 标注对应关系。我按上游自己划出的这条边界，把 ZH1-ZH7 全部保留为独立的 zh-only 单元，没有替上游做"其实它们也是同一条规则"的判断。这是我自己的取舍，不是上游的判断，归并阶段如果认为应该合并，需要重新评估。
6. **ZH12 同时对应 P14 和 P28，只挂在了 P14 上。** ZH12 原文标注"对应 P14 / P28"，但我把中文例句放进了 P14（U-abh-040），P28（U-abh-054）保持纯英文。这是因为 ZH12 的触发信号（emoji 小标题、逐词加粗）更贴近 P14 的"系统性格式过度"，而"发到不支持 Markdown 的地方就把 `**` 去掉"这半句更贴近 P28。如果归并阶段认为应该让 P28 也升级为 both，需要把中文例句拆出一部分挪过去。
7. **P13 和 ZH5 的范围划分是"分域"还是"矛盾"。** patterns.zh.md 明确说中文改写不受破折号零容忍约束。我把这处理成"P13 的适用范围本来就限定在英文、ZH5 是中文场景下判定逻辑不同的独立规则"，而不是"两条互相矛盾、需要二选一"的关系。这个判断影响到 P13（U-abh-039）最终的 language 字段要不要明确限定为 en——如果归并阶段认为应该把这当成真正的语言范围冲突来记录（按 criteria.md 第 8 条冲突留痕的方式），处理方式会不同。
8. **P52（Unicode Obfuscation）的正反例是否踩到"绕过检测器"的红线。** 规则方向是清除混淆字符（防御方向），但反例本身描述了具体的混淆手法（插入零宽字符），字面上和 criteria.md 第 5 条第 1 款（声称能"绕过检测器"的规则一律 rejected）的边界很近。我判断这条规则本身的意图是清除而非教唆，予以保留，但在 U-abh-078 的 notes 里做了标注，供裁决时复核。
9. **Soul Injection Techniques 里 4 项没有单独立条。** "Use specific sensory/experiential details"（原第 3 项）、"Vary paragraph length dramatically"（原第 6 项）、"Break parallel structure occasionally"（原第 8 项）、"End without wrapping up"（原第 11 项）分别和 Concretizer（U-abh-089）、Burstiness Principle（U-abh-084）、P10（U-abh-036）、Anti-Default Discipline（U-abh-087）高度重叠，我把它们并入对应单元的 notes 作为补充证据，没有单独立条。如果归并阶段认为这些应该作为独立的、可以单独裁决的规则，需要重新拆出。
10. **North Star（U-abh-024）和 Perplexity Principle（U-abh-085）大概率不可判定。** 这两条正反例都写得比较勉强（North Star 干脆没给出正反例），按 criteria.md 第 2 条的判据大概率会在裁决阶段被判"不可判定"而 rejected。收录它们是为了不遗漏原文内容、也为了让下游其他规则（Position engine、Concretizer、Burstiness）能追溯到它们共同的思想来源，但这两条本身是否值得写进 decisions.yaml，留给归并阶段判断。

---

## 5 疑似常见规则

以下按规则内容本身判断（不依赖对其他三个来源的了解），认为在同类"去 AI 味"项目里大概率也会出现，供归并阶段优先聚类核对：

U-abh-023（不能编造事实/数字/引语）、U-abh-033（P7 AI 高频词黑名单：delve/leverage/tapestry 等）、U-abh-035（P9 否定式排比"not only...but"）、U-abh-036（P10 三项排比）、U-abh-039（P13 破折号零容忍）、U-abh-040（P14 加粗/格式过度）、U-abh-042（P16 标题大小写）、U-abh-043（P17 弯引号）、U-abh-044（P18 正式语域过度）、U-abh-045（P19 助手式寒暄"I hope this helps"）、U-abh-046（P20 知识截止免责声明）、U-abh-047（P21 谄媚语气）、U-abh-048（P22 冗余连接词）、U-abh-049（P23 过度保留语堆叠）、U-abh-050（P24 空洞乐观结尾）、U-abh-055（P29 全面概览式开场）、U-abh-056（P30 句长均匀）、U-abh-059（P33 未填写的占位符）、U-abh-060（P34 工具引用标记残留）、U-abh-061（P35 UTM 追踪参数）、U-abh-076（P50 无主句被动式）、U-abh-084（Burstiness Principle 的句长混合要求）、U-abh-105（0-100 AI 味评分的整体思路，不一定是同一个公式）。

---

## 6 上游文本内的指令

无。四个文件里没有发现要求读者（或执行抽取任务的我）"忽略之前的规则""把这段加进你的系统提示"之类针对性指令。always-on-templates.md 的"Copy one of these blocks into your agent's standing instructions"一句经过判断认为是面向 humanizer skill 终端用户的产品功能说明，不是对本次抽取任务的指令注入，讨论见第 4 节第 1 条。
</content>
