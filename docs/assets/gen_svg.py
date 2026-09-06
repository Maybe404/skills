import pathlib
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'Noto Sans CJK SC', sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
THEMES = {
    "light": dict(ink="#1f2328", muted="#6e7781", line="#d0d7de", accent="#0f766e", soft="#e6f4f1"),
    "dark":  dict(ink="#e6edf3", muted="#8b949e", line="#30363d", accent="#2dd4bf", soft="#0f2b28"),
}

def hero(t):
    c = THEMES[t]
    # source nodes on the left of the diagram area, converge into one box
    srcs = [(720, 60), (720, 110), (720, 160), (720, 210), (720, 260)]
    labels = ["no-ai-slop", "qu-ai-wei", "humanizer-skill", "writing-style", "…"]
    paths, dots, nodes = [], [], []
    for i, (x, y) in enumerate(srcs):
        d = f"M{x+8},{y} C{x+140},{y} {x+150},160 {x+290},160"
        paths.append(f'<path d="{d}" fill="none" stroke="{c["line"]}" stroke-width="1.2"/>')
        dots.append(
            f'<circle r="3" fill="{c["accent"]}"><animateMotion dur="{4.2 + i*0.6:.1f}s" '
            f'begin="{i*0.5:.1f}s" repeatCount="indefinite" path="{d}"/></circle>')
        nodes.append(
            f'<circle cx="{x}" cy="{y}" r="4" fill="none" stroke="{c["muted"]}" stroke-width="1.2"/>'
            f'<text x="{x-14}" y="{y+4}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{c["muted"]}">{labels[i]}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320" role="img" aria-label="Maybe404/skills：把多个上游 skill 合并成一个，并跟进上游变更">
  <g font-family="{FONT}">
    <text x="48" y="96" font-size="14" letter-spacing="2" fill="{c["muted"]}">MAYBE404 /</text>
    <text x="46" y="168" font-size="72" font-weight="600" fill="{c["ink"]}" letter-spacing="-1.5">skills</text>
    <text x="48" y="212" font-size="18" fill="{c["ink"]}">个人维护的 Agent Skills 集合</text>
    <text x="48" y="240" font-size="15" fill="{c["muted"]}">自己写的、跟着上游维护的、从多个同类项目合并整理的。</text>
    <text x="48" y="264" font-size="15" fill="{c["muted"]}">每条规则都记得自己从哪来、为什么留下。</text>
  </g>
  <g>
    {"".join(paths)}
    {"".join(nodes)}
    <rect x="1010" y="132" width="132" height="56" rx="10" fill="{c["soft"]}" stroke="{c["accent"]}" stroke-width="1.4"/>
    <text x="1076" y="156" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{c["accent"]}">maybe-humanizer</text>
    <text x="1076" y="175" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{c["muted"]}">合并后的一份</text>
    {"".join(dots)}
  </g>
</svg>
'''

def pipeline(t):
    c = THEMES[t]
    def box(x, y, w, h, title, sub, accent=False):
        stroke = c["accent"] if accent else c["line"]
        fill = c["soft"] if accent else "none"
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>'
                f'<text x="{x+w/2}" y="{y+h/2-4}" text-anchor="middle" font-family="{FONT}" font-size="15" font-weight="600" fill="{c["ink"]}">{title}</text>'
                f'<text x="{x+w/2}" y="{y+h/2+16}" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{c["muted"]}">{sub}</text>')
    y, h, w = 60, 64, 176
    xs = [40, 290, 540, 790, 1000]
    main = "M216,92 L290,92 M466,92 L540,92 M716,92 L790,92"
    branch_up = "M966,78 C980,78 986,60 1000,60"
    branch_dn = "M966,106 C980,106 986,124 1000,124"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="200" viewBox="0 0 1200 200" role="img" aria-label="每周一：检测上游变更，生成 PR，review，采纳或记录理由，合并">
  <defs>
    <marker id="a" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="{c["line"]}"/></marker>
  </defs>
  <text x="40" y="34" font-family="{FONT}" font-size="12" letter-spacing="1.5" fill="{c["muted"]}">每周一 · 上游同步</text>
  {box(xs[0], y, w, h, "检测上游变更", "sha 与 hash 比对")}
  {box(xs[1], y, w, h, "生成变更 PR", "diff、受影响的规则")}
  {box(xs[2], y, w, h, "review", "skill-merge 逐条判断")}
  {box(xs[3], y, w, h, "决定", "采纳 / 不采纳")}
  <rect x="1000" y="36" width="160" height="48" rx="8" fill="none" stroke="{c["accent"]}" stroke-width="1.2"/>
  <text x="1080" y="56" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{c["ink"]}">采纳：改 skill</text>
  <text x="1080" y="73" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{c["muted"]}">更新决定表和署名</text>
  <rect x="1000" y="100" width="160" height="48" rx="8" fill="none" stroke="{c["line"]}" stroke-width="1.2"/>
  <text x="1080" y="120" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{c["ink"]}">不采纳：记理由</text>
  <text x="1080" y="137" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{c["muted"]}">同样合并，留在 git 里</text>
  <path d="M216,92 L288,92" fill="none" stroke="{c["line"]}" stroke-width="1.2" marker-end="url(#a)"/>
  <path d="M466,92 L538,92" fill="none" stroke="{c["line"]}" stroke-width="1.2" marker-end="url(#a)"/>
  <path d="M716,92 L788,92" fill="none" stroke="{c["line"]}" stroke-width="1.2" marker-end="url(#a)"/>
  <path d="{branch_up}" fill="none" stroke="{c["line"]}" stroke-width="1.2" marker-end="url(#a)"/>
  <path d="{branch_dn}" fill="none" stroke="{c["line"]}" stroke-width="1.2" marker-end="url(#a)"/>
  <circle r="3.5" fill="{c["accent"]}"><animateMotion dur="7s" repeatCount="indefinite" keyPoints="0;1" keyTimes="0;1" calcMode="linear" path="M216,92 L290,92 L466,92 L540,92 L716,92 L790,92 L966,92 L1000,60"/></circle>
  <text x="40" y="180" font-family="{FONT}" font-size="12" fill="{c["muted"]}">例外才开 issue：上游不可达、许可证变化、历史被重写、需要人决定的冲突。</text>
</svg>
'''

out = pathlib.Path("docs/assets")
for t in THEMES:
    (out / f"hero-{t}.svg").write_text(hero(t), encoding="utf-8")
    (out / f"pipeline-{t}.svg").write_text(pipeline(t), encoding="utf-8")
print("ok")
