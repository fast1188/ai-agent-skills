# Cursor Go Project Rules

# 版本
- Go 1.21+
- go mod 依赖管理

# 命名
- 导出:PascalCase
- 私有:camelCase
- 包:小写单词
- 接口:小接口(1-3 方法),-er 结尾

# 错误处理
- err 显式处理,不忽略
- 不使用 panic 处理业务错误
- 包装:fmt.Errorf("ctx: %w", err)

# 测试
- 标准库 testing
- testify 断言
- 表驱动测试

# 并发
- channel 用于通信
- mutex 用于共享状态
- 避免 goroutine 泄漏

# 代码组织
- 按功能分包,不按层
- internal/ 用于私有代码
- cmd/ 用于 main 函数