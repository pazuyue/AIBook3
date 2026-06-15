# /rewrite

Description: 按 Trae 写作风格 skill 执行局部 `/rewrite`，不是章节重写流程。

## Source of truth
- 读取并服从 `.trae\rules\三月女神写作风格skill.md`。
- 章节级重写另走 `.trae\rules\三月女神章节重写skill.md` 的 `/rewrite-plan`。

## Steps
1. 只做局部正文工艺改写，不接管 `/rewrite-plan`、`/rewrite-next`、`/rewrite-check`、`/rewrite-fix`。
2. 不改变事件结果、设定、人物能力、战斗规则或关系走向。
3. 保持清冷、白话、镜头清楚和角色辨识度。
4. 若用户实际要整章重写，停止并提示使用 `/rewrite-plan`。
5. 按 Trae skill 输出修订后的正文或写回文件。
