# /rewrite-final-check

Description: 按 Trae 章节重写 skill 执行 `/rewrite-final-check`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神章节重写skill.md`。

## Steps
1. 只做整章重写终审，不入库。
2. 核对整章是否完成重写计划、不可改事实、当前卷口径、人物阶段、章尾钩子和连续性。
3. 检查是否还有旧稿残留、旧口径回潮、段落缝合痕迹或章节目标缺失。
4. 输出终审结论；通过后再进入 `/finalize`。
5. 不替代 `/finalize` 入库。
