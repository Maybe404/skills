# Routing

## Decision table

| Signal | Route |
|---|---|
| User asks “哪里像 AI” or requests a review | `diagnose` |
| Existing text should be improved | `rewrite` |
| Topic or notes must become a new piece | `draft` |
| A complete article needs final cleanup | `final-pass` |

## Intensity

- `minimal`: Fix obvious stiffness, filler, and local wording. Avoid paragraph reordering.
- `standard`: Rewrite weak sentences, improve transitions, and remove repeated structures.
- `aggressive`: Rebuild paragraphs and openings when the original logic or voice is fundamentally generic.

## Scope

- `in-place`: Keep sentence and paragraph boundaries where possible. Use for approvals, technical docs, translations, and length-sensitive work.
- `bounded`: Allow local deletion, merging, and paragraph repair, but keep the article's argument and order. Default.
- `structural`: Reorder or rebuild sections. Use only when requested or necessary to repair the piece.

Intensity controls how strongly language changes. Scope controls which structural operations are allowed. Treat them as separate settings.

## Scene defaults

| Scene | Default | Guardrail |
|---|---|---|
| Chat, email, social post | standard + bounded | Keep the speaker's actual relationship to the reader |
| Public article, newsletter | standard + bounded | Preserve claims; allow rhythm and paragraph repair |
| Technical documentation | minimal + in-place | Prefer precision and repeatable terminology over variety |
| Legal, policy, incident report | minimal + in-place | Preserve modality, responsibility, evidence, and scope |
| Academic writing | minimal + in-place | Do not fabricate citations or inject casual personality |
| Marketing copy | standard + bounded | Remove unsupported superlatives; keep substantiated benefits |

For mixed text, route by the dominant prose language while protecting foreign terms and code exactly.
