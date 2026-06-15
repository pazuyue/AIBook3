# /continuity-check

Description: 按 Trae 定稿前检查 skill 执行 `/continuity-check`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神定稿前检查skill.md`。
- 执行前必查 `设定\当前硬口径.md`。

## Steps
1. 只做连续性核对，不套完整 `/review`。
2. 默认读取当前章、上一章、当前写作状态和已定稿章节摘要。
3. 核对人物关系阶段、居住/队伍状态、时间月相、关键行为次数、信息暴露、物品伤痕和空间连续。
4. 正文定稿与状态文件冲突时，以正文定稿优先并标注。
5. 按 Trae skill 固定格式输出。
