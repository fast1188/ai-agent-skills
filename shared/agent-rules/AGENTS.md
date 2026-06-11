# Codex Agent 项目开发规范

> 由 AGENT_RULES.md v2.0 自动生成

---

# 第一原则
**禁止直接写代码**。先读 README / ARCHITECTURE / CURRENT_TASK / BUG_HISTORY / CODING_RULES / CHANGELOG,输出方案,等待确认。

# 流程
分析 → 设计 → 编码 → 测试 → 更新文档

# 禁止
- 删除核心代码/API/数据库模型(除非批准)
- 全项目重构(除非批准)
- 引入闭源/收费/未维护依赖
- 硬编码密钥/API Key

# Git
`feat:` `fix:` `docs:` `refactor:` `test:` `chore:`

# 质量
- 文件 ≤ 500 行,函数 ≤ 100 行,类 ≤ 300 行
- 命名规范:snake_case / PascalCase / UPPER_SNAKE
- 用 logger,不用 print

# 安全
不提交 .env / *.key / cookies.json。日志脱敏。

# 文档
改完同步 README / ARCHITECTURE / CHANGELOG。

# Token 中转站
禁止存聊天内容/图片/API Key。分层:Provider / Model / Billing / User / Admin。

完整:https://github.com/fast118/ai-agent-skills/blob/main/shared/agent-rules/AGENT_RULES.md