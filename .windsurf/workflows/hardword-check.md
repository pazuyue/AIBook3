# /hardword-check

Description: 按 Trae 定稿前检查 skill 执行 `/hardword-check`。

## Source of truth
- 读取并服从 `.trae\rules\三月女神定稿前检查skill.md`。
- 硬词表以 `设定\文风设定.md` 为准，术语类按 `设定\术语口径统一表.md` 判断。

## Steps
1. 只做硬词、套路句和 AI 腔复查，不套完整 `/review`。
2. 默认检查当前章；用户指定章节或贴正文时按指定对象检查。
3. 命中不等于机械删除，必须给原位改法。
4. 额外检查诊断式旁白：过分端正、用力太均匀、节奏太稳、没有半点迟疑、找不出半点摸索感、不该有的分辨率、像精密仪器等。
5. 术语类风险转入或同步执行 `/setting-term-check` 口径。
6. 按 Trae skill 固定格式输出。
