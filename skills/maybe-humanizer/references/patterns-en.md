# 英文模式表

这份文件只收英文正文的写法模式。中文正文的模式在 patterns-zh.md，两种语言都适用的在 patterns-common.md。79 条按十一组排列，组的先后就是查的顺序：先过词与短语，再过句子形状，最后过语域与体裁形态。

三条边界适用于全表。

一、词表列的是这个模式的代表项，不是完整枚举。按 ALL-PROC-039，先判定文本命中的是哪个模式，再用词条兜底；词表里没有而模式对得上的说法，照样处理。

二、词表不适用于三种位置：引语、代码块、标题内的原文按 ALL-PROT-008 逐字不动；某个词在当前领域是精确术语时按 ALL-PROT-009 保留；判定为技术长文档位时，EN-P-084 另有一份逐词的放行与照标清单。

三、单一信号不算证据（ALL-M-002）。这份表的用途是指出稿子里的具体位置，不是拿几处命中给一段文字定性。命中数归零不是验收标准，执行强度上限见 SKILL.md 里的 ALL-PROC-056。

词表条目照录自上游是有意为之：把 delve 换成别的词，这条规则就不再管 delve 了。照录只限词条本身，说明文字、正反例和执行强度都是重写的。

## 一 词表与短语

### EN-P-001 AI 高频词一律不用

**判据。** 下列词出现在英文正文里即命中，换成大白话，不是换成另一个书面词：delve、leverage、utilize、facilitate、foster、empower、streamline、multifaceted、tapestry、testament、underscore、interplay、realm、beacon、pivotal、crucial、paramount、meticulous、intricate、transformative、elevate、embark、supercharge、harness、garner、bolster、ever-evolving、paradigm shift、game changer。

**通过条件。** 引语、代码块、标题里的原文按 ALL-PROT-008 逐字不动，词表在这些位置不适用。某个词在当前领域承担精确技术含义时按 ALL-PROT-009 保留，判定依据是这个词在当前句子里的语义，不是文章属于哪个体裁。技术长文档位另有 EN-P-084 的逐词清单，那份清单放行 robust、leverage 一类，仍然要求处理 delve、tapestry、embark。本条只负责列出词条，这张表的三档执行强度在 EN-M-001。EN-P-051 收的是英文职场黑话，两份表只有 game changer 一条重合。

**已知会漏掉什么。** 表外的同族词查不到：learnings、actionable、impactful、thought leadership、best practices、holistic、bustling、daunting、symphony 在上游的同一份高频表里，本条的词表没有收。词表也不区分密度：同一个词在一篇里出现一次和出现六次，本条给出的是同一个结果，聚集程度归 EN-M-001 和 ALL-M-002 判。误伤集中在技术写作，harness 和 elevate 在硬件与前端语境里是字面用法，逐词替换会改坏意思。

- 正例：`We used the existing queue and looked at the logs.`
- 反例：`This update will supercharge your workflow and foster a truly transformative shift.` 违反点：supercharge、foster、transformative 是词表里的三条，句子在替换掉这三个词之后信息一点不少。

### EN-P-002 宣传册式形容词

**判据。** 词表逐条同序照录，这些形容词占住本该是事实的位置就要处理：nestled、in the heart of、vibrant、breathtaking、must-visit、cutting-edge、seamless、robust、world-class、state-of-the-art、renowned、rich（比喻义）。处理动作是写出具体是什么让它值得一提。

**通过条件。** rich 只在比喻义上命中，rich in iron 这类字面用法保留。引用某个机构或产品自己的标语时按 ALL-PROT-008 逐字保留。技术长文档位下 robust、seamless、cutting-edge 按 EN-P-084 放行。ZH-P-018 管中文旅游与城市宣传语料里的同一组词，两条各管一种语言，中文稿不套用本条的词表。

**已知会漏掉什么。** 开发者营销的现成口号形状相同而词不同，本条查不到：batteries included、it just works、zero config、sane defaults、small enough to fit in your head，这些同样是用口号替代一个本可以演示的属性。thriving、stunning、profound、groundbreaking 也不在词表里。

- 正例：`Bahir Dar is a town in the Amhara region, and 12 startups are registered there.`
- 反例：`Nestled within the breathtaking foothills, Bahir Dar is a vibrant hub of innovation with a rich cultural heritage.` 违反点：nestled、breathtaking、vibrant、rich 四处宣传语并列，整句没有给出一条可核对的事实。

### EN-P-003 空洞副词

**判据。** just、literally、honestly、simply、actually、truly、fundamentally、importantly、crucially、inherently、inevitably、really、genuinely、deeply、interestingly 这类副词，不承担强调、不确定、对比或作者语感时删掉。actually 的默认处理是删除而不是换词，换词只是把一个空词换成另一个空词。deeply 只在意义类搭配上算（deeply integrated、deeply committed、deeply rooted），deeply nested 这类字面用法不算。

**通过条件。** 承担命题限定的副词按 ALL-PROT-004 一律保留，不在本条范围内：possibly、probably、roughly、approximately、arguably。副词确实标记了一处更正或与预期的落差，且句子本身写出了那个落差时保留（we expected a cache hit; it was actually a miss）。EN-S-005 要求删掉全部副词、不留例外，与本条的判据正面冲突，取本条。

**已知会漏掉什么。** 本条按单处功能判，不数密度：一篇文字里每一处副词都各自承担了一点功能，但四处强调词挤在五百词里，这个整体问题本条查不出来，需要另行按段落读。real、actual、genuine 修饰抽象名词的形容词形式不归本条，按 EN-P-060 处理。

- 正例：`I actually think this will work.`（actually 标记了一处与预期的落差，保留）
- 反例：`This is just a simple bug fix that we simply need to ship.` 违反点：just 和两处 simply 都不承担强调、不确定或对比，删掉之后句子的意思完全相同。

### EN-P-004 空洞短语与冗余连接词

**判据。** 下列短语与连接词照录：it's worth noting、it's important to note、at the end of the day、when it comes to、at its core、in today's world、in the age of、the reality is、the truth is、in terms of、with regard to、in order to、due to the fact that、at this point in time、going forward、in connection with、associated with。处理动作分两种，按短语本身承不承载信息定：整体不承载信息的删掉（it's worth noting、at the end of the day、in today's world）；承载了真实的因果、条件、转折或时间关系的，缩短成表达这个关系的最短说法，不整段删（due to the fact that 写成 because，in order to 写成 to，at this point in time 写成 now 或直接给日期）。

**通过条件。** 删掉的是词，不是词背后原文真实存在的逻辑关系，按 ALL-PROT-020 那层关系一律保留。EN-S-012 要求段落一律不以 So 开头，那条只作参考；承担真实逻辑关系的 So 归本条按"缩短"处理，不按"删掉"处理。ZH-P-023 管中文里同一类名词化填充结构，两条各管一种语言。it's worth noting 同时在 EN-P-049 的词表里，同一处只计一次命中：作为不承载信息的短语删掉走本条，作为陈述事实之前的预先辩解删掉走 EN-P-049。

**已知会漏掉什么。** 过渡词不在这份词表里：Moreover、Furthermore、Additionally、That said、In conclusion 属于同一类现象，但它们孤立出现一次是正当的，命中条件是堆叠，本条的逐条词表判不出堆叠。in a world where、It is important to note that 的完整从句形式也不在表内。

- 正例：`We upgraded the server to handle more traffic.`
- 反例：`Due to the fact that we needed to handle more traffic, and in connection with our scaling plans, we upgraded the server at this point in time.` 违反点：due to the fact that 承载了真实的因果关系，该缩成 because 而不是整句删；in connection with 和 at this point in time 不承载任何关系，该直接删掉。

### EN-P-005 官僚式正式语域

**判据。** 在读者期待大白话的场合出现官僚式正式语域，这一处算违反：it should be noted that、it is essential to、in the context of、the implementation of、prior to，以及 utilize 式的名词化堆叠（the implementation of the configuration of…）。处理动作是降到该有的语域，把动作写成动词。

**通过条件。** 法律、合规、学术论文、正式公文的语域本来就该是这样，本条不适用。判定"读者期待什么语域"要先按 ALL-PROC-053 定档位，档位判不出来时不动。语域本身不构成 AI 的证据（ALL-M-002），本条命中说明这段文字可以写得更好读，不说明它是机器写的。

**已知会漏掉什么。** commence、ascertain、endeavor、presents 这类同族的过度正式词不在词表里，它们的问题与表内几条一样，都是有一个更短的日常说法。名词化堆叠没有可数的阈值，一句话里堆几层算命中要靠判断。

- 正例：`Set the timeout to 30 seconds before you start the migration.`
- 反例：`It should be noted that it is essential to configure the implementation of the timeout parameter prior to commencing the migration.` 违反点：it should be noted that、it is essential to、the implementation of、prior to 四处官僚语域，一句能说清的操作绕了一圈。

### EN-P-051 英文职场黑话

**判据。** 英文职场黑话换成大白话，替换表逐条同序照录：navigate (challenges) → handle / address；unpack (analysis) → explain / examine；lean into → accept / embrace；landscape (context) → situation / field；game-changer → significant / important；double down → commit / increase；deep dive → analysis / examination；take a step back → reconsider；moving forward → next / from now；circle back → return to / revisit；on the same page → aligned / agreed。

**通过条件。** 词条正在被定义或讨论时不动；它是产品名或功能名时不动；项目已经把它声明为术语时不动。EN-P-001 收的是 AI 高频词，本条收的是职场黑话，两份表只有 game changer 一条重合，同一处命中不重复计。ZH-P-001 的赋能、抓手、闭环、底层逻辑是同一类现象的中文形态，中英各一份表。

**已知会漏掉什么。** 表外的同类说法查不到：synergy、bandwidth、touch base、low-hanging fruit、boil the ocean。landscape 同时在 EN-P-001 的词表里，一处 landscape 会同时命中两条，改一次即可，不必两条各改一遍。

- 正例：`Next quarter we increase the retry budget, and both teams agree on the target.`
- 反例：`Moving forward, we'll double down on the retry budget and circle back once both teams are on the same page.` 违反点：moving forward、double down、circle back、on the same page 是替换表里的四条，每一条都有一个更短的日常说法。

### EN-P-060 real / actual 当空修饰语挂在抽象名词前

**判据。** real、actual、genuine、true 修饰一个抽象名词、句子却不点名被它排除的那个假版本时命中：real on-chain tokenomics、actual reward sustainability、genuine utility、true product-market fit。形容词暗示这个领域的其余部分是假的，却不说破假的是什么。修法是去掉形容词，把那个具体主张补上。

**通过条件。** 句子里点名了被排除的那一版就保留，这时对比是真的（Real on-chain settlement, not bridged IOUs）。边界与 EN-P-003 按词性划：genuinely、truly 在句子层作强调副词时按 EN-P-003 处理，real / actual / genuine / true 修饰抽象名词时按本条处理。

**已知会漏掉什么。** 判定要读整句甚至整段，才知道那个假版本有没有在别处被点名，因此这条做不成词形匹配。修饰具体名词的用法（a real fire、the actual file）不在范围内，本条只管抽象名词。

- 正例：`Rewards are funded from $40k per month in fees rather than from emissions.`
- 反例：`The protocol has real on-chain tokenomics and genuine utility.` 违反点：real 与 genuine 都没有排除任何东西，句子没说假的那一版是什么，两个形容词只在给名词加分量。

### EN-P-063 套话短语的密度与聚集

**判据。** 下面十条多词套话短语单独出现一次不处理。两条触发条件任一成立即命中：同一篇里出现三个以上互不相同的短语，即使每个只出现一次；或者同一个短语在一篇里出现两次以上。词表逐条同序照录：emerging sector / emerging space / emerging category、the integration of (X with Y)、the intersection of (X and Y)、community-driven、long-term sustainability、user engagement、decentralized compute、(sustainable) reward emissions、tokenized incentive structures、designed for long-term [X]。修法不是换词，是点名那个具体的东西：那个领域是什么、整合之后用户那边变了什么、这个社区做了什么、时间跨度和约束是什么、机制是什么。

**通过条件。** 一处孤立命中不标记，两条触发条件都不满足时放过。EN-M-001 第三档管的是单个高频词，判据是它与前两档聚在一起；本条管多词短语，两条触发条件各自独立，对象和判据都不同。本条的修法是 ALL-P-007 在这十个短语上的落地：能给名字、数字、机制的位置不用抽象词。

**已知会漏掉什么。** 这份表在 crypto、web3、DePIN 和 AI 基础设施类内容里密度最高，其他题材里同样空洞的多词短语不在表内。两条触发条件都要通读全文才能数，单段审阅判不出来。

- 正例：`The network pays validators from transaction fees, and the emission schedule ends in 2028.`
- 反例：同一篇里出现 `emerging sector`、`community-driven`、`long-term sustainability` 三个各出现一次的短语。违反点：三个互不相同的表内短语聚在一篇里，满足第一条触发条件，不需要任何一个重复出现。

