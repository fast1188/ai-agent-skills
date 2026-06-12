#!/usr/bin/env python3
"""
benchmark.py - Model benchmark runner
Runs the same tasks across multiple models and generates a comparison report.
"""

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime
from openai import OpenAI

CONFIG_FILE = Path(__file__).parent / "config.json"

# Test tasks
TASKS = {
    "code-gen": {
        "name": "代码生成 - 快速排序",
        "prompt": "用 Python 写一个快速排序算法,要求:\n1. 函数名 quicksort\n2. 接收一个列表,返回排序后的列表\n3. 添加类型注解\n4. 加 docstring\n5. 加 1-2 条注释",
        "eval": lambda x: 1 if "def quicksort" in x and "-> " in x else 0,
    },
    "code-refactor": {
        "name": "代码重构",
        "prompt": "把下面这段过程式代码改成面向对象:\n\ndef calc(x, y, op):\n    if op == 'add': return x + y\n    elif op == 'sub': return x - y\n    elif op == 'mul': return x * y\n    elif op == 'div': return x / y",
        "eval": lambda x: 1 if "class" in x else 0,
    },
    "bug-fix": {
        "name": "Bug 修复",
        "prompt": "找出下面 Python 代码里的 bug:\n\ndef add_item(lst, item):\n    lst.append(item)\n    return lst\n\nresult = add_item(None, 'x')\nprint(result)",
        "eval": lambda x: 1 if "None" in x else 0,
    },
    "translate": {
        "name": "翻译 EN → ZH",
        "prompt": "把下面这段英文翻译成中文:\n\n'Open source software is developed in a collaborative manner, where developers from around the world contribute to projects they care about.'",
        "eval": lambda x: 1 if any("\u4e00" <= c <= "\u9fff" for c in x) else 0,
    },
    "summarize": {
        "name": "长文摘要",
        "prompt": "用 100 字总结下面这段话的核心:\n\n'Python 是一种广泛使用的高级编程语言,属于通用型编程语言,由 Guido van Rossum 创建,首次发布于 1991 年。Python 的设计哲学强调代码的可读性和简洁的语法,特别是使用空格缩进划分代码块。相比于 C++ 或 Java,Python 让开发者能够用更少的代码表达想法。它支持多种编程范式,包括面向对象、命令式、函数式和过程式编程。Python 拥有动态类型系统和垃圾回收功能,能够自动管理内存使用,并且有庞大的标准库和第三方包生态系统。'",
        "eval": lambda x: 1 if len(x) > 30 and len(x) < 300 else 0,
    },
    "reason": {
        "name": "推理",
        "prompt": "一个房间里有 3 个人。\n- 第 1 个人说:\"我们都戴着红帽子\"\n- 第 2 个人说:\"至少一个人戴着蓝帽子\"\n- 第 3 个人说:\"我戴着绿帽子\"\n\n已知这 3 句话里恰好 1 句是真的。\n问:每个人戴的什么帽子?\n请用 50 字以内说明推理。",
        "eval": lambda x: 1 if len(x) > 30 and len(x) < 200 else 0,
    },
}


def load_config():
    """Load config, fall back to defaults."""
    if not CONFIG_FILE.exists():
        return {
            "providers": {
                "github_models": {
                    "base_url": "https://api.skillai.top",
                    "key_file": "github_models.key.txt",
                    "default_model": "gpt-4o-mini",
                },
                "groq": {
                    "base_url": "https://api.skillai.top",
                    "key_file": "groq.key.txt",
                    "default_model": "llama-3.3-70b-versatile",
                },
                "gemini": {
                    "base_url": "https://api.skillai.top",
                    "key_file": "gemini.key.txt",
                    "default_model": "gemini-2.0-flash-exp",
                },
            },
            "iterations": 3,
        }
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_api_key(key_file):
    """Load API key from file."""
    key_path = Path(__file__).parent / key_file
    if key_path.exists():
        with open(key_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return os.getenv(key_file.upper().replace(".KEY.TXT", "_API_KEY"))


def run_single_task(client, model, task_id, task):
    """Run a single task, return (latency, output, score)."""
    start = time.time()
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": task["prompt"]}],
            max_tokens=1000,
            temperature=0.7,
        )
        latency = time.time() - start
        output = response.choices[0].message.content
        score = task["eval"](output)
        tokens = response.usage.total_tokens if response.usage else 0
        return {"latency": latency, "output": output, "score": score, "tokens": tokens}
    except Exception as e:
        return {"latency": 0, "output": f"[ERROR] {e}", "score": 0, "tokens": 0}


def main():
    print("=" * 50)
    print(" model-benchmark v1.0")
    print("=" * 50)
    print()

    config = load_config()

    # Build clients per provider
    clients = {}
    for prov_name, prov_cfg in config["providers"].items():
        api_key = load_api_key(prov_cfg["key_file"])
        if api_key:
            try:
                clients[prov_name] = {
                    "client": OpenAI(base_url=prov_cfg["base_url"], api_key=api_key),
                    "model": prov_cfg["default_model"],
                    "name": prov_name,
                }
            except Exception as e:
                print(f"[SKIP] {prov_name}: {e}")

    if not clients:
        print("[ERROR] No providers configured. Add API keys first.")
        return 1

    print(f"Loaded {len(clients)} providers: {', '.join(clients.keys())}")
    print()

    # Run benchmarks
    results = {}
    iterations = config.get("iterations", 3)

    for task_id, task in TASKS.items():
        print(f"\nTask: {task['name']}")
        results[task_id] = {}

        for prov_name, prov in clients.items():
            print(f"  {prov_name} ({prov['model']}):")
            scores = []
            latencies = []

            for i in range(iterations):
                r = run_single_task(prov["client"], prov["model"], task_id, task)
                scores.append(r["score"])
                latencies.append(r["latency"])
                print(f"    [{i+1}/{iterations}] {r['latency']:.2f}s score={r['score']}")

            avg_score = sum(scores) / len(scores) if scores else 0
            avg_latency = sum(latencies) / len(latencies) if latencies else 0
            results[task_id][prov_name] = {
                "avg_score": avg_score,
                "avg_latency": avg_latency,
                "model": prov["model"],
            }
            print(f"  -> {prov_name}: avg_score={avg_score:.2f} avg_latency={avg_latency:.2f}s")

    # Generate report
    print()
    print("=" * 50)
    print(" 报告")
    print("=" * 50)
    print()

    # Overall scores
    overall = {p: 0 for p in clients}
    counts = {p: 0 for p in clients}
    for task_id, task_results in results.items():
        for prov_name, r in task_results.items():
            overall[prov_name] += r["avg_score"]
            counts[prov_name] += 1

    print("综合排名:")
    sorted_providers = sorted(clients.keys(), key=lambda p: overall[p] / counts[p] if counts[p] else 0, reverse=True)
    for i, p in enumerate(sorted_providers, 1):
        avg = overall[p] / counts[p] if counts[p] else 0
        print(f"  {i}. {p} ({clients[p]['model']}): {avg:.2f}")

    # Save report
    report = {
        "timestamp": datetime.now().isoformat(),
        "results": results,
        "overall": {p: overall[p] / counts[p] if counts[p] else 0 for p in clients},
    }
    report_file = Path(__file__).parent / f"report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nReport saved: {report_file}")


if __name__ == "__main__":
    main()