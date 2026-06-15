# /style

Description: 按 Trae 写作风格 skill 执行 `/style`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神写作风格skill.md`。
- 文风依据同步参考 `设定\文风设定.md`。

## Steps
1. 只处理正文工艺：文风、镜头、节奏、对话、战斗质感、去 AI 腔。
2. 不改剧情目标、设定、人物能力、胜负条件或章节事件结果。
3. 若发现必须改设定或章纲才能解决，停止并提示改用 `/chapter-review`、`/plot-review` 或 `/rewrite-plan`。
4. 用户给路径则读取目标文件；用户贴正文则只处理贴出的正文。
5. 按 Trae skill 要求输出或写回。