### EN-P-066 load-bearing 的两层形式边界

**判据。** load-bearing 只在两个条件同时成立时算命中。一、带连字符，不带连字符的 the load bearing down on the bridge 是普通英语，不算。二、在同一行里紧接着修饰下列八个抽象名词之一（含复数）：assumption、claim、invariant、premise、constraint、dependency、argument、abstraction。

**通过条件。** 建筑领域的字面用法保留（the load-bearing wall in the kitchen）。清单之外的名词保留。连字符与名词之间隔了修饰语的情形保留。作表语的用法保留（that claim is load-bearing）。physical 与抽象两可的名词也放过：structure、element、frame、foundation、test、detail。ALL-PROC-039 管的是词表里没有的说法要不要处理，本条管的是词表里已有的一条在什么形式条件下才算命中，两条方向相反，各管一半。

**已知会漏掉什么。** 这条口径是故意收窄的，代价写在上游的规则旁边：它漏掉一部分正当的比喻用法，换来的是不误伤普通写作。名词清单是封闭的，load-bearing decision、load-bearing sentence 这类同样是比喻的搭配一律漏掉。

- 正例：`That claim is load-bearing, and the load-bearing wall in the kitchen stays.`
- 反例：`The load-bearing assumption here is that clocks are synchronised.` 违反点：带连字符，且在同一行里紧接着修饰清单内的 assumption，两个条件同时成立。

### EN-P-073 现造且从不定义的伪分析术语

**判据。** 句中现造一个复合名词当作分析术语、通篇又不给它定义即命中：the supervision paradox、the context-collapse problem、a coordination tax。给一个东西起名不等于解释了它。修法有两条：首次出现时定义这个术语，或者干脆描述那个机制而不给它起名。

**通过条件。** 文中任何位置定义过这个术语就通过，不要求定义紧跟首次出现。领域里真实存在的术语不算现造，判断标准是这个说法在本文之外有没有出处。EN-P-062 管的是对仗里恰好一半是现造的，本条管一个孤立的现造术语，两条同源、对象不同。现造术语被当成既有概念引用时属于疑似捏造，按 EN-P-039 标出来交作者确认，不自行替换成另一个术语。

**已知会漏掉什么。** 判定要读完全文才能确认"从不定义"，单段审阅只能存疑。作者本人在系列文章里已经定义过、本篇直接引用的术语会被误命中。

- 正例：`When two teams both approve, neither reviews carefully: each assumes the other did.`
- 反例：`This is the supervision paradox at work.` 违反点：the supervision paradox 是句中现造、通篇没有定义的复合术语，读者拿到的是一个名字而不是一个机制。

## 二 动词与系动词

### EN-P-013 假装分析的分词从句

**判据。** 句尾挂一个假装在解释意义的现在分词从句就要处理，触发词：highlighting、underscoring、emphasizing、reflecting、symbolizing、showcasing、ensuring、fostering。处理动作分两种：从句里有真正的信息，就把它提升成一句有出处的独立句子；没有信息，整句删。

**通过条件。** 分词从句陈述的是一个可核对的事实或后果时保留（the launch adds file search, letting users reopen a draft without leaving the editor 里的从句说的是具体行为）。判据是这个从句给的是事实还是评价，不是它带不带 -ing。ZH-P-017 给出同一模式在中文里的形状（句末追加的评论性小句），中文没有 -ing 形态，两条各管一种语言。

**已知会漏掉什么。** 不带 -ing 的陈述式"点意义"本条查不到：this represents a broader shift、the decision symbolizes a commitment to excellence、it speaks to a larger trend，这些做的是同一件事，归 EN-P-014。词表之外的分词（cementing、affirming、illustrating）也漏。

- 正例：`The launch adds file search, so users can find old drafts without leaving the editor.`
- 反例：`The launch adds file search, highlighting the team's commitment to better workflows.` 违反点：highlighting 引出的是一句评价而不是后果，从句里没有任何可核对的信息。

### EN-P-015 不回避系动词

**判据。** 用花哨的动词短语替代 is / are / has / was 即命中，触发词：serves as、stands as、marks、represents、boasts、features、offers。处理动作是换回系动词，让等同关系和所属关系保持它本来的样子。

**通过条件。** 某个更具体的动词确实比系动词多说了一件事时保留（the gallery hosts three shows a year 比 the gallery is a venue 多给了频次）。判据是替换之后信息有没有增加，不是这个词好不好看。ZH-P-021 管中文的同一组替身，并补上中文特有的"作为 X"缺谓语问题，两条各管一种语言。

**已知会漏掉什么。** 词表之外的同族词漏掉：presents、constitutes、embodies、exemplifies。这条与 EN-P-014 在 represents 一词上重叠，EN-P-014 命中的是拔高评价，本条命中的是回避系动词，同一处 represents 判成哪一条要看句子在做什么。

- 正例：`Gallery 825 is LAAA's exhibition space. It has four rooms.`
- 反例：`Gallery 825 serves as LAAA's exhibition space. It features four rooms and boasts 3,000 square feet.` 违反点：serves as、features、boasts 三处都在替代 is 和 has，没有一处比系动词多说了什么。

### EN-P-016 让动词做事

**判据。** 用一个弱动词加名词的短语代替现成的动词算违反：made a decision 写成 decided，conducted an analysis 写成 analyzed，gave consideration to 写成 considered。判据是这个名词里已经有一个动词。

**通过条件。** 名词形式是这个领域的固定说法时保留（file a motion、issue a refund）。名词短语承担了动词形式承担不了的限定时保留（made three separate decisions 不能压成 decided three times）。

**已知会漏掉什么。** 这类结构没有可数的词表，本条靠"名词里有没有一个现成动词"这条判断走，因此依赖执行者的英语语感，机械匹配做不出来。被动式加名词化的组合（a decision was made）本条同样查不到，那是语态问题。

- 正例：`The team decided on Tuesday and analyzed the logs the same night.`
- 反例：`The team made a decision on Tuesday and conducted an analysis of the logs the same night.` 违反点：made a decision 里现成有 decide，conducted an analysis 里现成有 analyze，两处都在用短语替代动词。

## 三 开场

### EN-P-007 清嗓子式开场

**判据。** 开头位置的清嗓子和对话框架残留即命中，触发词：Here's the thing、Let me be clear、I'll be honest、The uncomfortable truth is、in this article we will explore、this comprehensive guide、let's dive in、let me walk you through、here's what you need to know、There are several ways to、In general, it is a good idea to。处理动作是删掉铺垫，直接从内容开始。

**通过条件。** 开头是能带出语境、张力或人物的个人化插叙时保留，这一条不看句式看功能。EN-P-053 要求删掉 "By the time X, I was Y." 这个叙事模板，与本条明写的这条例外正面冲突，取本条。本条管开场位置，EN-P-050 管任意位置的自指插话，两条合起来覆盖同一类现象的两个位置。

**已知会漏掉什么。** 词表漏掉几类同形的说法：It turns out、The real [X] is、Can we talk about、Look,、Honestly? 作独立开场、以及任何做过渡用的 let's + 动词。位置判据也会漏：honestly 和 look 出现在句子中间是普通英语，不标记，而同一个词换到句首作停顿就该标记，本条的词表不带位置信息。

- 正例：`The webpack dev server doesn't send the CORS header by default.`
- 反例：`Here's the thing: the webpack dev server doesn't send the CORS header. Let me walk you through what you need to know.` 违反点：Here's the thing 和 Let me walk you through 都只做预告，删掉之后第一句的信息一点不少。

### EN-P-008 故作洞见的铺垫

**判据。** 用"别人都没看出来"的铺垫给一个普通论断加分量，这半句要删：The part everyone misses、what most people get wrong、nobody tells you this、here's what they don't say。处理动作是删掉铺垫，让论断本身站住。

**通过条件。** 铺垫之后确实跟着一条与通行说法相反、且有依据的论断时，保留论断、删掉铺垫，这一条的处理对象只是那半句铺垫。ZH-P-031 管中文里同一套铺垫，两条各管一种语言。

**已知会漏掉什么。** 同源的一类没有收进词表：把一个已有概念说成当事人发明的（he introduced a term、she coined the phrase），那是事实性问题而不是措辞问题，拿不准新不新时的默认值是假定它不新。制造知识稀缺的变体也漏：the failure mode nobody's naming、a problem nobody talks about。权威腔（the real question is、make no mistake、the deeper issue）与本条断言的东西不同，那些宣告的是深度而不是稀缺。

- 正例：`Distribution is the moat.`
- 反例：`The part everyone misses: distribution is the real moat.` 违反点：The part everyone misses 把作者包装成孤独的行家，删掉之后论断照样成立。

### EN-P-009 假戏剧停顿与修辞性设问

**判据。** 三种形状都算违反：短促的揭晓钩子（The catch?、The kicker?、The brutal truth?、The best part?、The result?）、招呼读者的设问（Sound familiar?、What if I told you、Think about it）、以及自问自答的"问题？答案。"。处理动作是删掉钩子或问句，把后面那句话直接说出来。

**通过条件。** 问句在前文铺垫之后挣得到位置、并且答案不紧跟其后时保留。访谈、FAQ 和对话体里连打问句是这些体裁的正当写法，不适用本条。EN-P-064 管的是跨句的铺垫与反转，带两处以上的计数门槛，本条只管句内的假停顿与设问，两条的范围不同。

**已知会漏掉什么。** 本条没有计数门槛，一处孤立的设问和一篇里五处得到同样的判定，密度问题查不出来。小标题位置的问句归 EN-P-032，本条不覆盖标题。连打两个以上问句这个具体形状本条也没有单列，它需要读语域才能判，正则读不出访谈和随笔的区别。

- 正例：`It only works on weekends.`
- 反例：`The catch? It only works on weekends. Sound familiar?` 违反点：The catch? 是揭晓钩子，Sound familiar? 是招呼读者的设问，两处删掉之后句子更短而信息不减。

### EN-P-058 声称一件事一直占着脑子的分享式开场

**判据。** 开场声称某件事持续占据作者的注意力即命中：the line I keep coming back to、I can't stop thinking about this、still thinking about this one、this has been rattling around in my head all week、I've been chewing on this since Tuesday。这类声称无法核对，读者在读到那件事本身之前没有理由在意。

**通过条件。** 例外只有一种：同一句里说出了它为什么反复出现。说出理由之后，句子谈的就不再是作者的注意力，而是这个想法的解释力。EN-P-076 管的是声称一种感受，本条管的是声称注意力的持续时间，两条形状相近、判据不同。

**已知会漏掉什么。** 词表之外的同义说法漏掉：this has stayed with me、I keep returning to。理由写在下一句而不是同一句时会被误命中，本条的例外要求理由与声称同句。

- 正例：`I keep coming back to Hirschman's exit-voice framing because it predicts which engineers quit and which ones file the RFC.`
- 反例：`The line I keep coming back to: agents are teenagers.` 违反点：句子里没有说这句话凭什么值得反复看，读者拿到的只是作者注意力的时长。

### EN-P-059 宣告自己要坦白的那层框

**判据。** 宣告作者即将坦白的那层框要删掉：Two caveats I would rather flag than let you discover later:、I want to be upfront:、To be fully transparent:、Rather than bury this, I'll say it plainly:、I could have left this out, but:、Being honest about the limitations here:。判据是删除测试：把这层框去掉之后句子没丢信息，它就不是内容。

**通过条件。** 两条例外。实质性的自曝保留（I haven't tested this on Windows），那句话本身是一条事实。利益冲突披露的惯例开场保留（In the interest of full disclosure, I own shares in the company discussed here），因为后面跟着真实的事实。按 ALL-PROT-036，利益冲突披露与实质性自曝属于不得清理的内容，本条对它们不适用。本条管的是输入侧的标记，EN-PROT-001 管的是改写时不得新增表演式坦白，同一现象的两端。

**已知会漏掉什么。** 这条做不成检测器：能放过两条例外的匹配规则都不再命中这个痕迹，判定它要读出这个从句有没有信息。普通的比较句形状相近而不命中，I'd rather fix it than let you inherit the mess 是一句真话，不算这层框。

- 正例：`The benchmark ran on one machine, so the numbers are not comparable across configs.`
- 反例：`In the interest of full disclosure, I would rather flag this than let you discover it later: the benchmark ran on one machine.` 违反点：I would rather flag this than let you discover it later 删掉之后句子一个信息都没少；此处的 In the interest of full disclosure 后面跟的不是利益冲突事实，不适用那条例外。

### EN-P-074 产品发布文案里的戏剧化登场句

**判据。** 产品与发布文案里把产品像选手一样介绍出场的句子即命中：Enter Flowdesk.、Meet Flowdesk, your new favorite treasury dashboard、Say hello to Flowdesk、Think Notion meets Figma。这个动作介绍了出场，却没有说出关于它的任何事。修法是说清这东西做什么、给谁用。判定要先确认这段文字是发布或公告文案。

