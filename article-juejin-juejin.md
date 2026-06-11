# 5 个 Claude Code 神级 Skills 开源了!免费白嫖,亲测有效

> 一套代码搞定 Claude Code 撞限速、token 飞涨、中文 prompt 不友好、跨工具配置混乱 4 大痛点

---

## 📌 前言:Claude Code 的 4 大痛点,你中了几个?

我用了半年 Claude Code,撞过 4 次墙,每次都:

- ❌ 写到一半 "You've reached your limit"
- ❌ 一晚烧掉 200 万 token
- ❌ 中文 prompt 它理解偏了
- ❌ 想换个工具,配置得重写

直到我做了一件事 —— 把这 4 个痛点变成 5 个 skill 开源了出来。

今天一次性放出,**GitHub + Gitee 双仓同步**:

- GitHub: https://github.com/fast118/ai-agent-skills
- Gitee: https://gitee.com/wudijia2026/ai-agent-skills

5 分钟看完,拿走直接用。

> 💡 **封面图建议**:把 5 个 skill 的 logo 拼成一张图,标题写 "Claude Code 必备 Skills",放文章顶部。

---

## 🛡️ Skill 1: api-fallback —— 撞限速时自动救场

**痛点**:Claude Code 撞限速就停工,等 3 小时?等不了。

**解决**:实时监控 Claude Code 日志,检测到 `429` / `quota exceeded` 立即弹窗,推荐国内直连 API 中转。

**实测效果**:

- **之前**:Claude Pro 撞限速停工 3 小时;API key 失效报错一堆;网络抽风重启也没用。
- **现在**:自动切中转继续干活;弹窗提醒换 key;自动重试 + 提示。

> 💡 **配图建议**:截图 api-fallback 弹窗(显示 "撞限速?试试 api.skillai.top")。

**安装命令**:

```bash
git clone https://github.com/fast118/ai-agent-skills
cd ai-agent-skills/claude-code/api-fallback
install.bat
```

桌面会出现 "Claude API Fallback Monitor" 快捷方式,双击启动,后台静默运行。

---

## 📋 Skill 2: agent-rules —— 跨 4 个 AI 工具的统一规范

**痛点**:Claude Code 用 CLAUDE.md,Codex 用 AGENTS.md,Cursor 用 .cursorrules —— 4 个工具 4 套配置,改一次得改 4 处。

**解决**:一份中文 master 文档(`AGENT_RULES.md`),一键自动转换为 4 个工具原生格式。

**实测对比**:

- **之前**:改命名规范要改 4 个文件;加新工具要写一遍规则;团队同步要发 4 份文档。
- **现在**:改 master,跑 `convert.py` 一行搞定;改 converter 一次;发一份文档搞定。

**包含的规范**(部分):

- 代码风格 + 命名约定
- 错误处理 + 测试要求
- 安全规范(防 .env 泄露)
- Git commit + 分支策略
- **Token 中转站专项规范**(独家,做中转站的必看)

> 💡 **配图建议**:截图 convert.py 运行前后的对比。

---

## 💰 Skill 3: token-saver —— prompt 自动压缩省 65% token

**痛点**:Claude Code 一晚烧掉几百万 token,Pro 用户月费扛不住。

**解决**:借鉴 GitHub 上 71k stars 的 `caveman` 思路,做自动 prompt 压缩器。

**3 种模式**:

- **轻度模式**:省 30-40% token。适合写文档、要礼貌。
- **中度模式**(默认):省 50-60% token。日常推荐。
- **极度模式**:省 65-75% token。写代码、批量任务首选。

**实测对比**:

输入:
> 请你帮我编写一个 Python 函数,这个函数的作用是接收一个列表作为输入参数,然后计算并返回这个列表中所有数字元素的总和。请确保代码风格遵循 PEP 8 规范,并且添加适当的注释。

输出(极度模式):
> 写 Python 函数:输入列表,返回所有数字和。PEP 8 + 注释。

**节省 72% token**。

> 💡 **配图建议**:左边原 prompt,右边压缩后,中间一个大箭头。

---

## 🇨🇳 Skill 4: chinese-dev-helper —— 中文开发专属

**痛点**:中文 prompt 给 AI,它经常理解偏。中文文档写起来不像样。

**解决**:内置 40+ 中英文技术术语自动对照,加中文 README 模板,撞限速时自动推国内中转。

**实测效果**:

输入:`帮我部署到 k8s 集群`

skill 自动补充:
```
[术语对照]
  - 部署 = deploy
  - 集群 = cluster (k8s)
[推荐国内直连 API: api.skillai.top]
```

AI 输出质量明显提升,因为有了术语对照 + 国内中转备用。

**内置 40+ 中英文术语对照表**(部分):

