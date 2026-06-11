#!/bin/bash
# install-all.sh - Install all major AI coding agents on Linux/macOS

set -e

echo "======================================"
echo " multi-agent-install v1.0"
echo "======================================"
echo

# Detect OS
echo "Detecting system..."
OS="$(uname -s)"
case "$OS" in
    Linux*)     OS_NAME="Linux";;
    Darwin*)    OS_NAME="macOS";;
    *)          OS_NAME="Unknown: $OS";;
esac
echo "  OS: $OS_NAME"

# Check tools
echo "  Node.js: $(node --version 2>/dev/null || echo 'NOT FOUND')"
echo "  Python:  $(python3 --version 2>/dev/null || echo 'NOT FOUND')"
echo "  npm:     $(npm --version 2>/dev/null || echo 'NOT FOUND')"
echo "  pip:     $(pip3 --version 2>/dev/null || echo 'NOT FOUND')"
echo

# Check existing
echo "Checking existing tools..."
for tool in claude codex cursor openclaw hermes; do
    if command -v "$tool" >/dev/null 2>&1; then
        echo "  [OK] $tool"
    else
        echo "  [MISS] $tool"
    fi
done
echo

# Ask user
read -p "Install all? [Y/n]: " INSTALL_ALL
INSTALL_ALL=${INSTALL_ALL:-Y}

# Install Claude Code
if [[ "$INSTALL_ALL" =~ ^[Yy]$ ]]; then
    echo "Installing Claude Code..."
    if npm install -g @anthropic-ai/claude-code 2>/dev/null; then
        echo "  [OK] Claude Code installed"
    else
        echo "  [FAIL] Claude Code install failed (try: npm install -g @anthropic-ai/claude-code)"
    fi

    echo "Installing Codex..."
    if npm install -g @openai/codex 2>/dev/null; then
        echo "  [OK] Codex installed"
    else
        echo "  [FAIL] Codex install failed"
    fi

    echo "Installing OpenClaw..."
    if npm install -g @openclaw/openclaw 2>/dev/null; then
        echo "  [OK] OpenClaw installed"
    else
        echo "  [FAIL] OpenClaw install failed"
    fi

    echo "Installing Hermes Agent..."
    if pip3 install hermes-agent 2>/dev/null; then
        echo "  [OK] Hermes Agent installed"
    else
        echo "  [FAIL] Hermes install failed"
    fi
fi

echo
echo "======================================"
echo " Installation complete!"
echo "======================================"