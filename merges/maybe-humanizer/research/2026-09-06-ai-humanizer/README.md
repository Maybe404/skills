# 去 AI 味 Skills 调研

调研日期：2026-09-06，Asia/Shanghai。

## 先看结论

这次尽量扩大了搜索范围，但没有把搜到的东西全部包装成推荐：

- skills CLI 搜索 16 组关键词，返回 320 条结果，按完整 package 去重后是 **297 个目录候选**。
- 结合 GitHub、Google、X 公开索引/转载、YouTube、Reddit、Hacker News、Linux.do、V2EX，核对 **114 个 GitHub 地址，其中 112 个可访问**。
- 这些数量包含同源适配、技能集合、普通 prompt（提示词）、检测工具、UI 和代码方向的相邻项目，**不是 112 个独立有效的文本去味 skills**。
- 对重点项目读取了 README、SKILL.md 或相关源码路径，做的是**定位与规则初筛**，没有安装，也没有对同一组文本做效果实测。

我的首轮试用建议：中文从 **qu-ai-wei、shuorenhua、Humanizer-zh、ai-zixun/humanizer-zh** 选；英文从 **no-ai-slop、avoid-ai-writing、stop-slop、blader/humanizer** 选；如果问题是“写得不像我”，另看 **tramstop-skill、writing-style-skill、human-writing**。这是基于已读规则的选择，不是实测排名。

完整交付：

- [114 个项目地址完整目录](catalog.md)：逐项定位、GitHub stars、skills.sh 子技能与安装量。
- [仓库清单 CSV](repositories.csv)：可筛选的仓库、许可证、fork 上游、最近 push、安装入口。
- [297 个原始目录候选 CSV](directory-candidates.csv)：保留长尾、误命中和同源分支，方便继续扩搜。
- [结构化证据](evidence.json)：仓库元数据与抓取到的 SKILL.md 路径。
- [16 组 CLI 检索记录](search-log.json)：每组 20 条，不假装穷尽整个生态。

## 核验口径

1. **推荐不只看搜索结果。** 重点比较源文件的事实保护、适用语言、体裁边界、改写方式、依赖和可解释性。
2. **Stars 是仓库总量，安装量是 skills CLI 当次显示值。** 大型集合的 stars 不能给某一个子 skill 背书；K 是目录近似展示值，不能解释为独立用户数。
3. **低热度不等于无用。** 少于 100 stars 或少于 100 次目录安装的项目，保留为实验备选，不当成熟默认项。反过来，高热度也不证明改写效果。
4. **纯 Markdown 不等于全文永不出本机。** skill 本身不调用第三方 API，与承载它的模型是否在云端运行，是两回事。
5. **作者声明不是独立验证。** “降低检测率”“盲测提高”“几乎无法检测”等，均不能从项目宣传直接升级成结论。
6. **文件存在不等于全面审计。** `evidence.json` 中的源码路径表示已抓取；本次没有审计全部脚本、逐个安装、跑安全测试或复现作者 benchmark（基准测试）。

## 一、中文优先

下表的 stars 来自本次 GitHub API 快照；安装量来自本次 skills CLI。没有命中写“未命中”，不等于零安装。

