---
name: novel_flow_sanyue_full
description: 《三月女神今天也只是普通学生》专属续写技能，适配Inkstone、变身无敌流、隐藏身份、异世神秘学；自动绑定Qdrant向量记忆、强制前置去AI化写作工艺，并优先服从当前有效大纲续写。
version: v2.1
updated: 2026-05-22
trigger:
  - /write
  - /word-check
tools:
  - qdrant_mcp
---

# novel-flow-sanyue-full（薄壳引用版）

> 本文件是平台路由壳，不保存任何规则正文。规则正文的唯一来源是 `.trae/rules/novel-flow-sanyue-full.md`。

执行规则：

1. 本 skill 被触发时，必须先完整读取 `.trae/rules/novel-flow-sanyue-full.md` 并严格按其内容执行。
2. 若源文件与 `设定/当前硬口径.md` 或其他权威源冲突，按 `写作执行说明.md` 第三节裁决优先级处理。
3. 修改规则只改 `.trae/rules/` 源文件；本壳文件仅在 trigger、description 或 tools 声明变化时同步 frontmatter，frontmatter 以源文件为准。
