#!/bin/bash
# install.sh - Install hermes-tutorial skill (Linux/Mac)

set -e

SKILL_DIR="$HOME/.hermes/skills/hermes-tutorial"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "===================================="
echo " hermes-tutorial skill installer"
echo "===================================="
echo

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 not found. Install Python 3.10+"
    exit 1
fi

mkdir -p "$HOME/.hermes/skills"

if [ -d "$SKILL_DIR" ]; then
    echo "[INFO] Updating existing installation..."
    rm -rf "$SKILL_DIR"
fi

mkdir -p "$SKILL_DIR"
cp "$SCRIPT_DIR/SKILL.md" "$SKILL_DIR/SKILL.md"
cp "$SCRIPT_DIR/config.toml" "$SKILL_DIR/config.toml"

echo "Installing hermes-agent..."
python3 -m pip install hermes-agent || echo "[WARN] hermes-agent install failed"

echo
echo "===================================="
echo " Installed!"
echo "====================================
echo
echo "Try:"
echo "  python3 -m hermes init"
echo "  python3 -m hermes chat"
echo