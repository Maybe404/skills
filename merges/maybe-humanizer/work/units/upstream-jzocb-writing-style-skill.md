# 来源摘要

- 来源 id：upstream-jzocb-writing-style-skill
- 仓库：jzOcb/writing-style-skill，分支 main
- 抓取文件（临时抓取到 scratchpad，未落入仓库）：
  - SKILL.md（commit d94826e1cd48f5403b82a5a909efdfab96221259，206 行，raw_sha256 = 8c965846e4c298e0de74d44d1cd61f931f54a946f305769cc09a0ee1d05f0488，与 sources.lock.json 记录一致）
  - scripts/observe.py（同一 commit，309 行，只读，未落入仓库）
  - scripts/improve.py（同一 commit，426 行，只读，未落入仓库）
- commit：d94826e1cd48f5403b82a5a909efdfab96221259（取自 sources.lock.json 的 last_seen_commit）
- 上游定位（自己的话）：这不是一份直接可用的去 AI 味规则集，而是一个空白模板加一套自动学习机制。使用者要先手填身份、读者、语气量表这些占位项，真正的禁用词和句式偏好留空，靠脚本不断比较"AI 初稿"和"人工定稿"之间的差异，把重复出现的改动自动提炼成新规则写回模板。换句话说，它交付的不是某个人的写作规则，而是一套从个人改稿行为里持续挖掘规则的流水线，外加一套按证据强度分级、决定新规则要不要自动生效的机制。这与仓库里另外三个来源（直接给出成品规则表）方向不同，偏 process 和 measurement。
- 总单元数：16
- 按 category 计数：measurement 11，process 4，genre 1
- 来源为 metadata-only，本清单不含原文。

# 单元清单

## U-wss-001

- category: measurement
- language: both
- rule_summary: 记录写作风格时，不用一句笼统的形容词描述（比如"随意一点""专业一点"），而是拆成几个互相独立、各自可以打 1-10 分的量表维度，每个维度单独定值。
- positive: 给一个新客户写风格说明时，分别标出"用词正式程度 7/10""专业术语密度 4/10""语气严肃程度 6/10"三项独立打分，互不干扰地调整每一项。
- negative: 风格说明只写一句"语气要专业但不要太生硬"。违反点：把多个互不相同的维度（正式程度、语气、态度）压进一句模糊描述里，没有拆成可以分别打分的独立项。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: SKILL.md
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "【0】Voice Dimensions（量化你的风格）"
- notes: 来源为 metadata-only，本单元不含原文。上游给了五个具体维度名和一张打分表，这里只保留"多维度独立打分"这个思路，没有照抄维度名称本身，因为维度名接近词表条目。

## U-wss-002

- category: measurement
- language: both
- rule_summary: 某个风格维度暂时不知道该打几分时，先留空，不要凭第一印象随便填一个初始值；等积累了足够多的真实改稿记录之后，再从这些记录里倒推出该维度的实际取值。
- positive: 新建风格档案时，"简洁程度"一栏先留空，等改了十几篇稿子、观察到作者反复把长句拆短之后，再据此把这一项定为偏简洁。
- negative: 档案刚建好就凭感觉把"简洁程度"填成 8/10，之后也不再根据实际改稿记录复核这个数字。违反点：在没有任何实际改稿证据的情况下就把估计值当成定值使用。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: SKILL.md
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "【0】Voice Dimensions（量化你的风格）"
- notes: 来源为 metadata-only，本单元不含原文。与 U-wss-001 共用同一个锚点小节，二者分别对应"怎么定义维度"和"怎么给维度赋值"两条不同的判定点。

## U-wss-003

- category: process
- language: both
- rule_summary: 在给出具体的措辞规则之前，先确定三件事：写作者本人的身份定位、目标读者是谁、写作者和读者之间是什么关系（比如是同行交流还是单向科普）；后面的用词和句式规则应当服务于这层关系，而不是脱离关系凭空定规则。
- positive: 先写明"作者是某领域的独立从业者，读者是同领域的同行，双方是平等交流关系"，再据此定出"不用入门科普式的解释性铺垫"这条规则。
- negative: 直接列一堆禁用词和偏好句式，全文没有交代这些规则是写给谁看、面向什么读者定的。违反点：跳过身份和读者关系这一步，规则脱离了具体的写作情境。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: SKILL.md
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "【1】角色与读者"
- notes: 来源为 metadata-only，本单元不含原文。

## U-wss-004

