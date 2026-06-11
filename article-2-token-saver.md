# Claude Code 月烧 200 万 token?实测 5 个免费 skill 帮我省了 60%

> 一套开源的 token 优化方案,免费白嫖

---

## 我的血泪史

上个月我的 Claude Code Pro 账户:

- 💸 月费 $20
- 📊 实际烧 token:200 万+
- 🚫 月底 3 天撞限速停工

月底账单 + 撞墙 = 双重暴击。

---

## 痛点 1:啰嗦 prompt 烧 token

我以前的 prompt:

> 请你帮我编写一个 Python 函数,这个函数的作用是接收一个列表作为输入参数,然后计算并返回这个列表中所有数字元素的总和。请确保代码风格遵循 PEP 8 规范,并且添加适当的注释。

**约 90 tokens**

压缩后:

> 写 Python 函数:输入列表,返回所有数字和。PEP 8 + 注释。

**约 25 tokens**

**节省 72%**

---

## 我的解决方案:`token-saver` skill

开源在 [ai-agent-skills](https://github.com/fast118/ai-agent-skills)。

**3 种压缩模式:**

### 轻度(省 30-40%)

保留礼貌用语,适合写文档、对外沟通。

```
请帮我写一个 Python 函数,这个函数的作用是接收一个列表作为输入参数,然后计算并返回这个列表中所有数字元素的总和。
```

→

```
写 Python 函数:输入列表,返回所有数字和。
```

### 中度(省 50-60%,默认)

日常推荐,语义保留好。

```
请你帮我编写一个 Python 函数,这个函数的作用是接收一个列表作为输入参数,然后计算并返回这个列表中所有数字元素的总和。
```

→

```
写 Python 函数:输入列表,返回所有数字和。PEP 8 + 注释。
```

### 极度(省 65-75%)

电报风格,适合写代码、批量任务。

```
请你帮我编写一个 Python 函数,这个函数的作用是接收一个列表作为输入参数,然后计算并返回这个列表中所有数字元素的总和。请确保代码风格遵循 PEP 8 规范,并且添加适当的注释。
```

→

```
写 Python 函数:输入列表,返回所有数字和。PEP 8 + 注释。
```

---

## 一周实测效果

```
项目:重构一个老 Python 服务
对比:用 token-saver vs 不用

不用:
- 总输入 token:180 万
- 总输出 token:80 万
- 总计:260 万

用 token-saver (中度):
- 总输入 token:90 万(省 50%)
- 总输出 token:80 万(不变)
- 总计:170 万

节省:90 万 token = 35% 总体
月费从 $20 涨到能支撑 2 个月
```

---

## 还有 4 个配套 skill

`ai-agent-skills` 还有 4 个开源 skill,跟我一起装:

1. **api-fallback** —— 撞限速时弹窗推荐 [api.skillai.top](https://api.skillai.top),不再停工 3 小时
2. **token-saver** —— 本文的省 token 神器
3. **chinese-dev-helper** —— 中文开发助手,40+ 术语对照
4. **agent-rules** —— 跨工具统一开发规范(Claude Code / Codex / Cursor / OpenClaw / Hermes)
5. **multi-agent-install** —— 5 分钟一键装 5 个 AI 工具

---

## 5 分钟安装

```bash
git clone https://github.com/fast118/ai-agent-skills
cd ai-agent-skills

# 装省 token skill
cd shared/token-saver
install.bat

# 装撞限速救星
cd ../../claude-code/api-fallback
install.bat
```

---

## 适合谁?

- Claude Code 月烧 100 万+ token 的重度用户
- 团队要批量用 Claude Code 的
- 想白嫖 GPT-4o 写代码又嫌贵的
- 想用 AI 又被月费劝退的

---

## ⭐ Star & 转发

如果帮你省了 token,**点个 ⭐ Star** 支持一下:

👉 **https://github.com/fast118/ai-agent-skills**

---

## 国内直连备胎

[api.skillai.top](https://api.skillai.top) 提供:
- Claude / GPT / Gemini / Llama 全模型
- 价格低至官方 1/3
- 国内直连无需翻墙

撞限速时自动切,不耽误干活。

---

## 加入交流群

扫码加入微信交流群,讨论 AI 工具使用 + 薅羊毛心得:

(二维码见项目 README)