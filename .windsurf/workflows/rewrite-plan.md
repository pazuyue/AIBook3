# /rewrite-plan

Description: 按 Trae 章节重写 skill 执行 `/rewrite-plan`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神章节重写skill.md`。
- 重写前仍以 `设定\当前硬口径.md` 和当前卷权威源裁决。

## Steps
1. 只制定重写方案，不直接写正文。
2. 读取原章节、当前状态、事件链、章纲/质量卡和相关审稿结论。
3. 明确保留事实、必须改的问题、分段重写顺序和禁止改动项。
4. 写入 Trae skill 指定的重写计划缓存。
5. 后续正文分段改用 `/rewrite-next`。
