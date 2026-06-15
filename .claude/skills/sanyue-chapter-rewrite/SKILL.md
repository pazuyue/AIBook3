---
name: sanyue_chapter_rewrite
description: 《三月女神今天也只是普通学生》专属章节重写流程，用短命令完成重写规划、分段续写、规则审稿、原位修文和整章终审；适合重写跑偏章节。
version: v2.1
updated: 2026-05-22
trigger:
  - /rewrite-plan
  - /rewrite-next
  - /rewrite-check
  - /rewrite-fix
  - /rewrite-final-check
---

# sanyue-chapter-rewrite（薄壳引用版）

> 本文件是平台路由壳，不保存任何规则正文。规则正文的唯一来源是 `.trae/rules/三月女神章节重写skill.md`。

执行规则：

1. 本 skill 被触发时，必须先完整读取 `.trae/rules/三月女神章节重写skill.md` 并严格按其内容执行。
2. 若源文件与 `设定/当前硬口径.md` 或其他权威源冲突，按 `写作执行说明.md` 第三节裁决优先级处理。
3. 修改规则只改 `.trae/rules/` 源文件；本壳文件仅在 trigger、description 或 tools 声明变化时同步 frontmatter，frontmatter 以源文件为准。
