---
name: api-prompts
description: 提示词模板库 - 50+ Claude Code 实战 prompt 模板,涵盖代码、文档、调试、重构等场景
version: 1.0.0
author: fast118
license: MIT
applies_to: [claude-code, codex, cursor]
---

# api-prompts

> 50+ Claude Code 实战 prompt 模板,即用即生效

## 这是什么?

`api-prompts` 是按场景分类的**高质量 prompt 模板库**。每个 prompt 都是**经过验证**(实测有效),不是网上抄的那种空洞 prompt。

## 分类

### 1. 代码生成(8 个)

- `gen-function.md` - 函数生成(类型注解 + docstring + 测试)
- `gen-class.md` - 类生成(OOP 设计 + 最佳实践)
- `gen-api.md` - REST API 生成(完整路由 + 验证 + 错误处理)
- `gen-script.md` - 一次性脚本(异常处理 + 日志)
- `gen-cli.md` - CLI 工具(argparse + 子命令)
- `gen-test.md` - 测试生成(覆盖率 80%+)
- `gen-config.md` - 配置文件生成(yaml / toml / json)
- `gen-dockerfile.md` - Dockerfile 生成(多阶段 + 优化)

### 2. 代码审查(6 个)

- `review-security.md` - 安全审查(SQL 注入 / XSS / 密钥泄露)
- `review-performance.md` - 性能审查(O(n²) → O(n))
- `review-style.md` - 代码风格(PEP 8 / 项目约定)
- `review-arch.md` - 架构审查(分层 / 解耦 / 可测试)
- `review-error.md` - 错误处理审查(异常覆盖)
- `review-test.md` - 测试覆盖审查(覆盖率 + 边界)

### 3. 重构(5 个)

- `refactor-class.md` - 过程式 → OOP
- `refactor-split.md` - 大函数拆分
- `refactor-name.md` - 命名优化
- `refactor-coupling.md` - 解耦(依赖注入)
- `refactor-test.md` - 加测试不改行为

### 4. 调试(5 个)

- `debug-error.md` - 找 bug
- `debug-perf.md` - 找性能瓶颈
- `debug-memory.md` - 找内存泄漏
- `debug-network.md` - 找网络问题
- `debug-concurrency.md` - 找并发问题

### 5. 文档(6 个)

- `doc-readme.md` - README 生成
- `doc-api.md` - API 文档(OpenAPI)
- `doc-architecture.md` - 架构文档
- `doc-changelog.md` - CHANGELOG
- `doc-comment.md` - 加代码注释
- `doc-readme-zh.md` - 中文 README

### 6. 中文开发(5 个)

- `zh-explain.md` - 让 AI 用中文解释代码
- `zh-translate.md` - 翻译英文文档成中文
- `zh-review.md` - 中文代码审查
- `zh-commit.md` - 中文 commit message
- `zh-doc.md` - 写中文技术文档

### 7. 测试(5 个)

- `test-unit.md` - 单元测试
- `test-integration.md` - 集成测试
- `test-e2e.md` - 端到端测试
- `test-perf.md` - 性能测试
- `test-coverage.md` - 提高覆盖率

### 8. 高级(5 个)

- `advanced-architect.md` - 架构设计
- `advanced-security.md` - 安全审计
- `advanced-refactor.md` - 大型重构
- `advanced-migrate.md` - 代码迁移(框架升级)
- `advanced-monitor.md` - 性能监控

## 用法

**CLI 方式:**
```bash
py ~/.claude/skills/api-prompts/show.py review-security
```

**直接复制:**
模板在 `prompts/` 目录下,挑你要的 .md 文件打开,粘到 Claude Code 即可。

**配合其他 skill:**
```bash
# 用 token-saver 先压缩,再调 API
py ~/.claude/skills/token-saver/compress.py "$(cat prompts/review-security.md)"
```

## 安装

```bash
git clone https://github.com/fast118/ai-agent-skills
cd ai-agent-skills/claude-code/api-prompts
install.bat
```

## 模板示例

### review-security.md

```markdown
审查以下代码的安全问题:

1. SQL 注入风险
2. XSS 风险
3. 密钥泄露
4. 权限提升
5. CSRF
6. 不安全反序列化
7. 路径遍历
8. 敏感信息日志

对每个问题:
- 位置(file:line)
- 风险等级(高/中/低)
- 修复代码
- 测试用例
```

## 相关项目

- [token-saver](../token-saver/) - 压缩 prompt
- [chinese-dev-helper](../chinese-dev-helper/) - 中文开发
- [ai-agent-skills](https://github.com/fast118/ai-agent-skills) - 11 个 skills

## License

MIT