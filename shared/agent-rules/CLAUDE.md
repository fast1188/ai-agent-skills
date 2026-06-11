# AI Agent 项目开发总规范 v2.0

> 由 AGENT_RULES.md 自动生成。不要直接编辑,改 master 后跑 convert.py

---

## Phase 1 分析

分析:

- 当前需求
- 影响模块
- 风险点
- 数据流
- API 影响
- 数据库影响

**输出分析结果**。

---

## Phase 2 设计

输出:

- 修改方案
- 文件清单
- 影响范围
- 回滚方案

**禁止直接写代码**。

---

## Phase 3 编码

要求:

- 小步提交
- 模块化开发
- 保持兼容
- 不破坏已有功能

---

## Phase 4 测试

必须执行:

**Python 项目**

```bash
ruff check .
black .
mypy .
pytest
```

**Node 项目**

```bash
npm run lint
npm run build
npm run test
```

**测试通过后才能结束任务**。

---

**禁止事项**

绝对禁止:

## 禁止删除

禁止删除:

- 核心业务代码
- 数据库模型
- API 接口
- 配置文件

**除非明确获得批准**。

---

## 禁止重构

禁止:

- 全项目重构
- 大规模目录迁移
- 大规模重命名
- 修改公共 API

**除非明确获得批准**。

---

## 禁止引入

禁止引入:

- 闭源依赖
- 收费依赖
- 未维护依赖
- 高风险依赖

**优先使用**:

- MIT
- Apache-2.0

协议项目。

---

## 禁止硬编码

禁止:

```python
API_KEY = "xxxx"
PASSWORD = "xxxx"
```

必须:

```python
os.getenv()
```

读取环境变量。

---

**Git 规范**

每次修改后:

先输出:

## 修改文件

例如:

- app/main.py
- app/api/user.py

---

## 修改内容

说明:

- 新增
- 删除
- 修复

---

## Git Commit

使用规范:

```bash
feat:
fix:
docs:
refactor:
test:
chore:
```

示例:

```bash
feat: 增加用户登录接口
fix: 修复支付回调错误
docs: 更新部署文档
refactor: 优化用户模块结构
```

---

**代码质量规范**

## 文件长度

单文件:

**≤ 500 行**

超过必须拆分。

---

## 函数长度

单函数:

**≤ 100 行**

超过必须拆分。

---

## 类长度

单类:

**≤ 300 行**

超过必须拆分。

---

## 重复代码

重复率:

**< 5%**

必须抽象公共模块。

---

## 命名规范

变量:

```python
user_name
```

函数:

```python
get_user_info()
```

类:

```python
UserService
```

**禁止**:

```python
a
b
tmp
test1
```

这种无意义命名。

---

**日志规范**

**必须**:

```python
logger.info()
logger.warning()
logger.error()
```

**禁止**:

```python
print()
```

用于生产代码。

---

**异常处理规范**

**禁止**:

```python
except:
pass
```

**必须**:

```python
except Exception as e:
logger.error(str(e))
```

记录异常。

---

**安全规范**

发布前必须检查:

## 不允许提交

```text
.env
.env.local
.env.production

*.key
*.pem

database.db

cookies.json

session.json
```

---

## API 安全

禁止记录:

- 用户 API Key
- 用户 Token
- 用户 Cookie
- 用户密码

日志必须脱敏。

例如:

```text
sk-1234567890
```

显示:

```text
sk-****7890
```

---

**数据库规范**

**禁止**:

```sql
SELECT *
```

必须指定字段。

---

所有数据库变更:

必须提供:

- Migration
- 回滚方案

---

**API 规范**

新增 API 必须:

提供:

- 请求示例
- 响应示例
- 错误码

例如:

```json
{
"code": 0,
"message": "success",
"data": {}
}
```

---

**文档同步规范**

修改功能后:

必须同步更新:

## README.md

更新:

- 功能介绍
- 使用说明

---

## ARCHITECTURE.md

更新:

- 架构变化
- 模块变化

---

## CURRENT_TASK.md

更新:

- 当前任务状态

---

## BUG_HISTORY.md

记录:

- BUG 原因
- 修复方案
- 修复时间

---

## CHANGELOG.md

记录:

- 新功能
- 修复内容
- 版本号

---

**开源发布规范**

发布到 GitHub 或 Gitee 前:

必须检查:

## README

包含:

- 项目介绍
- 功能说明
- 安装教程
- 配置教程
- API 文档
- 开发文档
- 常见问题
- License

---

## LICENSE

优先:

**MIT License**

其次:

**Apache License 2.0**

---

## Issue 模板

必须生成:

```text
.github/ISSUE_TEMPLATE
```

---

## PR 模板

必须生成:

```text
.github/PULL_REQUEST_TEMPLATE.md
```

---

**Token 中转站专项规范**

如果项目属于:

- OpenAI 兼容接口
- Claude 兼容接口
- Gemini 兼容接口
- AI 聚合网关
- **Token 中转站**

额外要求:

---

禁止存储:

- 用户聊天内容
- 用户图片
- 用户文件
- 用户 API Key

---

必须支持:

- 多供应商切换
- 自动重试
- 熔断机制
- 限流机制
- 日志脱敏

---

必须设计:

- Provider 层
- Model 层
- Billing 层
- User 层
- Admin 层

**解耦架构**。

---

**Agent 工作原则**

始终遵守:

1. 先分析
2. 再设计
3. 后编码
4. 再测试
5. 最后更新文档

---

**禁止**:

- 直接写代码
- 猜测需求
- 为了完成任务而破坏架构

---

**目标**:

构建一个长期维护、生产可用、可商业化、可开源发布、高质量的软件项目。


...(详见 master)

## 唯一允许建文件夹的地方

1. **`D:\Claude解决各种问题\`** —— AI Agent 专属工作区(主战场)
2. **`C:\Users\Administrator\.claude\projects\D--Claude------\`** —— 记忆系统(Claude 自带)
3. **`C:\Users\Administrator\Desktop\`** —— 桌面(已建 AI-Agent-Rules 文件夹,这是终点,不再加)

## 绝对禁止建的地方

- ❌ D: 根(Users/、tmp/、articles/ 等)
- ❌ C: 根
- ❌ C: 任何非 .claude / Desktop 的目录
- ❌ 其他任何盘符
- ❌ 系统目录(ProgramData/、System32/、AppData/ 等)
- ❌ Users/Administrator/ 下的 Downloads、Documents、Music 等

## 文件散落禁止

- ❌ 不能在 D:/ 根 / 桌面 单独扔 .py / .md / .json
- ✓ 所有工作文件必须在 `D:\Claude解决各种问题\` 下分类目录

## 违反处理

发现违规时,先转移文件到正确位置 → 删除散落的文件 → 写明原因。

---

**版本:** 2.0.0
**更新日期:** 2026-06-11
**适用工具:** Claude Code, Codex, Cursor Agent, OpenClaw, Hermes, 等
**License:** MIT
