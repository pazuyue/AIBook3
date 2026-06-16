---
name: sanyue_finalize
description: 《三月女神今天也只是普通学生》定稿入库与向量上传规则；处理 /finalize、/refinalize 系列和 /upload-*；被 /split-chapter 流程内部调用时负责 C 层入库清理；不负责正文续写。
version: v2.4
updated: 2026-06-15
trigger:
  - /finalize
  - /refinalize
  - /refinalize-text-only
  - /refinalize-major
  - /upload-chapter
  - /upload-world
  - /upload-char
  - /upload-lore
tools:
  - qdrant_mcp
---

# 三月女神定稿入库技能（Trae 规则版）

## 定位

本 skill 只处理已确认定稿内容的同步、入库和状态更新。正文续写归 `novel_flow_sanyue_full`，文风修订归 `sanyue_writing_style`，审稿归 `sanyue_review`。

## Master 角色定位

本 skill 在 Master 总导演调度制中承担：定稿归档员 + 伏笔控制器 + 拆章协调员（C 层）。

职责：
1. 对已确认定稿章节执行状态更新、章节摘要、伏笔追踪、references 同步和 Qdrant 入库。
2. 归档已完成的章节计划和 write brief，推进当前写作状态到下一章。
3. 对世界观、人物、伏笔等已确认权威片段执行上传或同步。
4. 被 `/split-chapter` 流程内部调用时，负责 C 层入库清理：清理 Qdrant 旧数据、重新定稿入库、同步 references。

不负责：
1. 不续写正文，不原位修文。
2. 不审稿，不裁决章节是否好看。
3. 不在未确认定稿或章节号明显不匹配时强行入库。
4. 不作为 `/split-chapter` 的外部入口，不执行拆章的 A 层（计划层）和 B 层（正文层）操作；外部入口由新章节规划 skill 负责。

被 Master 调用时，只处理定稿归档和记忆同步维度，不反向改正文。

## 触发与工作流

1. 收到「定稿正文 + /finalize」：
   - 自动执行下方「定稿自动化流程」
   - 禁止跳步，禁止询问确认
2. 收到 `/upload-chapter`：
   - 只接收已定稿小说正文；大纲、设定、节奏表、写作包不得存入 chapter 集合
   - 自动向量化存入 Qdrant chapter 集合
   - 仅回复：`✅ 章节已存入记忆库`
3. 收到 `/upload-world`：更新 world 集合；默认追加/更新当前权威片段，只有用户明确要求“全量重建”时才覆盖重灌。
4. 收到 `/upload-char`：更新 char 集合；默认追加/更新当前权威片段，只有用户明确要求“全量重建”时才覆盖重灌。
5. 收到 `/upload-lore`：更新 foreshadow 集合；默认追加/更新当前权威片段，只有用户明确要求“全量重建”时才覆盖重灌。

## 定稿自动化流程（/finalize 触发）

当用户发送「定稿章节正文 + /finalize」时，自动按以下 9 步顺序执行。

注意：当前 AIBook3 工作区是正文与状态源，`D:/Users/yueguang/NovelFlow/references` 只是外部同步目标。定稿正文源和写作状态源都以 AIBook3 工作区为准；必须先更新 AIBook3 内当前卷状态文件，再运行同步脚本推送到 NovelFlow references 和 Qdrant。

前置确认：若用户未明确声明“定稿”却触发 `/finalize`，或正文解析出的章节号与 writing_state 当前章节号明显不匹配，或正文明显不完整（缺章节标题、缺正文主体或只贴片段），先提示用户确认，不自动入库。

### Step 1：解析章节信息

从定稿正文中自动提取：
- 章节号（如“第11章”→ 11）
- 章节标题（如“白色画面”）
- 章节结尾最后 3 段（用于更新 writing_state 的“上一章结尾摘要”）

### Step 2：更新 AIBook3 当前卷状态文件

读取当前项目工作区内的当前卷状态文件，并根据定稿正文内容自动更新。第一卷固定为：

