---
name: multi-agent-install
description: One-click installer for Claude Code + Codex + Cursor Agent + OpenClaw + Hermes Agent. Sets up all major AI coding agents with proper config.
version: 1.0.0
author: fast118
license: MIT
applies_to: [claude-code, codex, cursor, openclaw, hermes]
---

# multi-agent-install

> **5 分钟一键装好 5 个主流 AI 编程工具**
>
> Claude Code + Codex + Cursor Agent + OpenClaw + Hermes Agent

## 这是什么?

一个 shell 脚本,自动检测你的系统,一键装好 5 个主流 AI 编程工具:

| 工具 | 类型 | 安装方式 |
|------|------|----------|
| **Claude Code** | CLI | npm |
| **Codex** | CLI | npm (OpenAI) |
| **Cursor Agent** | IDE | download .exe / .dmg |
| **OpenClaw** | CLI | npm |
| **Hermes Agent** | CLI | pip |

## 安装这个 skill

### Windows
```bash
install.bat
```

### Linux/Mac
```bash
chmod +x install.sh && ./install.sh
```

## 使用

装好 skill 后,运行 **install-all.bat** 或 **install-all.sh**:

### Windows
```cmd
multi-agent-install\install-all.bat
```

### Linux/Mac
```bash
chmod +x multi-agent-install/install-all.sh
./multi-agent-install/install-all.sh
```

脚本会:
1. 检测 OS(Windows / macOS / Linux)
2. 检测已安装的工具
3. 提示选择要装的工具(默认全选)
4. 逐个安装 + 验证
5. 输出安装报告

## 安装过程

```
======================================
 multi-agent-install v1.0
======================================

Detecting system...
  OS: Windows 11
  Shell: cmd
  Package manager: npm, pip

Checking existing tools...
  [OK] Node.js v20.10.0
  [OK] Python 3.13.13
  [MISS] Claude Code
  [MISS] Codex
  [OK] Cursor (auto-detected)
  [MISS] OpenClaw
  [MISS] Hermes Agent

Install which tools?
  [1] Claude Code    [y/N]: y
  [2] Codex         [y/N]: y
  [3] Cursor Agent  [y/N]: y
  [4] OpenClaw      [y/N]: y
  [5] Hermes Agent  [y/N]: y

Installing Claude Code...
  [OK] npm install -g @anthropic-ai/claude-code
  [OK] claude --version

Installing Codex...
  [OK] npm install -g @openai/codex
  ...

======================================
 Installation complete!
======================================

Installed:
  - Claude Code v2.0.0
  - Codex v1.2.0
  - Cursor Agent (existing)
  - OpenClaw v0.8.1
  - Hermes Agent v1.5.0

Next: see README.md in this repo for skill setup.
```

## 高级选项

### 只装某个工具
```bash
./install-all.sh --only claude-code
```

### 跳过 IDE 类工具(只装 CLI)
```bash
./install-all.sh --cli-only
```

### 静默安装(用默认选项)
```bash
./install-all.sh --yes
```

## 系统要求

| OS | 要求 |
|----|------|
| Windows | Node.js 18+, Python 3.8+, PowerShell 5+ |
| macOS | Node.js 18+, Python 3.8+, Xcode CLT |
| Linux | Node.js 18+, Python 3.8+, build-essential |

## 相关项目

- [free-ai-router](https://github.com/fast1188/free-ai-router)
- [ai-agent-skills](https://github.com/fast1188/ai-agent-skills)

## 许可证

MIT