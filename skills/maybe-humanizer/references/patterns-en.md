# 英文模式表

只管英文文本。中文见 patterns-zh.md，两种语言都适用的见 patterns-common.md。全部让位于 protection.md：引语、代码、标题内的原文不动（ALL-PROT-008），精确术语的重复不动（ALL-PROT-009）。

## 词与短语

### EN-P-001 AI 高频词一律不用

delve、leverage、utilize、facilitate、foster、empower、streamline、multifaceted、tapestry、testament、underscore、interplay、realm、beacon、pivotal、crucial、paramount、meticulous、intricate、transformative、elevate、embark、supercharge、harness、garner、bolster、ever-evolving、paradigm shift、game changer。换成大白话。执行强度见 EN-M-001。

- 正例："This update makes review faster."
- 反例："This update will supercharge your workflow and foster a truly transformative shift." 违反点：supercharge、foster、transformative 三个词表内的词。

### EN-P-002 宣传册式形容词

nestled、in the heart of、vibrant、breathtaking、must-visit、cutting-edge、seamless、robust、world-class、state-of-the-art、renowned、比喻义的 rich。换成具体是什么让它值得一提。

- 正例："A town in the Gonder region, known for its weekly market and an 18th-century church."
- 反例："Nestled within the breathtaking region of Gonder, a vibrant town with rich cultural heritage." 违反点：四个宣传语形容词占了本该是事实的位置。

### EN-P-003 空洞副词

just、literally、honestly、simply、actually、truly、fundamentally、importantly、crucially、inherently、inevitably。这些词不承担强调、不确定、对比或作者语感时删掉，承担时保留。

- 正例："I actually think this will work."（actually 承担了带意外的强调，留）
- 反例："This is just a simple bug fix that we simply need to ship." 违反点：just 和两个 simply 都不承担任何功能。

### EN-P-004 空洞短语与冗余连接词

it's worth noting、it's important to note、at the end of the day、when it comes to、at its core、in today's world、in the age of、the reality is、the truth is、in terms of、with regard to、in order to、due to the fact that、at this point in time、going forward、in connection with、associated with。

删还是缩，按短语本身有没有承载逻辑关系分：整体不承载信息的删掉（it's worth noting、at the end of the day、in today's world）；承载了真实的因果、条件、转折或时间关系的，缩短成表达这个关系的最短说法，不整段删（due to the fact that 写成 because，in order to 写成 to，at this point in time 写成 now 或直接给日期）。关系本身一律保留（ALL-PROT-020）。

- 正例："We upgraded the server to handle more traffic."
- 反例："Due to the fact that we needed to handle more traffic, and in connection with our scaling plans, we upgraded the server at this point in time." 违反点：三个冗余连接词，删掉意思不变。

### EN-P-005 官僚式正式语域

it should be noted that、it is essential to、in the context of、the implementation of、prior to，以及名词化堆叠。在读者期待大白话的场合降到该有的语域。受 ALL-M-002 约束：正式语域本身不是证据。

- 正例："Set the timeout to 30 seconds."
- 反例："It should be noted that it is essential to configure the implementation of the timeout parameter." 违反点：三个官僚式短语，一句话说得清的事绕了一圈。

### EN-P-015 不回避系动词

serves as、stands as、marks、represents、boasts、features、offers。能换成 is / are / has / was 就换。

- 正例："Gallery 825 is the exhibition space."
- 反例："Gallery 825 serves as the exhibition space." 违反点：serves as 可以直接换成 is。

### EN-P-016 让动词做事

made a decision 写成 decided，conducted an analysis 写成 analyzed。

- 正例："The team decided on Tuesday."
- 反例："The team made a decision on Tuesday." 违反点：made a decision 里现成有一个 decide。

### EN-P-019 同义词轮换

指代同一件事时，一个清楚的词够用就重复用它。例外见 ALL-PROT-009。

