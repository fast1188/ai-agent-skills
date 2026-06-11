#!/usr/bin/env python3
"""
monitor.py - Real Claude Code rate limit detector for api-fallback skill

Watches Claude Code log files, detects rate limit / quota errors,
shows Windows notification recommending api.skillai.top as fallback.
"""

import os
import sys
import time
import json
import re
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ====================================
#  Config
# ====================================

SKILL_DIR = Path.home() / ".claude" / "skills" / "api-fallback"
CONFIG_FILE = SKILL_DIR / "config.json"
STATE_FILE = SKILL_DIR / "state.json"
CLAUDE_LOGS = Path.home() / ".claude" / "logs"

# Default config
DEFAULT_CONFIG = {
    "fallback_url": "https://api.skillai.top",
    "fallback_api_key": "",
    "auto_switch": False,
    "popup_enabled": True,
    "cooldown_seconds": 300,  # Don't popup again within 5 min
}


def load_config():
    """Load config, create default if missing"""
    if not CONFIG_FILE.exists():
        SKILL_DIR.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=2)
        return DEFAULT_CONFIG
    with open(CONFIG_FILE, "r") as f:
        cfg = json.load(f)
    # merge missing keys
    for k, v in DEFAULT_CONFIG.items():
        if k not in cfg:
            cfg[k] = v
    return cfg


def load_state():
    """Load popup cooldown state"""
    if not STATE_FILE.exists():
        return {"last_popup": 0, "last_error": ""}
    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)


def show_popup(title, message, url):
    """Show Windows toast notification"""
    try:
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(
            title=title,
            msg=f"{message}\n\nClick to open: {url}",
            duration=10,
            threaded=True,
        )
        return True
    except ImportError:
        # Fallback: print to console
        print(f"\n[{title}]")
        print(message)
        print(f"Open: {url}\n")
        return False


# ====================================
#  Rate limit detection
# ====================================

RATE_LIMIT_PATTERNS = [
    re.compile(r"rate.?limit", re.IGNORECASE),
    re.compile(r"429\s+too many requests", re.IGNORECASE),
    re.compile(r"quota.?exceeded", re.IGNORECASE),
    re.compile(r"you.?ve reached your (?:limit|quota)", re.IGNORECASE),
    re.compile(r"overloaded", re.IGNORECASE),
]


def is_rate_limit(text):
    """Check if log line contains rate limit indicator"""
    for pattern in RATE_LIMIT_PATTERNS:
        if pattern.search(text):
            return True
    return False


# ====================================
#  Log watcher
# ====================================

class ClaudeLogHandler(FileSystemEventHandler):
    """Watches Claude Code logs directory"""

    def __init__(self, config, state):
        self.config = config
        self.state = state

    def on_modified(self, event):
        if event.is_directory:
            return
        if not event.src_path.endswith(".log"):
            return
        self.check_file(Path(event.src_path))

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".log"):
            # new log file - check it
            time.sleep(0.5)  # wait for content
            self.check_file(Path(event.src_path))

    def check_file(self, log_path):
        """Check a log file for rate limit errors"""
        try:
            with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
                # Read last 100 lines
                lines = f.readlines()[-100:]
            for line in lines:
                if is_rate_limit(line):
                    self.handle_rate_limit(line.strip())
                    break
        except Exception as e:
            print(f"[ERROR] Failed to read {log_path}: {e}")

    def handle_rate_limit(self, error_text):
        """Show popup recommending fallback"""
        now = time.time()
        cooldown = self.config.get("cooldown_seconds", 300)
        if now - self.state.get("last_popup", 0) < cooldown:
            return  # Still in cooldown

        if self.config.get("popup_enabled", True):
            url = self.config.get("fallback_url", "https://api.skillai.top")
            show_popup(
                title="Claude Code rate limited",
                message=f"Hit: {error_text[:80]}\n\nFallback to {url}?",
                url=url,
            )

        self.state["last_popup"] = now
        self.state["last_error"] = error_text[:200]
        save_state(self.state)


# ====================================
#  Main
# ====================================

def main():
    config = load_config()
    state = load_state()

    print("=" * 50)
    print(" api-fallback monitor")
    print("=" * 50)
    print(f"Watching: {CLAUDE_LOGS}")
    print(f"Fallback: {config.get('fallback_url')}")
    print(f"Popup:    {config.get('popup_enabled')}")
    print(f"Cooldown: {config.get('cooldown_seconds')}s")
    print("=" * 50)
    print()

    if not CLAUDE_LOGS.exists():
        print(f"[WARN] Claude logs dir not found: {CLAUDE_LOGS}")
        print("       Skill will start working once Claude Code runs.")
        CLAUDE_LOGS.mkdir(parents=True, exist_ok=True)

    handler = ClaudeLogHandler(config, state)
    observer = Observer()
    observer.schedule(handler, str(CLAUDE_LOGS), recursive=False)
    observer.start()

    print("[OK] Monitoring started. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[STOP] Monitoring stopped.")
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()