**通过条件。** 本条只在判定为社交帖或商务与投资邮件两档时适用，档位按 ALL-PROC-053 判定。三种表面故意留作判断题，不做形式匹配：Say hello to X（Say hello to Grandma. 是普通人话）、光秃秃的 Meet X, your new [角色]（真人就是这样介绍同事、宠物和婴儿的）、光秃秃的 Enter X.（这也是 UI 与文档的写法 Enter Password.，还是剧本的舞台指示和专栏叙事）。ALL-PROC-039 规定先按模式判定再用词条兜底，本条补上"哪些表面故意不做机械匹配及其理由"这一层。

**已知会漏掉什么。** 上游把这条规则的两侧失败都测过并写了出来：机械匹配分不清产品名和人名，Meet Alice, your new favorite aunt 会误命中；产品名超过一个词就漏掉，Meet North Star、Think Google Docs meets Microsoft Word 不命中。

- 正例：`Flowdesk shows a fund's full treasury position on one screen.`
- 反例：`Meet Flowdesk, your new favorite treasury dashboard. Think Notion meets Figma.` 违反点：两句都在介绍出场，读者读完不知道这个产品做什么、给谁用。

### EN-P-076 情感断言当结构支架

**判据。** 用宣布一种感受来充当段落或列表的引子算违反：What surprised me most、I was fascinated to discover、What struck me was、I was excited to learn、The most interesting part，以及去掉"最"字的小标题形式（Interesting part of the project:、Interesting thing here:、Interesting aspect:）。同源的一种是用流行语抄近路制造共鸣：hit differently / hits different。

**通过条件。** 修法不是不许说自己惊讶。要声称一种情绪，周围的文字就得配得上它：读者从内容里能感到那件事确实意外时，声称保留；感不到，删掉声称、直接把那件事摆出来。EN-P-022 管的是给内容贴标签的旁白，本条管的是宣布作者自己的感受，两条形状相近、对象不同。EN-P-058 声称的是注意力的持续时间，本条声称的是一种感受。EN-P-077 宣布的是列表里某一项的地位，本条宣布的是作者的感受。

**已知会漏掉什么。** 这条不总是指向 AI，真人写顺手了也会这样开头，规则管的是文字不是作者，两种都标，因此它对人写的稿子误报率不低。词表之外的同类引子（What I found most striking、The part that stayed with me）漏掉。

- 正例：`The parser accepted a 4GB input without allocating more than 12MB.`
- 反例：`What surprised me most was the memory behaviour. Interesting thing here: it hits different.` 违反点：What surprised me most 与 Interesting thing here: 都在宣布感受，hits different 用流行语替代了具体说法，三处没有一处给出让人感到意外的内容。

## 四 收尾与金句

### EN-P-023 结尾不做总结和展望

**判据。** 结尾停在最后一个具体的事实、收获或下一步上。三类命中：空洞乐观（the future looks bright、exciting times lie ahead、poised for growth、only time will tell、one thing is certain）、总结复述（In summary、To sum up、Overall、总之本文讨论了）、以及 Whether you prefer X or Y 式的收束。

**通过条件。** 原文给出的真实计划保留，那是事实不是展望。一句收尾只在它只对这一篇的论证成立时保留，换到任何一篇文章上都成立的收尾属于填充。EN-P-057 管的是社交帖最后一行替读者背书的推荐语，位置和形状与本条都不同，两条不同时适用。EN-P-081 管的是小节标题里的 Summary、Conclusion，处理动作是改写成具体说法，本条管的是正文里的总结句，处理动作是删掉。

**已知会漏掉什么。** 带构式的未来断言本条查不到：情态词 + become + one of the most [形容词] + narrative / story / trend / theme / chapter / movement / force，这个骨架语法上是预测，实际不可证伪。词表也漏掉 As we move forward 一类。

- 正例：`The next milestone is the schema migration in March.`
- 反例：`The future looks bright for the platform. Whether you prefer speed or safety, there's something here for everyone. Only time will tell.` 违反点：三句都是可以放到任何一篇文章末尾的收束，没有一句给出这一篇特有的事实。

### EN-P-024 故作深刻的金句

**判据。** 收尾用格言模板包装一个普通论断即命中：X is the new Y、the currency of、not a X but a Y、X is where Y meets Z、X is the language of Y、X becomes a trap。处理动作是删掉，不是改写成一个更好的隐喻，也不是为了保留节奏而留着。删掉之后用稿子里已有的最具体的一句收尾。

**通过条件。** 引语保留。已经进入日常语言的固定说法保留（time is money）。这条明写了一种常见的错误修法：把金句换成另一个更精致的金句不算完成，处理动作只有删。

**已知会漏掉什么。** 上游把"听起来像可以摘出来当引言的句子"也归进这一类，但那个判据需要判断，本条只给出六个可以逐字核对的模板，模板之外的金句形状漏掉。可用的形式线索是整句不依赖上下文也能独立成立，这个线索不在原始规则里。

- 正例：`Ad networks pay about $8 per thousand views, so publishers chase pageviews.`
- 反例：`Data is the new oil, and attention is the currency of the modern web.` 违反点：X is the new Y 与 the currency of 两个模板叠加，两句都把一个可以说清楚的观察换成了无法核对的普遍规律。

### EN-P-057 社交帖尾部替读者背书的收束

**判据。** 社交帖最后一行替读者做推荐要删掉：This one is worth your time:、This one's a must-read:、I highly recommend giving this a read.、Do yourself a favor and read this.、You won't want to miss this one.、Save this for later.、Bookmark this.、Don't sleep on this one.、Trust me, you'll want to read this.、Thank me later.。这类句子靠 this one 指代，换到任何一条链接下面都成立。修法是说清这东西是什么、给谁看的，然后把整句行动号召去掉。

**通过条件。** 说不出具体理由就不加收尾，不要用另一句更委婉的推荐替换。EN-P-023 管的是文章结尾的空洞乐观与总结复述，本条管的是社交帖最后一行的推荐语，两者位置和形状不同，不同时适用。

**已知会漏掉什么。** 句子里的弱背书本条查不到：worth reading、worth paying attention to、worth a look、worth exploring、worth checking out、worth your time 作为句中成分出现时，形状与本条不同。本条只管整条帖子的最后一行。

- 正例：`Sarah's breakdown of why context windows leak, the clearest explanation I've found for anyone debugging RAG pipelines.`
- 反例：`This one is worth your time: read the method section. Thank me later.` 违反点：This one is worth your time: 与 Thank me later. 都是可以放在任何链接下面的背书，没有给读者点开的理由。

### EN-P-064 反复出现的铺垫—反转式抖包袱

**判据。** 一篇里出现两处以上"铺垫—反转"式抖包袱、且它们替代了本该给出的具体解释时才命中（We planned for every failure mode. Except the one that happened.）。重点看三个位置：钩子、收尾、列表末项。重复本身不构成命中，替代解释才是。

**通过条件。** 四类不命中：单独一处；有支撑的反转；传达了具体区别的重复反转；有意的喜剧、虚构、演讲和引语。修法是保住有依据的那半句、删掉空的转折。作者没有说出那个失败原因时按 ALL-PROC-047 处理：向他要，或者改写成一句不需要它的说法，不得自己编一个磁盘故障或时钟漂移。EN-P-009 管的是句内的假戏剧停顿与修辞设问，本条管的是跨句的铺垫与反转，且带计数门槛与四类通过条件。

**已知会漏掉什么。** 本条需要读上下文才能判定解释是不是真的缺失，按 ALL-M-023 在报告里要与出处相关的命中分开列。它也明确不是作者身份的证据，只是清晰度和节奏的编辑意见，把一种修辞手法本身当罪状是这条最容易出的错。

- 正例：`We rebuilt billing to group charges by project. Your invoice total didn't change.`（这一处反转传达了一个具体区别，按通过条件不命中）
- 反例：`We planned for every failure mode. Except the one that happened. The migration went smoothly, which is how we knew something was wrong.` 违反点：一段里两处反转，都在用"意料之外"替代那个从未写出的解释，读者不知道是哪个失败模式、哪里不对劲。

### EN-P-077 列完之后回指其中一项并给它贴标签

**判据。** 列完或写完几项之后回指其中一项、给它贴上"反直觉／聪明／意外／关键"标签即命中：That last move is the contrarian one、This is the interesting part、That third bullet is the real story、Here's where it gets clever。触发标签的形容词有十二个：contrarian、clever、surprising、counterintuitive、interesting、key、important、unusual、smart、brilliant、real、actual。形状通常是 [that / this / the Xth / the last] [名词] is the [形容词] one.。修法是删掉这句贴标签的话让后面的解释直接干活，或者重排把想强调的那一项放到最前并展开写具体。

**通过条件。** 真的反直觉，读者从描述里就能认出来，这时标签是多余的；认不出来，这个标签就是没挣到的。两种情况的处理动作相同，因此本条没有"保留"的出口，只有两种修法。EN-P-022 管的是给内容贴标签的旁白，本条给的是事后回指某一项并贴标签这个具体形状与十二个触发词。EN-P-076 宣布的是作者的感受，本条宣布的是列表里某一项的地位。

**已知会漏掉什么。** 判定要看到被回指的那一项，因此跨段回指会漏。形容词清单是封闭的，用 subtle、tricky、underrated 贴的标签不在其中。

- 正例：`Two separate indexes for tiered storage. Co-locating related data usually helps cache locality, but splitting the indexes is what makes the hot path cheap.`
- 反例：`Two separate indexes for tiered storage. That last move is the contrarian one. Co-locating related data usually helps cache locality.` 违反点：That last move is the contrarian one. 是回指加标签，删掉之后后面那句解释照样成立。

## 五 对比、否定与假选项

### EN-P-006 二元对比与否定式排比

**判据。** 用否定作铺垫再揭晓的骨架即命中：It's not X, it's Y、not only X but Y、The question isn't X. It's Y.、Not a X. Not a Y. A Z.。拆掉骨架，直接陈述结论。同一动作的几种变体一并算：同句里靠破折号或逗号转折的原形、拆成两句的形态（The headline isn't the speed. The real story is Y.）、多重否定倒数（It's not the price. It's not the features. It's the trust.）。

**通过条件。** 列表里逐项列出规格约束的否定是清单内容，不是揭晓（no dependencies, no telemetry）。被否定的那个说法在上下文里真的有人主张过时，这个对比是真的，保留。ZH-P-024 管中文里同一骨架，并给出"多数删掉前半句"这个具体动作。本条管的是先否定再给出 Y 的骨架，EN-P-043 管的是只剩否定、没有 Y 的句尾截断。

**已知会漏掉什么。** 拆成两句的形态最容易漏：单看每句都像普通陈述句，只有连起来读才看得出是同一个动作。上游明说检测规则按原形写，模型就把同一个动作拆开写。stops being X and starts being Y、doesn't mean X, but actually Y、is about X but not Y 这三种骨架不在本条的四个例子里。

- 正例：`The eval matters more than the model.`
- 反例：`The question isn't the model. It's the eval. It's not just a metric, it's a whole methodology.` 违反点：前两句是 The question isn't X. It's Y. 骨架，后一句是 not just X, it's Y 骨架，被否定的两个说法在上下文里都没有人主张过。

### EN-P-021 假范围

**判据。** 用 from X to Y 制造并不存在的跨度算违反，成立条件是 X 和 Y 不在同一个维度上，中间不存在一条连续的轴。这个句式让读者以为中间还有很多没列出来的东西，而作者其实只有这两项。修法是直接列出具体的项，或者只留最重要的一项。

**通过条件。** X 和 Y 确实构成一条真实跨度的两端时保留（from 10ms to 400ms、from 1998 to 2004）。列举本身是完整的、句子没有暗示中间还有别的项时保留。

**已知会漏掉什么。** 判定要懂这两项属不属于同一个维度，这是领域知识，机械匹配做不出来。同一动作的另一种形状本条不覆盖：连排三个以上历史先例来借分量，那归 EN-P-069。

- 正例：`The course covers stellar nucleosynthesis and the cosmic microwave background.`
- 反例：`The course covers everything from the Big Bang to dark matter.` 违反点：Big Bang 和 dark matter 不构成同一条轴的两端，跨度是修辞造出来的，读者读完不知道这门课到底讲什么。

### EN-P-041 假想反方

**判据。** 反驳一个原文里没人提出过的反对意见算违反：While some might argue、It would be easy to dismiss this as、One might object that... but、This isn't (mainly/really) about、I'm not saying / arguing、Don't get me wrong、Some might say… but。可查的判据是：被否定的那个话题在文章别处出不出现。

**通过条件。** 只回应原文里真实存在、点名的反对意见时保留。一个直接的论断里带否定不算这个模式（the API is not thread-safe）。本条管的是回应原文里没人提出过的反对意见，EN-P-046 管的是否掉没人会考虑的备选方案，一段文字可以只命中其中一条。EN-P-078 命中的是虚构的落后群体，本条命中的是虚构的异议，两条形状相近、对象不同。

