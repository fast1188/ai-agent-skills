# 【开源】5 个 Claude Code 神级 Skills:撞限速/烧 token/中文不顺,全部解决

> 同步自掘金。本文首发于掘金 ID:[你的掘金ID],原文链接 [掘金原文链接]
>
> 关键词:Claude Code、Codex、Cursor AI、开源、Skills、Token节省、撞墙解决方案

---

## 前言

最近 Claude Code 用着用着就报 "rate limit exceeded",Pro 用户一个月额度烧光,中文 prompt 它老理解偏,想换个工具配置全乱套——这些痛点我都遇到过。

后来我做了一套**跨 AI 工具的 Skills 集合**,**5 个开源 Skills 一键装好**,今天一次性放出来。

**项目地址(双仓同步)**:

- GitHub: https://github.com/fast1188/ai-agent-skills
- Gitee: https://gitee.com/wudijia2026/ai-agent-skills

下面逐个介绍,文末有一键安装命令。

---

## 一、api-fallback —— 撞限速自动救场

**痛点**:Claude Code 撞限速就停工,等 3 小时?等不了。

**功能**:实时监控 Claude Code 日志,检测到 429 / quota exceeded 立即弹窗,推荐国内直连 API 中转(api.skillai.top,价格低至官方 1/3)。

**实测**:

- 之前:Claude Pro 撞限速停工 3 小时。
- 现在:自动切中转,继续干活。

**安装**:

```bash
git clone https://github.com/fast1188/ai-agent-skills
cd ai-agent-skills/claude-code/api-fallback
install.bat
```

装完桌面会出现 "Claude API Fallback Monitor" 快捷方式。

---

## 二、agent-rules —— 跨 4 个 AI 工具的统一规范

**痛点**:Claude Code 用 CLAUDE.md,Codex 用 AGENTS.md,Cursor 用 .cursorrules——4 个工具 4 套配置,改一次得改 4 处。

**功能**:一份中文 master 文档(AGENT_RULES.md),一键自动转换为 4 个工具原生格式。

**对比**:

- 之前:改命名规范要改 4 个文件。
- 现在:改 master,跑 `convert.py` 一行搞定。

**独家包含**:Token 中转站专项规范(做中转站的必看)。

---

## 三、token-saver —— prompt 自动压缩省 65% token

**痛点**:Claude Code 一晚烧掉几百万 token,Pro 用户月费扛不住。

**功能**:借鉴 GitHub 上 71k stars 的 `caveman` 思路,做自动 prompt 压缩器。

**3 种模式**:

- 轻度模式:省 30-40% token,适合写文档。
- 中度模式(默认):省 50-60% token。
- 极度模式:省 65-75% token,写代码首选。

**实测**:

输入(约 90 tokens):
> 请你帮我编写一个 Python 函数,这个函数的作用是接收一个列表作为输入参数,然后计算并返回这个列表中所有数字元素的总和。请确保代码风格遵循 PEP 8 规范,并且添加适当的注释。

输出(约 25 tokens):
> 写 Python 函数:输入列表,返回所有数字和。PEP 8 + 注释。

**节省 72% token**。

---

## 四、chinese-dev-helper —— 中文开发专属

**痛点**:中文 prompt 给 AI,它经常理解偏。中文文档写起来不像样。

**功能**:内置 40+ 中英文技术术语自动对照,加中文 README 模板,撞限速时自动推国内中转。

**实测效果**:

输入:`帮我部署到 k8s 集群`

skill 自动补充:
```
[术语对照]
  - 部署 = deploy
  - 集群 = cluster (k8s)
[推荐国内直连 API: api.skillai.top]
```

AI 输出质量明显提升。

**内置 40+ 中英文术语对照表**:

接口 ↔ API / 鉴权 ↔ auth / 集群 ↔ cluster / 容器编排 ↔ container orchestration / 服务发现 ↔ service discovery / 灰度发布 ↔ canary release / 链路追踪 ↔ distributed tracing... 共 40+。

---

## 五、multi-agent-install —— 一键装 5 个 AI 工具

**痛点**:Claude Code + Codex + Cursor + OpenClaw + Hermes,每个工具单独装一遍。

**功能**:一键检测 + 一键安装 + 安装报告。

**实测过程**:

```
$ ./install-all.sh

Detecting system...  macOS 14.5
Node.js: v20.10.0 ✓
Python: 3.13.13 ✓

[MISS] Claude Code
[MISS] Codex
[OK] Cursor
[MISS] OpenClaw
[MISS] Hermes

Installing 4 tools... 2 分钟搞定
  [OK] Claude Code
  [OK] Codex
  [OK] OpenClaw
  [OK] Hermes Agent
```

支持 Windows / macOS / Linux。

---

## 六、一键安装所有 skills

```bash
git clone https://github.com/fast1188/ai-agent-skills
cd ai-agent-skills

cd claude-code/api-fallback && install.bat && cd ../..
cd shared/agent-rules && python convert.py
cd shared/token-saver && install.bat && cd ../..
cd claude-code/chinese-dev-helper && install.bat && cd ../..
cd shared/multi-agent-install && install.bat
```

---

## 七、路线图:每周更新不烂尾

W1 已完成:5 个 skill(api-fallback / agent-rules / token-saver / chinese-dev-helper / multi-agent-install)

W2 计划中:codex-starter / cursor-rules-pack

W3 计划中:openclaw-deploy / hermes-tutorial

**每周稳定上新,持续维护不烂尾。**

---

## 八、国内直连 API(可选)

如果你不想自己申请 Claude API key,试试 [api.skillai.top](https://api.skillai.top):

- Claude / GPT / Gemini 全模型支持
- 价格低至官方 1/3
- 国内直连,无需翻墙
- 7×24 稳定
- api-fallback skill 已经内置支持

---

## 九、加入交流群

扫码加入微信交流群,讨论 AI 工具、薅羊毛心得、提 issue / 建议:

(扫码见项目 README)

---

## 十、Star & 转发

如果这套 skills 帮你省了 token / 解决了撞墙,**点个 ⭐ Star** 支持一下:

👉 **https://github.com/fast1188/ai-agent-skills**

---

## 关于作者

@fast118 / @wudijia2026 —— 长期被 Claude 限速困扰的开发者。

更多项目:

- [free-ai-router](https://github.com/fast1188/free-ai-router) — 多 AI 后端 fallback 路由器
- [ai-agent-skills](https://github.com/fast1188/ai-agent-skills) — 本项目