- 接口 ↔ API
- 鉴权 ↔ auth / authentication
- 集群 ↔ cluster
- 容器编排 ↔ container orchestration
- 服务发现 ↔ service discovery
- 灰度发布 ↔ canary release
- 链路追踪 ↔ distributed tracing
- ... (共 40+ 术语)

> 💡 **配图建议**:截图术语对照表的实际效果。

---

## 🚀 Skill 5: multi-agent-install —— 一键装 5 个 AI 工具

**痛点**:Claude Code + Codex + Cursor + OpenClaw + Hermes,每个工具单独装一遍,重复劳动。

**解决**:一键检测 + 一键安装 + 安装报告。

**实测过程**:

```
$ ./install-all.sh

Detecting system...  macOS 14.5
Node.js: v20.10.0 ✓
Python: 3.13.13 ✓

[MISS] Claude Code    ← 装
[MISS] Codex         ← 装
[OK]   Cursor        ← 跳过
[MISS] OpenClaw      ← 装
[MISS] Hermes        ← 装

Installing 4 tools... 2 分钟搞定
```

**支持的工具**:

- Claude Code (npm)
- Codex (npm)
- Cursor Agent (下载)
- OpenClaw (npm)
- Hermes Agent (pip)

支持 Windows / macOS / Linux 全平台。

> 💡 **配图建议**:终端截图,展示检测 + 安装过程。

---

## 📦 一键安装所有 skills

```bash
git clone https://github.com/fast118/ai-agent-skills
cd ai-agent-skills

# 每个 skill 都独立
cd claude-code/api-fallback && install.bat && cd ../..
cd shared/agent-rules && python convert.py
cd shared/token-saver && install.bat && cd ../..
cd claude-code/chinese-dev-helper && install.bat && cd ../..
cd shared/multi-agent-install && install.bat
```

> 💡 **配图建议**:5 个 install 命令排成一张图。

---

## 🗓️ 路线图:每周更新不烂尾

| Week | Skill | 状态 |
|------|-------|------|
| W1 | api-fallback | ✅ |
| W1 | agent-rules | ✅ |
| W1 | token-saver | ✅ |
| W1 | chinese-dev-helper | ✅ |
| W1 | multi-agent-install | ✅ |
| W2 | codex-starter | 🔜 |
| W2 | cursor-rules-pack | 🔜 |
| W3 | openclaw-deploy | 🔜 |
| W3 | hermes-tutorial | 🔜 |
| W4 | vscode-extension-pack | 🔜 |

**每周稳定上新,持续维护不烂尾。**

---

## 🚀 国内直连 API(可选,撞墙救星)

如果你不想自己申请 Claude API key,试试 **[api.skillai.top](https://api.skillai.top)**:

- ✅ Claude / GPT / Gemini 全模型支持
- ✅ 价格低至官方 1/3
- ✅ 国内直连,无需翻墙
- ✅ 7×24 稳定
- ✅ api-fallback skill 已经内置支持

(本项目作者也在用,确实是撞墙救星。)

---

## 💬 加入交流群

扫码加入微信交流群,讨论 AI 工具使用、薅羊毛心得、提 issue / 建议:

> 💡 **配图建议**:用你之前生成的微信群二维码。

群内福利:

- 第一时间推送 skill 更新
- 讨论 AI 工具使用技巧
- 提 issue / 需求
- 偶尔发免费薅羊毛教程

---

## ⭐ Star & 转发

如果这套 skills 帮你省了 token / 解决了撞墙,**点个 ⭐ Star** 支持一下:

👉 **https://github.com/fast118/ai-agent-skills**

转发给身边用 Claude Code / Codex / Cursor 的朋友,一起告别"撞墙焦虑"。

---

## 👤 关于作者

**@fast118 / @wudijia2026** —— 长期被 Claude 限速困扰的开发者,做了这套 skills 自救顺便开源。

更多项目:

- [free-ai-router](https://github.com/fast118/free-ai-router) — 多 AI 后端 fallback 路由器
- [ai-agent-skills](https://github.com/fast118/ai-agent-skills) — 本项目

---

## 📝 发布 checklist

发布前记得:

- [ ] 封面图(5 个 skill 拼图 + 标题)
- [ ] 文章里 5 个配图(每个 skill 一张)
- [ ] 标签:`AI`、`Claude Code`、`开源`、`Skills`、`GitHub`、`Codex`
- [ ] 简介:"5 个实测可用的 Claude Code skill,完全开源,解决撞限速 + 烧 token + 中文 prompt + 跨工具配置 4 大痛点"
- [ ] 字数:3000-5000 字最佳
- [ ] 发布时间:工作日晚上 8-10 点,流量最高

发布后:

- [ ] 复制链接,发到微信群
- [ ] 在评论区留一句"已 Star,持续关注"
- [ ] 自己点一波赞(账号活跃度)