- category: process
- language: both
- rule_summary: 随着改稿积累出的个人规则，按三个固定类别归档：一般性行为要求、禁止使用的词、偏好的句式结构；新规则产生时先判断属于哪一类再归档，而不是全部堆在一张不分类的清单里。
- positive: 新发现"作者总把'首先其次最后'这种三段式删掉"这条规律后，把它归进"偏好句式结构"这一类，而不是和禁用词混在一起。
- negative: 所有观察到的改动，不管是词汇层面还是结构层面，都写进同一份"注意事项"列表里，没有分类。违反点：新规则不落入任何固定类别，导致同一份清单里词汇规则和结构规则混杂，后续没法按类别单独维护。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: SKILL.md
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "【2】写作规则"
- notes: 来源为 metadata-only，本单元不含原文。上游这一节下的"基础规则/禁止词/句式偏好"三个子节全是空占位符（括号里写的是举例提示），没有可提取的具体禁用词或句式规则本身，能提取的只有"分三类归档"这个结构性做法。

## U-wss-005

- category: genre
- language: both
- rule_summary: 输出格式要按发布平台调整：不支持渲染 markdown 语法的平台要用纯文本，短内容为主、常配图配表情的平台要用短段落，允许完整排版的长文平台（如博客）可以用标准 markdown；同一份内容发到不同平台，格式处理不能用一套模板套所有平台。
- positive: 同一篇稿子发布到不支持 markdown 的短消息平台时去掉标题符号和加粗星号，改成纯文字加换行；发到博客时保留标题层级和加粗。
- negative: 把带三级标题、加粗、无序列表的 markdown 原文直接复制到一个不解析 markdown 的短消息平台上发布。违反点：忽略目标平台不渲染 markdown 这一限制，星号、井号等标记符号会被当作普通字符原样显示。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: SKILL.md
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "【3】格式规范 / ### 平台适配"
- notes: 来源为 metadata-only，本单元不含原文。上游表格里列的具体平台名和对应格式要求属于示例内容，这里只保留"按平台特性分类处理格式"的判定逻辑。

## U-wss-006

- category: process
- language: both
- rule_summary: 规则积累走一个固定闭环：先由 AI 写出初稿；再由人对初稿做修改，改到本人认可为止；然后把"改之前"和"改完认可"这两个版本放在一起比较，找出其中系统性的改动；把这些改动整理成新规则，写回同一份规则文件；下一次生成内容时使用更新后的规则。任何一环缺失（比如跳过人工确认、或者提炼出的规则不写回规则文件），这个闭环就不成立。
- positive: AI 写完初稿后交给作者本人修改，作者改到自己满意才算定稿；系统把这两版拿去比较，发现作者总是删掉总结性的收尾句，就把"不写总结性收尾句"写进规则文件，供下次生成时参考。
- negative: 系统直接比较同一个人在两次不同任务里写的两份 AI 初稿，从中总结规律，全程没有人工修改和确认环节。违反点：比较的两份材料里没有一份是经过人工认可的定稿，闭环里"人工修改并确认"这一环被跳过了。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: SKILL.md
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "🔄 自动学习（内置） / ### 工作原理"
- notes: 来源为 metadata-only，本单元不含原文。"## 🎯 怎么用"一节的五步说明是同一个闭环的简写版本，两节共用这一个单元，覆盖表里一并标注。

## U-wss-007

- category: measurement
- language: both
- rule_summary: 从一次改稿里学习规则时，只看两个时间点的版本：AI 给出的第一版，和人最终确认下来的那一版；中间来回改了多少轮、每一轮改了什么都不必记录和比较，只有这两个端点的差异才算数。
- positive: 一篇稿子在协作文档里被反复调整了八次才定稿，系统只取最初的 AI 版本和第八次之后的定稿版本做比较，中间七次的过程一律不看。
- negative: 系统把每一次中间修改都单独记录下来，逐轮比较相邻两个版本之间的差异，试图从每一轮的小改动里都提炼规则。违反点：把中间过程的每一轮改动都当成独立的比较对象，而不是只取首尾两个端点。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: SKILL.md
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "只需要两个数据点"
- notes: 来源为 metadata-only，本单元不含原文。

## U-wss-008

- category: measurement
- language: both
- rule_summary: 如果人工确认定稿时对 AI 初稿一个字都没改，这次记录要当作"当前规则用对了"的正向证据保留下来，不能当成没有信息量而丢弃或跳过不记。
- positive: 某次改稿记录里定稿和初稿完全一致，系统把这条记为一次成功案例计入统计，用来说明现有规则在这类内容上是有效的。
- negative: 系统只统计有实际改动的记录，凡是初稿和定稿一模一样的情况一律不写入日志、不计入任何统计。违反点：把"没有改动"等同于"没有价值的数据"直接丢弃，损失了本该算作正向反馈的信息。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: scripts/observe.py
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "def record_final(args):"
- notes: 来源为 metadata-only，本单元不含原文。此规则只能从脚本代码逻辑中读出，SKILL.md 正文没有明说，按要求归入 measurement。

