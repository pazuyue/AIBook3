# /rewrite-next

Description: 按 Trae 章节重写 skill 执行 `/rewrite-next`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神章节重写skill.md`。

## Steps
1. 只按当前 `rewrite_plan_cache.md` 续写下一段重写正文。
2. 不跳段、不改重写计划、不越过不可改事实。
3. 每段重写都核对当前硬口径、人物关系阶段、隐藏身份和战斗边界。
4. 输出当前段正文或按 skill 写回。
5. 完成一段后等待 `/rewrite-check`。
