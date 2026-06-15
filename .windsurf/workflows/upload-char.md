# /upload-char

Description: 按 Trae 定稿入库 skill 执行 `/upload-char`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神定稿入库skill.md`。

## Steps
1. 只处理人物设定、角色状态、角色能力等材料上传或入库。
2. 不新增人物设定，不覆盖权威文件。
3. 读取用户指定文件或文本，并标注角色标签和适用章节/卷。
4. 按 Trae skill 写入对应 char 向量库或本地同步目标。
5. 输出入库结果和必要的冲突说明。
