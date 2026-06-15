# /upload-world

Description: 按 Trae 定稿入库 skill 执行 `/upload-world`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神定稿入库skill.md`。

## Steps
1. 只处理世界观/设定类材料上传或入库。
2. 不生成新设定，不擅自改写权威源。
3. 读取用户指定文件或文本，并核对其权威等级和适用范围。
4. 按 Trae skill 写入对应 world 向量库或本地同步目标。
5. 输出入库结果和必要的口径缺口。