## U-wss-009

- category: measurement
- language: both
- rule_summary: 把一份 AI 初稿和它后来对应的人工定稿配对起来时，靠对初稿内容本身算出的一个指纹值来匹配，不依赖文件名、保存顺序或者人工手动记录哪份对应哪份。
- positive: 系统给每份初稿的正文内容算一个指纹码，人工确认定稿时只需要报出这个指纹码，系统就能自动找到对应的初稿，不用管文件叫什么名字、存在哪个文件夹。
- negative: 系统靠文件保存的先后顺序去猜测哪份定稿对应哪份初稿，遇到多篇稿子同时在改时经常配对错误。违反点：用外部的、和内容本身无关的线索（保存顺序）做匹配，而不是从内容本身推出一个稳定的标识。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: scripts/observe.py
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "def compute_hash(content):"
- notes: 来源为 metadata-only，本单元不含原文。此规则只能从脚本代码逻辑中读出，按要求归入 measurement。

## U-wss-010

- category: measurement
- language: both
- rule_summary: 从改稿差异里提炼一条新规则之前，先看这类改动够不够格：要么同类改动在不同稿子里出现过不止一次，要么虽然只出现一次但改动幅度大、意图很明确；只出现一次而且改动很小、很零散的情况不足以单独立一条规则。
- positive: 三篇不同主题的稿子里，作者都把同一个词换成了另一个词，这种反复出现的改动被提炼成一条禁用词规则；而某一篇稿子里一处无关紧要的用词微调，只出现过一次且改动很小，不被单独提炼成规则。
- negative: 只因为某一篇稿子里有一处很小的用词调整，就据此新增一条正式规则。违反点：仅凭一次、且改动幅度很小的孤立案例就下结论，既不满足"反复出现"也不满足"改动幅度大且明确"这两个门槛中的任何一个。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: scripts/improve.py
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "def extract_improvements(args):"
- notes: 来源为 metadata-only，本单元不含原文。此规则来自脚本里嵌入的提炼要求，按要求归入 measurement。

## U-wss-011

- category: measurement
- language: both
- rule_summary: 提炼出一条候选新规则后，先和规则文件里已经记录的规则比对，如果说的是同一件事就不再重复添加。
- positive: 提炼出"少用被动语态"这条候选规则前，先检查规则文件，发现已经有一条内容相同的规则在，于是不再新增。
- negative: 每次提炼都直接往规则文件里追加新条目，不检查是否已经有意思相同的规则存在。违反点：跳过了与已有规则的比对环节，导致同一条规则被反复重复记录。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: scripts/improve.py
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "def extract_improvements(args):"
- notes: 来源为 metadata-only，本单元不含原文。与 U-wss-010 共用同一处代码位置，二者分别对应"够不够格提炼"和"是否与已有规则重复"两个不同判定点。

## U-wss-012

- category: measurement
- language: both
- rule_summary: 每一条被提炼出来的新规则，都要写成可以直接照做的具体指令（比如"不用某个词，换成某个词"），不能只写一句对改动的笼统印象。
- positive: 提炼出的规则写成"不用某某词，改用某某词，理由是原词偏书面"，写作者拿到这条规则可以直接照做。
- negative: 提炼出的规则写成"这篇改得更自然了"。违反点：只描述了改动之后的整体印象，没有指出具体该怎么做，写作者拿到这条规则无法直接照办。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: scripts/improve.py
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "def extract_improvements(args):"
- notes: 来源为 metadata-only，本单元不含原文。与本仓库 criteria.md 第 2 条"规则必须可判定"的判据高度一致，属于同一思路在提炼环节的体现，归并阶段可能直接判 duplicate。

## U-wss-013

- category: measurement
- language: both
- rule_summary: 给每条提炼出的新规则按证据出现次数打一个置信等级：反复出现多次的等级最高，出现次数中等的次之，只出现过一次的最低；只有最高等级的规则允许不经人工确认就自动生效，中间等级要等人工看过再生效，最低等级只存档观察，不生效。
- positive: 某条候选规则在过去一周的改稿里出现了五次，被判为最高等级后自动写入规则文件；另一条只出现过一次的候选规则被记下来但暂不生效，等以后再次出现时重新评估。
- negative: 系统把只出现过一次的候选规则和反复出现多次的候选规则一视同仁，全部不经人工确认就自动写入规则文件。违反点：跳过了按证据出现次数分级的步骤，让证据不足的规则获得了和证据充分的规则相同的自动生效权限。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: SKILL.md
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "规则分级"
- notes: 来源为 metadata-only，本单元不含原文。scripts/improve.py 里的 auto_improve、apply_proposal 两个函数实现了同一套分级只应用最高档的逻辑，用作本单元的补充证据，anchor 仍以 SKILL.md 小节为主。这条打分机制与本仓库 criteria.md 第 3 条"证据不等于结论"（不按票数自动定采用）方向相反，归并阶段需要重点核对，已记入"冲突与取舍"候选项。

