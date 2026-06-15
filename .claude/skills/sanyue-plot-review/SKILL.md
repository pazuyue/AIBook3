---
name: sanyue_plot_review
description: 《三月女神今天也只是普通学生》专属剧情策划师+创意顾问技能；用 /plot-review 对已写章节执行结构评分+机会挖掘+优化建议；用 /idea-boost 只输出创意机会；不写正文，不直接修改文件。
version: v2.1
updated: 2026-05-22
trigger:
  - /plot-review
  - /idea-boost
---

# sanyue-plot-review（薄壳引用版）

> 本文件是平台路由壳，不保存任何规则正文。规则正文的唯一来源是 `.trae/rules/三月女神剧情策划skill.md`。

执行规则：

1. 本 skill 被触发时，必须先完整读取 `.trae/rules/三月女神剧情策划skill.md` 并严格按其内容执行。
2. 若源文件与 `设定/当前硬口径.md` 或其他权威源冲突，按 `写作执行说明.md` 第三节裁决优先级处理。
3. 修改规则只改 `.trae/rules/` 源文件；本壳文件仅在 trigger、description 或 tools 声明变化时同步 frontmatter，frontmatter 以源文件为准。
