# /chapter-review

Description: 按 Trae 新章节规划 skill 执行 `/chapter-review`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神新章节规划skill.md`。

## Steps
1. 只对已写章节做复盘反推，不写正文。
2. 从正文倒推问题来源：章纲、质量卡、事件链、执行口径还是正文写法。
3. 不把“设定一致”当作质量合格；必须检查事件、选择、后果和追读理由。
4. 若结论要求重做章纲，按 Trae skill 写入反推结论供下一次 `/chapter-plan` 读取。
5. 按固定结构输出。