- 正例："The agent reviews the draft, scores it, and suggests fixes."
- 反例："The agent reviews the draft. The assistant scores the piece. The tool suggests fixes." 违反点：agent、assistant、tool 指同一个东西。

### EN-P-020 名词短语轮换

不给同一个实体换整个名词短语。这类替换往往还会带进原文没有的评价，一并触发 ALL-PROT-001。

- 正例："Yankilevsky and other non-conformist artists faced obstacles. His work continued."
- 反例："Yankilevsky, alongside other non-conformist artists, faced obstacles. The visionary creator's distinctive journey continued." 违反点：the visionary creator 既是换称，也加了原文没有的评价。

### EN-P-021 假范围

from X to Y：X 和 Y 不在同一个维度上时不构成跨度，直接列出具体的项。

- 正例："the plan covers three cities: Austin, Denver, and Raleigh"
- 反例："the plan ranges from grassroots outreach to enterprise partnerships" 违反点：两端不是同一个量的两头。

## 句式与铺垫

### EN-P-006 二元对比与否定式排比

It's not X, it's Y；not only X but Y；The question isn't X. It's Y.；Not a X. Not a Y. A Z. 这些句式一律改成直接陈述结论。

- 正例："The eval matters more than the model."
- 反例："The question isn't the model. It's the eval." 违反点：先否定一个没人提出过的选项再给答案。

### EN-P-007 清嗓子式开场

Here's the thing、Let me be clear、I'll be honest、The uncomfortable truth is、in this article we will explore、this comprehensive guide、let's dive in、let me walk you through、here's what you need to know、There are several ways to、In general, it is a good idea to。开头如果是能带出语境、张力或人物的个人化插叙，保留。

- 正例："Add an index on user_id. That one change took the query from 900ms to 12ms."
- 反例："There are several ways to speed up a slow query. In general, it is a good idea to consider indexing." 违反点：两处空转，具体答案被推到后面。

### EN-P-008 故作洞见的铺垫

The part everyone misses、what most people get wrong、nobody tells you this、here's what they don't say。

- 正例："Distribution is the moat."
- 反例："The part everyone misses: distribution is the real moat." 违反点：把作者包装成孤独的行家来给论断加分。

### EN-P-009 假戏剧停顿与修辞性设问

The catch?、The kicker?、The brutal truth?、Sound familiar?、What if I told you、Think about it，以及自问自答式的“问题？答案。”

- 正例："Most people abandon goals in week three. The ones who don't make the failure threshold explicit before they start."
- 反例："Most people abandon goals in week three. The brutal truth? They lack a clear failure threshold." 违反点：The brutal truth? 不在问任何东西。

### EN-P-010 冒号式揭晓

不用“名词短语＋冒号＋小写的戏剧化揭晓”制造悬念。冒号只用于列表、标签和引语。

- 正例："A separate agent does the grading, which is what makes it work."
- 反例："The detail that makes it work: a separate agent grades it." 违反点：冒号在制造悬念，不在引出列表。

### EN-P-025 戏剧化碎片句

That's it. That's the whole thing.、X. And Y. And Z. 这类碎片写成完整句子。作者本人的片段句语感要保留（ALL-PROT-017），这条针对的是批量出现的碎片。

- 正例："That is the whole mechanism, and it fits in twenty lines."
- 反例："That's it. That's the whole thing." 违反点：两句碎片只承担节奏，不承担信息。

### EN-P-031 挑战小节套路

Despite [好的一面]，[模糊的问题]。Despite these, [空话]。写清具体问题（带时间和数据），或者删掉整段——原文没有具体问题时删段，不是编一个。

- 正例："Traffic worsened after 2015 when three IT parks opened. A stormwater project started in 2022."
- 反例："Despite its prosperity, the city faces challenges typical of urban areas. Despite these challenges, it continues to thrive." 违反点：两次 Despite，问题和结论都是空话。

### EN-P-041 假想反方

While some might argue、It would be easy to dismiss this as、One might object that... but。只回应原文里真实存在、点名的反对意见。

