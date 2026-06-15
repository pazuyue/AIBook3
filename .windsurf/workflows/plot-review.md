# /plot-review

Description: 按 Trae 剧情策划 skill 执行 `/plot-review`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神剧情策划skill.md`。
- 同步核对 `设定\当前硬口径.md`、当前卷状态、事件链和章节正文。

## Steps
1. 只做结构评分、创意机会和综合建议，不直接修改正文或设定文件。
2. 读取指定章节或当前章节，并按 skill 要求读取当前卷权威源。
3. 评估事件链兑现、冲突、人物选择、追读理由和创意机会。
4. 若事件链兑现评分过低，按 Trae skill 提示先执行 `/chapter-review`。
5. 按固定结构输出报告。
