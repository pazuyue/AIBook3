---
name: sanyue_chapter_plan
description: 《三月女神今天也只是普通学生》新章节写前校准规则；用 /chapter-plan 读取当前状态、大纲和上一章正文，输出并写入不可改事实与分场计划；用 /quality-card 输出并写入写前质量任务卡；用 /chapter-review 对已写章节做复盘反推；不写正文。
version: v2.2
updated: 2026-05-26
trigger:
  - /chapter-plan
  - /quality-card
  - /chapter-review
  - /split-chapter
---

# sanyue-chapter-planning（薄壳引用版）

> 本文件是平台路由壳，不保存任何规则正文。规则正文的唯一来源是 `.trae/rules/三月女神新章节规划skill.md`。

执行规则：

1. 本 skill 被触发时，必须先完整读取 `.trae/rules/三月女神新章节规划skill.md` 并严格按其内容执行。
2. 若源文件与 `设定/当前硬口径.md` 或其他权威源冲突，按 `写作执行说明.md` 第三节裁决优先级处理。
3. 修改规则只改 `.trae/rules/` 源文件；本壳文件仅在 trigger、description 或 tools 声明变化时同步 frontmatter，frontmatter 以源文件为准。
