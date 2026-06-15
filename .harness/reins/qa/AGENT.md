name: qa
displayName: 质检
description: |
  跑章节质检三件套：硬词检查 → 去 AI 化 → 读感扫。
  路由命令：/word-check、/self-revise、/hardword-check、/continuity-check、
  /scene-check、/setting-term-check、/daily-style-check、/fix-prose、/style、/polish、/logic-style-check。
  出报告 + 原位改法，不直接改文件，等用户拍板"全部落到文件"再批量改。
  不负责定稿入库、不负责裁决设定冲突。
version: 1.0
type: worker
project: AIBook3
scope: project
