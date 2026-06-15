# /rewrite-fix

Description: 按 Trae 章节重写 skill 执行 `/rewrite-fix`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神章节重写skill.md`。

## Steps
1. 只按 `/rewrite-check` 结论修当前重写段。
2. 不擅自扩写新段、不改重写计划、不改章节事实。
3. 原位处理硬伤、文风、动作线、对话和逻辑断点。
4. 修完后输出或写回当前段。
5. 仍有结构问题时提示回到 `/rewrite-plan`。