| 项目 | Stars | 安装量 | 主要特点 | 我的判断 |
|---|---:|---:|---|---|
| [LifelongLazyLearner/qu-ai-wei](https://github.com/LifelongLazyLearner/qu-ai-wei) | 531 | 625 | 信息账本、引用绑定、语体保护，允许全文结构重写 | 中文保真改写优先试；规则较长，默认会输出门检和报告 |
| [MrGeDiao/shuorenhua](https://github.com/MrGeDiao/shuorenhua) | 1,438 | 975 | 区分聊天、状态更新、文档、公开写作；保护术语和责任主体 | 很适合技术人写中文、README、论坛和 issue 回复 |
| [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | 16,729 | 47.2K | 英文 Humanizer 的中文适配，24 类模式 | 热度高的中文基线，适合对照；不是中文所有体裁的标准答案 |
| [ai-zixun/humanizer-zh](https://github.com/ai-zixun/humanizer-zh) | 137 | 890 | 中文母语表达、翻译腔、长文节奏，可选声音参考 | 和上一项同名但不同项目；博客、评论、产品分析值得试 |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | 3,465 | 未命中 | 中文创作和改稿，强调具体人物的声音 | 从社区补到的强相关项目；本次以 README 定位，仍需试写 |
| [alchaincyf/tramstop-skill](https://github.com/alchaincyf/tramstop-skill) | 37 | 未命中 | 词汇、句式、结构、经验四层诊断；要求真实素材 | 方法值得读；实验结论未复现，不能因“实证”二字就视为成熟 |
| [superchun/no-slop-zh](https://github.com/superchun/no-slop-zh) | 28 | 未命中 | 保留事实、术语、版本和命令，清理中文空话 | 轻量候选，低热度，适合加入对照 |
| [chengzhi-c/natural-talk](https://github.com/chengzhi-c/natural-talk) | 38 | 未命中 | 对话与创作规则集 | 适合“回答别像模板”，不只针对文章末端润色 |
| [OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL](https://github.com/OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL) | 753 | 未命中 | 作者风格底座、de-AI-writing、风格审计脚本 | 约束细，但风格强；不要默认适合公文、技术说明或所有作者 |
| [taxueseek/say-it-human](https://github.com/taxueseek/say-it-human) | 65 | editor-revisor 51 | 改稿手、AI 味处理、声音澄清三个模块 | 有意思的小项目；部分示例的具体化需额外核对事实 |
| [yyx20202020/natural-writing-skill](https://github.com/yyx20202020/natural-writing-skill) | 14 | 24 | 中英文、事实保护、场景路由、文风校准 | 规则方向合理，热度低，只列试用备选 |
| [dongbeixiaohuo/writing-agent](https://github.com/dongbeixiaohuo/writing-agent) | 403 | style-modeler 120 | 选题、真实素材、证据账本、风格建模、审稿、最终事实核查 | 想搭完整写作 Workflow（工作流）再看，单段润色太重 |

### 这几项的区别

- **Humanizer-zh** 适合作为广为传播的基线，看看模式清理能做到什么。[源码](https://github.com/op7418/Humanizer-zh/blob/main/SKILL.md)
- **qu-ai-wei** 在改写权限、证据强度、原文信息和正式语体方面写了很多边界。它明确不把“自然”简单等同于“口语化”。[源码](https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/SKILL.md)
- **shuorenhua** 对技术文本更有针对性，明确保护接口字段、命令、日志、责任主体和条件关系。[源码](https://github.com/MrGeDiao/shuorenhua/blob/main/SKILL.md)
- **tramstop-skill** 的核心是向作者要真实经历、原话和判断，而不是把空泛句子改成更像聊天的空泛句子。[源码](https://github.com/alchaincyf/tramstop-skill/blob/main/SKILL.md)

## 二、英文通用写作

| 项目 | Stars | 安装量 | 主要特点 | 注意事项 |
|---|---:|---:|---|---|
| [blader/humanizer](https://github.com/blader/humanizer) | 43,628 | 5.8K | 24 类 AI 写作模式，初稿后再次审视和改写 | 多个本地化版本的上游；示例和实际事实边界要分开 |
| [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | 7,293 | 9.9K | 保留作者声口，区分审稿与编辑，清理 20 多类套路 | 我会优先拿它做英文文章对照 |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | 16,842 | 13.4K | 删除铺垫、机械对照、套话；五维自评 | 对副词、被动语态等禁令强，不宜无脑套所有文体 |
| [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | 4,136 | 未命中 | detect/rewrite/edit、分级问题、文风配置、可选迭代 | 对引文、表格、代码和文件范围有明确保护，值得重点试 |
| [aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill) | 215 | 631 | 55 类模式、五种 voice（文风）、CLI 分数、CI 入口 | 分数是规则指标，不是“AI 作者概率” |
| [jpeggdev/humanize-writing](https://github.com/jpeggdev/humanize-writing) | 58 | 1.6K | 八轮编辑，从篇章到节奏和声音 | 安装量和仓库 stars 不一致，不能只看一个热度指标 |
| [jalaalrd/anti-ai-slop-writing](https://github.com/jalaalrd/anti-ai-slop-writing) | 441 | 448 | 结构、标点、文风约束与不编造规则 | 适合提取规则；不代表外部检测器认可 |
| [adenaufal/anti-slop-writing](https://github.com/adenaufal/anti-slop-writing) | 124 | 82 | 通用系统 prompt/反模板规则 | 和 adewale 同名仓库不是同一个项目 |
| [adewale/anti-slop-writing](https://github.com/adewale/anti-slop-writing) | 17 | 46 | 英文 prose 编辑 skill | 低热度备选 |
| [theclaymethod/unslop](https://github.com/theclaymethod/unslop) | 355 | 未命中 | audit-only 或诊断后重构，两阶段流程 | 从论坛扩搜补到，值得与 Humanizer 对照 |
| [asavvin-pixel/unslop](https://github.com/asavvin-pixel/unslop) | 63 | 未命中 | 排版、词汇、结构三层处理，可用作者样本校准 | 引用论文和效果数字未在本次独立核实 |
| [aplaceforallmystuff/the-antislop](https://github.com/aplaceforallmystuff/the-antislop) | 28 | 57 | 35+ 模式、分层评分、编辑模式 | 仅简介/目录核验，保留候选 |
| [brandonwise/humanizer](https://github.com/brandonwise/humanizer) | 118 | 377 | 面向 OpenClaw 的 Humanizer 方案 | 同源规则，不应重复算成新方法 |

**观察：** 这些方案不能简单按“禁词更多”“规则更多”排序。`stop-slop` 强调严格删减，`no-ai-slop` 强调保住真实声音，`avoid-ai-writing` 增加了审稿模式和编辑边界，`aboudjem/humanizer-skill` 增加了可执行扫描。选择取决于要解决的失真类型，而不是功能清单长度。[stop-slop](https://github.com/hardikpandya/stop-slop) · [no-ai-slop](https://github.com/petergyang/no-ai-slop) · [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) · [aboudjem](https://github.com/Aboudjem/humanizer-skill)

## 三、中文长尾与同源适配

下面的条目以扩充候选为目的，没有全部细读，也不代表已经排除了复制、重命名或旧版本问题。安装量均来自本次 CLI，相应仓库 stars 和链接见完整目录。

| 仓库 | 子 skill | 安装量 | 定位 |
|---|---|---:|---|
| [hairyf/skills](https://github.com/hairyf/skills) | writing-humanizer-zh | 574 | 中文去味 |
| [z0gsh1u/oh-my-writing-skill](https://github.com/z0gsh1u/oh-my-writing-skill) | humanizer-cn | 742 | 创作流程中的去味模块 |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | humanize-chinese | 656 | 大型集合中的中文模块 |
| [smallnest/goal-workflow](https://github.com/smallnest/goal-workflow) | humanize-it | 445 | Workflow 中的去味模块 |
| [chujianyun/skills](https://github.com/chujianyun/skills) | remove-ai-flavor | 130 | 中文去味 |
| [jackywxsz/jacky-opc](https://github.com/jackywxsz/jacky-opc) | jacky-de-ai | 109 | 中文创作流程候选 |
| [allinherog-star/ai-skills](https://github.com/allinherog-star/ai-skills) | ai-humanizer-zh | 65 | 技能库收录 |
| [aaaaqwq/agi-super-team](https://github.com/aaaaqwq/agi-super-team) | de-ai-ify | 49 | 团队型 agent 体系中的模块 |
| [hardydai-cell/qu-ai-wei](https://github.com/hardydai-cell/qu-ai-wei) | 去ai味 | 22 | 不同作者的同名项目 |
| [kevinaimonster/skill-hub](https://github.com/kevinaimonster/skill-hub) | chinese-copyfix | 12 | 中文改稿线索 |
| [lanyasheng/content-deai-engine](https://github.com/lanyasheng/content-deai-engine) | content-deai-engine | 3 | 低热度中文候选 |
| [peng-666/deai-zh](https://github.com/peng-666/deai-zh) | deai-zh | 2 | 低热度中文重写 |
| [xcc864451691/gongwen-deai-skill](https://github.com/xcc864451691/gongwen-deai-skill) | gongwen-deai | 2 | 公文、工作汇报方向 |
| [cycleuser/skills](https://github.com/cycleuser/skills) | humanizer | 33 | 技能集合中的去味 |
| [1-skill/shuorenhua](https://github.com/1-skill/shuorenhua) | shuorenhua | 65 | 不同于 MrGeDiao；查重宣传未验证 |
| [yanyintingyou/stop-slop-cn-en](https://github.com/yanyintingyou/stop-slop-cn-en) | stop-slop-cn-en | 未命中 | 中英文适配，低热度 |

**两个失效/不可解析线索：** `b1lli/remove-ai-flavor-writing-skill` 的目录显示 86 次安装，`allblueuk/academic-deai` 显示 7 次，但本次 GitHub API 无法解析仓库。可能删除、改名或转私有，本次不能确定原因，因此不推荐直接安装。[目录一](https://skills.sh/b1lli/remove-ai-flavor-writing-skill/remove-ai-flavor) · [目录二](https://skills.sh/allblueuk/academic-deai/academic-deai)

最后一轮公开搜索还补到 6 条线索，**未纳入上述 114 个地址的 API 核验统计，也不计入推荐**：

- [mjlens-spec/human-flavor-pipeline](https://github.com/mjlens-spec/human-flavor-pipeline)：中文六阶段处理流程，声明复用了 qu-ai-wei 的部分内容。
- [peakseazhu/humanizer-chinese](https://github.com/peakseazhu/humanizer-chinese)：36 类中文写作模式。
- [Oxforce/haning-humanize-writing-skill](https://github.com/Oxforce/haning-humanize-writing-skill)：中文写作自然化，强调事实和披露保护。
- [AAzzAAzzAAzzAA/remove-chinese-ai-tics](https://github.com/AAzzAAzzAAzzAA/remove-chinese-ai-tics)：简体中文口癖清理，搜索结果标注为 beta。
- [wuxiiing/wash-ink](https://github.com/wuxiiing/wash-ink)：古言、武侠、仙侠的润色和对白保护。
- [z123-cloud/humanizer](https://github.com/z123-cloud/humanizer)：搜索结果内容与 qu-ai-wei 相近，先按疑似同源线索处理。

## 四、学术与专业材料

| 项目 | Stars | 适用方向 | 边界 |
|---|---:|---|---|
| [humanizer-zh-academic](https://github.com/redbaronyyyyy-eng/humanizer-zh-academic) | 273 | 中文论文 | “>50% 降至 11%”是作者报告，未复现，不能保证你的结果 |
| [momo2young/humanize-academic-writing](https://github.com/momo2young/humanize-academic-writing) | 18 | 英文社科论文 | 低 stars，先检验术语、论证强度和引文保真 |
| [stephenturner/skill-deslop](https://github.com/stephenturner/skill-deslop) | 381 | 英文科研文章、摘要、基金申请 | 科学语域比营销文案更匹配，但仍要核查主动语态等硬规则 |
| [stephenlzc/humanize-mba-text-skill](https://github.com/stephenlzc/humanize-mba-text-skill) | 43 | 中文 MBA 论文 | 规则数据化，有扫描流程；不是通用中文最佳项 |
| [WantongC/journal-adapt-writing-skill](https://github.com/WantongC/journal-adapt-writing-skill) | 770 | 按目标期刊样本校准文章 | 属“学目标文体”，不是靠禁词降检测率 |
| [yzhao062/agent-style](https://github.com/yzhao062/agent-style) | 671 | 技术文档、设计文档、研究写作 | 有规则与 bench；未在本次复现作者分数 |
| [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills) | 110 | qa-report-humanizer | QA 报告子场景，目录 565 次安装 |
| [vincentkoc/dotskills](https://github.com/vincentkoc/dotskills) | 102 | technical-deslop | 目录 87 次安装；需进一步核实具体作用范围 |

本报告只评价表达和工具定位，不认可规避机构披露要求的保证。学术场景的首要验收应是事实、数字、公式、引用及论证强度不漂移。

## 五、从“像人”到“像我”

| 项目/子 skill | Stars | 核心思路 |
|---|---:|---|
| [jzocb/writing-style-skill](https://github.com/jzocb/writing-style-skill) | 264 | 对比 AI 原稿与用户终稿，提取风格规则；含观察和改进脚本 |
| [sugarforever/01coder-agent-skills](https://github.com/sugarforever/01coder-agent-skills) | 133 | personal-chinese-writing-style，个人中文风格 |
| [haowjy/creative-writing-skills](https://github.com/haowjy/creative-writing-skills) | 447 | style-analysis、cw-prose-writing 等创作模块 |
| [jwynia/agent-skills](https://github.com/jwynia/agent-skills) | 153 | voice-analysis，先分析声音特征 |
| [realrossmanngroup/no_ai_slop_writing_rules](https://github.com/realrossmanngroup/no_ai_slop_writing_rules) | 672 | no-ai-slop 与 rossmann-voice，特定人物风格 |
| [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | 32,101 | 人物思维与表达建模，不仅仅是措辞 |
| [obra/the-elements-of-style](https://github.com/obra/the-elements-of-style) | 559 | 清晰、简洁的英文写作规则，目录 1.7K |
| [tamdogood/builder-essential-skills](https://github.com/tamdogood/builder-essential-skills) | 183 | orwell-writing，目录 162 |

我的建议：想建立自己的长期写作 skill，优先研究“真实样本 -> 提取偏好 -> 保真改写 -> 用户修订反馈”这条路径。它需要作者素材，不适合假装一条通用 prompt 就能学会你的声音。`writing-style-skill` 的自动学习会写入文件并调用 LLM CLI，使用前需审脚本和数据目录。[源码说明](https://github.com/jzocb/writing-style-skill)

## 六、其他语言、小说与营销

| 项目/子 skill | Stars | 安装量 | 方向 |
|---|---:|---:|---|
| [kevintsai1202/humanizer-zh-tw](https://github.com/kevintsai1202/humanizer-zh-tw) | 831 | 1.2K | 繁体中文，fork 自 op7418 |
| [daleseo/korean-skills](https://github.com/daleseo/korean-skills) / humanizer | 187 | 2.7K | 韩文 |
| [nomadamas/k-skill](https://github.com/nomadamas/k-skill) / korean-humanizer | 7,432 | 2.2K | 韩文 |
| [evergreentree97/K-Humanizer](https://github.com/evergreentree97/K-Humanizer) | 8 | 未命中 | 韩文，小项目 |
| [ikora128/stop-ai-slop-jp](https://github.com/ikora128/stop-ai-slop-jp) | 447 | 93 | 日文 |
| [vladimir-human/humanizer-ru](https://github.com/vladimir-human/humanizer-ru) | 123 | 601 | 俄文文本卫生 |
| [ilyautov/humanizer-ru](https://github.com/ilyautov/humanizer-ru) | 286 | 未命中 | 另一俄文项目，不能因同名混用安装路径 |
| [bencium/bencium-marketplace](https://github.com/bencium/bencium-marketplace) / hungarian-humanizer | 419 | 819 | 匈牙利文 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) / finnish-humanizer | 38,675 | 9.2K | 芬兰文；stars 属整个社区集合 |
| [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode) / story-deslop | 6,533 | 13.5K | 中文网文，强体裁约束 |
| [tance-mang/chinese-webnovel-skills](https://github.com/tance-mang/chinese-webnovel-skills) / deslop | 48 | 21 | 中文网文 |
| [chained1001/mo-shu](https://github.com/chained1001/mo-shu) / moshu-deslop | 0 | 13 | 小说流程线索，未细读 |
| [Wooooooooood/ai-fiction-writer](https://github.com/Wooooooooood/ai-fiction-writer) | 37 | 未命中 | 小说全流程，非单一去味 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) / content-humanizer | 25,587 | 804 | 内容营销；stars 属整个集合 |
| [every-app/open-seo](https://github.com/every-app/open-seo) / deslop | 17,310 | 1.4K | SEO 内容流程 |
| [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) / antislop-copywriting、antislop-human | 1,161 | 589 / 555 | 文案/自然表达，需与 UI/code 模块分开 |

## 七、带测量器或外部服务的方案

| 项目 | 类型 | 我的处理方式 |
|---|---|---|
| [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill) | skill + 本地规则 CLI | 可以研究评分与 CI；不把规则分数当作者身份鉴定 |
| [SadhvikChirunomula/measured-humanizer](https://github.com/SadhvikChirunomula/measured-humanizer) | 校准、评分、改写循环 | 2 stars 的实验线索；没跑过校准，不能推荐为已验证检测器 |
| [JCarterJohnson/vibecoded-design-tells](https://github.com/JCarterJohnson/vibecoded-design-tells) | Reddit 数据研究 + unslop-text/UI/code | 方法和原始数据值得读；社区抱怨频次不是写作质量真值 |
| [humanizerai/agent-skills](https://github.com/humanizerai/agent-skills) | 商业 API 包装 | 需要 API key、发送正文、消耗 credits，不是纯本地规则 |
| [rephrasyai/rephrasy-skills](https://github.com/rephrasyai/rephrasy-skills) | 厂商内容技能集 | 仅核对仓库和简介；具体联网、付费及子技能依赖待审 |
| [numen-tech/slopornot](https://github.com/numen-tech/slopornot) | humanizer/检测导向工具 | 46 stars，宣传绕检测，未验证 |
| [lynote-ai/humanize-text](https://github.com/lynote-ai/humanize-text) | pipeline/参考实现 | 非单一 Markdown skill，单独列相邻工具 |
| [mdeloughry/unslop](https://github.com/mdeloughry/unslop) | Obsidian 插件 | 本地规则分析与可选外部模型改写要分开看 |

不要把机密草稿交给陌生 humanization API。就本次已读源码，HumanizerAI 的 `humanize` 明确会把文本 POST 到其 API；这是能确认的实际依赖，不是只根据产品名字推测。[源码](https://github.com/humanizerai/agent-skills/blob/main/skills/humanize/SKILL.md)

## 八、UI“去 AI 味”，另开一类

如果你说的“去 AI 味”也包含默认紫色渐变、雷同 hero、三张卡片、装饰性图形和模板感，这一类才相关；它们不应挤占文章写作的排行榜。

| 项目/子 skill | Stars | 安装量/定位 |
|---|---:|---|
| [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) | 84,663 | design-taste-frontend 447.5K；另有多种设计子技能 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 65,865 | impeccable 263.7K；设计、审视、细化等工具 |
| [anthropics/skills](https://github.com/anthropics/skills) | 174,639 | 官方 frontend-design 等，非专门文章去味 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) / anti-ui-slop | 38,675 | 514；与同仓库 finnish-humanizer 不同领域 |
| [mengto/skills](https://github.com/mengto/skills) / no-ai-design-slop | 5,817 | 277 |
| [samber/cc-skills](https://github.com/samber/cc-skills) / frontend-design-deslop | 203 | 2.2K |
| [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) / antislop-ui | 1,161 | 619 |
| [gesso-build/skills](https://github.com/gesso-build/skills) / anti-slop | 84 | 20；设计规则检测方向 |
| [learnprompt/humanize-ppt](https://github.com/learnprompt/humanize-ppt) | 925 | 509；PPT 大纲与叙事 |

目录还返回 `uizze.com@anti-ui-slop`，显示 692.6K 安装。它不是本次 GitHub 地址核验中的仓库，未独立核实作者、实现、安装统计来源，因此只留在原始候选表，不以这个巨大数字直接推荐。[目录](https://skills.sh/uizze.com/anti-ui-slop)

同样要排除混淆：`dmmulroy/anti-slop` 是 JS/TS Oxlint 规则；`cursor/plugins@deslop` 是代码清理；`Hello-SimpleAI/chatgpt-comparison-detection` 是 HC3 数据/检测研究；`jere-mie/unslop` 主要做字符标点清理。名字相近，不等于能改善文章内容。[dmmulroy](https://github.com/dmmulroy/anti-slop) · [Cursor 源码](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/deslop/SKILL.md) · [HC3](https://github.com/Hello-SimpleAI/chatgpt-comparison-detection) · [jere-mie](https://github.com/jere-mie/unslop)

## 九、各平台找到的材料

### Google / 公开网页

实际打开 Google 的 `"humanizer" "skill"` 搜索页，结果指向 blader/humanizer；此外使用公开网页搜索扩展关键词和平台限定。Google 搜索只作发现入口，项目判断回到 GitHub 和源文件。另有两份可继续挖掘的材料：

- [Daguilar0123/ai-writing-skill-field-guide](https://github.com/Daguilar0123/ai-writing-skill-field-guide)：第三方整理了 68 项与测试材料。只有 1 star，不照搬其“最佳”结论。
- [lynote-ai/best-humanizer-handbook](https://github.com/lynote-ai/best-humanizer-handbook)：厂商发布的写作手册，作为参考，不算独立 skill。

### X / Twitter

X 原帖读取和搜索命中不稳定。本次使用可核对的作者入口、仓库引用和公开转载，**没有声称完整读过所有 X 原帖，更没有拿转发量当效果证据**。

- [归藏 Humanizer-zh 的公开转载](https://www.paio.com.cn/605.html)：作为找到 op7418 项目的线索，项目内容已回到 GitHub 核验。
- [Hardik Pandya / stop-slop 传播页](https://mindpattern.ai/e/stop-slop)：作为传播线索，规则以源仓库为准。
- [Alchain 的 X](https://x.com/AlchainHust)：tramstop-skill/nuwa-skill 的 README 给出的作者入口。
- [Jalaaldeen 的 X](https://x.com/jalaal_tweets)：anti-ai-slop-writing 的 README 给出的作者入口。
- [@mkbijaksana 的帖子](https://x.com/mkbijaksana/status/2027714311330627877)：adenaufal 项目 README 引用的灵感来源；不把它当已全文核验的实测。

### YouTube

这些是搜到的具体视频/作者入口。**本次没有逐条观看完整视频或逐条核验字幕**；用于发现项目与了解教程选题，不当独立 benchmark。

- [Humanizer Skill](https://www.youtube.com/watch?v=kp01PM9bqPU)，Artem Zakharchenko：展示 Humanizer 的技能使用。
- [去AI味十大skill：AI润色方法告别机器味，写出地道文章](https://www.youtube.com/watch?v=ZU_i2ANMVjw)，AI进化论-花生：综合名单线索，其中混合了技能、检测研究与 UI 方向，需回源分类。
- [去AI味提示词效果如何](https://www.youtube.com/watch?v=iYINsiuOzYQ)，AI进化论-花生：提示词对照线索，不等于可安装 skill。
- [AI-generated text reads too robotic?](https://www.youtube.com/watch?v=MCXXoVDCDxM)，阿拉新思维：Humanizer 介绍。
- [Peter Yang 的频道](https://www.youtube.com/@PeterYangYT)：no-ai-slop README 给出的作者频道。
- [hylarucoder 的频道](https://www.youtube.com/@hylarucoder)：ai-flavor-remover README 给出的作者频道；其项目本质上是长 prompt。

### Reddit / Hacker News

- [Made a Claude Code skill that catches 55 AI writing patterns](https://www.reddit.com/r/ClaudeAI/comments/1tgmd1o/made_a_claude_code_skill_that_catches_55_ai_writing/)：作者介绍 Aboudjem 版本，评论不是独立效果验收。
- [My Claude Code still writes like AI after using humanizer](https://www.reddit.com/r/ClaudeCode/comments/1tplv6o/my_claude_code_still_writes_like_ai_after_using/)：提醒“调用过 humanizer”不等于结果自然。
- [Humanizer skill rewrote my own writing](https://www.reddit.com/r/ClaudeCode/comments/1sz87xd/humanizer_skill_rewrote_my_own_writing/)：值得作为真人原稿误改的测试线索，不能当发生率统计。
- [HN: Show HN: Claude Code Skill to Remove AI Writing Cliches](https://news.ycombinator.com/item?id=47282353)：发现 conorbronsdon/avoid-ai-writing 的入口。
- [HN: Remove AI Writing Patterns with Skills](https://news.ycombinator.com/item?id=47048187)：补充项目传播与讨论。

### Linux.do / V2EX

- [Linux.do：去 AI 味：用于中文文本改写的开源 Skill](https://linux.do/t/topic/2082513)：qu-ai-wei 的作者介绍，随后核验源文件。
- [Linux.do：最佳AI去味skills方案](https://linux.do/t/topic/2057553)：混合讨论与候选发现，不照搬“最佳”标题。
- [Linux.do：写小说的去ai味skill终于磨出来了](https://linux.do/t/topic/2215168)：提醒网文是单独体裁，不宜拿它做技术文档默认方案。
- [V2EX：以目标期刊语料生成写作规范](https://v2ex.com/t/1212607)：发现 journal-adapt-writing-skill。
- [V2EX：新发布 skill：让你的 AI 跟你一样毒舌](https://www.v2ex.com/t/1201880)：风格注入方向的边界线索，作者声音和粗口不能等同“去 AI 味”。

## 十、真正要防的坑

1. **规则正确，示例却造事实。** 阅读到的若干项目示例，把笼统好评改成原文没有的数字、场景或第一人称感受。实际改稿必须明确禁止照着这种方式补事实，不能只看改后读着顺不顺。[Humanizer 示例](https://github.com/blader/humanizer) · [unslop 示例](https://github.com/asavvin-pixel/unslop)
2. **禁词不等于语境判断。** `stop-slop` 的“删所有副词”“不用被动语态”是强风格选择，不是所有英文体裁都必须遵守的事实。[规则](https://github.com/hardikpandya/stop-slop/blob/main/SKILL.md)
3. **多装几个不一定更好。** 有的鼓励第一人称，有的要求保持原声口；有的打散结构，有的保护说明文结构。我的建议是一次只激活一套主改写规则，其他做对照或按需审稿。
4. **同名覆盖与搬运。** `humanizer-zh`、`humanizer`、`deslop`、`unslop` 都出现多作者版本。安装前检查完整 owner/repo 和 skill 名称，不能只搜名字。
5. **规则分数和作者鉴定是两件事。** 本次没有验证任何检测器的准确率；“45 分变 12 分”最多先解释为该评分器的规则命中减少。
6. **真实素材不等于任意搜私密数据。** 采用样本学习时，应由你指定可用文章、日记或素材范围；不要因为 skill 说需要素材，就扫描全部私人记录。

## 十一、首轮安装清单

以下是本次实际在 skills CLI 结果中出现的 package 写法。**只是提供安装命令，没有执行；安装成功与运行效果仍需单独验证。** 不加 `-g -y`，避免在未选定前全局安装一堆同名规则。

```bash
# Chinese: choose one primary editor first.
npx skills add LifelongLazyLearner/qu-ai-wei@qu-ai-wei
npx skills add MrGeDiao/shuorenhua@shuorenhua
npx skills add op7418/humanizer-zh@humanizer-zh
npx skills add ai-zixun/humanizer-zh@humanizer-zh

# English: choose one baseline and one comparison.
npx skills add petergyang/no-ai-slop@no-ai-slop
npx skills add hardikpandya/stop-slop@stop-slop
npx skills add blader/humanizer@humanizer
npx skills add aboudjem/humanizer-skill@humanizer

# Personal voice, only after inspecting its scripts.
npx skills add jzocb/writing-style-skill@writing-style-skill
```

完整的 skills.sh 页面和其他安装命令在两份 CSV 中。不要将所有命令一次性执行。

## 十二、下一步怎么选出真正适合你的

建议的最小对照，不把未做的测试写成结果：

1. 用同一模型、相同生成设置和同一输入，分别测试无 skill 基线、qu-ai-wei、shuorenhua、Humanizer-zh、ai-zixun；英文另开一组。
2. 至少覆盖中文技术说明、产品评论、公众号短文、正式工作汇报和你自己写的原文。
3. 先核验事实/数字/否定/条件/责任主体/引文；任意漂移先判失败，再看风格。
4. 隐去 skill 名称，比较自然度、信息密度、个人声口和修改必要性。
5. 单独记录误改真人文本、删掉必要术语、编造经历、过度缩短及固定新套路。
6. 从胜出的主编辑中提取真正有用的规则，再决定是否组合；不要先把十套规则拼成一套。

**本轮交付边界：** 广搜、回源、分类和静态初筛已完成；安装、安全审计、跨模型改写对照和检测率实验均未执行。
