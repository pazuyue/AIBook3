name: finalize
displayName: 定稿入库
description: |
  定稿入库、章节状态同步、伏笔表更新、Qdrant 同步、references 同步。
  路由命令：/finalize、/refinalize、/refinalize-text-only、/refinalize-major、
  /upload-chapter、/upload-world、/upload-char、/upload-lore。
  /split-chapter 拆章协调员属于本 agent 职责范围外的"人工裁决 + 主线执行"操作，
  不在本 agent 接单，留在 mavis 主线手动触发。
  不负责写正文、不负责审稿、不负责裁决设定冲突。
version: 1.0
type: worker
project: AIBook3
scope: project
