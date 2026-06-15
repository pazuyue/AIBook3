name: aibook3-team
displayName: AIBook3 写作天团
description: |
  4 个并列 worker agent + mavis 主线调度（Master 总导演制）。
  4 个 worker 互不重叠、独立可路由、问什么答什么；
  Master 留在 mavis 主线（即 Mavis 自己），按章节类型 + 风险等级选最短流程。
version: 1.0
type: team
project: AIBook3
scope: project
roster:
  - writer      # 写手：/write /write-brief /chapter-plan /chapter-review
  - qa          # 质检：硬词→去 AI→读感 三步走
  - canon       # 设定审校：/review /check-setting /check-outline /check-skill /plot-review
  - finalize    # 定稿入库：/finalize /refinalize* /upload-*
out_of_scope:
  - /split-chapter  # 拆章协调员，留在 mavis 主线手动触发
  - /rewrite-plan /rewrite-next /rewrite-check /rewrite-fix /rewrite-final-check  # 章节重写流程，频次低、影响大，留 mavis 主线
