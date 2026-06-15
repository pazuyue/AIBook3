# /finalize

Description: 按 Trae 定稿入库 skill 执行 `/finalize`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神定稿入库skill.md`。
- 定稿前不得绕过必要检查流程。

## Steps
1. 只处理已确认定稿内容的同步、入库和状态更新。
2. 不续写正文，不做审稿，不做风格润色。
3. 读取目标正文、章节号、标题和当前卷状态。
4. 按 Trae skill 更新本地定稿相关文件，并在可用时执行向量入库。
5. 输出简短完成结果和必要的缺口说明。
