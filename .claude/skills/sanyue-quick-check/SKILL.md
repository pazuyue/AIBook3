---
name: sanyue_quick_check
description: 《三月女神今天也只是普通学生》定稿前轻量检查工具集；/scene-check 场景通读、/continuity-check 连续性核对、/hardword-check 硬词套路句、/setting-term-check 设定术语；不做完整审稿，不写正文。
version: v1.1
updated: 2026-05-26
trigger:
  - /scene-check
  - /continuity-check
  - /hardword-check
  - /setting-term-check
---

# sanyue-quick-check（薄壳引用版）

> 本文件是平台路由壳，不保存任何规则正文。规则正文的唯一来源是 `.trae/rules/三月女神定稿前检查skill.md`。

执行规则：

1. 本 skill 被触发时，必须先完整读取 `.trae/rules/三月女神定稿前检查skill.md` 并严格按其内容执行。
2. 若源文件与 `设定/当前硬口径.md` 或其他权威源冲突，按 `写作执行说明.md` 第三节裁决优先级处理。
3. 修改规则只改 `.trae/rules/` 源文件；本壳文件仅在 trigger、description 或 tools 声明变化时同步 frontmatter，frontmatter 以源文件为准。
