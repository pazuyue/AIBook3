# /word-check

Description: 按 Trae 续写 skill 执行 `/word-check` 字数与完成度闸门。

## Source of truth
- 读取并服从 `.trae\rules\novel-flow-sanyue-full.md`。
- 同步核对 `设定\当前硬口径.md` 与当前卷写作状态。

## Steps
1. 只执行 `/word-check` 分支。
2. 统计当前章去空白字数。
3. 核对当前章节号、分场计划、章尾钩子和章节完成度。
4. 低于 4000 字时判定未完成，只允许继续 `/write` 补完当前章。
5. 按 Trae skill 的字数区间输出结论和下一步。
