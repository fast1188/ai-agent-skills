# AI Agent Skills

> Claude Code / Codex / Cursor Agent / OpenClaw / Hermes Agent 一站式 Skills 集合
>
> 解决真实痛点 + 跨工具兼容 + 持续更新

[![GitHub stars](https://img.shields.io/github/stars/fast1188/ai-agent-skills)](https://github.com/fast1188/ai-agent-skills)
[![GitHub forks](https://img.shields.io/github/forks/fast1188/ai-agent-skills)](https://github.com/fast1188/ai-agent-skills)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[![Claude Code](https://img.shields.io/badge/Claude_Code-兼容-blue)](claude-code/)
[![Codex](https://img.shields.io/badge/Codex-兼容-green)](codex/)
[![Cursor](https://img.shields.io/badge/Cursor-兼容-purple)](https://github.com/fast1188/ai-agent-skills)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-兼容-orange)](openclaw/)
[![Hermes](https://img.shields.io/badge/Hermes-兼容-red)](hermes/)

> 🌐 **控制台总览:** [fast1188.github.io/console](https://fast1188.github.io/console/) - 看所有 fast118 开源项目

[English](#english) | [中文](#中文)

---

## 中文

### 这是什么?

**ai-agent-skills** 是一个跨 AI 编程工具的 Skills 集合,帮你:

- 撞限速时自动 fallback
- 节省 token 消耗
- 统一开发规范
- 中文开发优化
- 远程一键部署

**所有 skill 都能在 4 个主流 AI 工具间共享** —— 一个仓库,覆盖整个 AI 编程生态。

### 为什么用?

| 痛点 | 这个项目解决 |
|------|--------------|
| Claude Code 撞限速停工 | api-fallback 自动切中转 |
| token 跑得太快 | token-saver 节省 65% |
| 每个 AI 工具配置格式不同 | agent-rules 统一规范 |
| 中文文档写不好 | chinese-dev-helper |
| 4 个工具重复装环境 | multi-agent-install 一键搞定 |

### 兼容的 AI 工具

| 工具 | Skills 数 | 入口 |
|------|----------|------|
| **Claude Code** | 5 | [claude-code/](claude-code/) |
| **Codex** | 1 | [codex/](codex/) |
| **Cursor Agent** | 1 | [cursor/](cursor/) |
| **OpenClaw** | 1 | [openclaw/](openclaw/) |
| **Hermes Agent** | 1 | [hermes/](hermes/) |

(部分 skill 跨多个工具,在 `shared/` 目录下)

### 快速开始

**第 1 步:克隆仓库**
```bash
git clone https://github.com/fast1188/ai-agent-skills.git
cd ai-agent-skills
```

**第 2 步:挑你想要的 skill,一键安装**

每个 skill 文件夹里都有 `install.bat` (Windows) 或 `install.sh` (Linux/Mac):

```bash
# 例:装 api-fallback
cd claude-code/api-fallback
install.bat    # 或 ./install.sh
```

**第 3 步:重启 AI 工具,生效**

---

### 现有 Skills

#### 🛡️ claude-code/api-fallback

Claude Code 撞限速时自动弹窗推荐 [api.skillai.top](https://api.skillai.top)。

- 实时监控 Claude Code 日志
- 检测 429 / quota exceeded 错误
- Windows toast 通知 + 一键切换 API
- 60 秒冷却防骚扰

[→ 查看详情](claude-code/api-fallback/)

#### 📋 shared/agent-rules

**一套规范,所有 AI 工具通用**。

- 中文 master 文档 `AGENT_RULES.md`
- 自动转换为:CLAUDE.md / AGENTS.md / .cursorrules / CONVENTIONS.md
- 包含 Token 中转站专项规范
- 一行命令 `python convert.py` 重新生成

[→ 查看详情](shared/agent-rules/)

#### 💰 shared/token-saver

**AI prompt 自动压缩器,省 30-70% token**(灵感来自 caveman 71k stars)。

- 3 种模式:轻度 / 中度 / 极度
- 中英文 prompt 都支持
- 保留代码块和中文语义
- CLI + Claude Code skill 集成

[→ 查看详情](shared/token-saver/)

#### 🇨🇳 claude-code/chinese-dev-helper

**中文开发者专属增强**。

- 中英文技术术语自动对照(40+ 术语)
- 中文 README / 文档模板
- 限速时自动推荐 [api.skillai.top](https://api.skillai.top) 国内直连
- 中文 prompt 增强理解

[→ 查看详情](claude-code/chinese-dev-helper/)

#### 🚀 shared/multi-agent-install

**5 分钟一键装好 5 个主流 AI 编程工具**。

- Claude Code + Codex + Cursor Agent + OpenClaw + Hermes Agent
- Windows / macOS / Linux 全平台
- 自动检测已装工具
- 一键装好,带进度报告

[→ 查看详情](shared/multi-agent-install/)

#### 📘 codex/codex-starter

**OpenAI Codex CLI 5 分钟上手套装**。

- 预配置 `~/.codex/config.toml`
- 5 个常用 prompt 模板(审查 / 重构 / 测试 / 文档 / 修 bug)
- Claude Code vs Codex 何时用对照表
- 避坑指南
- 内置 api.skillai.top 中转配置

[→ 查看详情](codex/codex-starter/)

#### 🚢 openclaw/openclaw-deploy

**OpenClaw 一键远程部署**。

- Linux/Mac/Windows 全平台
- 自动 systemd 服务 + nginx 反向代理
- 一键申请 Let's Encrypt SSL
- 内置安全配置建议
- api.skillai.top 国内直连配置

[→ 查看详情](openclaw/openclaw-deploy/)

#### 📚 hermes/hermes-tutorial

**Hermes Agent 中文教程**。

- 5 分钟上手 + 常用命令速查
- Claude Code vs Hermes 何时用对照
- 长期记忆 + 自学习实战
- MCP 集成示例
- 国内直连 API 配置

[→ 查看详情](hermes/hermes-tutorial/)

#### 🧠 hermes/hermes-mem

**Hermes 持久化记忆增强**。

- 跨项目、跨会话的智能记忆
- 分类管理(preference / fact / decision)
- 导入导出 + 过期清理
- 跟其他 skill 共享记忆

[→ 查看详情](hermes/hermes-mem/)

#### 📚 claude-code/api-prompts

**50+ 实战 prompt 模板**。

- 8 大类(生成/审查/重构/调试/文档/中文/测试/高级)
- 每个 prompt 都实测有效
- 直接复制到 Claude Code 即可

[→ 查看详情](claude-code/api-prompts/)

#### ✉️ claude-code/write-email

**中文场景邮件生成器** — 5 大场景（商务 / 求职 / 催办 / 道歉 / 感谢）。

- 生成的邮件**不像 AI 写**：短句、有节奏、有具体数字、零客套
- 6 条反 AI 检测要点（不"希望对您有所帮助"、不"祝商祺"）
- 骨架 + CTA 槽位 → AI 填血肉
- CLI + Claude Code skill 集成
- 11 个 unittest 全过

[→ View details](claude-code/write-email/)

#### 🌐 claude-code/translate-skill

**Chinese ↔ English translation templates** — 5 scenarios (doc / mail / chat / tech / lit).

- Not literal translation — matches **register + person + tense** per scenario + glossary lock
- 6 anti-AI translation rules (no Furthermore / no big words / keep var names / no padding)
- 5 scenario examples + style comparison table
- CLI + Claude Code skill integration
- 10 unit tests pass

[→ View details](claude-code/translate-skill/)

#### 🌐 claude-code/translate-skill

**中英翻译模板** — 5 大场景 (文档 / 邮件 / 口语 / 技术 / 文学)。

- 不是逐字翻译 — 按场景匹配**语域 + 人称 + 时态** + 术语表锁定
- 6 条反 AI 翻译要点 (不堆 Furthermore / 不用大词 / 保留变量名 / 不补客套)
- 5 场景示例 + 风格对照表 (register / person / tense / length_pct)
- CLI + Claude Code skill 集成
- 10 个 unittest 全过

[→ 查看详情](claude-code/translate-skill/)

#### 📊 codex/codex-bench

**Codex CLI 性能基准**。

- 同任务跑多模型(codex-mini / gpt-4o / gpt-4o-mini)
- 速度 / 质量 / token 维度对比
- 自动出报告

[→ 查看详情](codex/codex-bench/)

#### 🖱️ cursor/cursor-rules-pack

**Cursor Agent 专属 skill pack**。

- 7 种项目类型模板(React / Python / Go / Vue / etc.)
- 预配置 `.cursorrules` 主模板
- 按文件类型应用规则
- 团队统一方案

[→ 查看详情](cursor/cursor-rules-pack/)

#### 📦 shared/vscode-extension-pack

**VSCode AI 扩展集合包**。

- 一键装 Cline / Continue / Copilot / Codeium 等
- 推荐 .vscode/settings.json 配置
- 国内直连(api.skillai.top)配置
- 多扩展冲突解决方案

[→ 查看详情](shared/vscode-extension-pack/)

#### 📊 shared/model-benchmark

**免费 AI 模型跑分对比工具**。

- 同任务跑 5 个模型,自动评分
- 6 类测试(代码 / 重构 / 翻译 / 总结 / 推理)
- 自动出报告(markdown / html / 雷达图)
- 一键对比"哪个免费模型最强"

[→ 查看详情](shared/model-benchmark/)

---

### 支持的模型 (SUPPORTED_MODELS)

`api-fallback` / `model-benchmark` / `codex-starter` 默认走 **MiniMax 官方** (https://api.minimaxi.com/anthropic, 模型 `MiniMax-M3`)。其他 provider 通过 `config.json` 配置为 fallback。

| Provider | base_url | 默认模型 | 用途 |
|----------|----------|---------|------|
| **MiniMax 官方** (default) | `https://api.minimaxi.com/anthropic` | `MiniMax-M3` | 主用 |
| api.skillai.top (备) | `https://api.skillai.top` | `deepseek-v4-flash` | 中转降本 |
| OpenAI (备) | `https://api.openai.com/v1` | `gpt-4o-mini` | 直连 |
| GitHub Models (备) | `https://models.inference.ai.azure.com` | `gpt-4o` | 免费层 |

切换 provider：编辑 `shared/model-benchmark/config.json` 或 `claude-code/api-fallback/.env`。
完整对比跑分：[→ model-benchmark 报告](shared/model-benchmark/)。

---

### 路线图

每周上新 1-2 个 skill,持续维护。

| Week | Skill | 状态 |
|------|-------|------|
| W1 | api-fallback | ✅ 完成 |
| W1 | agent-rules | ✅ 完成 |
| W1 | token-saver | ✅ 完成 |
| W1 | chinese-dev-helper | ✅ 完成 |
| W1 | multi-agent-install | ✅ 完成 |
| W2 | codex-starter | ✅ 完成 |
| W2 | openclaw-deploy | ✅ 完成 |
| W2 | hermes-tutorial | ✅ 完成 |
| W3 | cursor-rules-pack | ✅ 完成 |
| W3 | vscode-extension-pack | ✅ 完成 |
| W4 | model-benchmark | ✅ 完成 |

---

### API 中转(国内直连)

**Claude Code 撞限速?试试 [api.skillai.top](https://api.skillai.top)**

- ✅ Claude / GPT / Gemini 全模型支持
- ✅ 价格低至官方 1/3
- ✅ 国内直连,无需翻墙
- ✅ 7×24 稳定
- ✅ 自动计费 + 用量统计

---

### 加入交流群

扫码加入微信交流群,讨论 AI 工具、薅羊毛心得、提 issue / 建议:

![WeChat Group](assets/wechat-qr.png)

---

### 贡献

欢迎贡献:
- 新的 skill(在 `claude-code/` / `codex/` / `openclaw/` / `hermes/` / `shared/` 下加)
- 改进现有 skill
- 文档改进
- Bug 修复

参见 [CONTRIBUTING.md](CONTRIBUTING.md)

### 许可证

[MIT](LICENSE)

---

## English

### What is this?

**ai-agent-skills** is a cross-tool skills collection for AI programming agents like Claude Code / Codex / Cursor Agent / OpenClaw / Hermes. Solve real pain points + cross-tool compatibility + continuous updates.

### Why use?

| Pain | Solution |
|------|----------|
| Claude Code hits rate limit | api-fallback auto-switches |
| Tokens burn too fast | token-saver cuts 65% |
| Every AI tool has different config format | agent-rules unified standard |
| Chinese docs hard to write | chinese-dev-helper |
| 4 tools = 4 setups | multi-agent-install one-click |

### Compatible Tools

| Tool | Skills | Path |
|------|--------|------|
| **Claude Code** | 5 | [claude-code/](claude-code/) |
| **Codex** | 1 | [codex/](codex/) |
| **Cursor Agent** | 1 | [cursor/](cursor/) |
| **OpenClaw** | 1 | [openclaw/](openclaw/) |
| **Hermes Agent** | 1 | [hermes/](hermes/) |

### Quick Start

```bash
git clone https://github.com/fast1188/ai-agent-skills.git
cd ai-agent-skills
# Pick a skill, then:
cd claude-code/api-fallback
install.bat    # or ./install.sh on Linux/Mac
```

### API Relay (China)

Hit rate limits on Claude Code? Try [api.skillai.top](https://api.skillai.top):
- Claude / GPT / Gemini full model support
- 1/3 official pricing
- Direct China connection, no proxy needed
- 7×24 stability

#### ✉️ claude-code/write-email

**Chinese email generator** — 5 scenarios (BD / job / follow-up / apology / thanks).

- Output sounds human: short sentences, rhythm, concrete numbers, zero clichés
- 6 anti-AI detection rules
- Skeleton + CTA slots filled by AI
- CLI + Claude Code skill integration
- 11 unit tests pass

[→ View details](claude-code/write-email/)

### WeChat Group

![WeChat Group](assets/wechat-qr.png)

### License

[MIT](LICENSE)