# Cursor Python Project Rules

# 版本
- Python 3.10+
- 类型注解(强制,所有公共 API)

# 风格
- Black + Ruff
- 命名:snake_case
- 文档字符串:Google 风格

# 依赖
- Poetry 或 pip-tools
- 不引入未维护包

# 架构
- 分层: api / service / repository
- 不在 controller 里写业务逻辑
- DB 访问只在 repository 层
- 业务逻辑在 service 层

# 测试
- pytest
- 覆盖率 ≥ 80%
- 集成测试用 testcontainers

# 异步
- async / await 优先
- 不在同步函数里调用阻塞 IO

# 错误处理
- 自定义异常继承 AppError
- 不吞异常
- 异常信息要可操作