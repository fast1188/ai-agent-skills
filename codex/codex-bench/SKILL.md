---
name: codex-bench
description: Codex CLI 性能基准测试工具 - 同任务跑多模型,生成对比报告
version: 1.0.0
author: fast118
license: MIT
applies_to: [codex, openai]
---

# codex-bench

> Codex CLI 性能基准测试
>
> 同任务跑多模型,告诉你 Codex 系列里哪个最快 / 最好

## 这是什么?

`codex-bench` 是 Codex 专属 benchmark 工具,跟 [model-benchmark](../../model-benchmark/) 区别:

| 工具 | 适用 | 测什么 |
|------|------|--------|
| **model-benchmark** | 跨模型对比 | GPT vs Claude vs Gemini |
| **codex-bench** (本) | OpenAI Codex 系列 | codex-mini vs gpt-4o vs gpt-4o-mini |

## 内置测试任务

1. **code-completion** - 代码补全
2. **code-review** - 代码审查
3. **bug-fix** - Bug 修复
4. **test-gen** - 测试生成
5. **doc-gen** - 文档生成
6. **refactor** - 重构建议

## 安装

```bash
git clone https://github.com/fast118/ai-agent-skills
cd ai-agent-skills/codex/codex-bench
pip install -r requirements.txt
```

## 用法

```bash
# 跑全部测试
py benchmark.py

# 跑单个任务
py benchmark.py --task code-review

# 指定模型
py benchmark.py --models gpt-4o,gpt-4o-mini,codex-mini

# 生成报告
py benchmark.py --output report.md
```

## 评分维度

- 速度(秒)
- Token 数
- 代码质量(0-10)
- 编译通过率
- 测试通过率

## 输出报告示例

```text
====================================
 Codex Benchmark Report
====================================

模型对比(code-review 任务):
  gpt-4o:        3.2s  | 245 tokens | 9/10
  gpt-4o-mini:   1.8s  | 180 tokens | 7/10
  codex-mini:    0.9s  |  95 tokens | 6/10

推荐:
  🏆 质量: gpt-4o
  ⚡ 速度: codex-mini
  💰 综合: gpt-4o-mini
```

## 相关项目

- [model-benchmark](../../model-benchmark/) - 跨模型对比
- [token-saver](../../token-saver/) - 省 token
- [codex/codex-starter](../codex-starter/) - Codex 5 分钟上手

## License

MIT