**已知会漏掉什么。** 判定要通读全文核对那个话题是否出现过，单段审阅判不了。误伤集中在辩论体和论文的文献综述部分，那些体裁里回应假想异议是正当的写法。

- 正例：`Remote work hasn't hurt our collaboration. Our incident response time improved after we went remote.`
- 反例：`While some might argue that remote work hurts collaboration, the data tells a different story.` 违反点：some might argue 指向的那个说法在文章别处从未出现，反驳的是一个作者自己立起来的对手。

### EN-P-043 句尾截断式否定

**判据。** 句尾拖一个截断的否定短语代替把话说完的从句要处理。成立条件是这个否定短语后面没有跟一个正面的说法，读者要自己补出被省掉的意思。处理动作有两条：写成一个完整的从句，或者整个删掉。

**通过条件。** 否定短语本身承载一条具体的规格约束时保留（the endpoint takes no arguments）。句尾否定之后跟着正面说法的属于 EN-P-006 的骨架，不归本条：EN-P-006 管的是先否定一个说法再给出另一个的对比骨架，本条管的是只剩否定、没有 Y 的句尾截断，两条各管上游同一节的一半。

**已知会漏掉什么。** 这个形状很短，没有可数的词表，判定靠"这里本该有一个从句"这条语感。作者有意为之的简洁写法会被误命中，判断的依据只能是句子读完之后读者要不要补出意思。

- 正例：`The options come from the selected item without forcing the user to guess.`
- 反例：`The options come from the selected item, no guessing.` 违反点：句尾的 no guessing 是一个截断的否定短语，它替代了一个说明"为什么用户不必猜"的从句。

### EN-P-046 假备选方案

**判据。** 引入一个读者不会考虑的备选方案、在一个从句里否掉它、之后再不提即命中。触发词：A tempting option / approach would be、One might be tempted to、An obvious approach would be、You might think… but、It would be easy to just、Some would suggest。这类句子多半是起草过程的残留：写的人考虑过、否掉了，把思考过程留在了成稿里。修法是删掉这个假选项，直接说出真正的约束。

**通过条件。** 判定门槛按数量定：全文只有一处、且它交代了一条真实约束的不标记；几处简短、互不相关的否定聚在同一段里才处理，处理时围绕这一段的主旨重写整段，不逐处点掉。设计文档、教程和论证里读者会真的考虑的选型比较不算命中，那是这些体裁的正当内容。EN-P-041 管的是回应原文里没人提出过的反对意见，本条管的是否掉没人会考虑的备选方案。

**已知会漏掉什么。** "读者会不会真的考虑这个方案"要靠领域判断，同一个句式在设计文档里正当、在随笔里是残留，本条给不出形式判据。数量门槛也意味着孤立一处的残留会被放过。

- 正例：`Session tokens are rotated every 24 hours, in place, and clients refresh transparently.`
- 反例：`Session tokens are rotated every 24 hours. A tempting approach would be to rotate them by restarting the auth service on a cron job, but that would drop every active session. Rotation happens in place.` 违反点：A tempting approach would be to…, but… 引入并否掉了一个没人会提的方案，之后再没提过。

### EN-P-055 否定对偶充当具体让步

**判据。** 用 "Not always. Not perfectly." 这类否定对偶充当具体让步即命中：形式上是承认局限，实际没有说出任何一处真实的例外。修法有两条：写出真实的例外场合，或者删掉这两句。

**通过条件。** 孤立出现一次不标记。同一段里出现两处以上，或者全篇反复出现，才处理。原文真实表达的不确定按 ALL-PROT-004 不动，本条只处理不指向任何具体例外的否定对偶。EN-P-030 删的是与句子实际语气自相矛盾的保留语，本条删的是以否定对偶表演坦诚的那一种，判据不同，两条各管一半。

**已知会漏掉什么。** 判定要读上下文才知道那个例外有没有在别处写出来，单句读不出来。两处以上这个门槛意味着一处漂亮的假让步会被放过，而它在收尾位置的说服效果最强。

- 正例：`The cache misses on the first request after a deploy, and on any key written in the last 200ms.`
- 反例：`The cache works. Not always. Not perfectly. It handles most cases. Not all of them.` 违反点：同一段里两组否定对偶，四句都是保留语，没有指出任何一处真实的例外场合。

### EN-P-082 否定连串

**判据。** 三种形式的否定连串即命中：连着两个以上句首的 no … 项（No fluff, no filler, no jargon.）、为节奏叠两个以上 didn't … 从句（It didn't ask. It didn't wait.）、否定之后重复同一个动词（Don't call it a pivot. Call it a correction.）。修法是把这个东西是什么说出来。

**通过条件。** 两条例外。句中的事实清单是普通散文（the endpoint takes no arguments, no headers, and no body）；按 ALL-PROT-025，删掉会改变命题真值或适用范围的子句是保真对象，这类清单不得当成节奏问题删掉。主语重复出现的顺序叙述也是普通散文（I did not sleep well. I did not eat breakfast.）。EN-P-006 管的是带正面揭晓的二元对比与否定式排比，本条管的是没有揭晓的纯否定连串。EN-P-025 按句子完整性判碎片句，本条按否定结构判，与写成不写成碎片无关。

**已知会漏掉什么。** 上游把确定性匹配的范围写得比规则窄：只匹配句首三个以上的短 no … 连串和主语省略的逗号连接 did not … 连串，两项的连串和其余形式一律留作判断。因此恰好两项的否定连串在自动检查里会漏。

- 正例：`The endpoint takes a single JSON body and returns 204.`
- 反例：`No fluff. No filler. No jargon. It didn't ask. It didn't wait.` 违反点：前三句是句首的 no … 连串，后两句是叠起来的 didn't … 从句，两种形式都命中，且没有一句说出这个东西是什么。

## 六 归因、证据与捏造

### EN-P-017 模糊归因

**判据。** 把一条论断挂在查不到的主体上即命中：experts agree、research suggests、studies show、observers have cited、several sources、it is widely believed、industry reports、many argue。两条出口：点名具体来源，或者删掉整个论断。

**通过条件。** 点了名、可核对的归因保留（带日期的报告、具名的基准、有链接的审计）。删掉归因、把论断直接说出来这条出口，要先按 ALL-PROC-040 判断这条论断离开来源之后还成不成立。用户给不出来源时按 ALL-PROT-001 去问，不得编一个：编一个具体来源比模糊归因更糟。ZH-P-019 管中文资讯稿里同一模式的固定说法。

**已知会漏掉什么。** 一种组合形式不在词表里：不点名的外部权威配一个泛泛的最高级（independent testing confirms、third-party benchmarks show we lead）。它比表内几条更难查也更容易编，因为权威是刻意不点名的。

- 正例：`A 2024 EPA report attributes the change to runoff from upstream farms.`
- 反例：`Experts believe the change is driven by upstream runoff, and studies show the trend is accelerating.` 违反点：Experts believe 与 studies show 把两条论断挂在查不到的主体上，读者无法核对是谁说的、哪项研究。

### EN-P-018 来源清单当内容

**判据。** 用"被哪些媒体报道过"的清单证明重要性算违反：featured in X, Y, Z、profiled in、cited in、independent coverage、active social media presence。判据是这份清单有没有说出内容：说了在哪里被报道而没说报道了什么，清单就只是在借名号撑分量。修法是挑一个来源说清它具体报道了什么，或者删掉。

**通过条件。** 原文说清了这个人说了什么、在哪里说的，这条引用有内容，保留；压缩篇幅时不得把具体语境换成一句概括的说法。ZH-P-016 管中文里同一模式的固定说法。EN-P-018 管的是堆媒体名，EN-P-069 管的是堆历史先例，两条形状相同、对象不同。

**已知会漏掉什么。** 粉丝数、奖项数、客户 logo 墙做的是同一件事，词表里只有 active social media presence 一条沾边。挑一个来源展开这个修法需要原文里本来就有内容，原文只有名字时，唯一的动作是删掉，本条没有写出这一层。

- 正例：`In a 2024 NYT interview, she argued that the latency numbers exclude cold starts.`
- 反例：`Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence.` 违反点：四个媒体名并列，没有一处说出它们具体报道了什么，名字在替论证承担分量。

### EN-P-038 生成过程残留

**判据。** 四类生成过程残留一律删掉。未填写的占位符：[Your Name]、[INSERT SOURCE URL]、2025-XX-XX，以及带 add / fill in / todo / insert 这类动词的 HTML 或 Markdown 注释。工具内部引用标记：citeturn0search0、contentReference、[cite: 1]、grok_card、oai_citation、[attached_file:1]。AI 来源的 UTM 参数：utm_source=chatgpt.com、referrer=grok.com。推理链脚手架：Let me think、Step 1:、Breaking this down、First, I'll。

**通过条件。** URL 上只删那一个跟踪参数，查询串的其余部分不动：?page=2、?v=4 是功能性参数，不构成任何证据，链接本身有意义就保留链接。引用标记删掉之后那处引用如果有意义，换成一条真实的引用，不要把标记改得自然些。ALL-M-025 要求 URL 逐字不动，本条去掉的 AI 来源追踪参数是那条的两个例外之一。EN-P-038 删的是生成过程留在英文正文里的痕迹，ALL-PROT-021 管的是加载进来的提示词片段被当成待改写素材输出，两者是同一族的两半。

**已知会漏掉什么。** 真人写模板时也用占位符，只是很少发出去，因此模板文件本身会被误命中；处理上一律当成发布事故，但这意味着未发布的草稿模板不该拿本条去查。孤立的脚注字符和 RAG 的 attribution 标签不在上面四类的例子里。

- 正例：`Contact Dana Reyes at dana@example.com. See the 2024 EPA report at https://example.com/report?page=2`
- 反例：`Contact [Your Name] at [INSERT EMAIL], last updated 2025-XX-XX. See the report citeturn0search0 at https://example.com/report?page=2&utm_source=chatgpt.com` 违反点：三处未填写的占位符、一处工具内部引用标记、一处 AI 来源的 UTM 参数；其中 ?page=2 是功能性参数，不该一并删掉。

### EN-P-039 疑似捏造的痕迹

**判据。** 三类痕迹标出来交给作者确认：精确到小数位却无法核实的统计数字、归到查不到的来源的引用、对冷门事实的自信断言且没有出处。这三类的共同点是它们看起来像真的，形式上没有任何标记说明作者没有依据。

**通过条件。** 不自行删除，也不自行改写：删掉会丢掉一条也许成立的信息，改写会把一个没有依据的断言换成另一个。ALL-PROT-014 规定不得静默纠正，本条与它走同一个出口，写进"需作者确认"。EN-P-045 管的是自带保留语式填空标记的猜测（likely began、appears to have studied），那类形式本身就是没有依据的信号，处理动作是删掉或换成有出处的事实。判定顺序：先看这句话有没有保留语式的填空标记，有则归 EN-P-045，无则归本条。EN-P-062 里生造的那一半是一个没有出处的术语主张，EN-P-073 里被当成既有概念引用的现造术语同样如此，两处都按本条标出来交作者确认。

**已知会漏掉什么。** 判定要有能力识别"这个来源查不到"和"这个事实冷门"，这依赖领域知识和外部核查，本条给不出形式判据。真实但罕见的精确数字会被误命中。

- 正例：`A 2024 EPA report, published on 12 March, puts the figure at 31%.` 来源具名、带日期、可以核对。
- 反例：`According to a 2019 internal Gartner memo, 73.4% of enterprises had adopted this by Q2.` 违反点：来源是无法核实的内部备忘录，数字精确到小数位，两条痕迹同时具备，应当标出来交作者确认而不是删掉或改写。

### EN-P-045 找不到资料时的猜测填空

**判据。** 把"找不到资料"当成推理前提、编出关于这个人或这件事的断言即命中。触发词：maintains a low profile、keeps personal details private、prefers to stay out of the spotlight、likely [grew up / studied / began]、it is believed that、appears to have。这类句子比知识截止免责声明更糟：那种句子承认了缺口，这种句子把缺口藏在听着合理的填充后面。

**通过条件。** 处理方式有两条：写明原文没有这项信息，或者整段略去。不得把猜测保留在正文里，也不得把猜测改写成一个语气更弱的猜测。EN-P-028 删的是知识截止免责声明本身，本条删的是接在免责声明后面、把"查不到"当证据的那一串猜测，两条常常同时命中同一段。与 EN-P-039 的分界写在那一条里：有保留语式填空标记的归本条，看起来像真的、没有标记的归 EN-P-039。

**已知会漏掉什么。** 保留语式标记之外的猜测漏掉：一句没有 likely、没有 appears 的自信断言，形式上与事实无异，本条查不到，那类归 EN-P-039。

- 正例：`The sources do not say where she trained; her first published paper is from 1998.`
- 反例：`Information about her early life is not publicly available, suggesting she maintains a low profile. She likely grew up in a middle-class household.` 违反点：suggesting she maintains a low profile 把"没有记录"当成了性格的证据，She likely grew up 再从这个虚构的性格推出更多细节。

### EN-P-047 全称量词代替真实范围

