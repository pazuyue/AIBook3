---
name: sanyue_finalize
description: 《三月女神今天也只是普通学生》定稿入库与向量上传规则；处理 /finalize、/refinalize 系列和 /upload-*；在 /split-chapter 流程中负责 C 层入库清理；不负责正文续写。
version: v2.3
updated: 2026-06-11
trigger:
  - /finalize
  - /refinalize
  - /refinalize-text-only
  - /refinalize-major
  - /upload-chapter
  - /upload-world
  - /upload-char
  - /upload-lore
  - /split-chapter
tools:
  - qdrant_mcp
---

# sanyue-finalize（薄壳引用版）

> 本文件是平台路由壳，不保存任何规则正文。规则正文的唯一来源是 `.trae/rules/三月女神定稿入库skill.md`。

执行规则：

1. 本 skill 被触发时，必须先完整读取 `.trae/rules/三月女神定稿入库skill.md` 并严格按其内容执行。
2. 若源文件与 `设定/当前硬口径.md` 或其他权威源冲突，按 `写作执行说明.md` 第三节裁决优先级处理。
3. 修改规则只改 `.trae/rules/` 源文件；本壳文件仅在 trigger、description 或 tools 声明变化时同步 frontmatter，frontmatter 以源文件为准。
