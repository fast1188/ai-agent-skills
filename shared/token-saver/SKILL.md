---
name: token-saver
description: Compresses verbose prompts into concise instructions before sending to AI tools. Reduces token consumption by 30-70% while preserving meaning. Inspired by caveman prompt style.
version: 1.0.0
author: fast118
license: MIT
applies_to: [claude-code, codex, cursor, openclaw, hermes]
---

# token-saver

> AI prompt 压缩器 —— 把啰嗦的提示变成精炼指令,省 30-70% token
>
> 灵感来自 `caveman` skill(71k stars 验证过的爆款套路)

## 这是什么?

`token-saver` 是一个 preprocessor skill,在你的 prompt 发给 AI 之前**自动压缩**:

| 输入 | 输出 |
|------|------|
| "请你帮我编写一个 Python 函数,这个函数的作用是接收一个列表作为输入参数,然后计算并返回这个列表中所有数字元素的总和。请确保代码风格遵循 PEP 8 规范,并且添加适当的注释。" | "写 Python 函数:输入列表,返回所有数字和。PEP 8 + 注释。" |

压缩前:**约 90 tokens**
压缩后:**约 25 tokens**
**节省 72% token**

## 工作原理

1. 监听 prompt 输入(键盘输入 / 文件内容 / CLI 参数)
2. 用本地规则 + AI 启发式压缩冗余:
 - 删除敬语 / 客套话("请你帮我..."、"非常感谢...")- 合并同义表达
 - 移除冗余修饰词- 缩写常用术语
3. 显示压缩前后对比(可选)
4. 发送压缩版给 AI

## 模式

### 1. 轻度压缩(默认)
- 删除客套话
- 保留完整语义
- 节省 **30-40% token**

### 2. 中度压缩
- 轻度压缩 + 同义合并
- 节省 **50-60% token**

### 3. 极度压缩(caveman 模式)
- 只保留核心动词 + 名词
- 类似电报风格
- 节省 **65-75% token**

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

把 `SKILL.md` 复制到 `~/.claude/skills/token-saver/SKILL.md`。

## 使用

**在 Claude Code / Codex 中:**

直接正常使用,skill 自动生效:

```
你: 请你帮我写一个函数
[token-saver 压缩后]: 写函数
Claude: 当然,请问什么函数?(reply 不压缩)
```

**命令行:**
```bash
py ~/.claude/skills/token-saver/compress.py "你的长 prompt"
# 输出压缩版,可直接发给 AI
```

## 配置

`~/.claude/skills/token-saver/config.json`:
```json
{
  "mode": "medium",
  "show_diff": false,
  "auto_apply": true,
  "preserve_code": true,
  "preserve_chinese": true
}
```

## 适用场景

| 场景 | 推荐模式 |
|------|----------|
| 写代码 | 极度(电报式最省) |
| 写文档 | 轻度(保留礼貌) |
| 中文交互 | 轻度(避免歧义) |
| 英文 prompt | 中度或极度 |
| 长篇任务 | 极度(节省最明显) |

## 局限

- ⚠️ 不压缩 AI 回复(只压输入)
- ⚠️ 压缩可能丢失微妙语气
- ⚠️ 极度模式需要 AI 理解能力强

## 相关项目

- [free-ai-router](https://github.com/fast118/free-ai-router) - 多 AI 后端 fallback
- [ai-agent-skills](https://github.com/fast118/ai-agent-skills) - 本仓库

## 许可证

MIT