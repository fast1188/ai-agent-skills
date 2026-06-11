# Claude Code 项目开发规范

> 由 AGENT_RULES.md v2.0 生成。请勿直接编辑,改 master 后跑 `convert.py`。

---

# 第一原则

任何修改代码之前,**必须先理解项目**。**禁止直接开始编写代码**。

执行流程:
1. 阅读 README.md
2. 阅读 ARCHITECTURE.md
3. 阅读 CURRENT_TASK.md
4. 阅读 BUG_HISTORY.md
5. 阅读 CODING_RULES.md
6. 阅读 CHANGELOG.md
7. 分析项目结构
8. 输出实施方案
9. 等待确认
10. 开始开发

---

# 开发流程

## Phase 1 分析
- 当前需求
- 影响模块
- 风险点
- 数据流
- API 影响
- 数据库影响

## Phase 2 设计(禁止写代码)
- 修改方案
- 文件清单
- 影响范围
- 回滚方案

## Phase 3 编码
- 小步提交
- 模块化开发
- 保持兼容
- 不破坏已有功能

## Phase 4 测试(必须通过)
Python:`ruff check .` `black .` `mypy .` `pytest`
Node:`npm run lint` `npm run build` `npm run test`

---

# 禁止事项

**禁止删除**:核心代码、数据库模型、API、配置(除非批准)
**禁止重构**:全项目重构、大目录迁移、大重命名、改公共 API(除非批准)
**禁止引入**:闭源/收费/未维护/高风险依赖,优先 MIT / Apache-2.0
**禁止硬编码**:`API_KEY = "xxx"`,必须用 `os.getenv()`

---

# Git 规范

每次修改后输出:修改文件清单 + 修改内容说明 + commit。

```
feat: 增加用户登录接口
fix: 修复支付回调错误
docs: 更新部署文档
refactor: 优化用户模块结构
```

---

# 代码质量

- 单文件 ≤ 500 行
- 单函数 ≤ 100 行
- 单类 ≤ 300 行
- 重复代码 < 5%
- 命名:`user_name` / `get_user_info()` / `UserService`

---

# 日志

必须用 `logger.info/warning/error()`,**禁止 `print()` 用于生产代码**。

---

# 异常处理

**禁止** `except: pass`。必须:
```python
except Exception as e:
    logger.error(str(e))
```

---

# 安全

禁止提交 `.env` / `*.key` / `*.pem` / `cookies.json` / `session.json`。
API Key / Token / Cookie / 密码 **必须脱敏**(`sk-****7890`)。

---

# 数据库

**禁止** `SELECT *`,必须指定字段。
所有变更必须提供 Migration + 回滚方案。

---

# API

新增 API 必须有:请求示例、响应示例、错误码。

---

# 文档同步

修改功能后必须同步更新:
- `README.md`
- `ARCHITECTURE.md`
- `CURRENT_TASK.md`
- `BUG_HISTORY.md`
- `CHANGELOG.md`

---

# 开源发布

发布前检查:README(完整)、LICENSE(MIT 优先)、Issue 模板、PR 模板。

---

# Token 中转站专项

禁止存储:聊天内容、图片、文件、API Key。
必须支持:多供应商切换、自动重试、熔断、限流、日志脱敏。
架构分层:Provider / Model / Billing / User / Admin。

---

# Agent 工作原则

1. 先分析
2. 再设计
3. 后编码
4. 再测试
5. 最后更新文档

禁止直接写代码、猜测需求、为了完成任务而破坏架构。

完整规范:https://github.com/fast118/ai-agent-skills/blob/main/shared/agent-rules/AGENT_RULES.md