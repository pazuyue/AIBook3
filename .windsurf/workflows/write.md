# /write

Description: 按 Trae 续写 skill 执行 `/write`。

## Source of truth
- 读取并服从 `.trae\rules\novel-flow-sanyue-full.md`。
- 最高裁决源仍是 `设定\当前硬口径.md`、当前卷状态、写作设定包、口径卡片、正文定稿与人工 `/write-brief`。

## Steps
1. 只执行 `/write` 分支；不要处理 `/finalize`、`/upload-*` 或审稿命令。
2. 按 Trae skill 的 L1 → L2 → L3 流程加载上下文；Qdrant 可用则按规则检索，不可用则按本地文件降级并说明。
3. 必须确认当前卷 `write_brief_cache.md` 有当前章节的人工 `/write-brief`；缺失时停止，不得直接按计划缓存写正文。
4. 用 `/write-brief` 建立场景任务卡，裁决计划缓存和旧召回冲突。
5. 只输出小说正文，不输出解释、计划或审稿意见。
