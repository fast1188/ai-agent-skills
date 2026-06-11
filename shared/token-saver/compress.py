#!/usr/bin/env python3
"""
compress.py - Prompt compression for AI agents

Usage:
    python compress.py "your long prompt here"
    echo "long prompt" | python compress.py
"""

import sys
import re
from pathlib import Path

# ====================================
#  Compression rules
# ====================================

# Polite phrases to remove (Chinese)
POLITE_REMOVES_ZH = [
    r"请你帮我",
    r"请帮我",
    r"麻烦你",
    r"非常感谢",
    r"谢谢",
    r"麻烦",
    r"拜托",
    r"劳驾",
    r"请",
]

# Polite phrases to remove (English)
POLITE_REMOVES_EN = [
    r"\bplease\b",
    r"\bcan you\b",
    r"\bcould you\b",
    r"\bwould you\b",
    r"\bI would like (?:you )?to\b",
    r"\bthanks?\b",
    r"\bthank you\b",
]

# Redundant words (Chinese)
REDUNDANT_ZH = [
    (r"的作用是", "是"),
    (r"的主要功能是", "功能:"),
    (r"它可以", ""),
    (r"能够", ""),
    (r"并且", "并"),
    (r"而且", "且"),
    (r"然后", "后"),
    (r"接下来", ""),
    (r"请确保", ""),
    (r"请注意", ""),
    (r"非常重要", ""),
]

# Redundant words (English)
REDUNDANT_EN = [
    (r"\bin order to\b", "to"),
    (r"\bbasically\b", ""),
    (r"\bactually\b", ""),
    (r"\breally\b", ""),
    (r"\bvery\b", ""),
    (r"\bquite\b", ""),
    (r"\bjust\b", ""),
    (r"\bsimply\b", ""),
]


def detect_language(text: str) -> str:
    """Detect if text is Chinese or English"""
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    return "zh" if chinese_chars > len(text) * 0.3 else "en"


def light_compress(text: str) -> str:
    """Light compression - remove polite phrases only"""
    lang = detect_language(text)
    removes = POLITE_REMOVES_ZH if lang == "zh" else POLITE_REMOVES_EN
    for pattern in removes:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text.strip()


def medium_compress(text: str) -> str:
    """Medium - light + redundant removal + collapse whitespace"""
    text = light_compress(text)
    lang = detect_language(text)
    rules = REDUNDANT_ZH if lang == "zh" else REDUNDANT_EN
    for pattern, replacement in rules:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    # Collapse multiple spaces
    text = re.sub(r"\s+", " ", text)
    # Collapse multiple punctuation
    text = re.sub(r"。{2,}", "。", text)
    text = re.sub(r"\.{2,}", ".", text)
    return text.strip()


def extreme_compress(text: str) -> str:
    """Extreme - caveman style, key verbs + nouns only"""
    text = medium_compress(text)
    # Remove articles and filler
    text = re.sub(r"\b(the|a|an)\b", "", text, flags=re.IGNORECASE)
    # Remove "I/we/you" pronouns (English)
    text = re.sub(r"\b(I|we|you|your|my)\b", "", text, flags=re.IGNORECASE)
    # Comma + space -> space
    text = re.sub(r",\s+", " ", text)
    return text.strip()


def estimate_tokens(text: str) -> int:
    """Rough token estimate (English ~ 4 chars / token, Chinese ~ 1.5 chars / token)"""
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    other_chars = len(text) - chinese_chars
    return int(chinese_chars / 1.5 + other_chars / 4)


def compress(text: str, mode: str = "medium") -> dict:
    """Compress text in given mode"""
    if mode == "light":
        compressed = light_compress(text)
    elif mode == "extreme":
        compressed = extreme_compress(text)
    else:
        compressed = medium_compress(text)

    return {
        "original": text,
        "compressed": compressed,
        "mode": mode,
        "original_tokens": estimate_tokens(text),
        "compressed_tokens": estimate_tokens(compressed),
    }


def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        mode = "medium"
    else:
        text = sys.stdin.read()
        mode = "medium"

    result = compress(text, mode)
    saved = result["original_tokens"] - result["compressed_tokens"]
    pct = (saved / result["original_tokens"] * 100) if result["original_tokens"] else 0

    print(result["compressed"])
    print()
    print(f"[tokens] {result['original_tokens']} -> {result['compressed_tokens']} (saved {saved}, {pct:.0f}%)")


if __name__ == "__main__":
    main()