- 正例："Remote work hasn't hurt our collaboration. Our incident response time improved after we went remote."
- 反例："While some might argue that remote work hurts collaboration, the data tells a different story." 违反点：这个反对意见原文里没有出处。

## 评价与归因

### EN-P-013 假装分析的分词从句

highlighting、underscoring、emphasizing、reflecting、symbolizing、showcasing、ensuring、fostering。把从句里真正的信息提升成一句有出处的独立句子，没有信息就整句删。

- 正例："The launch adds file search, so users can find old drafts without leaving the editor."
- 反例："The launch adds file search, highlighting the team's commitment to better workflows." 违反点：highlighting 从句说不出任何原文没说过的事实。

### EN-P-014 意义拔高与重要性吹捧

stands as、serves as a testament、marks a pivotal moment、plays a vital role、solidifies its position、underscores its significance、represents、symbolizes、speaks to、embodies、reflects broader。删掉评论，留下事实（事实要具体，见 ALL-PROT-002）。

- 正例："The factory closed in 2009. Three hundred jobs. The town's high school dropped football the following year."
- 反例："The closed factory represents the decline of American manufacturing and speaks to broader anxieties about post-industrial identity." 违反点：represents、speaks to broader 把一个具体事件解读成了象征。

### EN-P-017 模糊归因

experts agree、research suggests、studies show、observers have cited、several sources、it is widely believed、industry reports、many argue。点名具体来源或删掉整个论断。用户给不出来源时按 ALL-PROT-001 去问。

- 正例："A 2019 Chinese Academy of Sciences survey found 12 endemic fish species."
- 反例："Experts believe it plays a crucial role in the regional ecosystem." 违反点：Experts believe 指不到任何具体的人或研究。

### EN-P-018 来源清单当内容

featured in X, Y, Z、profiled in、cited in、independent coverage、active social media presence。挑一个来源说清它具体报道了什么，或者删掉。

- 正例："Wired profiled her 2024 research on algorithmic bias in hiring software."
- 反例："Her insights have been featured in Wired, Refinery29, and other prominent media outlets." 违反点：只列名字，没说任何一家报道了什么。

### EN-P-022 解读性旁白

That last part matters more than it sounds、The key point is、As you can see、This distinction matters、多余的 In other words。让事实自己承担重点。删掉后读者仍读不出重点的，补正文里已有的支撑事实，不补新事实。

- 正例："The feature cut review from two weeks to two days."
- 反例："The feature cut review from two weeks to two days. This distinction matters more than it sounds." 违反点：后一句跳出内容去指导读者。

### EN-P-039 疑似捏造的痕迹

精确到小数位却无法核实的统计数字、归到查不到的来源的引用、对冷门事实的自信断言且没有出处，这三种都标出来写进“需作者确认”，不自行删除，也不自行改写（ALL-PROT-014、ALL-PROT-015）。

- 正例：把 "According to a 2019 internal Gartner memo, 73.4% of enterprises had adopted this by Q2." 原样保留，在需作者确认里问这份 memo 是否可查。
- 反例：直接把这句删掉，或改成“许多企业已经采用”。违反点：删掉了原文的事实，或替作者改了结论。

## 收尾

### EN-P-023 结尾不做总结和展望

删掉空洞乐观（the future looks bright、exciting times lie ahead、poised for growth、a step in the right direction）、总结复述（In summary、To sum up、Overall）和 Whether you prefer X or Y 式的收束。停在最后一个具体的事实、收获或下一步上。

- 正例："Tokyo's best ramen counter doesn't have a phone, doesn't take reservations, and hasn't changed the broth recipe since 1987."
- 反例："Whether you prefer fine dining or street food, Tokyo has something for every palate." 违反点：整句没有一条具体信息。

### EN-P-024 故作深刻的金句

X is the new Y、the currency of、not a X but a Y、X is where Y meets Z。删掉，不要改写成一个更好的隐喻，也不要为了保留节奏而留着；用稿子里已有的最具体的一句收尾。