**判据。** every、always、never、everyone、everybody、nobody 这类全称量词，如果原文并没有主张全称、只是用它代替一个没查过的范围，就换成原文已经给出的具体范围，或者删掉整条主张。两个条件都要满足才算命中：这个全称无法核实，而且它对句子不必要。

**通过条件。** 原文本来就主张全称、或者全称有依据时保留（every request goes through the same middleware，代码可查）。换范围时按 ALL-PROT-023 不得放宽或收窄原文的范围；原文给不出范围就删掉整条主张，不自己编一个。ALL-P-007 要求能给具体内容的地方不用抽象词，本条管的是用全称词冒充范围这一种具体形式。

**已知会漏掉什么。** 判定"无法核实"要看作者手上有没有这个数据，同一句全称在有数据的人写来是事实、在没数据的人写来是借权威，本条从文本上分不出来。全称量词以外的范围词（most、the majority of、virtually all）不在词表里。

- 正例：`The reaction is taught in introductory biochemistry.`
- 反例：`Everybody knows every incident always starts the same way, and the reaction is taught in every first-year biochemistry course.` 违反点：everybody、every、always 三处把没有统计过的范围说成全称；每一处去掉之后句子的信息都不减。

### EN-P-052 以人格担保替代证据

**判据。** 用作者的人格担保替代证据要删掉：I promise、They exist, I promise、trust me on this。这类句子占着一个理由的位置却不给理由，拿作者与读者的关系换取读者的相信。

**通过条件。** 原文给不出例子或数据时按 ALL-P-007 标出这个缺口，不用一句保证顶上：ALL-P-007 要求能给具体内容的地方给具体内容，本条堵住给不出时最省力的替代品。上游同一节里的 creeps in 属于无生命事物做人的动作，归 ALL-P-004，本条只管以人格担保替代证据这一种。

**已知会漏掉什么。** 这份词表只有三条，实际只有两种形式。同类的说法漏掉：believe me、I can tell you that、take it from me。

- 正例：`Three of the five services time out at 30 seconds.`
- 反例：`These cases are real, I promise. Trust me on this one.` 违反点：I promise 与 Trust me 都在用作者的担保替代那三个本该给出的具体例子。

### EN-P-062 对仗式对比里有一半是现造的

**判据。** 一组对仗式对比里恰好有一半是领域里真实存在的术语、另一半是为了对称生造出来的镜像时命中。判据不是这两个词组对不对称，而是这两半是不是都真实存在。修法是找一个真的反义项，找不到就把对比结构整个去掉、直接陈述正面主张。

**通过条件。** 两半都真实的对比不算（real data rather than theoretical models）。生造的那一半是一个没有出处的术语主张，按 EN-P-039 标出来交作者确认，不自行替换成另一个术语。EN-P-006 按句式判定二元对比，本条按两半的真实性判定；一个不用那个句式的对仗（X rather than Y）只命中本条。EN-P-073 管的是一个孤立的现造术语，本条管的是对仗里恰好一半是现造的，两条同源、对象不同。

**已知会漏掉什么。** 上游写明了这条为什么危险：不对称之处只有懂这个领域的人看得出，读者会把生造的那一半当成同样有来历的术语。因此判定需要领域知识，跨领域审阅时这条基本失效。

- 正例：`The number has three decimal places but the measurement is only good to one.`
- 反例：`What we have is false precision rather than genuine accuracy.` 违反点：false precision 是真实的统计学术语，genuine accuracy 是为了配对现造的镜像，不查这个领域看不出这一半是假的。

## 七 意义拔高与旁白

### EN-P-014 意义拔高与重要性吹捧

**判据。** 把一件普通事实吹成有时代意义算违反：stands as、serves as a testament、marks a pivotal moment、plays a vital role、solidifies its position、underscores its significance、represents、symbolizes、speaks to、embodies、reflects broader。可执行的判据是删除测试：删掉那个拔高的从句之后句子还成立，就删。

**通过条件。** 意义是真的时候，用一个具体后果把它显示出来，而不是删掉了事。删完之后留下的必须是具体事实，不是另一句空话，这一层按 ALL-PROT-002 判。ZH-P-015 管中文的同一模式，触发词完全不同，两条各管一种语言。EN-P-014 命中的是评价本身，EN-P-069 命中的是用来支撑评价的那串历史类比。

**已知会漏掉什么。** 与 EN-P-015 在 represents、stands as 上重叠：同一处命中判成哪一条要看句子在做什么，回避系动词归 EN-P-015，追加时代意义归本条。带 -ing 的分词形式归 EN-P-013，本条只管主句里的拔高。

- 正例：`The team moved the release to Thursday.`
- 反例：`Moving the release to Thursday marks a pivotal moment in the evolution of the team's process.` 违反点：marks a pivotal moment in the evolution of 把一次排期调整说成转折点；删掉这个从句之后前半句完全成立。

### EN-P-022 解读性旁白

**判据。** 跳出内容本身、告诉读者该怎么理解的旁白即命中：That last part matters more than it sounds、The key point is、As you can see、This distinction matters、多余的 In other words，以及宣布重要性的强调句（Let that sink in.、Make no mistake、This matters because）。让事实、动作和后果自己承担重点，不给它贴"重要""惊人""微妙"的标签。

**通过条件。** This matters because 引出的是一个具体后果时保留（This matters because retries can charge the customer twice.）；引出的是对重要性的复述时删掉（This matters because it is important.）。原文没有给出那个后果时不得替作者编一个利害，按 ALL-PROT-001 处理。ZH-P-032 管中文里同一种旁白。EN-P-076 管的是宣布作者自己的感受，EN-P-077 管的是事后回指某一项并贴标签，三条形状相近、对象不同。

**已知会漏掉什么。** 一类同源形式不在词表里：宣布难度或意义而不演示（This is genuinely hard、This is what leadership actually looks like）。句中的弱背书（worth reading、worth a look）也漏，那类占着一个理由的位置却不给理由。

- 正例：`The migration dropped p99 latency from 400ms to 90ms.`
- 反例：`The migration dropped p99 latency. Let that sink in. As you can see, this distinction matters because latency is the whole product.` 违反点：Let that sink in.、As you can see、this distinction matters 三处旁白都在替读者规定该怎么看第一句，删掉之后第一句的信息一点不少。

### EN-P-031 挑战小节套路

**判据。** "Despite [好的一面]，[模糊的问题]。Despite these, [空话]" 这种挑战小节套路即命中。同一动作的另一个句式一并算：While X is impressive, Y remains a challenge。判据是两半都没有具体内容，句子摆出了权衡的姿势却没有权衡任何东西。修法是写清具体问题（带时间和数据），或者删掉整段。

**通过条件。** 有一半是具体的让步不在此列（The retrieval step is 40ms faster, but the reranker still times out on queries over 200 tokens.）。原文给不出具体的挑战时删掉整段，不得自己补一个。ZH-P-020 管中文里同一套路，并额外覆盖它作为固定小节标题出现的形态。

**已知会漏掉什么。** Challenges and Legacy、Future Outlook 这类固定小节标题本条只在正文层查，标题层归 EN-P-081。转折词换成 Although、Nevertheless、That said 时词形不同，本条的两个句式匹配不到。

- 正例：`The team lost two engineers in March and shipped the migration eight weeks late.`
- 反例：`Despite its industrial prosperity, the town faces challenges typical of urban areas. Despite these challenges, it continues to thrive.` 违反点：两句都是套路句，challenges typical of urban areas 没说出任何一个挑战，continues to thrive 没说出任何结果。

### EN-P-050 任意位置的自指插话

**判据。** 正文里任意位置交代文章自身结构、或对自己的行文发议论的插话要删掉：Hint:、Plot twist:、Spoiler:、You already know this, but、But that's another post、The rest of this essay explains…、Let me walk you through…、In this section, we'll…、As we'll see…、I want to explore…。判据是这句话谈的是文章本身而不是文章的主题。

**通过条件。** 长篇技术文档里指明结构的导航句是正当的（see the migration section below），本条针对的是不承载内容的插话，判据仍是这句话有没有给出关于主题的信息。EN-P-007 管的是开场位置的清嗓子，本条管的是任意位置的自指插话，两条合起来覆盖同一类现象的两个位置，词表在 let me walk you through、in this article we will explore 两条上重合，同一处命中不重复计。

**已知会漏掉什么。** X is a feature, not a bug、Dressed up as 这类对自己行文发的议论在上游的同一份词表里，形状与前面几条差别较大，容易被漏掉。

- 正例：`The three failure modes share one root cause: the retry budget is per-process, not per-request.`
- 反例：`In this section, we'll walk through the three failure modes. Plot twist: they share a root cause. But that's another post.` 违反点：三句都只谈文章自身，没有一句给出关于那三个失败模式的信息。

### EN-P-069 连珠炮式的历史类比堆砌

**判据。** 连排三个以上历史技术、公司或事件来给眼下这件事借分量算违反（like the printing press, the telegraph, and the internet before it）。罗列本身在替论证站台。修法是只留下那个真正在做分析工作的类比并说清它解释了什么，说不清就整段删掉。

**通过条件。** 一个类比、说清了它解释眼下这件事的什么，保留（Like the shift from dial-up to broadband, the cost curve here changes what people build.）。修法保留类比这个手法本身，删的是罗列。EN-P-018 管的是堆媒体名，本条管的是堆历史先例，两条形状相同、对象不同。EN-P-014 命中的是评价本身，本条命中的是用来支撑评价的那串类比。

**已知会漏掉什么。** 三个这个门槛意味着两个类比的并列会被放过，而两个已经足以制造同样的效果。类比的对象限定在历史技术、公司和事件，换成人物或作品的堆砌不在范围内。

- 正例：`Like the shift from dial-up to broadband, the cost curve here changes what people build, not just how fast it runs.`
- 反例：`This is like the printing press, the telegraph, and the internet before it.` 违反点：三个历史类比并列，没有一处说明它解释了眼下这件事的什么。

### EN-P-078 靠一群想象中落后的人撑主张

**判据。** 用一个没有名字的人群作对照来撑自己的主张即命中，通常还带一个时间戳（shipped it in 2022, while everyone else was still debating timelines）。那个人群是编出来的，所以这个对比不花任何代价。修法有两条：把事实说完、删掉人群那半句，或者点名真实的竞争者和他们做了什么。点不出名字，就说明它是编的。

**通过条件。** 字面意义的同时发生是普通叙述（she read while everyone else watched the movie）。点了名的比较保留（Datadog shipped a comparable feature in 2024）。ALL-PROT-001 管的是改写时不得生造逆反立场，本条管的是原文里已有这半句时的标记，一条在改写侧、一条在输入侧。EN-P-041 命中的是虚构的异议，本条命中的是虚构的落后群体，两条形状相近、对象不同。

**已知会漏掉什么。** 上游按测量结果公开了这条的两侧失败：误报出在字面用法上，几种匹配写法都会把 while everyone else 的字面同时性一并命中；漏报出在人群词是封闭清单，while every competitor was still debating 不命中。

- 正例：`We shipped the migration in 2022; Datadog shipped a comparable feature in 2024.`
- 反例：`We shipped it in 2022, while everyone else was still debating timelines.` 违反点：while everyone else 指的人群没有名字、无法核对，这个对比因此不花任何代价。

## 八 重复与轮换

### EN-P-019 同义词轮换

**判据。** 指代同一件事时，一个清楚的词够用就重复用它，不为文采换同义词（agent / assistant / tool 指同一个东西）。反向的判据同样成立：同一个名词或动词在一段里出现三次而它就是最准的那个词，三次都留着，强行变化读起来是查同义词典。

**通过条件。** 精确术语的重复不算违反，见 ALL-PROT-009。代词照应不算换称。先通读全文才看得出同一个东西被换了几种叫法，这一步按 ALL-PROC-009 的先全局后局部执行。ZH-P-029 管中文，并补上"逐次升格"这个中文特有的形态和"代词照应不算"的例外。

**已知会漏掉什么。** 判定要认出这几个词指的是同一个东西，跨段落的轮换比同段内的难认，本条给不出可数的门槛。上游把范围限定在同一段内，本条不限范围，代价是全文范围内的误报会多。

- 正例：`The agent reviews the draft, scores it, and suggests fixes.`
- 反例：`The agent reviews the draft. The assistant scores the piece. The tool suggests fixes.` 违反点：agent、assistant、tool 指同一个东西，读者要现场判断它们是不是同一个。

### EN-P-020 名词短语轮换

**判据。** 给同一个实体换整个名词短语要处理（the artist → the visionary creator → the non-conformist painter）。选定最清楚的说法反复用。这与 EN-P-019 的区别在层级：那条管单个词的替换，本条管整个名词短语的替换。

**通过条件。** 例外是 ALL-PROT-009 认定的固定表述，那类说法本身就是这个实体的正式名称。换称同时带进了原文没有的评价时，那部分另按 ALL-PROT-001 处理，不能算成换称一并改掉。ZH-P-029 是本条的中文形态。

