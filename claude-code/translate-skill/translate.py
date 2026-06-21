"""translate.py — 翻译 skill CLI (5 场景, 0 依赖, ≤100 行)

用法:
    py translate.py "你好" --to en                       # 默认 mail 场景
    py translate.py "API 调用失败" --scenario tech --to en
    py translate.py "行 那就这么定了" --scenario chat
"""
import re
import sys
import argparse
from pathlib import Path

SCENARIOS = {
    "doc": {
        "trigger": ["文档", "文章", "报告", "doc", "report", "article", "essay", "白皮书"],
        "register": "formal",
        "person": "third",
        "tense": "present",
        "length_pct": (90, 110),
    },
    "mail": {
        "trigger": ["邮件", "email", "mail", "回复", "re", "客户", "合作"],
        "register": "business",
        "person": "second",
        "tense": "present",
        "length_pct": (90, 110),
    },
    "chat": {
        "trigger": ["口语", "聊天", "对话", "chat", "whatsapp", "微信", "wechat", "群"],
        "register": "casual",
        "person": "first_second",
        "tense": "present_progressive",
        "length_pct": (80, 100),
    },
    "tech": {
        "trigger": ["code", "api", "错误", "log", "代码", "技术", "函数", "变量", "错误码", "token", "接口"],
        "register": "precise",
        "person": "third",
        "tense": "present",
        "length_pct": (95, 105),
    },
    "lit": {
        "trigger": ["小说", "散文", "诗", "文学", "story", "poem", "novel", "narration"],
        "register": "literary",
        "person": "first_third",
        "tense": "preserve",
        "length_pct": (90, 110),
    },
}

ANTI_AI_RULES = [
    "不用 Furthermore / Additionally / Moreover 起句",
    "不用大词 (utilize→use, commence→start)",
    "保持术语一致 (术语表锁定)",
    "口语场景用人称 (不用 one should)",
    "技术场景保留原变量名 (myVar 不译)",
    "原文没的 'I hope this helps' 不补",
]


def detect_scenario(text):
    """根据关键词打分, 同分按位置破 (越靠前越像用户本意)"""
    text_lower = text.lower()
    scored = []
    for scenario, cfg in SCENARIOS.items():
        score = 0
        first_pos = len(text)
        for kw in cfg["trigger"]:
            pos = text_lower.find(kw.lower())
            if pos >= 0:
                score += 1
                if pos < first_pos:
                    first_pos = pos
        scored.append((scenario, score, first_pos))
    scored.sort(key=lambda x: (-x[1], x[2]))
    return scored[0][0] if scored[0][1] > 0 else "mail"


def build_prompt(text, scenario, target_lang):
    """构造 Claude prompt (AI 实际填血肉)"""
    cfg = SCENARIOS[scenario]
    return f"""请把下面的中文翻译成 {target_lang}.

场景: {scenario} (语域: {cfg['register']}, 人称: {cfg['person']}, 时态: {cfg['tense']})

反 AI 翻译规则 (6 条):
{chr(10).join(f"- {r}" for r in ANTI_AI_RULES)}

原文:
{text}

只输出翻译结果, 格式:
<原文>
--->
<译文>
"""


def main():
    ap = argparse.ArgumentParser(description="中英翻译 skill (5 场景, AI 填血肉)")
    ap.add_argument("text", help="要翻译的中文")
    ap.add_argument("--to", default="en", help="目标语言 (默认 en)")
    ap.add_argument("--scenario", choices=list(SCENARIOS.keys()),
                    help="强制指定场景 (不传则自动检测)")
    ap.add_argument("--prompt-only", action="store_true",
                    help="只输出 prompt, 不调用 AI (给 Claude Code 用)")
    args = ap.parse_args()

    scenario = args.scenario or detect_scenario(args.text)
    cfg = SCENARIOS[scenario]

    print(f"检测场景: {scenario} (语域={cfg['register']}, 人称={cfg['person']}, 时态={cfg['tense']})")
    print(f"目标语言: {args.to}")
    print(f"长度范围: {cfg['length_pct'][0]}-{cfg['length_pct'][1]}% 原文")
    print()
    if args.prompt_only:
        print(build_prompt(args.text, scenario, args.to))
    else:
        print("[CLI 模式] 实际翻译请在 Claude Code 中调用本 skill.")
        print("  或用 --prompt-only 看 prompt 结构")
        print()
        print("=" * 60)
        print(build_prompt(args.text, scenario, args.to))
        print("=" * 60)


if __name__ == "__main__":
    main()
