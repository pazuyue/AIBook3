# Copilot Instructions

## Repository scope

This repository is a **content-spec repository** for 《三月女神今天也只是普通学生》, not an application codebase.

The current source of truth is the local AIBook3 setting system:

1. `设定/当前硬口径.md` — current hard caliber card (highest priority for execution rulings)
2. Current volume state under `设定/大纲内容/第N卷/*当前写作状态.md`
3. Current volume writing pack (`写作设定包`) and caliber card (`口径卡片`)
4. Global setting files under `设定/`
5. Finalized text (`正文`) under `正文/`

Legacy requirement documents or older generated plans are reference only. If they conflict with the current hard caliber or current volume state, treat them as stale.

## High-level architecture

When generating or editing materials in this repository, preserve consistency from top to bottom: the current hard caliber card rules over cached plans, Qdrant recall, and older outlines. Volume-specific writing packs and caliber cards rule over global settings within their volume scope.

## Key conventions

- Keep all outputs aligned to the existing Chinese source material unless the user explicitly asks for another language.
- Do **not** change the protagonist premise: the lead is the soul-transferred `哥伦比娅·希珀塞莱尼娅`, the only current `三月女神` in the target world.
- Do **not** invent unrelated abilities. Moon/divinity powers must stay tied to the repository's stated `三月` authority and the referenced Genshin setting.
- Preserve the target tone: mystery-first, strange, and fantastical, with suspense woven into exploration.
- Keep the three required story elements in balance: `异世冒险`, `种族秘史`, and `神秘学`.
- Match Inkstone pacing expectations called out in the source doc: strong momentum, visible conflict, distinctive character hooks, and frequent mystery payoffs.
- Respect the story-stage split when proposing long arcs: the early period should center on adaptation, combat, and companion formation in a campus-like setting; the later period should expand into guild/community plots, world secrets, and the ancient darkness conflict.
- For requests to produce outlines, default to **3-5 complete outlines** unless the user narrows the count.
- Each outline should end with a clear stage result while still leaving runway for the larger throughline of reclaiming full lunar authority and saving the world.

## Current Sanyue Authority Index

Use this index to reject stale outline or generation context. Do not treat this file as a setting backup.

- Read `设定/当前硬口径.md` first for the latest execution boundary.
- Read the current volume `*当前写作状态.md`, writing pack, caliber card, event chain, rhythm table, and chapter outline before generating or editing volume material.
- Read `设定/大纲内容/故事线推进表.md` for moon-line debut pacing and long-arc staging.
- Read `设定/术语口径统一表.md`, `设定/战斗设定.md`, and the current volume caliber card for术式/吟唱/展开, old-training-building, gray-zone investigation, and enemy-unit boundaries.
- If older cached outlines, Qdrant recall, references, or this instruction file conflict with local AIBook3 authority files, treat the older material as stale.

## Project docs and assistant configs

`.trae/rules` is the current Trae-side assistant rule source. The matching GitHub-side skill mirror lives under `.github/skills/*/SKILL.md` and should stay content-synchronized with `.trae/rules`.

When broad repository guidance changes, update the relevant `.trae/rules` source first, then mirror the corresponding `.github/skills` file instead of maintaining divergent copies.
