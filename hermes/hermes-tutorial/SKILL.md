---
name: hermes-tutorial
description: Hermes Agent 中文教程 skill。从入门到精通,包含安装、配置、常用命令、API 集成、实战示例。
version: 1.0.0
author: fast118
license: MIT
applies_to: [hermes]
---

# hermes-tutorial

> Hermes Agent 中文教程
>
> 从入门到精通的中文实战指南

## 这是什么?

Hermes Agent(NousResearch 出品)是一个**自学习的 AI 代理**,号称"the agent that grows with you"(跟你一起成长的代理)。

跟 Claude Code / Codex 不一样:

| 特性 | Hermes | Claude Code / Codex |
|------|--------|---------------------|
| 自学习 | ✅(随使用改进) | ❌ |
| 长期记忆 | ✅ | 部分 |
| 本地部署 | ✅ | 部分 |
| 中文支持 | 一般 | 一般 |
| 开源 | ✅ 完全 | 部分 |

## 适合谁?

- 想要**长期记忆**的 AI 助手(它会记得你的偏好)
- 想要**自托管**(不想依赖云)
- 想要**自学习**(用得越久越聪明)
- 不怕折腾(安装配置比 Claude Code 复杂)

## 安装

### 一键安装

```bash
git clone https://github.com/fast1188/ai-agent-skills
cd ai-agent-skills/hermes/hermes-tutorial
chmod +x install.sh
./install.sh
```

### 手动安装

```bash
pip install hermes-agent
hermes init
```

## 5 分钟上手

### Step 1:初始化

```bash
hermes init
```

会问几个问题:
- 你的名字
- 偏好语言(中文 / English)
- API 提供商(推荐选 api.skillai.top 国内直连)
- 模型(默认 llama-3.3-70b)

### Step 2:第一次对话

```bash
hermes chat
```

会进入交互模式,试试:

```
你: 你好,记住我是一名 Python 开发者,偏好中文交流
Hermes: 好的,已记录。
你: 我刚才说的什么?
Hermes: 你是 Python 开发者,偏好中文交流。
(关闭再开,记忆还在)
```

### Step 3:加 skill

Hermes 的 skill 跟 Claude Code 类似,放 `~/.hermes/skills/` 目录。

这个仓库的所有 skill 都可以直接复制过来用:

```bash
# 复制 api-fallback 到 Hermes
cp -r ../claude-code/api-fallback ~/.hermes/skills/
```

## 常用命令

| 命令 | 功能 |
|------|------|
| `hermes init` | 初始化配置 |
| `hermes chat` | 进入对话模式 |
| `hermes skill list` | 列出已装 skill |
| `hermes skill install <path>` | 安装 skill |
| `hermes memory show` | 查看记忆 |
| `hermes memory clear` | 清空记忆 |
| `hermes config` | 编辑配置 |
| `hermes serve` | 启动 Web 服务 |
| `hermes update` | 更新 Hermes |

## 配置示例

`~/.hermes/config.toml`:

```toml
[model]
provider = "openai"
base_url = "https://api.skillai.top"  # 国内直连
api_key = "your-key"
default = "llama-3.3-70b-versatile"

[memory]
type = "sqlite"
path = "~/.hermes/memory.db"
long_term_enabled = true

[ui]
language = "zh"
theme = "dark"

[skills]
auto_load = true
allow_network = true
```

## 实战示例

### 场景 1:长期项目助手

```bash
# 启动一个长期项目
hermes project init my-saas
# 进入项目目录,启动 Hermes
cd my-saas && hermes chat
```

Hermes 会记住:
- 项目架构
- 你的命名偏好
- 之前讨论过的方案

### 场景 2:团队知识库

```bash
# 启动 Web 服务
hermes serve --port 8080
```

团队成员可以浏览器访问,跟同一个 Hermes 实例对话,共享记忆。

### 场景 3:对接 Claude Code

```bash
# Hermes 作为 Claude Code 的"大脑"
hermes mcp serve
```

在 Claude Code 配置:
```json
{
  "mcpServers": {
    "hermes": {
      "command": "hermes",
      "args": ["mcp", "serve"]
    }
  }
}
```

Claude Code 调用 Hermes 的长期记忆 + 自学习能力。

## 配 Hermes + Claude Code

| 场景 | 谁来跑 |
|------|--------|
| 重活(架构、复杂) | Claude Code |
| 长记忆(项目历史、用户偏好) | Hermes |
| 简单代码生成 | Claude Code |
| 长期迭代 | Hermes |

**最佳实践:** Claude Code 做"前台",Hermes 做"后台记忆"。

## 国内直连(可选)

如果 Hermes 在国内访问 API 慢,可以用中转:

```toml
[model]
base_url = "https://api.skillai.top"
```

[sapi.skillai.top](https://api.skillai.top) 提供:
- Claude / GPT / Gemini / Llama 全模型
- 价格低至官方 1/3
- 国内直连

## 故障排查

### 安装失败

```bash
pip install --upgrade pip
pip install hermes-agent
```

### 模型不响应

```bash
# 测试 API 连通性
hermes doctor
```

### 记忆丢失

```bash
hermes memory show
# 检查 ~/.hermes/memory.db 是否存在
```

## 进阶:MCP 集成

Hermes 支持 Model Context Protocol,可以接:

- GitHub(读 issues / PRs)
- 文件系统(读本地文档)
- 数据库(查数据)
- 自定义 HTTP API

详见:https://github.com/fast1188/ai-agent-skills

## 相关项目

- [free-ai-router](https://github.com/fast1188/free-ai-router)
- [ai-agent-skills](https://github.com/fast1188/ai-agent-skills)
- [api.skillai.top](https://api.skillai.top) - 国内直连

## 许可证

MIT