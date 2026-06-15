# /upload-chapter

Description: 按 Trae 定稿入库 skill 执行 `/upload-chapter`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神定稿入库skill.md`。

## Steps
1. 只上传或入库章节正文相关内容。
2. 不修改正文内容，不代替 `/finalize` 做定稿判断。
3. 读取目标章节号、标题、正文和必要元数据。
4. 按 Trae skill 选择章节向量库和元数据格式。
5. 输出入库结果；失败时明确说明缺少什么。