`设定/大纲内容/第一卷/第一卷当前写作状态.md`

第二卷及以后按同结构路径更新：

`设定/大纲内容/第N卷/第N卷当前写作状态.md`

必须更新以下字段：
- **已定稿章节/已写章节**：追加本次定稿章节
- **章↔节拍映射表（一点五节）**：追加一行"正文章号 | 章名 | 对应节拍 | 登记日期"；对应节拍取自本章 `/chapter-plan` 的"对应节拍"字段（缺失时按事件链节拍内容比对正文确定）。已登记行不再变动。节拍制总约定见《第一卷事件链》第零节
- **当前可写章节/当前章节**：更新为下一章，并标注下一章计划承接的节拍范围
- **上一章结尾摘要**：用 2-3 句话概括定稿章节结尾的关键状态
- **主角当前状态**：
  - 变身适应阶段：根据正文中主角对女性身体的适应表现更新
  - 已展示的能力：如有新展示的能力则追加
  - 已登场关系：如有新角色登场或关系变化则更新
- **活跃伏笔/预定伏笔表**：根据正文新增/回收的伏笔更新
- **下一章任务卡/本章大纲要点**：从当前卷节拍节奏表、事件链和章节细纲中提取下一章（下一节拍）要点

### Step 3：生成章节摘要

基于定稿正文，生成一段 200 字左右的剧情摘要，包含：
- 本章核心事件（1-2 句）
- 主角关键行动/内心变化（1 句）
- 伏笔埋设/回收情况（如有，1 句）
- 章末钩子/关键转折（1 句）

将摘要追加到 `D:/Users/yueguang/NovelFlow/references/chapter_summaries.md`，格式为：

```text
## 第X章 标题
（摘要正文）
```

### Step 4：章节存入 Qdrant

调用 `ingest_chapter` MCP 工具，将定稿正文独立入库：
- `chapter_number`：从正文提取的章节号
- `chapter_title`：从正文提取的章节标题
- `text`：完整定稿正文

### Step 5：同步 references + 重新入库

依次执行以下命令：

1. `node D:/Users/yueguang/NovelFlow/scripts/sync-aibook3-to-references.js`
2. `node D:/Users/yueguang/NovelFlow/novel-qdrant-mcp/scripts/ingest-references.js`

若当前环境无法执行脚本（例如缺少 shell、Node 环境或外网向量服务暂不可用），不得假装成功；报告中标注同步失败，并优先使用 NovelQdrant MCP 对本次新增权威片段做最小入库。

### Step 6：校验 references 状态

同步脚本成功后，检查 `D:/Users/yueguang/NovelFlow/references/writing_state.md` 是否已经反映 AIBook3 当前卷状态。注意：当前同步脚本不会自动覆盖手写的 `writing_state.md` 和 `foreshadow_tracker.md`；若 references 状态未更新，必须手动同步对应摘要或在报告中标注 references 状态未更新。任何情况下，AIBook3 当前卷状态仍是权威源，不得把 references 当成更高优先级来源。

### Step 7：更新 foreshadow_tracker.md

读取当前 `D:/Users/yueguang/NovelFlow/references/foreshadow_tracker.md`，根据定稿正文内容：
- 新增伏笔 → 加入“已埋未收”表
- 已回收伏笔 → 从“已埋未收”移入“已回收”表
- 规则载体 → 如有新载体则追加到“规则载体追踪”表

### Step 8：清理或归档缓存文件

读取当前卷 `chapter_plan_cache.md`，将已定稿章节对应计划标注为"已定稿"并移入归档区，或从活跃计划区移除。同步读取当前卷 `write_brief_cache.md`，将已定稿章节对应 brief 标注为"已定稿"并移出活跃区。若任一缓存文件不存在，在完成报告中标注"无对应缓存可清理"，不影响定稿流程。

### Step 9：输出完成报告

全流程成功时，仅输出以下格式的简洁报告：