- 正例："Ad networks pay about $8 per thousand views, so publishers chase pageviews."
- 反例："Data is the new oil, and attention is the currency of the modern web." 违反点：两个格言模板叠加，没有一句具体论点。换成另一个更精致的隐喻同样违反。

## 保留语

### EN-P-029 保留语堆叠

could potentially possibly、it might perhaps be argued：要么表态，要么只说出那一个真正不确定的点。删到只剩一层，不得删成确定（ALL-PROT-004）。

- 正例："This might not scale past 10k users; I haven't tested it."
- 反例："It could potentially possibly be argued that this might perhaps not scale." 违反点：一个从句里四个表示不确定的词。

### EN-P-030 与语气矛盾的保留语

只删同一句里保留语与绝对化表述并存的那一种：to some extent、in some ways、arguably 后面接 definitely、will、always。原文真实表达的不确定不动。

- 正例："This approach solves the problem."
- 反例："To some extent, this approach is arguably the best option, and it will definitely solve the problem." 违反点：to some extent、arguably 与 will definitely 自相矛盾，保留语在这里没有承担犹疑。

## 标题与排版

### EN-P-011 冒号后用小写

冒号后面的内容用小写，除非语法要求、专有名词、标题或代码另有规定。

- 正例："The launch adds one thing: faster search."
- 反例："The launch adds one thing: Faster search." 违反点：Faster 没有理由大写。

### EN-P-012 标题用句子大小写

只有句首和专有名词大写，不用 Title Case。目标平台或出版方的样式指南另有规定时按指南。

- 正例："Strategic negotiations and global partnerships"
- 反例："Strategic Negotiations And Global Partnerships" 违反点：每个实词首字母都大写。

### EN-P-026 英文破折号

按全文词数分界：200 词以下算短文，一处都不用；200 词以上算长文，确实比逗号、句号或括号更合适时至多留一到两处。不论篇幅，同一段里出现两处以上算成串，成串出现的和纯装饰性的一律去掉。中文不受这条约束，走 ZH-P-007。

真人原文里的破折号另说：孤立一处不算证据（ALL-M-002），属于作者语感的按 ALL-PROT-017 保留，按 ALL-PROC-023 第 3 级压第 4 级，不因短文口径删掉。这条针对的是待清理的 AI 痕迹。

- 正例："The fix was simple: cache the response."
- 反例：一段 120 词的短文里连续三处破折号制造停顿。违反点：不到 200 词，短文里本该零个，且同段三处已成串。

### EN-P-027 分号冒号密集是弱信号

分号和冒号在连续三句以上密集出现时，提示复查该段；孤立出现不标记、不改写。这是一个提示，不单独触发改写。

- 正例：一段里各出现一次分号和冒号，不标记。
- 反例：把一处孤立的分号当成 AI 痕迹改掉。违反点：不满足聚类条件（ALL-M-002）。

### EN-P-032 问句小标题

长文的小标题不用问句，改成陈述句。常见问答体（FAQ）例外。

- 正例："Cache invalidation checks the config hash on every request"
- 反例："What Makes This Approach Unique?" 违反点：非问答体长文里用问句作小标题。

### EN-P-033 标题后的复述句

标题后面不跟一句只是复述标题的话，也不写 This section covers X。

- 正例："## Performance / The dashboard renders 10,000 rows in 40ms because it virtualizes the list."
- 反例："## Performance / Performance is important for a good user experience." 违反点：这句相对标题没有多说任何事。

### EN-P-036 连字符的位置

复合修饰语在名词前用连字符（a high-quality result），跟在动词后作表语时去掉（the results are high quality）。

- 正例："The results are high quality and the pipeline is genuinely new."
- 反例："The results are high-quality and the pipeline is state-of-the-art." 违反点：high-quality 作表语时不该带连字符。

### EN-P-037 引号排版跟随原稿

原稿用直引号就保持直引号，用弯引号就保持弯引号，不统一改成另一种。不据引号风格推断这段是哪个模型写的。

