# 规则单元的拆分与模板

## 一个单元只含一条规则

拆分的判据只有一个：这个单元能不能拿一句具体的文本去判定"违反了"还是"没违反"。

- 一个单元里出现两个"并且"连接的独立要求，拆成两个单元。
- 一个单元里的要求依赖另一条规则才成立（"在按 A 处理之后再做 B"），拆成两个，B 的 rule_summary 里写清前提。
- 上游用一张表列了二十个禁用词，这是一个单元还是二十个？判据是它们是否共用同一条判定逻辑：共用（"这些词一律不用"）就是一个单元，词表放进正例反例；每个词有各自的例外和替换建议，就一个词一个单元。
- 上游的一整节标题（"结构"）不是单元，节里的每条要求才是。

## 单元模板

```
id: <前缀>-<类别码>-<三位数>
category: pattern | protection | process | style-opinion | genre | measurement
language: zh | en | both
rule_summary: 一句话，说清什么行为被要求或被禁止，能据此判定
positive: 符合这条规则的一句或一段
negative: 违反这条规则的一句或一段，并指出违反在哪个词或哪个结构
source:
  type: upstream | self
  source_id: <sources.yaml 里的 id，或 self>
  path: <上游仓库内路径，或本仓库路径>
  commit: <40 位提交 id，或 null>
  anchor: <小节标题或稳定的行首文本>
notes: 拆分时的判断、与其他单元的关系、待确认的问题
```

这个模板是拆规则阶段的中间产物，不进仓库。拆规则阶段的 id 是临时编号，格式 `U-<来源简称>-<三位数>`，只在该来源的清单内唯一；正式的规则 id 在归并阶段分配，因为多个来源并行拆时无法保证全局唯一。归并阶段把单元写进 decisions.yaml：source 成为 sources 数组里的一条，category、language、rule_summary 同名对应。

三个键在 decisions.schema.json 里没有同名字段：`positive` 和 `negative` 是拆规则时的自查工具，落到 decisions.yaml 时并入 rationale 或者写进 skill 正文当例子；`notes` 只出现在 sources.schema.json 里，这里借用同一个词记拆分时的判断，不进 decisions.yaml。`source` 是单数形式，对应 decisions.yaml 里 sources 数组的一条。其余的键都是 decisions.schema.json 里的字段名。

## 前缀和类别码

前缀取自 language：zh 用 ZH，en 用 EN，both 用 ALL。

| category | 类别码 | 含什么 |
|---|---|---|
| pattern | P | 可识别的写法模式：句式、词汇、段落结构 |
| protection | PROT | 必须保留的事实、数字、术语、命令、责任主体、条件关系 |
| process | PROC | 流程步骤：先做什么、后做什么、什么时候停下问 |
| style-opinion | S | 风格主张：腔调、语气、人称、标点偏好 |
| genre | G | 体裁适配：哪种文本适用、哪种不适用 |
| measurement | M | 验证与度量：怎么判断改写是否成功 |

三位数在同一个前缀加类别码的组合内递增，从 001 起。号一经分配不改，规则撤下时 decision 改成 retired，号不回收。

## 正例反例怎么写

反例必须指出违反在哪里，不能只贴一段"不好的文字"。写法：先贴原句，再用一行写"违反点：<具体的词或结构>"。

正例和反例讲的是同一件事，只在被规则管住的那一点上不同。换了话题、换了长度、换了体裁的两段文字不构成一组正反例。

规则管的是中文时，正反例用中文写；管英文时用英文写；both 的两种语言各写一组。不要把英文例子直译成中文当中文例子——直译过来的句子在中文里往往不构成同样的问题。

## 来源锚点怎么取

anchor 用小节标题的原文，或者该段稳定的行首文本（前十到二十个字符）。不用行号：上游一改动行号就失效。

- 上游有小节标题：直接用标题原文，例如 `## Patterns to remove`。
- 规则在一张表里：用表格所在的小节标题，加上该行第一列的值，例如 `## Pattern table / "delve"`。
- 上游没有标题：用该段的行首文本，并在 notes 里写清它在哪个大节之下。

同一个来源里多条规则共用一个锚点是允许的，但要能靠 anchor 在文件里定位到不超过一屏的范围。

## metadata-only 来源怎么记

snapshot_policy 为 metadata-only 的来源，原文不进仓库。拆规则时：

- rule_summary 用自己的话重写，不复述上游句式。判据：这句话拿给没读过上游的人看，反推不出原句。
- positive 和 negative 自己造，不用上游的例句、词表条目、模式名。
- anchor 照常记小节标题——标题是定位信息，不是正文内容；标题本身就是一整条规则的完整表述时（例如整节只有一句"Never invent statistics"），也自己改写。
- notes 里写一行"来源为 metadata-only，本单元不含原文"。

这类单元在归并阶段按 criteria.md 正常裁决，许可证不限制思路的采用；只要求 rule_summary、正反例、rationale 里反推不出上游原句。
