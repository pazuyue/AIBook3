# /write-brief

Description: 按 Trae 新章节规划流程辅助填写人工 `/write-brief`。

## Source of truth
- 参考 `.trae\rules\三月女神新章节规划skill.md`。
- 使用 `write-brief模板.md`，并写入当前卷 `write_brief_cache.md`。

## Steps
1. 不写正文，只辅助生成或整理人工写作卡。
2. 读取当前卷状态、最近 `/chapter-plan`、`/quality-card`、事件链、上一章结尾和当前硬口径。
3. 按 `write-brief模板.md` 整理本章目标、四个创作指标、一页结构、不可改事实和最多 3 条本章禁区。
4. 若本章"写作抓手"中含变身适应段（宿舍/日常/被注视/衣物/长发），必须在抓手里明确标注：变身适应只写社交与感知层面（被看、被对待、衣着、长发、称呼、被照顾），不写运动功能适应；禁用精确计算/机器比喻和"过分端正/用力太均匀/节奏太稳"等诊断式旁白；读感须为"别扭、新鲜、慢半拍"。依据：`设定/文风设定.md` 第六节「变身适应线」硬口径。
5. 用户确认后写入当前卷 `write_brief_cache.md`；第一卷路径为 `设定\大纲内容\第一卷\write_brief_cache.md`。
6. 完成后提示下一步进入 `/write`。
