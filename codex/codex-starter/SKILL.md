---
name: codex-starter
description: Quick start kit for OpenAI Codex CLI. Pre-configured templates, common tasks, and best practices for new Codex users.
version: 1.0.0
author: fast118
license: MIT
applies_to: [codex]
---

# codex-starter

> OpenAI Codex CLI 5 分钟上手套装
>
> 预配置模板 + 常用任务 + 最佳实践

## 这是什么?

`codex-starter` 是一个 Codex CLI 新手套件,包含:

- 预配置 `~/.codex/config.toml`
- 常用 prompt 模板(代码生成 / 测试 / 重构)
- 最佳实践文档
- 避坑指南

## 为什么需要?

OpenAI Codex CLI 出来后,文档分散,新手不知道:

- ❓ 怎么配置 API key
- ❓ 哪些 prompt 模式最有效
- ❓ 怎么避免常见错误
- ❓ 怎么跟 Claude Code / Cursor 区分使用场景

这个 skill 把这些都打包好。

## 安装

### 一键安装

**Windows:**
```bash
install.bat
```

**Linux/Mac:**
```bash
chmod +x install.sh && ./install.sh
```

### 手动

```bash
# Codex 配置目录
mkdir -p ~/.codex/prompts

# 复制模板
cp config.toml ~/.codex/
cp prompts/*.md ~/.codex/prompts/
```

## 包含的模板

### config.toml(预配置)

```toml
# OpenAI Codex CLI 配置
[model]
default = "codex-mini"
max_tokens = 4096
temperature = 0.2

[ui]
theme = "dark"
show_token_usage = true
vim_mode = false

[safety]
confirm_destructive = true
max_auto_edits = 50

[telemetry]
enabled = true
```

### prompts/ 目录

- `code-review.md` —— 代码审查 prompt 模板
- `refactor.md` —— 重构 prompt 模板
- `test-gen.md` —— 测试生成 prompt 模板
- `doc-gen.md` —— 文档生成 prompt 模板
- `bug-fix.md` —— 修 bug prompt 模板

每个模板都是精炼的 prompt,直接 `/prompts:bug-fix` 用。

## 常用任务速查

### 任务1:代码审查

```bash
codex --prompt "$(cat ~/.codex/prompts/code-review.md)" src/
```

### 任务2:批量重构

```bash
codex refactor --style pep8 --tests src/*.py
```

### 任务3:生成测试

```bash
codex test --gen --framework pytest src/
```

### 任务4:文档生成

```bash
codex docs --format markdown src/api.py
```

## Claude Code vs Codex 何时用?

| 场景 | 推荐 |
|------|------|
| 复杂多步骤任务 | Claude Code |
| 快速代码生成 | Codex |
| 代码审查 | Codex |
| 大规模重构 | Claude Code |
| 测试生成 | Codex |
| 架构设计 | Claude Code |
| 文档写作 | Claude Code |
| Bug 修复 | 两者皆可 |

**经验法则:** 重活找 Claude Code,轻活找 Codex。

## 避坑指南

### ❌ 不要

```bash
# 不要在生产目录直接跑
codex --auto-apply .

# 不要给模糊指令
codex "fix the bug"

# 不要关闭安全检查
codex --no-confirm .
```

### ✅ 推荐

```bash
# 先 dry-run
codex --dry-run src/

# 指令要具体
codex "fix the TypeError in src/auth.py line 42"

# 保留安全检查
codex --interactive src/
```

## API 中转(可选)

如果 Codex 在国内访问慢,可以用中转 API:

```toml
# ~/.codex/config.toml
[api]
base_url = "https://api.skillai.top"  # 国内直连
api_key = "your-skillai-key"
```

[sapi.skillai.top](https://api.skillai.top) 提供 Claude / GPT / Gemini 全模型中转,价格低至官方 1/3。

## 相关项目

- [free-ai-router](https://github.com/fast118/free-ai-router) - 多 AI 后端 fallback
- [ai-agent-skills](https://github.com/fast118/ai-agent-skills) - 本仓库

## 许可证

MIT