- 正例：全文保持作者原来的直引号。
- 反例：把作者原稿里的直引号统一换成弯引号。违反点：改了作者的排版习惯。

## 生成残留与拼接痕迹

### EN-P-028 聊天残留

助手式寒暄（I hope this helps、Of course!、Certainly!、Would you like me to、Let me know if、Here is a）、谄媚（Great question!、That's an excellent point!、Absolutely!）、知识截止免责声明（As of my last training update、based on available information、while specific details are limited）。

- 正例："The library's latest release is 4.2, published in March."
- 反例："Great question! As of my last training update, while specific details are limited, the version may have changed. I hope this helps!" 违反点：三类残留各一处，全句没有实质内容。

### EN-P-038 生成过程残留

未填写的占位符（[Your Name]、[INSERT SOURCE URL]、2025-XX-XX）、工具内部引用标记（citeturn0search0、contentReference、[cite: 1]、grok_card、oai_citation）、AI 来源的 UTM 参数（utm_source=chatgpt.com、referrer=grok.com）、推理链脚手架（Let me think、Step 1:、Breaking this down、First, I'll）。不知道占位符该填什么时按 ALL-PROC-004 去问。

- 正例："Ops engineers hit this endpoint about 400 times a day. That is who we are designing for."
- 反例："Let me break this down. Step 1: identify who hits this endpoint. Dear [Recipient], see https://example.com/a?utm_source=chatgpt.com" 违反点：脚手架、占位符、UTM 参数三处残留。

### EN-P-040 语域与质量突变

同一篇里出现语域或质量的突然断裂（正式书面段落紧接口语错字段落，拼写风格中途从美式切到英式），提示这段是拼接的。按作者主体部分的声口统一，不得反过来把作者的口语段落改成书面语（ALL-PROT-017）。受 ALL-M-002 约束：单处不一致不算，要成段出现。

- 正例："yeah so the bug is in line 42. The loop allocates on every iteration instead of reusing the buffer."
- 反例："yeah so the bug is in line 42 lol. The aforementioned implementation exhibits suboptimal performance characteristics." 违反点：后半句突然切成正式书面语，与前半句断裂。

### EN-P-042 隐藏字符要清除

零宽空格（U+200B）、零宽连接符（U+200D）、软连字符（U+00AD）、密集的不换行空格（U+00A0），以及冒充拉丁字母的西里尔或希腊字母。文本规范化为 NFC。不换行空格算“密集”的阈值：同一段里三处以上，或两个以上相邻；排版需要的单个不换行空格不动。

- 正例：交付前扫一遍字符表，确认只剩正常的可见字符和空格。
- 反例：字母之间夹着零宽空格的文本原样交付。违反点：隐藏字符会让搜索、比对和拼写检查失效。

## 文档体裁

### EN-P-035 文档不写改动史

参考文档、README、接口说明描述现状，不叙述改动过程：was added to、now uses、has been updated to、replaces the old、previously。变更日志、发布说明、事故复盘不适用这条——那些体裁本来就该叙述改动。

- 正例："This function fetches the user and returns a promise."
- 反例（在 README 里）："This function was refactored to replace the old callback approach with async/await." 违反点：README 的职责是描述现状。

## 词表执行强度

### EN-M-001 英文 AI 词的三档处理

- 第一档，出现一次就改：delve、tapestry、testament、multifaceted、realm、interplay、in today's landscape。
- 第二档，同一段出现两次以上才改：crucial、pivotal、vibrant、robust、foster、enhance、showcase、notably、moreover、furthermore、garner、bolster、utilize、underscore、it's worth noting。
- 第三档，单独出现不动，只有与前两档聚在一起时才一并处理：key、important、significant、various、effective、valuable、powerful、essential。

- 正例：一段里只出现一次 significant，周围没有第一、第二档的词，不动。
- 反例：仅凭一次 significant 就把整段判定为 AI 写的并重写。违反点：第三档的词单独出现不构成信号（ALL-M-002）。