**已知会漏掉什么。** 名词短语的替换比单词替换更难认，因为每一个替换本身都是通顺的英语。上游把成因写了出来：模型有一条"不要重复"的规则，于是在不该避免重复的地方也照做，因此这类替换往往一次出现三四个，密度是可用的线索，本条没有把它写成门槛。

- 正例：`Yankilevsky and other non-conformist artists faced obstacles. His work continued.`
- 反例：`Yankilevsky, alongside other non-conformist artists, faced obstacles. The visionary creator's distinctive artistic journey continued.` 违反点：the visionary creator 是给同一个人换的整个名词短语，同时带进了原文没有的评价。

### EN-P-033 标题后的复述句

**判据。** 标题后面跟一句只是复述标题的话即命中，包括 This section covers X 这类明说。判据是标题已经做过这件事了。处理动作是删掉这句，或换成一句真正的事实。

**通过条件。** 标题之后的第一句给出新信息时保留，哪怕它用了标题里的词。EN-P-033 在小节标题层管复述，EN-P-070 在列表项层管同一个动作，两条各管一层。

**已知会漏掉什么。** 判定"只是复述"需要判断，Speed matters. 复述的是 Performance 这个标题，但两者没有一个共同的词，形式匹配做不到。

- 正例：`## Performance` 之后直接写 `The p99 dropped from 400ms to 90ms after the index rebuild.`
- 反例：`## Performance` 之后先写 `Speed matters.` 再进正文。违反点：Speed matters. 只是把标题换个说法重复了一遍，删掉之后正文照样从该开始的地方开始。

## 九 标题、列表与句子形状

### EN-P-010 冒号式揭晓

**判据。** 用"名词短语＋冒号＋小写的戏剧化揭晓"制造悬念即命中（The best part: it learns.）。改成一句平实的陈述句。冒号只用于列表、标签和引语。

**通过条件。** 冒号引出列表、标签或引语时正当，本条不适用。冒号两侧是同一个陈述的两半、后半不承担揭晓功能时保留（The result: 204.）。EN-P-011 决定冒号后面的内容用不用小写，本条决定该不该用这个冒号，两条的对象不同。

**已知会漏掉什么。** 悬念与说明的界线要靠判断：同一个"名词短语＋冒号"结构在文档里是标签、在随笔里是揭晓，本条给不出形式判据。列表标签后面该用冒号还是句点归 EN-P-071，本条不覆盖。

- 正例：`A separate agent does the grading, which is what makes it work.`
- 反例：`The detail that makes it work: a separate agent grades it.` 违反点：名词短语加冒号加小写揭晓，把一句可以平铺直叙的陈述做成了悬念。

### EN-P-011 冒号后用小写

**判据。** 冒号后面的内容用小写。首字母大写只在四种情况下正确：语法要求、专有名词、标题、代码另有规定。

**通过条件。** 上面四种情况保留原样。EN-P-071 决定列表标签后面用冒号还是句点，本条决定冒号后面的内容怎么写，顺序是先按 EN-P-071 定标点，再按本条定大小写。

**已知会漏掉什么。** 这是一条排版惯例，不同的出版体例对它的规定不同；目标发布格式有自己的规范时以那份规范为准，本条是默认值。

- 正例：`The launch adds one thing: faster search.`
- 反例：`The launch adds one thing: Faster search.` 违反点：Faster 没有语法、专有名词、标题或代码方面的理由却大写了首字母。

### EN-P-012 标题用句子大小写

**判据。** 标题用句子大小写，只有句首和专有名词大写，不用 Title Case。整篇的主标题是唯一可能的例外，小标题一律用句子大小写。

**通过条件。** 目标发布格式明确要求 Title Case 时按那份要求。ALL-M-025 要求七类内容逐字核对不得变动，EN-P-012 改的标题大小写是那条的两个例外之一；这条例外绑在本规则上，不写成"本 skill 要求的改动"这类会漂移的说法。ZH-G-001 已写明这条只对英文成立，不套用到中文标题。

**已知会漏掉什么。** 判定专有名词需要领域知识，产品名、库名、协议名在标题里大小写正确与否本条判不出来。

- 正例：`## Strategic negotiations and global partnerships`
- 反例：`## Strategic Negotiations And Global Partnerships` 违反点：每个词首字母大写，连虚词 And 也大写了。

### EN-P-025 戏剧化碎片句

**判据。** 用戏剧化的碎片句制造节奏算违反：That's it. That's the whole thing.、X. And Y. And Z.、以及三个以上同形碎片连排（No aesthetic prior. No nostalgia for human taste.）。判据是这些碎片靠断句制造重量，写成完整句子之后意思不变。

**通过条件。** 一句短句可以强调，命中条件是连排。作者本人的片段句语感属于声口，按 ALL-PROT-017 保留，本条只针对批量出现的碎片。EN-P-025 是碎片句的检测侧规则，EN-PROT-001 禁止改写时把完整句子剁成碎片来变化句长，两条是同一现象的两端。EN-P-082 按否定结构判连串，与写成不写成碎片无关，两条判据不同。

**已知会漏掉什么。** "三个以上同形"这个可数判据只对形状一致的碎片有效，形状各异的连排碎片本条判不出来。段落收尾位置的碎片归 EN-P-048，那条数的是连续几段用同一种收尾形状。

- 正例：`AlphaEvolve did not favor symmetry or human-looking designs, which made some of the older assumptions less useful.`
- 反例：`It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.` 违反点：三个同形碎片连排，每个都摆出揭晓的姿态，没有一个补上具体内容。

### EN-P-032 问句小标题

**判据。** 长文的小标题用问句要改：What makes X unique?、Why is Y important?、How does Z work?。改成陈述句标题，把答案写进标题。

**通过条件。** FAQ 体裁的小标题就是问句，本条不适用。ZH-P-005 管中文正文里反复自问自答的节奏，与本条管标题层的分工不同。

**已知会漏掉什么。** 正文里的修辞设问归 EN-P-009，本条只管标题。判定"长文"没有词数门槛，短文里的问句小标题本条给不出结论。

- 正例：`## Cache invalidation checks the config hash on every request`
- 反例：`## How does cache invalidation work?` 违反点：小标题写成问句，把答案推给了正文，读者从目录上看不出这一节讲什么。

### EN-P-036 连字符的位置

**判据。** 复合修饰语在名词前用连字符连接（a high-quality result），跟在动词后作表语时去掉连字符（the results are high quality）。判据是位置，不是这个词组本身。常见的一批：third-party、cross-functional、client-facing、data-driven、decision-making、well-known、high-quality、real-time、long-term、end-to-end。

**通过条件。** 已确立的技术复合词在任何位置都保留连字符（machine-readable、server-side、open-access）。作状语或作名词用时去掉定语连字符（in real time、works out of the box），同一个复合词放在名词前时保留（real-time analytics）。目标发布格式的体例另有规定时按体例。

**已知会漏掉什么。** 三类同族问题本条不覆盖：本该分写的名词短语误加连字符（research-impact aggregator）、标准写法是一个词的闭合复合词被拆开（road-map、data-set）、以及拼写随方言和体例而变的模棱两可情形。密度问题归 EN-P-072：三个各自写对的修饰语堆在一起只命中那一条。

- 正例：`The cross-functional team delivered a high-quality, data-driven report. The team is cross functional, the report is high quality, and the methodology is data driven.`
- 反例：`The team is cross-functional, the report is high-quality, and the methodology is data-driven.` 违反点：三处复合词都在系动词之后作表语，此处不该保留连字符。

### EN-P-067 「假设不再为真」这类范畴错误

**判据。** 把适用性的退化说成真值翻转即命中（The assumption stops being true.）。假设不会从真变成假，变的是它还适不适用。写成 the assumption no longer holds 或 the assumption fails。判据是形式的：这个搭配说不通，不需要判断作者想说什么。

**通过条件。** 句子谈的确实是一个命题的真值时保留（the measurement was wrong, so the claim is false）。ALL-PROT-023 禁止改写翻转原文的情态与强度，本条允许把 stops being true 改成 no longer holds，因为两种写法表达同一个命题，改的是说不通的搭配不是命题强度。

**已知会漏掉什么。** 同族的范畴错误不在本条：把道德形容词安在不具能动性的名词上归 EN-P-061，本条只管假设与真值这一种搭配。stops being valid、becomes untrue 这类变体词形不同。

- 正例：`The assumption no longer holds once the clocks drift by more than a second.`
- 反例：`The assumption stops being true once the clocks drift.` 违反点：stops being true 把适用性的退化写成了真值的翻转，假设本身没有真值可翻。

### EN-P-070 项目符号的加粗小标题重复自己

**判据。** 项目符号列表里每项以一个重复自身的加粗小标题开头，这个小标题要去掉（`- **Performance:** Performance improved by 40%…`）。去掉小标题，直接把那句话写出来。

**通过条件。** 小标题与后面的内容不重复时保留。这些项如果确实需要小标题，说明它们本来就该是段落，这时的处理动作是改写成段落而不是删标题。EN-P-071 管的是列表标签后面的标点，本条管的是标签本身重不重复，一份列表可以只命中其中一条。EN-P-033 在小节标题层管复述，本条在列表项层管同一个动作。

**已知会漏掉什么。** "重复自身"要靠判断：`**Latency:** The p99 dropped…` 里 latency 与 p99 是同一件事的两种说法，形式上不重复，实质上重复，本条的可数判据抓不到这种。

- 正例：`- Performance improved by 40% after the index rebuild.`
- 反例：`- **Performance:** Performance improved by 40% after the index rebuild.` 违反点：加粗小标题与紧随其后的第一个词重复，去掉之后这一项完全成立。

### EN-P-071 列表标签用句点而不是冒号

**判据。** 项目符号以一个短标签开头、标签用句点结束、解释另起一句大写开头时命中（`- **Intros.** Years of conferences…`）。真人几乎总是用冒号（`- **Intros:** years of…`）。加粗形式是最强的形态，不加粗的同一形状（`- Intros. Years of…`）弱一些但仍算。修法有两条：把句点改成冒号并让解释小写开头，或者去掉标签、把这一点写成一句普通的话。

**通过条件。** 两条例外。那段标签本身是一个完整句子时句点是对的，不是引出解释的标签。不加粗的形式只在开头那截明显是标签时才标记：一到四个词的名词短语、没有动词；一句短的完整句子开头是可以的。本条决定列表标签后面用冒号还是句点，EN-P-011 决定冒号后面的内容用小写，先本条再那条。EN-P-070 管的是标签本身重不重复，本条管的是标签后面的标点。

**已知会漏掉什么。** 词数限制是误伤控制，因此五个词以上的真标签会漏。不同的出版体例对列表标点的规定不同，目标格式有自己的规范时以那份规范为准。

- 正例：`- **Intros:** years of conferences and operator network.`
- 反例：`- **Intros.** Years of conferences and operator network.` 违反点：加粗标签用句点结尾、解释另起一句大写开头，正是这条规则的最强形态。

### EN-P-072 连字符复合修饰语堆叠

**判据。** 一个名词前堆三个以上连字符复合修饰语算违反（a high-quality, well-architected, future-proof solution）。每个连字符本身可能都是对的，痕迹在密度。修法是只留下那个真正要紧的修饰语。

**通过条件。** 三个以下不命中。修饰语各自给出具体属性、堆在一起仍然可读时保留，判据是这些修饰语有没有说出可核对的东西。EN-P-036 判的是单个连字符该不该有，本条数的是一个名词前的密度；三个各自写对的修饰语堆在一起只命中本条。

**已知会漏掉什么。** 只数连字符复合修饰语，不带连字符的形容词堆叠（a fast, cheap, reliable solution）本条查不到，那是 ALL-P-005 的对称骨架问题。

- 正例：`The solution is well-architected.`
- 反例：`This is a high-quality, well-architected, future-proof solution.` 违反点：一个名词前堆了三个连字符复合修饰语，没有一个说出具体的属性。

### EN-P-080 短文里的结构过密

**判据。** 短文里用结构装出条理，两条可数阈值任一成立即命中：不到 300 词里超过三个标题；不到 200 词里有八个以上项目符号。修法有三条：合并小节、改用散文过渡、或者把这部分内容写成段落。

**通过条件。** 参考手册、API 文档、清单类文档的密集结构是这些体裁的正确形状，本条按词数算，判定前要先确认体裁。ALL-P-002 按小节内容逐个判断该不该加标题、该不该用列表，本条按全文词数与结构元素数的比例算，两条各管一层。

**已知会漏掉什么。** 阈值是按散文体裁定的，落到别的体裁上误报率高。两条阈值都不看结构的质量：三个标题各有实质内容的短文与三个空标题的短文得到同样的判定。

- 正例：一篇 280 词的说明只用一个标题。
- 反例：一篇 260 词的说明分成五个小节、五个标题。违反点：不到 300 词里超过三个标题，超过可数的阈值。

### EN-P-081 套路化的小节标题

