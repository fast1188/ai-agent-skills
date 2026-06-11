#!/bin/bash
# install.sh - Install api-fallback skill for Claude Code (Linux/Mac)

set -e

SKILL_DIR="$HOME/.claude/skills/api-fallback"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "===================================="
echo " api-fallback skill installer"
echo "===================================="
echo

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 not found"
    exit 1
fi

# Create skills dir
mkdir -p "$HOME/.claude/skills"

# Remove old version
if [ -d "$SKILL_DIR" ]; then
    echo "[INFO] Updating existing installation..."
    rm -rf "$SKILL_DIR"
fi

mkdir -p "$SKILL_DIR"
cp "$SCRIPT_DIR/SKILL.md" "$SKILL_DIR/SKILL.md"
cp "$SCRIPT_DIR/monitor.py" "$SKILL_DIR/monitor.py"
cp "$SCRIPT_DIR/requirements.txt" "$SKILL_DIR/requirements.txt"

# Install Python deps
echo "Installing Python dependencies..."
python3 -m pip install -r "$SKILL_DIR/requirements.txt"

# Create start script
cat > "$SKILL_DIR/start.sh" <<EOF
#!/bin/bash
python3 "$SKILL_DIR/monitor.py"
EOF
chmod +x "$SKILL_DIR/start.sh"

echo
echo "===================================="
echo " Installed!"
echo "===================================="
echo
echo "Skill location: $SKILL_DIR"
echo "Start:          $SKILL_DIR/start.sh"
echo
echo "Next:"
echo "  1. Configure: edit $SKILL_DIR/config.json"
echo "  2. Add api.skillai.top API key"
echo "  3. Run start.sh in background or systemd"
echo