---
name: sanyue_writing_style
description: 《三月女神今天也只是普通学生》专属写作风格与正文工艺技能；只负责文风、镜头、节奏、对话、战斗质感、去AI腔和修文标准，不负责Qdrant检索、章节入库或定稿自动化。
version: v2.3
updated: 2026-06-11
trigger:
  - /style
  - /polish
  - /rewrite
  - /fix-prose
  - /self-revise
  - /daily-style-check
---

# novel-craft-sanyue（薄壳引用版）

> 本文件是平台路由壳，不保存任何规则正文。规则正文的唯一来源是 `.trae/rules/三月女神写作风格skill.md`。

执行规则：

1. 本 skill 被触发时，必须先完整读取 `.trae/rules/三月女神写作风格skill.md` 并严格按其内容执行。
2. 若源文件与 `设定/当前硬口径.md` 或其他权威源冲突，按 `写作执行说明.md` 第三节裁决优先级处理。
3. 修改规则只改 `.trae/rules/` 源文件；本壳文件仅在 trigger、description 或 tools 声明变化时同步 frontmatter，frontmatter 以源文件为准。