## U-wss-014

- category: process
- language: both
- rule_summary: 自动更新规则文件之前，先把被替换的旧版本保存一份；一旦新版本出问题，要能用一步操作恢复到最近保存的那份旧版本，不需要手动逐条对比找回。
- positive: 系统每次自动改写规则文件前都先复制一份旧文件存档，事后发现新规则有问题，运行一条恢复命令就能还原到改写前的样子。
- negative: 系统直接用新内容覆盖旧的规则文件，不保留任何旧版本副本，出问题后只能凭记忆手动重写。违反点：改写前没有保存旧版本，导致出错后无法一步恢复，只能人工从头重建。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: SKILL.md
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "安全"
- notes: 来源为 metadata-only，本单元不含原文。scripts/improve.py 里的 backup_skill、rollback 两个函数实现了这条规则，用作补充证据，anchor 仍以 SKILL.md 小节为主。

## U-wss-015

- category: measurement
- language: both
- rule_summary: 记录一次改稿时，把定稿相对初稿的字数变化算成一个百分比，作为衡量这次改动幅度大小的一个信号，单独记下来。
- positive: 某次改稿初稿是一千字，定稿变成一千二百字，系统记下"字数增加约百分之二十"作为这次改动幅度的参考信号。
- negative: 系统只记录"这次有改动"，不记录改动前后的字数变化幅度，导致无法区分是小幅度润色还是大幅度重写。违反点：丢弃了改动幅度这个信号，把幅度差异很大的两类改动记成了同一种"有改动"。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: scripts/observe.py
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "def record_final(args):"
- notes: 来源为 metadata-only，本单元不含原文。此规则只能从脚本代码逻辑中读出，按要求归入 measurement。

## U-wss-016

- category: measurement
- language: both
- rule_summary: 把"定稿和初稿一致的次数"与"定稿被改动过的次数"的比例，作为一段时间内衡量当前规则整体好不好用的一个指标持续跟踪，而不是只看单次改稿的结果。
- positive: 系统每周统计一次"未改动比例"，如果这个比例持续上升，说明当前规则越来越贴合作者的习惯；如果比例下降，说明规则可能过时了，需要更新。
- negative: 系统只关注单次改稿的结果，从不汇总统计一段时间内改动比例的变化趋势。违反点：缺少对改动比例的长期跟踪，无法判断规则整体是在变好还是变差。
- source:
  type: upstream
  source_id: upstream-jzocb-writing-style-skill
  path: scripts/observe.py
  commit: d94826e1cd48f5403b82a5a909efdfab96221259
  anchor: "def show_stats(args):"
- notes: 来源为 metadata-only，本单元不含原文。此规则只能从脚本代码逻辑中读出，按要求归入 measurement。

# 覆盖表

