# /chapter-plan

Description: 按 Trae 新章节规划 skill 执行 `/chapter-plan`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神新章节规划skill.md`。
- 写前校准以 `设定\当前硬口径.md`、当前卷状态、事件链、节奏表和上一章正文为准。

## Steps
1. 只做写前校准和分场计划，不写正文。
2. 读取当前状态、大纲、上一章正文、当前卷写作设定包和口径卡片。
3. 输出并写入不可改事实与分场计划。
4. 若已有正文且用户要求重做计划，先按 `/chapter-review` 思路复盘正文。
5. 按 Trae skill 的缓存写入规则执行。