```text
✅ 定稿流程完成

📖 第X章「标题」已入库
🔄 references 已同步 + 向量库已更新
📝 AIBook3 当前卷状态已更新 → 当前进度：下一章
📌 foreshadow_tracker.md 已更新 → 活跃伏笔：X条 | 新增：X条 | 回收：X条
```

## 定稿后修改回灌（/refinalize 系列，2026-06-11 新增）

适用于**已定稿入库**的章节在事后被修改的场景，对应 `写作执行说明.md` 4.3 的三个修改级别。三个命令都以"用户已确认修改完成"为前提；目标章节必须已在 Qdrant chapter 集合中有旧条目，否则提示改用 `/finalize`。

通用步骤：先删除该章在 chapter 集合中的旧向量条目，再入库新正文（避免新旧并存污染召回）；删除不被 MCP 支持时标注"需手动清理"。

1. `/refinalize-text-only`（小修：错字、AI腔、虚感比喻）：
   - 重灌该章向量（删旧+入新）→ 执行 Step 5 同步。
   - **不**更新状态文件、章节摘要和伏笔表。
   - 报告：`✅ 第X章正文已重灌（小修），状态/摘要/伏笔未变动。`
2. `/refinalize`（中修：改动作、反应、对白，不改事件结果）：
   - 重灌该章向量 → 按 Step 3 重新生成该章摘要并**覆盖** `chapter_summaries.md` 中对应条目 → 执行 Step 5 同步。
   - 若该章恰好是最新定稿章，按 Step 2 更新当前卷状态文件的"上一章结尾摘要"。
   - 伏笔表只在修改触碰伏笔句时按 Step 7 复核。
3. `/refinalize-major`（大修：改事件结果、胜负、身份暴露、关系走向）：
   - 前提：必须已走完 `/rewrite-plan` 重写流程并通过 `/rewrite-final-check`。
   - 等同重新定稿：删旧向量后完整执行 Step 1-9（状态、摘要、伏笔、缓存全量复核）。
   - 完成后必须提示：`⚠️ 大修可能影响下游章节，请对后续已写章节执行 /continuity-check。`

## 拆章入库清理口径（/split-chapter C 层）

当 `/split-chapter` 流程涉及定稿后拆章时，本 skill 负责 C 层入库清理。A/B 层由新章节规划 skill 执行完成后，按以下步骤执行：

### C1：清理 Qdrant 旧数据

删除原章节号在 chapter 集合中的旧向量条目。若 MCP 工具不支持按章节号删除，标注"需手动清理"并在完成报告中列出待删除的章节号。

### C2：重新定稿入库

对拆分后的每章重新执行 `/finalize` 入库流程（Step 1-9）。若拆分后某章正文不完整（如切割点缺失），提示用户先补完正文再入库。

### C3：同步 references

若 `D:/Users/yueguang/NovelFlow/references` 有旧章节号文件，删除旧文件并同步新文件。执行 Step 5 的同步脚本。

### 完成报告

C 层完成后，在 `/split-chapter` 完成报告中追加：

```text
📦 C 层入库清理完成
  - Qdrant 旧数据：已删除第X章旧条目
  - 重新入库：第X章、第Y章、第Z章已入库
  - references：已同步
```

## 定稿流程注意事项

- 如果 Step 5 的脚本执行失败，跳过脚本重建，在报告中标注 `⚠️ references 同步/全量入库失败`；若已用 MCP 完成本次片段入库，也要单独说明。
- Step 5 失败不阻塞 Step 6/7/8/9 执行；Step 4 失败时，跳过 Step 5，优先使用 MCP 做最小入库后继续 Step 6/7/8/9，并在报告中标注部分失败。
- AIBook3 当前卷状态文件和 foreshadow_tracker.md 的更新必须基于对定稿正文的实际分析，不能凭空编造。
- 如果无法从正文中提取章节号，默认使用 AIBook3 当前卷状态文件中记录的当前可写章节。
- 收到 `/write` 时，提示用户切换到 `novel_flow_sanyue_full` 执行；本 skill 不处理续写。