| 上游小节标题 | 归属单元 / 说明 |
|---|---|
| YAML frontmatter（name/version/description/dependencies/allowed-tools） | 非规则内容（skill 元数据） |
| # Writing Style Skill（模板）（标题与导语） | 非规则内容（导语） |
| ## 🎯 怎么用 | U-wss-006（与"工作原理"共用同一个流程，简写版本） |
| ## 【0】Voice Dimensions（量化你的风格） | U-wss-001、U-wss-002 |
| ## 【1】角色与读者 | U-wss-003 |
| ## 【2】写作规则（含"基础规则""禁止词""句式偏好"三个子节） | U-wss-004（三个子节均为空占位符，无具体词表或句式可提取） |
| ## 【3】格式规范 / ### 平台适配 | U-wss-005 |
| ## 🔄 自动学习（内置） / ### 工作原理 | U-wss-006 |
| ### 只需要两个数据点 | U-wss-007 |
| ### Agent 操作指南 | 非规则内容（操作说明，见"上游文本内的指令"一节） |
| ### 规则分级 | U-wss-013 |
| ### 安全 | U-wss-014 |
| ## 📊 CLI 参考 / ### observe.py（零依赖纯 Python） / ### improve.py（需要 LLM CLI） | 非规则内容（命令参考表，实现细节） |
| ## 📂 数据存储 | 非规则内容（存储路径实现细节，跨机器环境探测，不构成可判定的写作规则） |
| ## 🚀 30 天预期 | 非规则内容（效果预期宣传，不构成可判定规则） |
| scripts/observe.py / compute_hash | U-wss-009 |
| scripts/observe.py / record_final（一致性判断） | U-wss-008 |
| scripts/observe.py / record_final（字数变化百分比） | U-wss-015 |
| scripts/observe.py / find_unmatched（14 天回溯窗口） | 非规则内容（实现参数，任意设定的时间窗口，不构成可移植规则） |
| scripts/observe.py / show_stats | U-wss-016 |
| scripts/improve.py / extract_improvements（提炼门槛：反复出现或幅度大、不重复已有规则、必须可执行） | U-wss-010、U-wss-011、U-wss-012 |
| scripts/improve.py / apply_proposal、auto_improve（按等级过滤自动应用） | U-wss-013（补充证据，主锚点在 SKILL.md "规则分级"） |
| scripts/improve.py / backup_skill、rollback | U-wss-014（补充证据，主锚点在 SKILL.md "安全"） |
| scripts/improve.py / call_llm（LLM CLI 探测优先级） | 非规则内容（实现细节，不构成写作规则） |
| README.md | 未抓取：sources.yaml 的 paths 只追踪 SKILL.md，本轮按追踪范围未拉取 README.md，见"未解决问题" |

# 拆分时拿不准的地方

1. 本来源的绝大多数单元 language 都定为 both，而不是"这个来源多数是 en"的预期。原因：上游正文虽然用中文写成，但它交付的不是某种语言的写作规则，而是一套流程和度量机制（怎么配对版本、怎么打分、什么时候自动生效），这些机制本身不约束被改写文本用什么语言，中文稿和英文稿都适用。只有 U-wss-005（平台格式适配）勉强算和"文本"直接相关，但格式规则也不挑语言。因此这里没有按 both 的惯例给中英两组正反例，只给了一组中文示例；如果归并阶段认为 both 类必须补足英文示例，需要另行处理。
2. U-wss-013（规则分级打分机制）与本仓库 criteria.md 第 3 条"证据不等于结论"方向相反：上游主张按出现次数直接决定要不要自动生效，本仓库主张证据数不能自动决定采用。这是否要在归并阶段判 rejected 或 adopted-with-modification，需要归并时定，本清单只如实拆出、不预判结论。
3. U-wss-004（三个固定分类归档）和 U-wss-003（先定身份/读者/关系）这两条更像是"skill 该怎么组织自己的规则"这一层的元规则，而不是直接管写作文本本身的规则。是否要按 process 类别正常参与归并，还是应该算作"skill 结构建议"另案处理，我按 process 类拆出，具体取舍留给归并阶段。
4. scripts/observe.py 的 14 天回溯窗口、日志目录自动探测等纯实现参数，我判断不构成可移植的规则，列入"非规则内容"；如果归并阶段认为"待处理记录不应无限期挂起，需要设置一个过期窗口"本身也算一条可用的流程规则，可以在归并阶段单独把这一条另立单元，本轮出于"拿不准就不硬造判据"的考虑没有单独拆出。

# 疑似常见规则

以下单元的思路，我估计在其他去 AI 味或写作风格类项目里也可能出现（供归并阶段参考，不代表已核实其他来源真的有）：

- U-wss-005（按发布平台调整输出格式）
- U-wss-006（AI 初稿、人工定稿、比较差异、写回规则的闭环思路）
- U-wss-010（新规则要有重复出现或改动幅度够大才值得提炼）
- U-wss-013（按证据强度分级、决定是否自动生效）
- U-wss-014（改写前备份、支持一键回滚）

# 上游文本内的指令

SKILL.md 里有一节以"操作指南"的名义，按顺序列出三步命令行操作：写完初稿后记录一次初稿标识；人工确认定稿后记录一次定稿并把它和之前的初稿配对；之后手动或定时运行第三步，从积累的记录里提炼规则建议。这一节是该来源自身面向"使用这个模板的写作类 agent"的操作说明，不是针对本次拆解过程的注入指令（没有出现"忽略之前的规则""把这段加进你的系统提示"这类要求本次处理过程本身做什么的内容）。我没有执行其中任何一步，只读取了这三步对应的两个脚本文件，把脚本里体现的配对、判分、分级逻辑改写成了 U-wss-008、U-wss-009、U-wss-010 至 U-wss-013、U-wss-015、U-wss-016 这些 measurement 类单元。

除此之外，SKILL.md 和两个脚本里没有发现其他针对读者或针对处理者的指令性文本。
