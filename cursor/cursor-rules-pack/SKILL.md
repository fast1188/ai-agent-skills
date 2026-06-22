---
name: cursor-rules-pack
description: Cursor Agent 专属 skill pack. 预配置 .cursorrules + 多种项目类型模板 + 最佳实践。
version: 1.0.0
author: fast118
license: MIT
applies_to: [cursor]
---

# cursor-rules-pack

> Cursor Agent .cursorrules 一站式配置包
>
> 开箱即用,5 分钟配置好 Cursor

## 这是什么?

`cursor-rules-pack` 提供:

- 预配置的 `.cursorrules` 主模板
- 7 种项目类型专属模板(React / Python / Go / Vue / etc.)
- 最佳实践文档
- 团队统一规则方案

## 为什么需要?

很多 Cursor 用户:

- ❌ 不知道怎么写 `.cursorrules`
- ❌ 规则写得不够,AI 行为不可控
- ❌ 团队成员规则不一致
- ❌ 项目类型不同规则也不同

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

把 `.cursorrules-template` 复制到项目根目录,改名为 `.cursorrules`。

## 包含的模板

```
.cursor/
├── rules/
│ ├── base.md              # 通用基础规则
│ ├── react.md             # React 项目专用
│ ├── python.md            # Python 项目专用
│ ├── go.md                # Go 项目专用
│ ├── vue.md               # Vue 项目专用
│ ├── typescript.md        # TypeScript 强化
│ ├── api.md               # 后端 API 专用
│ └── docs.md              # 文档项目专用
```

每个模板都是精炼的指令集,Cursor 会自动根据文件类型选用。

## 通用模板示例 `.cursorrules`

```markdown
# 基础规则
- 中文回复用户
- 代码注释用英文
- 提交信息用中文
- 变量/函数:snake_case
- 类:PascalCase
- 常量:UPPER_SNAKE_CASE

# 安全
- 不硬编码密钥
- SQL 参数化
- 输入验证

# 测试
- pytest 覆盖率 ≥ 80%
- 命名: test_<fn>_<scenario>_<expected>

# Git
- feat: / fix: / docs: / refactor: / test: / chore:
```

## React 项目模板示例

```markdown
# React 项目规则
- 函数组件优先,不用 class 组件
- TypeScript 严格模式
- Hooks 规则遵守
- 状态管理:简单用 useState,复杂用 Zustand/Redux
- 样式:Tailwind CSS 优先,不用 inline style
- 命名:PascalCase 组件,useXxx hooks
- 测试:Vitest + React Testing Library

# 性能
- React.memo 包裹昂贵组件
- useMemo/useCallback 适当使用
- 不要过早优化

# 目录结构
src/
├── components/  # 复用组件
├── pages/       # 路由页面
├── hooks/       # 自定义 hooks
├── utils/       # 工具函数
└── types/       # TS 类型
```

## Python 项目模板

```markdown
# Python 项目规则
- Python 3.10+
- 类型注解(强制)
- pytest 测试
- 命名:snake_case
- 文档字符串:Google 风格
- 依赖:Poetry / pip-tools
- 代码风格:Black + Ruff

# 架构
- 分层: api / service / repository
- 不在 controller 里写业务逻辑
- 数据库访问只在 repository 层
```

## Go 项目模板

```markdown
# Go 项目规则
- Go 1.21+
- err 显式处理,不忽略
- 不使用 panic 处理业务错误
- 测试标准库 testing + testify
- 命名:驼峰(导出) / 小驼峰(私有)
- 包名:小写单词
- 接口:小接口(1-3 方法)

# 错误处理
if err != nil {
    return fmt.Errorf("context: %w", err)
}
```

## 实战技巧

### 技巧 1:按文件类型应用规则

Cursor 支持根据文件 glob 应用规则:

```markdown
# 仅对 src/components/** 生效
- 组件必须用 React.memo
- Props 必须用 interface 定义

# 仅对 **/*.test.ts 生效
- 必须用 describe / it
- 必须 mock 外部依赖
```

### 技巧 2:引用其他文件

```markdown
- 基础规则见 .cursor/rules/base.md
- React 项目额外规则见 .cursor/rules/react.md
- 团队规范见 docs/CONTRIBUTING.md
```

### 技巧 3:加 emoji 让规则易读

```markdown
🚨 安全:不提交 .env
📦 命名:snake_case
🧪 测试:覆盖率 ≥ 80%
📝 注释:解释"为什么"
```

## 团队统一方案

每个项目都装这个 skill,然后:

```
1. clone 项目到本地
2. 安装 cursor-rules-pack
3. 选择对应模板(react / python / go / ...)
4. 微调团队特定规则
5. commit .cursorrules 到 git
6. 团队成员拉下来就有了
```

## 相关项目

- [free-ai-router](https://github.com/fast1188/free-ai-router)
- [ai-agent-skills](https://github.com/fast1188/ai-agent-skills)
- 通用规则: [shared/agent-rules/](../shared/agent-rules/)

## 许可证

MIT