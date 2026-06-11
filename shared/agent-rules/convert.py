#!/usr/bin/env python3
"""
convert.py - 从 AGENT_RULES.md 生成各 AI 工具原生格式

Usage:
    python convert.py

Generates:
    - CLAUDE.md     (Claude Code)
    - AGENTS.md     (Codex)
    - .cursorrules  (Cursor)
    - CONVENTIONS.md (OpenClaw / Hermes / generic)
"""

import re
from pathlib import Path

HERE = Path(__file__).parent
MASTER = HERE / "AGENT_RULES.md"


def extract_sections(markdown: str) -> dict:
    """Parse AGENT_RULES.md into sections by ## heading."""
    sections = {}
    current_h2 = None
    current_lines = []

    for line in markdown.splitlines():
        m = re.match(r"^## (.+)$", line)
        if m:
            if current_h2:
                sections[current_h2] = "\n".join(current_lines).strip()
            current_h2 = m.group(1).strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_h2:
        sections[current_h2] = "\n".join(current_lines).strip()
    return sections


def to_compact(markdown: str, max_chars_per_section: int = 500) -> str:
    """Convert detailed markdown to compact form for native configs."""
    sections = extract_sections(markdown)
    out = []
    title_line = markdown.splitlines()[0].lstrip("# ").strip() if markdown else "AI Dev Standards"
    out.append(f"# {title_line}")
    out.append("")
    out.append("> 由 AGENT_RULES.md 自动生成。不要直接编辑,改 master 后跑 convert.py")
    out.append("")
    out.append("---")
    out.append("")

    section_labels = {
        "回复语言": "## 语言",
        "代码风格": "## 代码",
        "注释规范": "",
        "导入顺序": "",
        "错误处理": "## 错误处理",
        "测试要求": "## 测试",
        "安全规范": "## 安全",
        "提交规范": "## Commit",
        "分支命名": "",
        "PR 要求": "",
        "文档规范": "## 文档",
        "性能规范": "## 性能",
        "AI 工具特定行为": "## 行为",
        "协作规范": "",
    }

    for h2, content in sections.items():
        label = section_labels.get(h2, f"## {h2}")
        if not label:
            continue
        out.append(label)
        out.append("")
        # Compact: keep first list items
        lines = content.splitlines()
        compact = []
        for line in lines:
            stripped = line.strip()
            if not stripped:
                compact.append("")
                continue
            if stripped.startswith("|") or stripped.startswith("-") or stripped.startswith("*") or stripped.startswith("```"):
                compact.append(line)
            elif stripped.startswith("#"):
                compact.append("**" + stripped.lstrip("# ").strip() + "**")
            else:
                compact.append(stripped)
        text = "\n".join(compact).strip()
        if len(text) > max_chars_per_section:
            text = text[:max_chars_per_section] + "\n...(详见 master)"
        out.append(text)
        out.append("")

    return "\n".join(out)


def write_outputs(markdown: str):
    """Write all native format files."""
    compact = to_compact(markdown)

    files = {
        "CLAUDE.md": compact,
        "AGENTS.md": compact,
        ".cursorrules": compact,
        "CONVENTIONS.md": compact,
    }
    for filename, content in files.items():
        path = HERE / filename
        path.write_text(content, encoding="utf-8")
        print(f"  Generated: {filename}")


def main():
    if not MASTER.exists():
        print(f"ERROR: {MASTER} not found")
        return 1
    markdown = MASTER.read_text(encoding="utf-8")
    print(f"Master file: {MASTER}")
    print(f"Size: {len(markdown)} chars")
    print()
    print("Generating native formats:")
    write_outputs(markdown)
    print()
    print("Done!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())