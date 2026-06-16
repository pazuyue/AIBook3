# AIBook3 Master 调度规则（mavis 主线内部用）

> 这不是给 worker 看的，是给 mavis 主线（即 Mavis 自己）做 Master 调度用的内部规则。
> 4 个 worker agent 都在 `.harness/reins/` 下，命令路由由 mavis 主线判断后派发。

## 一、调度原则

执行流程（来自《写作执行说明》第二节 2.1）：

1. **角色 = 判断维度**：mavis 主线做 Master，判断本章需要关注什么风险。
2. **skill/命令 = 执行动作**：派发给对应 worker 跑。
3. **Master = 流程裁决器**：先判断章节类型和风险等级，再选择最短可用流程。

## 二、风险等级判定

| 等级 | 适用 | 流程 |
| ---- | ---- | ---- |
| 低风险 | 普通校园推进、低风险日常过渡、无战斗、无大段设定显影、无身份暴露风险 | 写手 → 质检（word-check + self-revise + hardword-check）→ 设定审校（轻量）→ 定稿入库 |
| 中风险 | 含日常/关系/变身适应重点、战斗/术式明显、设定密集、身份风险 | 写手 → 质检（加 daily-style-check / scene-check / setting-term-check）→ 设定审校（重点）→ 定稿入库 |
| 高风险 | 战斗章、设定章、身份风险章、重写后章节、连续性复杂章节、用户明确"全量定稿前检查" | 写手 → 质检（全套）→ 设定审校（全套）→ 定稿入库 |

## 三、命令路由表

| 用户给的信号 | 派发对象 | 命令 |
| ------------ | -------- | ---- |
| "写下一章" / "/write" / "/write-brief" | writer | /chapter-plan → /write-brief → /write |
| "这章跑偏了，重做" / "/rewrite-plan" | mavis 主线（不派发）| /rewrite-plan → /rewrite-next → /rewrite-check → /rewrite-fix → /rewrite-final-check → finalize |
| "质检一下" / "/word-check" / "/hardword-check" / "/self-revise" | qa | 三步走：硬词→去 AI→读感 |
| "改文风" / "/style" / "/polish" / "/fix-prose" | qa | /fix-prose → /self-revise |
| "看看设定有没有冲突" / "/review" / "/check-setting" / "/check-outline" / "/check-skill" | canon | 读取权威源 + 出审校报告 |
| "剧情存疑" / "/plot-review" / "/idea-boost" | canon | 出建议报告 |
| "定稿" / "/finalize" / "/refinalize*" | finalize | 入库 + 同步状态/伏笔/Qdrant/references |
| "拆章" / "/split-chapter" | mavis 主线（不派发）| 先做节拍分流；人工裁决后执行正文/映射/缓存同步，定稿后结构变更再接 C 层入库清理 |

## 四、派发约束

1. **写手 → 质检 → 审校 → 入库是顺序依赖**，不并行。
2. **质检内部三步走**（硬词→去 AI→读感）也是顺序依赖，qa agent 内部串行跑。
3. **写手不审稿、审校不写正文**，派发时不要越界。
4. **质检出报告 + 原位改法**，不直接改文件；等用户拍板"全部落到文件"再批量改。
5. **冲突裁决**走 canon，canon 不自行补设定，只标冲突来源 + 给建议。

## 五、首次启动检查

mavis 主线接到 AIBook3 写作任务时，先确认：

1. 当前章节号和上一章结尾（读 `设定/大纲内容/第一卷/第一卷当前写作状态.md` 二节）
2. 本章写作目标和禁区（读 `write_brief_cache.md`）
3. 章节类型和风险等级（按本文件第二节判定）
4. 派发流程（按本文件第三节路由表）

## 六、相关权威源

- `设定/当前硬口径.md` —— 日常执行最高
- `设定/术语口径统一表.md` —— 术语裁决、禁写/慎写
- `设定/文风设定.md` —— 正文工艺、硬词表
- `设定/大纲内容/第一卷/第一卷分卷大纲.md` —— 冲突时为准
- `设定/大纲内容/第一卷/第一卷事件链.md` —— 章节母版
- `设定/大纲内容/第一卷/第一卷当前写作状态.md` —— 当前进度 + 活跃伏笔
- `.trae/rules/*.md` —— 8 个 skill 源文件（规则正文唯一来源）
