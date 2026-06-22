# 5 篇文章发布清单 (Day 9-10 流量作战)

> 创建: 2026-06-22 · 适用文件: `D:/Github开源项目/项目源码/ai-agent-skills/article-*.md` (5 篇)
> 一键脚本: `D:/Github开源项目/脚本工具/publish_articles.bat`
> 预计耗时: 2 小时(每篇 20 分钟,主要是填占位符 + 调格式)
> 预期流量: 5 平台 × 30-100 阅读/篇 = 150-500 主动 UV,带动 10-30 star

---

## 占位符总览

| 文件 | 占位符 | 数量 | 备注 |
|---|---|---|---|
| article-juejin.md | (无) | 0 | 可直接发 |
| article-juejin-juejin.md | (无) | 0 | 可直接发 |
| article-csdn.md | `[你的掘金ID]` / `[掘金原文链接]` | 2 | **改后才能发** |
| article-2-token-saver.md | (无) | 0 | 可直接发 |
| article-3-comparison.md | (无) | 0 | 可直接发 |

**article-csdn.md line 3 需改**:
```
> 同步自掘金。本文首发于掘金 ID:[你的掘金ID],原文链接 [掘金原文链接]
```
↓
```
> 同步自掘金。本文首发于掘金 ID:fast118_ai,原文链接 https://juejin.cn/post/XXXXX
```

(等 article-juejin.md 先发到掘金,拿到 ID + URL 后回来填)

---

## 5 篇文章 × 4 平台 = 20 个发文点

| # | 草稿 | 首发平台 | 同步平台 | 标题 |
|---|---|---|---|---|
| 1 | article-juejin.md | **掘金** | CSDN / 思否 / 博客园 | 5 个 Claude Code 神级 Skills 开源了!免费白嫖,亲测有效 |
| 2 | article-juejin-juejin.md | **掘金 (备用号)** | 知乎 / 简书 | (同上,内容略不同 emoji) |
| 3 | article-csdn.md | **CSDN** | 思否 / 掘金 | 5 个 Claude Code 神级 Skills 开源了 |
| 4 | article-2-token-saver.md | **掘金** | 知乎 / 简书 / 推特 | Claude Code 月烧 200 万 token?实测 5 个免费 skill 帮我省了 60% |
| 5 | article-3-comparison.md | **掘金** | 知乎 / 简书 | Claude Code / Codex / Cursor 三选一:实测对比 + 选型指南 |

---

## 每篇发文标准流程 (15 分钟 / 篇)

1. 打开 publish_articles.bat → 自动打开 5 个发文页 + 复制内容到剪贴板
2. 登录发文平台 → 粘贴 (Ctrl+V)
3. 改占位符 (article-csdn.md 要等 article-juejin.md 发完拿到 URL)
4. 加封面图 (用 assets/ 下的 wechat-qr.png 或新做一张 1200×630)
5. 加 5 个 tag (每个平台 tag 列表不同,见下)
6. 预览 → 发布
7. 复制最终 URL → 填到本表的"已发 URL"列

### 平台 tag 推荐

| 平台 | 推荐 tag (5-8 个) |
|---|---|
| 掘金 | `Claude Code`, `Codex`, `Cursor AI`, `Skills`, `开源`, `Token节省`, `AI编程`, `国产化` |
| CSDN | `Claude`, `Codex`, `Cursor`, `AI编程`, `开源`, `Skills`, `Token优化` |
| 思否 | `Claude Code`, `Codex`, `AI`, `Skills`, `开源` |
| 知乎 | `Claude Code` 话题, `AI 编程` 话题, `Codex` 话题, `开源工具` 话题, `Cursor` 话题 |
| 博客园 | `AI`, `Claude Code`, `Codex`, `开源` |
| 简书 | `AI`, `Claude Code`, `开源` |

---

## 发文后流量跟踪

每篇文章发布后,**1 / 3 / 7 / 30 天** 4 次查:
- 阅读量
- 点赞 / 收藏 / 评论
- 带来的 GitHub star (用 `fast1188/ai-agent-skills` 仓的 referrer 查)

填到下表:

| # | 平台 | 标题 | 已发 URL | 1d | 3d | 7d | 30d |
|---|---|---|---|---|---|---|---|
| 1 | 掘金 | 5 个 Claude Code Skills... | (待发) | - | - | - | - |
| 2 | 掘金备用号 | (同上) | (待发) | - | - | - | - |
| 3 | CSDN | 5 个 Claude Code Skills... | (待发) | - | - | - | - |
| 4 | 掘金 | Claude Code token 优化 | (待发) | - | - | - | - |
| 5 | 掘金 | Claude Code / Codex / Cursor 选型 | (待发) | - | - | - | - |

---

## 注意事项 (发文平台规则,别违规)

- **掘金**: 不允许直接贴微信号,放二维码行,但要在文末注明"扫码进群"
- **CSDN**: 不允许外链引流超过 3 个 → 仓链接只在文末,正文用仓名代指
- **思否**: 标签不超过 5 个
- **知乎**: 话题比标签重要,选 3-5 个高关注话题
- **简书**: 流量差但收录快,作为 SEO 补充
- **微博 / 推特**: 一句话 + 链接 + 2 张图,流量爆发力强

---

## 跨平台引流 (发文后立刻做)

1. **V2EX**: 发 "快 118 - 5 个 Claude Code 神级 skills 开源" 节点 `分享创造`
2. **即刻**: 发 1 句话 + 仓截图
3. **Twitter**: 5 个 thread,每天 1 个,@fast1188 账号
4. **微博**: 1 句话 + 仓链接 + 配图
5. **Hacker News (Show HN)**: 翻译成英文发,标题 "Show HN: 5 Open-source Skills to fix Claude Code pain points"
6. **Reddit r/ClaudeAI**: 标题 "I built 5 free skills to fix Claude Code rate limits & token waste"

---

## 优先级 (今天 / 明天 / 后天)

| 时段 | 动作 |
|---|---|
| **今天 (Day 8)** | 占位符替换 + 跑 publish_articles.bat + 发第 1 篇 (article-juejin.md → 掘金) |
| 明天 (Day 9) | 发第 2-3 篇 (article-csdn.md → CSDN, article-2-token-saver.md → 掘金) |
| 后天 (Day 10) | 发第 4-5 篇 + 跨平台引流 6 渠道 |
