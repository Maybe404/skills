# maybe-humanizer 来源

`skills/maybe-humanizer/` 正文是对下列来源的重写，不是上游内容的转载。上游各来源的著作权归各自作者所有。

## 来源表

| id | repository | branch | license | snapshot_policy | lineage | selection_status | 支持的规则数 | 落地的规则数 |
|---|---|---|---|---|---|---|---|---|
| upstream-petergyang-no-ai-slop | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | main | MIT | full-text | no-ai-slop | representative | 42 | 42 |
| upstream-lifelonglazylearner-qu-ai-wei | [LifelongLazyLearner/qu-ai-wei](https://github.com/LifelongLazyLearner/qu-ai-wei) | main | MIT | full-text | qu-ai-wei | representative | 46 | 46 |
| upstream-jzocb-writing-style-skill | [jzOcb/writing-style-skill](https://github.com/jzOcb/writing-style-skill) | main | unknown（未取得许可证，本仓库不含其原文） | metadata-only | writing-style-skill | representative | 16 | 2 |
| upstream-aboudjem-humanizer-skill | [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill) | main | MIT | full-text | aboudjem-humanizer | representative | 84 | 72 |

## 各来源详情

### upstream-petergyang-no-ai-slop

- 作者：Peter Yang
- 仓库：[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)
- 许可证：MIT

许可声明原文（逐字节照抄自 `merges/maybe-humanizer/snapshots/upstream-petergyang-no-ai-slop/LICENSE`）：

```
MIT License

Copyright (c) 2026 Peter Yang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

支持的规则，按 decision 分组：

- adopted（采用）：ALL-M-001, ALL-P-002, ALL-P-004, ALL-P-006, ALL-P-007, ALL-P-010, ALL-PROC-001, ALL-PROC-002, ALL-PROC-003, ALL-PROC-004, ALL-PROC-009, ALL-PROC-029, ALL-PROT-001, ALL-PROT-002, ALL-PROT-003, ALL-PROT-012, ALL-PROT-017, EN-P-001, EN-P-003, EN-P-004, EN-P-006, EN-P-007, EN-P-008, EN-P-009, EN-P-010, EN-P-011, EN-P-013, EN-P-014, EN-P-015, EN-P-016, EN-P-017, EN-P-019, EN-P-022, EN-P-023, EN-P-024, EN-P-025
- adopted-with-modification（改写后采用）：ALL-P-001, ALL-PROC-007, ALL-PROC-008, ALL-PROC-014, ALL-PROC-030, EN-P-026

### upstream-lifelonglazylearner-qu-ai-wei

- 作者：@LifelongLazyLearner
- 仓库：[LifelongLazyLearner/qu-ai-wei](https://github.com/LifelongLazyLearner/qu-ai-wei)
- 许可证：MIT

许可声明原文（逐字节照抄自 `merges/maybe-humanizer/snapshots/upstream-lifelonglazylearner-qu-ai-wei/LICENSE`）：

```
MIT License

Copyright (c) 2026 @LifelongLazyLearner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

支持的规则，按 decision 分组：

- adopted（采用）：ALL-P-004, ALL-P-005, ALL-P-006, ALL-P-009, ALL-PROC-003, ALL-PROC-004, ALL-PROC-005, ALL-PROC-006, ALL-PROC-009, ALL-PROC-011, ALL-PROC-013, ALL-PROC-015, ALL-PROC-020, ALL-PROC-022, ALL-PROC-023, ALL-PROC-029, ALL-PROT-001, ALL-PROT-003, ALL-PROT-008, ALL-PROT-009, ALL-PROT-010, ALL-PROT-011, ALL-PROT-012, ALL-PROT-014, ALL-PROT-015, ALL-PROT-016, ALL-PROT-017, ALL-PROT-018, ALL-PROT-020, ZH-P-001, ZH-P-008
- adopted-with-modification（改写后采用）：ALL-G-001, ALL-P-001, ALL-PROC-008, ALL-PROC-010, ALL-PROC-012, ALL-PROC-014, ALL-PROC-021, ALL-PROC-024, ALL-PROC-028, ALL-PROT-004, ALL-PROT-005, ALL-PROT-006, ALL-PROT-007, ALL-PROT-019, ZH-P-009

### upstream-jzocb-writing-style-skill

- 仓库：[jzOcb/writing-style-skill](https://github.com/jzOcb/writing-style-skill)
- 许可证：未知，未取得许可证，本仓库不含其原文。
- 本来源按 metadata-only 处理：只记录了追踪文件的 commit 和哈希，不保存原文；它支持的规则都是用自己的话重写的，不引用原文的例句、词表条目或措辞。

支持的规则，按 decision 分组：

- adopted（采用）：ALL-P-003, ALL-PROC-001
- deferred（暂缓）：ALL-M-008, ALL-M-009, ALL-M-011, ALL-PROC-033
- duplicate（重复）：ALL-M-013
- reference-only（仅供参考）：ALL-M-006, ALL-M-007, ALL-PROC-032
- rejected（不采用）：ALL-M-010, ALL-M-012, ALL-M-014, ALL-M-015, ALL-M-016, ALL-PROC-034

### upstream-aboudjem-humanizer-skill

- 作者：Adam Boudjemaa
- 仓库：[Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill)
- 许可证：MIT

许可声明原文（逐字节照抄自 `merges/maybe-humanizer/snapshots/upstream-aboudjem-humanizer-skill/LICENSE`）：

```
MIT License

Copyright (c) 2026 Adam Boudjemaa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

支持的规则，按 decision 分组：

- adopted（采用）：ALL-G-003, ALL-M-002, ALL-M-004, ALL-P-002, ALL-P-003, ALL-P-004, ALL-P-005, ALL-P-007, ALL-P-008, ALL-P-011, ALL-PROC-001, ALL-PROC-002, ALL-PROC-016, ALL-PROC-017, ALL-PROC-018, ALL-PROC-029, ALL-PROT-001, ALL-PROT-002, ALL-PROT-008, ALL-PROT-009, ALL-PROT-017, EN-P-001, EN-P-002, EN-P-004, EN-P-005, EN-P-006, EN-P-007, EN-P-009, EN-P-012, EN-P-013, EN-P-014, EN-P-015, EN-P-017, EN-P-018, EN-P-019, EN-P-020, EN-P-021, EN-P-023, EN-P-024, EN-P-028, EN-P-029, EN-P-031, EN-P-032, EN-P-033, EN-P-036, EN-P-038, EN-P-041, ZH-M-001, ZH-P-001, ZH-P-002, ZH-P-003, ZH-P-004, ZH-P-005, ZH-P-006, ZH-P-007
- adopted-with-modification（改写后采用）：ALL-G-002, ALL-M-003, ALL-P-001, ALL-PROC-007, ALL-PROC-014, ALL-PROC-019, ALL-PROC-025, ALL-PROT-013, EN-M-001, EN-P-026, EN-P-027, EN-P-030, EN-P-035, EN-P-037, EN-P-039, EN-P-040, EN-P-042
- duplicate（重复）：ALL-PROC-027, ALL-PROC-031
- reference-only（仅供参考）：ALL-PROC-026, ALL-S-002, EN-P-034, EN-S-001, EN-S-002
- rejected（不采用）：ALL-M-005, ALL-S-001, EN-S-003
- unverified（未核实）：ZH-P-010, ZH-P-011

## 已移除的来源

无。

## 生成信息

- 渲染时间：2026-09-06T12:28:33Z
- 渲染依据：`merges/maybe-humanizer/decisions.yaml`（144 条规则）与 `merges/maybe-humanizer/sources.yaml`（4 个来源）。

本文件由脚本从 decisions.yaml 和 sources.yaml 生成，不要手工编辑。