**判据。** 小节标题用 Overview、Key Points、Summary、Conclusion、Introduction 这类通用词即命中。标题要告诉读者下面这一节具体讲什么。修法是把标题改成一句关于该节内容的具体说法（`## Why the retry budget ran out`）。

**通过条件。** 目标格式规定了固定的章节名时按格式（论文的 Introduction、变更日志的固定小节）。ZH-P-020 是本条在中文侧的对应规则，两条分立是因为 references 中英分表、正反例不能直译。EN-P-023 管的是正文里的总结复述句，本条管的是小节标题；处理动作不同，一个该删，一个该改写成具体说法。

**已知会漏掉什么。** 词表只有五条，同样空洞的标题（Background、Details、Notes、Other）不在其中。判定"具体"没有形式判据，一个稍具体但仍然通用的标题（Performance considerations）本条给不出结论。

- 正例：`## Why the retry budget ran out`
- 反例：`## Overview` 违反点：Overview 是词表里的一条，它没有告诉读者这一节讲什么。

## 十 标点、引号与不可见字符

### EN-P-026 英文破折号

**判据。** 英文破折号按全文词数分界。计入范围：em dash（—）与两个连字符（--）的替代写法，两种字形一并计入；标题、小标题与正文同样计入。200 词以下算短文，一处都不用。200 词以上按每千词至多一处折算，向下取整、至少允许一处：1000 词内至多一处，2000 到 2999 词至多两处，3000 词至多三处。不论篇幅，同一段里出现两处以上算成串，成串出现的和纯装饰性的一律去掉。

**通过条件。** 一种豁免不计入频率：项目符号或编号列表项里、跟在加粗引导词或 markdown 链接后面充当分隔符的破折号（`- **Term** — description`）。句中的插入用法照算。列表之外行首的 `**Bold lead** — 整句` 照算，那本身就是一处痕迹。两个连字符的写法永远不豁免。中文不适用本条的口径，中文走 ZH-P-007。EN-S-004 是禁令加作者样本例外，EN-S-009 是无条件禁令、不设任何频率口径，两条与本条冲突，取本条；样本例外单独立成 ALL-PROC-049。EN-PROC-001 定交付前的查法和时机，本条只定密度口径。EN-P-026 是频率上限，EN-PROT-001 规定改写时一处都不得新增，频率没超上限不构成新增的豁免。

**已知会漏掉什么。** 三个上游在破折号上给了三种互不相同的口径，本条取的是密度口径，因此它放过的那些用法在另外两种口径下都算违反。豁免只按形式判，一个写在列表项里但实际是句中插入的破折号会被误豁免。

- 正例：一篇 1500 词的文章正文里用了一处破折号，另有三处出现在 `- **Term** — description` 形式的列表项里。
- 反例：一篇 800 词的文章正文里用了三处破折号，其中一处是行首的 `**Bold lead** — full sentence`。违反点：折算约每千词 3.75 处，超过上限；行首加粗引导词后的那一处不在列表里，不适用豁免。

### EN-P-027 分号冒号密集是弱信号

**判据。** 分号和冒号在连续三句以上密集出现时，作为一个弱信号提示复查该段。这条只提示复查，不给出处理动作。

**通过条件。** 孤立出现不标记、不改写。复查之后那些分号和冒号各自正当时保留，本条不构成删除的依据。这个信号的置信度低，它的来源是社区报告而不是对照研究，按 ALL-M-024 不得当已验证事实转述。ZH-P-026 给中文侧同一现象加上处理动作，两条各管一种语言，触发门槛一致。

**已知会漏掉什么。** 连续三句这个门槛不区分分号与冒号的用途：列表引导、比例书写、时间格式里的冒号会一并计入。技术文档里冒号密度天然偏高，这条在那类文本上几乎必然触发。

- 正例：`The build failed; the log points at the linker. The fix took one flag.` 分号和冒号各出现一次，不标记。
- 反例：`The build failed; the linker ran out of memory. The fix: raise the limit. Two jobs still failed; both were on ARM. The pattern: every ARM runner has 4GB.` 违反点：连续四句里出现两处分号与两处冒号，达到复查门槛，该段需要重读一遍。

### EN-P-029 保留语堆叠

**判据。** 多层保留语叠在一起即命中：could potentially possibly、it might perhaps be argued、may eventually unlock、might ultimately transform。单独用哪一个都正当，叠起来才是痕迹。修法二选一：表态，或者只说出那一个真正不确定的点。触发词还包括 to be fair、it's also possible、in some cases it may、this is an inference。

**通过条件。** 原文支持且意义确实需要时留一个。只用来补救前面说过头的话的保留语要删掉。先按本条判是不是堆叠，再按 ALL-PROT-004 判剩下的那一个能不能删：ALL-PROT-004 保住其中真实表达不确定的那一个。

**已知会漏掉什么。** 括号里的保留式插注本条查不到（(and, increasingly, Z)、(or, more precisely, Y)），那类插注补了一层限定却不承担一句话的分量。堆叠没有可数的阈值，两层算不算堆叠要靠判断。

- 正例：`This might not scale past 10k users; I haven't tested it.`
- 反例：`It could potentially possibly be argued that this might perhaps not scale.` 违反点：could、potentially、possibly、be argued that、might、perhaps 六层保留语叠在一句里，句子最后什么都没主张。

### EN-P-030 与语气矛盾的保留语

**判据。** 同一句里保留语与绝对化表述并存时，删掉那个保留语（To some extent, this is arguably the best option, and it will definitely work.）。触发词：to some extent、in some ways、to a certain degree、arguably。判据是这个保留语的底气与句子实际的自信程度对不上。

**通过条件。** 原文真实表达的不确定不动。本条与 ALL-PROT-004 的边界写死在触发条件上：只有"同一句里保留语与绝对化表述并存"才归本条，分不清的归 ALL-PROT-004，按不删处理。两条一起划出保留语的边界：真实的犹疑保留，与绝对化表述并存的那一种删。EN-P-055 删的是以否定对偶表演坦诚的那一种，本条删的是与句子语气自相矛盾的那一种。

**已知会漏掉什么。** 保留语与绝对化表述跨句出现时本条查不到，触发条件限定在同一句内。成因是多轮编辑的积累，每一轮为上一轮的过头说法打一个补丁，因此这类矛盾在长期维护的文档里最多，而那类文档往往整段读才看得出来。

- 正例：`This approach solves the problem.`
- 反例：`To some extent, this approach is arguably the best option, and it will definitely solve the problem.` 违反点：To some extent 与 arguably 两处保留语，和后半句 will definitely 的绝对化表述在同一句里并存。

### EN-P-037 引号排版跟随原稿

**判据。** 引号排版跟随作者原稿：原稿用直引号就保持直引号，用弯引号就保持弯引号，不统一改成另一种。

**通过条件。** 本条只管原稿只用一种引号的情形。原稿混用时按 EN-P-044 的取值顺序处理，两条按原稿状态分域，不同时适用。弯引号单独出现不构成 AI 的证据：macOS、Word、Google Docs 和多数 CMS 默认会自动转成弯引号。ZH-P-025 管中文的直角引号与弯引号，两条各管一种语言，默认值的取法已经对齐。EN-PROC-002 保证执行时手上还有原稿的引号分布可以参照，本条给的是判定口径。

**已知会漏掉什么。** "原稿用哪一种"要在改写之前采样，改写开始之后原稿的分布已经被自己的输入法覆盖，这时本条无法执行。牛津逗号的刚性统一是同一类排版信号，本条不覆盖。

- 正例：原稿写 `He said "the project is on track" and left.`，改写稿保持这一对直引号。
- 反例：把同一句改写成 `He said “the project is on track” and left.` 违反点：原稿本来一致地使用直引号，改写把它统一成了另一种排版，而这个一致本身就是作者的选择。

### EN-P-042 隐藏字符要清除

**判据。** 清除四类隐藏字符：零宽空格（U+200B）、零宽连接符（U+200D）、软连字符（U+00AD）、密集的不换行空格（U+00A0，同一段里三处以上，或两个以上相邻即算密集）。另外清除冒充拉丁字母的西里尔或希腊字母。文本规范化为 NFC。

**通过条件。** 不换行空格在非密集情形下保留，排版上它有正当用途（数字与单位之间）。代码块里的一切按 ALL-PROT-008 不动，包括其中的不可见字符。本条的清理与 NFC 规范化按整篇跑是机械步骤，执行时按 ALL-PROT-040 只对改动过的段落跑。

**已知会漏掉什么。** 本条的方向是检测并清除，不是构造混淆。多语种文本里西里尔与希腊字母是正当内容，"冒充拉丁字母"这个判据要看上下文语言，混合语种的稿子上误报率高。

- 正例：`Set the timeout to 30 seconds.` 全句为 NFC，不含零宽字符，段内只有一处不换行空格。
- 反例：`Set the<U+200B>timeout to 30<U+00A0><U+00A0><U+00A0><U+00A0>seconds.` 违反点：单词之间插入了零宽空格，属于四类之一；四个相邻的不换行空格达到密集判据。

### EN-P-044 原稿引号混用时的取值顺序

**判据。** 英文原稿里直引号和弯引号混用时，双引号族和单引号（撇号）族各自独立取值、不绑在一起处理。每一族按这个顺序取一种并全篇统一：用户在本轮请求里指定的 > 目标发布格式要求的 > 该族在未受保护的原稿里占多数的一种 > 该族里第一次出现的那一种。某一族在原稿里没有证据时，那一族不动。同一族在一篇里出现两种样式即命中。

**通过条件。** 四项都判断不了时不动，在改动说明里点出混用。原稿的两族都只用一种时按 EN-P-037 沿用原稿，本条不适用：两条按原稿状态分域。ZH-P-025 是中文的同一套取值顺序，口径对齐：原文已经一致时那个一致就是作者的选择，兜底值只在没有任何信号时生效。EN-PROC-002 规定这一步在什么时候做、对哪些内容做。

**已知会漏掉什么。** "未受保护的原稿"要先排除引语、代码块和标题内的原文再统计，这一步做错会让多数决的结果偏向粘贴进来的内容。两族独立取值意味着一篇稿子里可能出现双引号是直的、撇号是弯的这种看起来不一致的结果，那是本条的预期结果而不是漏网。

- 正例：原稿里 `He said "on track"` 这样的直引号 12 处、`He said “on track”` 这样的弯引号 2 处，撇号全部写成 `don’t`：双引号按多数统一成直引号，撇号保持弯的。
- 反例：同一份原稿，改写稿把双引号和撇号一起写成 `He said “on track”` 与 `don’t`。违反点：把两族绑在一起处理，且撇号那一族按另一族的多数改了。

## 十一 语域、体裁形态与技术例外

### EN-P-028 聊天残留

**判据。** 三类聊天残留一律删掉。助手式寒暄：I hope this helps、Of course!、Certainly!、Would you like me to、Let me know if、Here is a。谄媚：Great question!、That's an excellent point!、Absolutely!、You're absolutely right!。知识截止免责声明：As of my last training update、based on available information、while specific details are limited、I don't have access to real-time data。

**通过条件。** 知识截止免责声明只有两条出口：去把这个信息查出来，或者删掉这句保留语，不得发表一句承认作者没去查过的话。原文没有这项信息时写明"原文没有给出"，那是一句关于原文的事实，不是免责声明。ZH-P-022 管中文对话模型自己会说的那一组，两条各管一种语言。本条删的是知识截止免责声明本身，EN-P-045 删的是接在后面的猜测，两条常常同时命中同一段。

**已知会漏掉什么。** 元叙述式开场（In this article, we will explore…、Let's dive in!）来源相同但形状不同，归 EN-P-007 和 EN-P-050。Feel free to reach out、Let me know if you need anything else 这类结语在词表里只有近似形式。

- 正例：`The French Revolution began in 1789. The exact founding date of the company is not in the sources provided.`
- 反例：`Great question! Here is an overview of the French Revolution. As of my last training update, specific details are limited. I hope this helps!` 违反点：Great question! 是谄媚，Here is a 与 I hope this helps! 是助手式寒暄，As of my last training update 与 specific details are limited 是知识截止免责声明，四句里没有一句有正文对象。

### EN-P-035 文档不写改动史

**判据。** 文档描述现状，叙述改动过程算违反：was added to、now uses、has been updated to、replaces the old、previously。直接写这个东西现在是什么样。没有提交历史的读者拿到一段改动叙述，得到的是考古报告而不是文档。

**通过条件。** 以版本为范围的文档里叙述改动是正确的：变更日志、发布说明、迁移指南、决策记录。历史确实要紧时写进变更日志或提交信息，不写进接口文档。

**已知会漏掉什么。** 判定要知道这份文档属于哪一类，同一段话在 API 文档里是命中、在迁移指南里是正确内容，本条给不出形式判据。词表之外的形式漏掉：used to、in the old version、before this change。

- 正例：`This function uses a hash map for O(1) lookups, avoiding the O(n²) cost of naive iteration.`
- 反例：一份 API 文档里写 `This function was added to replace the previous approach of iterating through all items.` 违反点：文档在叙述一次改动，没有提交历史的读者读不懂 previous approach 指什么。

