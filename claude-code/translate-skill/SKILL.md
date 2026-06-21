---
name: translate
description: 翻译 skill — 中英 (含日韩) 翻译模板。给场景 (文档/邮件/口语/技术/文学) 自动选风格 + 术语, AI 味 0。
version: 1.0.0
author: fast118
license: MIT
applies_to: [claude-code, codex, cursor, openclaw, hermes]
---

# translate

> 中英翻译模板 — 5 大场景 (文档 / 邮件 / 口语 / 技术 / 文学)
>
> 不是逐字翻译 — 是**按场景匹配风格 + 术语表 + 6 条反 AI 翻译要点**

## 这是什么

`translate` 把"翻译这段"拆成可控的 5 个场景，每个场景有不同的语域、术语处理规则、风格约束。

不像 Google 直接翻 — 那样出来是机翻味（"the"开头、"is"+"ing"、连接词臃肿）。

5 大场景：

| 场景 | 触发关键词 | 风格 | 长度 |
|------|-----------|------|------|
| 文档 | doc / 文章 / 报告 / 文档 | 正式书面 | 90-110% 原文 |
| 邮件 | mail / email / 邮件 | 商务口吻 | 90-110% |
| 口语 | chat / 口语 / 对话 / 聊天 | 简短自然 | 80-100% |
| 技术 | code / API / 错误 / log | 精准保留术语 | 100% |
| 文学 | 小说 / 散文 / 诗 / 文学 | 保持文风 | 90-110% |

## 输出格式

```
<原文>
--->
<译文>
```

## 使用

**在 Claude Code 中：**
```
你: 用 translate skill 把这段邮件翻成英文 "你好, 感谢您..."
[自动调用 skill]
AI: 输出翻译结果
```

**单独 CLI：**
```bash
py translate.py "你好, 感谢您的支持" --to en --scenario mail
```

## 6 条反 AI 翻译要点

1. **不堆连接词** — 不 "Furthermore, Additionally, Moreover" 起句
2. **不用大词** — "utilize" → "use", "commence" → "start"
3. **保持术语一致** — 同一术语全文统一译法 (用术语表)
4. **口语化场景用人称** — 不 "one should" 而是 "you should"
5. **技术场景保留原变量名** — `myVar` 不译为 `我的变量`
6. **不补 AI 套话** — 原文没的 "I hope this helps" 不加

## 风格对照（5 场景）

| 维度 | 文档 | 邮件 | 口语 | 技术 | 文学 |
|------|------|------|------|------|------|
| 时态 | 一般现在 | 一般现在 | 现在/进行 | 一般现在 | 依原文 |
| 人称 | 第三 | 第二 | 第一/第二 | 第三 | 第一/三 |
| 语域 | 正式 | 商务 | 随意 | 精准 | 文艺 |
| 术语 | 标准 | 商务 | 通用 | 保留 | 文学化 |
| 长度 | 100% | 100% | 80% | 100% | 100% |
| 注脚 | 可加 | 不可 | 不可 | 必加 | 可加 |

## 例子

### 例 1: 邮件场景
**输入**："您好, 感谢您百忙之中回复, 我们会尽快处理。"
**输出**：
```
您好, 感谢您百忙之中回复, 我们会尽快处理。
--->
Hi, thanks for getting back despite your busy schedule. We'll get it sorted shortly.
```

### 例 2: 技术场景
**输入**："API 调用失败, 返回 401 错误码, 请检查 token 是否过期"
**输出**：
```
API 调用失败, 返回 401 错误码, 请检查 token 是否过期
--->
API call failed, returned 401. Please check if the token has expired.
```

### 例 3: 口语场景
**输入**："行, 那就这么定了, 周五见"
**输出**：
```
行, 那就这么定了, 周五见
--->
OK, deal. See you Friday.
```

## 配置

`~/.claude/skills/translate/config.json`:
```json
{
  "default_scenario": "mail",
  "default_target": "en",
  "glossary": {
    "API": "API",
    "token": "token",
    "回调": "callback",
    "部署": "deploy"
  }
}
```

## 相关

- [write-email](../write-email/) — 邮件撰写 (与 translate mail 场景配套)
- [chinese-dev-helper](../chinese-dev-helper/) — 中文 prompt 增强
- [ai-agent-skills 主页](../../README.md)

## License

MIT
