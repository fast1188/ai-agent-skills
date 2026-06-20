"""write_email.py — 5 大场景邮件生成器（prompt skill 配套 CLI）
≤100 行 · 0 第三方依赖
"""
import re
import sys
import argparse
from pathlib import Path

SCENARIOS = {
    "商务": {
        # 不放"客户"(太泛,"催客户"也带客户 → 误判)
        "trigger": ["合作", "报价", "提案", "试用邀请", "proposal", "BD", "demo", "签约"],
        "length": "150-250 字",
    },
    "求职": {
        "trigger": ["应聘", "求职", "简历", "面试", "apply", "job", "招聘"],
        "length": "200-300 字",
    },
    "催办": {
        "trigger": ["催", "跟进", "卡在哪", "什么时候", "进度", "等回", "follow up"],
        "length": "80-150 字",
    },
    "道歉": {
        "trigger": ["抱歉", "道歉", "事故", "挂了", "延期", "sorry", "apology", "故障"],
        "length": "100-200 字",
    },
    "感谢": {
        "trigger": ["谢谢", "感谢", "帮了", "推荐", "thank", "thanks"],
        "length": "60-120 字",
    },
}

CLICHE_BLACKLIST = [
    "希望对您有所帮助", "感谢您的宝贵时间", "如有任何疑问请随时",
    "祝商祺", "敬请", "打扰了", "冒昧", "亲爱的合作伙伴",
    "我们致力于", "如果您方便的话", "期待您的回复",
]


def detect_scenario(text: str) -> str:
    """根据关键词打分，并列时按"先出现位置"破（越靠前越像用户本意）"""
    text_lower = text.lower()
    scored = []
    for scenario, cfg in SCENARIOS.items():
        s = 0
        first_pos = len(text)  # 大数表示"未出现"
        for kw in cfg["trigger"]:
            pos = text.find(kw)
            if pos < 0:
                pos = text_lower.find(kw.lower())
            if pos >= 0:
                s += 1
                if pos < first_pos:
                    first_pos = pos
        scored.append((scenario, s, first_pos))
    # 先按分数降序，再按位置升序
    scored.sort(key=lambda x: (-x[1], x[2]))
    return scored[0][0] if scored[0][1] > 0 else "商务"


def build_email(scenario: str, requirement: str, to_name: str = "X总") -> str:
    """根据场景 + 需求生成邮件骨架（实际由 AI 填充血肉）"""
    cfg = SCENARIOS.get(scenario, SCENARIOS["商务"])
    return f"""主题行: [{scenario} - {to_name}] {requirement[:14]}

{to_name},

[正文 1: 切入 — 1 句具体事实或数据]
[正文 2: 价值 — 1-2 句你能给什么]
[正文 3: 行动 — 1 句明确 CTA]

老张
fast118 创始人
"""


def main():
    ap = argparse.ArgumentParser(description="5 大场景邮件骨架生成器")
    ap.add_argument("requirement", help="邮件需求描述")
    ap.add_argument("--to", default="X总", help="收件人称谓")
    ap.add_argument("--tone", choices=list(SCENARIOS.keys()), help="指定场景（不传则自动检测）")
    args = ap.parse_args()

    scenario = args.tone or detect_scenario(args.requirement)
    print(f"检测场景: {scenario}（长度建议 {SCENARIOS[scenario]['length']}）\n")
    print(build_email(scenario, args.requirement, args.to))
    print("\n注意: 这是骨架,实际血肉由 AI 在 Claude Code / Codex 里填充。")
    print("详细原则见 SKILL.md 的 '6 条反 AI 检测要点'。")


if __name__ == "__main__":
    main()