### EN-P-040 语域与质量突变

**判据。** 同一篇文字里出现语域或质量的突然断裂要标出来：正式书面段落紧接口语错字段落，语法无懈可击的一段后面跟着有基础拼写错误的一句，拼写风格中途从美式切到英式。这提示这段文字是拼接的。

**通过条件。** 处理方向是单向的：按作者主体部分的声口统一，不得反过来把作者的口语段落改成书面语。引语、他人贡献的段落、粘贴进来的日志按 ALL-PROT-008 不动，这些位置的语域差异是正当的。EN-P-040 管的是识别原文里已有的语域断裂并据此判断这段是拼接的，ALL-P-012 管的是改写方自己不得造成语域跳跃，两条是同一现象的检测面和产出面。

**已知会漏掉什么。** "主体部分的声口"要靠采样判断，一篇里 AI 段落占多数时，按多数统一会统一到错误的一边。合著稿件、引用大段他人文字的稿件会被误命中，那类语域差异是来源差异不是拼接痕迹。

- 正例：`yeah so the bug is in line 42. the loop allocates on every iteration instead of reusing the buffer.`（全篇统一的随意口吻）
- 反例：`yeah so the bug is in line 42 lol. The aforementioned implementation exhibits suboptimal performance characteristics.` 违反点：前一句是随意口语，后一句突然切换成正式书面语，两句之间没有任何过渡。

### EN-P-048 段落收尾形状雷同

**判据。** 同一篇里连续三段以上用同一种收尾形状算违反：都以一句短促的独立单句收尾、都以一句判断收尾、都以一个数字收尾。改掉其中至少一段。

**通过条件。** 三段以下不命中。收尾形状相同但内容各自承担了不同工作时，改一段即可，不必全改。ZH-P-013 是同一条判据的中文版，判据和阈值一致，本条管英文。ALL-P-001 管句长和段落开头，本条管段落收尾，两条合起来覆盖节奏的三个位置。

**已知会漏掉什么。** "同一种收尾形状"没有穷举，三段各以一句反问收尾也是同一种形状，本条给的三个例子不包括它。间隔出现的雷同（第一、三、五段同形）不满足"连续"，本条查不到。

- 正例：一段收在 `The p99 dropped from 400ms to 90ms after the index rebuild.`，下一段收在 `Nobody has reproduced it on Linux.`，第三段收在 `What happens above 4GB is still open.` 三段的收尾形状各不相同。
- 反例：连续三段分别以 `That's the whole trick.`、`It just works.`、`Nothing else changed.` 收尾。违反点：三段都用同一种收尾形状，一句短促的独立单句。

### EN-P-049 陈述事实前的铺垫层

**判据。** 陈述一个事实之前加铺垫层要删，三类：缓和语（may, in some cases）、预先辩解（It's worth noting that、this is expected behavior）、手把手安抚（there's no need to worry、let's walk through this together）。直接把事实说出来。

**通过条件。** 限定这个命题成立范围的保留语不在本条范围内，按 ALL-PROT-004 保留：本条只删陈述事实之前的铺垫层，限定原命题成立范围的保留语不得当铺垫删掉。两者的区别在于删掉之后命题的适用范围变不变。ZH-P-014 是同一条判据的中文版，本条管英文。

**已知会漏掉什么。** 缓和语与命题限定语在词形上分不开：同一个 in some cases，限定了适用范围就该留，只是软化语气就该删，判定要读出这句话主张的范围。it's worth noting 同时在 EN-P-004 的词表里，两条会重复命中同一处。

- 正例：`The migration will drop 40 rows that have no matching parent.`
- 反例：`It's worth noting that the migration may, in some cases, drop a small number of rows. This is expected behavior, and there's no need to worry.` 违反点：It's worth noting that 是预先辩解，may, in some cases 在这里没有限定任何范围、只是软化语气，there's no need to worry 是手把手安抚，三层铺垫叠在一个事实前面。

### EN-P-056 话题标签堆砌

**判据。** 一条短社交帖尾部带六个以上话题标签即命中，改成最多留两到三个具体标签或一个都不留。判据是这个标签帮不帮得上读者找到相关内容，帮不上就是填充。计数前先减掉不是标签的 `#`：issue 与 PR 编号（`#88`、`owner/repo#88`）、含数字的六位与八位十六进制色值、C 预处理指令（`#include`）、URL 片段、Markdown 标题，以及行内代码和代码块里的一切。形状像十六进制的短词（`#fff`、`#decade`）和频道名（`#general`）仍然计数，把它们和标签分开需要猜作者的意图。

**通过条件。** 五个标签在社交帖与商务邮件两档上值得复看一眼，但不构成命中。长文档位上按 ALL-G-008 放宽触发门槛，判据不变。ALL-PROC-016 规定代码块与引用块不计入任何模式命中，本条的计数口径把同一原则细化到单个 `#` 字符。

**已知会漏掉什么。** 六这个阈值是按两类错误的代价定的，不是口味主张：它是误伤真人的概率开始低于漏掉机器输出的那个点，因此真人的发布帖（本来就带十个标签）会被命中。计数口径在拿不准的地方选择多数一个，短十六进制词和频道名因此会被计入。

- 正例：`Shipped the retry-budget fix today. Write-up tomorrow. #distributedsystems`
- 反例：一条社交帖结尾接了 `#AI #Crypto #Web3 #Innovation #FutureTech #Technology` 六个标签。违反点：数量到了六个的阈值，且全是宽泛的类别标签，对读者找到相关内容没有帮助。

### EN-P-061 道德形容词安在不具能动性的名词上

**判据。** honest、genuine、faithful、truthful 这类道德或品格形容词修饰 shape、number、representation、accuracy、curve、output 这类不具能动性的技术名词即命中，这是范畴错误。副词形式同样算（described honestly、flagged honestly），被动式还顺带隐去了那个本该具备诚实与否的主体。修法分两种：把道德属性换成具体属性（an honest shape → a more realistic curve），被动结构里的道德副词整个删掉（flagged honestly → noted）。

**通过条件。** 形容词修饰的是人或组织时保留，那不是范畴错误（an honest reviewer）。让证据本身承担诚实这个含义是修法的方向，不是删掉一切与诚实有关的说法。ALL-P-004 管的是抽象事物做只有人能做的动作，本条管的是道德形容词与副词安在不具能动性的名词上，两条各管一半。

**已知会漏掉什么。** 形容词与名词两份清单都是封闭的，honest error bars、truthful visualization 一类的搭配不在其中。判定名词有没有能动性在边界上要靠判断：the report、the model 这类词既可以指文档也可以指作者的工作。

- 正例：`The chart's axis starts at zero, so the difference is not exaggerated.`
- 反例：`The chart has an honest shape, and the outliers were flagged honestly.` 违反点：honest 修饰 shape 是范畴错误，形状不是能诚实与否的东西；flagged honestly 是同一个动作的副词形式，被动式里没有那个能诚实的主体。

### EN-P-068 用改称呼冒充解释

**判据。** 一段里反复出现不加解释的重新命名时命中：the concern turns into panic、a feature turns into a strategy、the risk becomes real。句子说了一个东西变成另一个东西，却没有说出变化的动作、阈值或后果。判定前要先读完这一段。

**通过条件。** 三类不命中：字面意义的转化（water turns into ice）、有支撑的比喻、以及在这一段任何地方解释过的变化。对已解释变化的有意概括也通过，一段里出现多次也通过；只有不带解释的重复改称呼才命中。命中之后向作者问清变化的是什么、用他给的事实改写，绝不自己编一个机制或行动者；缺那个机制时按 ALL-PROC-047 处理，向用户要，或者改写成一句不需要它的说法。ZH-P-030 是本条在中文侧的对应规则，判据一致，两条分立是因为 references 中英分表、正反例不能直译。

**已知会漏掉什么。** 本条需要读上下文才能判定，按 ALL-M-023 在报告里要与出处相关的命中分开列。它是清晰度判断，不是机器写作的证据。孤立一处的改称呼不命中，而一处也足以掩盖一个缺失的机制。

- 正例：`The queue hit its 500-message cap at 14:02, so the queue turns into a bottleneck for everything behind it.`
- 反例：`The concern turns into panic. The feature turns into a strategy. The risk becomes real.` 违反点：一段里三处重新命名，没有一处说出变化的动作、阈值或后果。

### EN-P-075 被安上去的随意语域

**判据。** 写小写随意社交声口时端出一整套道具即命中，六类共用一条判据：戏被外包给了道具而不是由内容承担。六类是一个词的判决式收尾（wild. / insane. / unhinged.）、舞台指示（*checks notes*、*chef's kiss*、*mic drop*）、挤眉弄眼的插注（(yes, really)、(no, seriously)）、标签式开场（hot take、fun fact、pro tip、PSA、unpopular opinion，带不带冒号都算）、because of course it does、自问自答的连打（Is it fast? Yes. Is it cheap? Also yes.）。修法是删掉道具、把那件事说出来。

**通过条件。** 作者本来的声口就建立在这些道具上时保留，按 ALL-PROT-017 那属于声口。本条针对的是被安上去的随意，不是禁止俏皮。判定优先看 ALL-PROC-048 记下的写作样本，样本里有这套道具就说明它是作者的。ALL-PROC-018 管的是改写时不得硬注入个性，本条管的是输入文本里已经有这套道具时怎么判。

**已知会漏掉什么。** 这套道具与真实的随意声口最接近，一条帖子可以通过所有词表检查而仍然穿着这身行头。六类里只有星号舞台指示和括号插注做得成形式匹配，判决式收尾、标签式开场、自问自答、because of course it does 四类与普通抱怨同形，只能靠判断。

- 正例：`The build finished in 40 seconds, down from six minutes.`
- 反例：`hot take: the new build is fast. *chef's kiss* (yes, really). wild.` 违反点：hot take:、*chef's kiss*、(yes, really)、wild. 分属四类道具，一条短帖里全部戏剧效果都由道具承担。

### EN-P-079 对话式回复里一处换行都没有

**判据。** 对话式回复语域里（issue 与 PR 评论、聊天、私信、随意邮件）三个条件同时成立即命中：一段回复长度的文字（大约 150 词以内）、四句以上、通篇没有一处换行。真人在想法的边界处断开，一个意思断一行。修法是按想法的边界断开。

**通过条件。** 正式的长文语域里一整段密集文字是正确形状：博客开头、文档段落、有意写紧的一段邮件。本条不适用于那些位置，不得因为一段长文没有内部换行就标记它。ALL-P-001 管的是长文里的段落长度与句长变化，本条只在对话式回复语域生效，两条不同时适用。

**已知会漏掉什么。** 语域限定没法交给自动判定：一条普通的 issue 评论会被档位判定归成长文档位，因此这条只能靠人判语域。结构检测器正是因为这类误报被撤掉过。150 词与四句这两个数是经验值，超过 150 词的密集回复本条查不到。

- 正例：一条 PR 评论写成三个短段，每段一个意思，段与段之间有换行。
- 反例：一条 issue 评论从头到尾写成一整块：`I looked at this. The retry budget is per-process, so each worker gets its own. That means the total is eight times what the config says. The fix is to move the counter into Redis. Let me know if you want me to open a PR.` 违反点：这条回复在 150 词以内、五句、没有一处换行，三个条件同时满足，且语域是对话式回复。

### EN-P-084 技术语境下的词表例外清单

**判据。** 判定为技术长文档位时，下面这些词在技术语境里有正当的技术含义，不按词表命中处理：robust、comprehensive、seamless、ecosystem、leverage（讨论真实的平台杠杆或接口时）、facilitate、underpin、streamline。同一档位下仍然要处理的：delve、tapestry、beacon、embark、testament to、game-changer、harness。放行的依据是这个词在当前句子里承担的是技术含义，不是这篇文章属于技术体裁。

**通过条件。** 本条只在技术长文档位下查，档位定位见 ALL-G-007。ALL-PROT-009 给的是三类例外的原则，本条给的是技术语境下具体哪些词放行、哪些仍要标；放行依据是词在当前句子里的语义，不是文章的体裁。ALL-PROC-056 规定语境里明显正确的词表命中要保留，本条把这个判断在技术档位上落成一份可以逐条核的清单。

**已知会漏掉什么。** 两份清单都是封闭的，技术语境里同样正当的其他词（orchestrate、provision、instrument）不在放行清单上，仍会按 EN-P-001 命中。放行清单也不区分同一个词的两种用法：一篇技术文章里 seamless integration 指的是接口无缝时放行，指的是体验美好时该标，本条给不出这个区分的形式判据。

- 正例：一篇技术博客里的 `a robust retry policy` 不标记，同一篇里的 `delve into the internals` 照标。
- 反例：一篇技术博客里把 `robust retry policy` 按 EN-P-001 的词表改掉。违反点：robust 在技术长文档位是本条明确列出的放行词，这里的 robust 承担的是技术含义。
