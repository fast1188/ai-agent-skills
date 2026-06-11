---
name: model-benchmark
description: 免费 AI 模型跑分对比工具。同样的任务用 5 个模型跑一遍,生成对比报告,告诉你哪个模型性价比最高。
version: 1.0.0
author: fast118
license: MIT
applies_to: [all]
---

# model-benchmark

> 免费 AI 模型跑分对比工具
>
> 同样的题跑 5 个模型,出对比报告

## 这是什么?

`model-benchmark` 自动跑同一组测试任务(代码生成 / 翻译 / 总结)在 5 个不同模型上,然后生成对比报告:

| 模型 | 速度 | 质量 | 价格 | 总分 |
|------|------|------|------|------|
| gpt-4o-mini | ⚡⚡⚡ | ⭐⭐⭐⭐ | 免费 | ... |
| llama-3.3-70b | ⚡⚡ | ⭐⭐⭐⭐ | 免费 | ... |
| phi-4 | ⚡⚡⚡ | ⭐⭐⭐ | 免费 | ... |
| deepseek-r1 | ⚡ | ⭐⭐⭐⭐⭐ | 免费 | ... |
| gemini-2.0-flash | ⚡⚡⚡ | ⭐⭐⭐⭐ | 免费 | ... |

## 测试任务集

内置 6 类测试:

1. **代码生成**:写一个快排算法
2. **代码重构**:把过程式改成面向对象
3. **bug 修复**:找 Python 代码里的 3 个 bug
4. **翻译**:技术文档英 → 中
5. **总结**:长文 → 200 字摘要
6. **推理**:数学题

每个任务跑 5 次取平均,消除随机性。

## 安装

```bash
git clone https://github.com/fast118/ai-agent-skills
cd ai-agent-skills/shared/model-benchmark
pip install -r requirements.txt
```

## 使用

### 跑全部测试

```bash
py benchmark.py
```

输出:
```
=====================================
 model-benchmark v1.0
=====================================

测试任务 1/6: 代码生成 - 快排
  ✓ gpt-4o-mini: 3.2s, 85分
  ✓ llama-3.3-70b: 5.1s, 88分
  ✓ phi-4: 2.8s, 80分
  ✓ deepseek-r1: 8.2s, 92分
  ✓ gemini-2.0-flash: 3.5s, 87分

测试任务 2/6: 代码重构
  ...

=====================================
 报告
=====================================

🏆 综合最佳:deepseek-r1(质量最强,但慢)
⚡ 速度最佳:phi-4(最快,质量够用)
💰 性价比最佳:gpt-4o-mini(快 + 质量好 + 免费)
```

### 自定义模型

```bash
py benchmark.py --models "gpt-4o-mini,llama-3.3-70b" --task code-gen
```

### 输出报告

```bash
py benchmark.py --report markdown > report.md
```

## 配置 `config.json`

```json
{
  "models": [
    {
      "name": "gpt-4o-mini",
      "provider": "github_models",
      "enabled": true
    },
    {
      "name": "llama-3.3-70b",
      "provider": "groq",
      "enabled": true
    }
  ],
  "tasks": [
    "code-gen",
    "code-refactor",
    "bug-fix",
    "translate",
    "summarize",
    "reason"
  ],
  "iterations": 5,
  "output_format": "markdown"
}
```

## 评分维度

每个任务打 4 个分:

| 维度 | 说明 |
|------|------|
| **正确性** | 输出能用 / 跑通? |
| **速度** | 响应时间(秒) |
| **简洁** | token 越少越好 |
| **稳定** | 多次跑一致? |

## 自动出报告

跑完自动生成:

1. `report.md` —— Markdown 报告
2. `report.html` —— 网页版(可分享)
3. `chart.png` —— 雷达图

直接发到微信群 / Twitter / 博客,引流神器。

## 适合谁?

- 想知道哪个免费模型最强
- 团队选型决策
- 写"AI 工具测评"内容
- 性能调优

## 已知局限

- 只测文本生成任务(不测多模态)
- 评分基于规则,不是绝对精确
- 不同 provider 响应时间不稳定,需多次取平均

## 相关项目

- [free-ai-router](https://github.com/fast118/free-ai-router)
- [ai-agent-skills](https://github.com/fast118/ai-agent-skills)

## 许可证

MIT