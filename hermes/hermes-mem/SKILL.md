---
name: hermes-mem
description: Hermes Agent 持久化记忆增强 - 跨项目跨会话的智能记忆系统
version: 1.0.0
author: fast118
license: MIT
applies_to: [hermes]
---

# hermes-mem

> Hermes Agent 持久化记忆增强
>
> 跨项目、跨会话的智能记忆,记什么都忘不了

## 这是什么?

`hermes-mem` 是 Hermes Agent 记忆系统的增强版:

| 功能 | 官方 | hermes-mem |
|------|------|------------|
| 本地 SQLite 存储 | ✓ | ✓ |
| 跨会话记忆 | ✓ | ✓ |
| **项目隔离** | ✗ | ✓ |
| **记忆分类**(preference/fact/decision) | ✗ | ✓ |
| **记忆导入导出** | ✗ | ✓ |
| **过期自动清理** | ✗ | ✓ |
| **向量检索**(语义搜索) | ✗ | ✓ (可选) |

## 分类系统

记忆分 3 类:

1. **preference** - 用户偏好(语言、风格、习惯)
2. **fact** - 事实(项目背景、技术栈、API)
3. **decision** - 决策(为什么选 A 不选 B)

## 用法

**CLI 方式:**
```bash
# 加记忆
py ~/.claude/skills/hermes-mem/mem.py add preference "我偏好中文回复"
py ~/.claude/skills/hermes-mem/mem.py add fact "项目用 FastAPI + PostgreSQL"

# 查记忆
py ~/.claude/skills/hermes-mem/mem.py list
py ~/.claude/skills/hermes-mem/mem.py search "中文"

# 删记忆
py ~/.claude/skills/hermes-mem/mem.py delete 1

# 导入导出
py ~/.claude/skills/hermes-mem/mem.py export backup.json
py ~/.claude/skills/hermes-mem/mem.py import backup.json
```

**自动集成:**
- 每次 chat 自动保存关键信息
- 启动时自动加载相关记忆
- 跟其他 skill 共享记忆

## 跟其他 skill 集成

| Skill | 集成方式 |
|-------|----------|
| codex-pp | 共享 ~/.codex-pp/memory.db |
| api-fallback | 记下撞限速历史 |
| token-saver | 记下你的 prompt 风格 |

## 安装

```bash
git clone https://github.com/fast118/ai-agent-skills
cd ai-agent-skills/hermes/hermes-mem
pip install -r requirements.txt
install.bat
```

## 数据结构

```sql
CREATE TABLE memories (
    id INTEGER PRIMARY KEY,
    category TEXT NOT NULL,  -- preference/fact/decision
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    project TEXT,  -- 关联项目(可空)
    expires_at REAL,  -- 过期时间(可空)
    created_at REAL NOT NULL,
    updated_at REAL NOT NULL
)
```

## 隐私

- 数据 100% 本地(`~/.claude/memories.db`)
- 不会上传任何数据
- 删除命令: `py mem.py delete <id>` 或 `rm ~/.claude/memories.db`

## 相关项目

- [hermes-tutorial](../hermes-tutorial/) - Hermes 上手指南
- [codex-pp](https://github.com/fast118/codex-pp) - 国产化 AI CLI

## License

MIT