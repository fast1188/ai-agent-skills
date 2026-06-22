# Security Policy

## Supported Versions

| Version | Supported          |
|---------|-------------------|
| 0.3.x   | :white_check_mark: |
| 0.2.x   | :white_check_mark: |
| < 0.2   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability:

1. **DO NOT** open a public issue
2. Email: fast118.security@gmail.com (or contact via WeChat group)
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Impact assessment
   - Suggested fix (optional)

We will respond within 48 hours.

## Security Best Practices

When using ai-agent-skills:

### DO
- ✅ Keep your API keys in environment variables, never in code
- ✅ Use `.env` files and add them to `.gitignore`
- ✅ Review skill code before installation
- ✅ Use unique passwords for each AI tool
- ✅ Enable 2FA on GitHub/Gitee accounts
- ✅ Run skills in sandboxed environments when possible

### DON'T
- ❌ Commit `.env` / `*.key` / `*.pem` / `cookies.json`
- ❌ Share API keys in chat / screenshots / issues
- ❌ Disable SSL verification
- ❌ Run untrusted skill code with admin/root privileges
- ❌ Use the same API key across multiple public repos

## Known Security Considerations

### api-fallback skill
- Reads Claude Code log files (read-only)
- Shows system notifications
- Sends anonymous error type to api.skillai.top (optional)
- **Does NOT** transmit user code or conversation content

### token-saver skill
- Operates on local prompts only
- No network calls
- Pure string transformation

### chinese-dev-helper skill
- Local term mapping
- Only sends prompts to AI tools user already configured
- No data collection

### multi-agent-install skill
- Runs `npm install -g` and `pip install` commands
- **Verify** package names before installation
- Only install packages from official npm/pypi registries

### agent-rules skill
- Generates configuration files
- No network calls
- Local file writes only

### codex-starter skill
- Copies prompt templates to `~/.codex/prompts/`
- Local-only operation
- No data collection

### openclaw-deploy skill
- Installs OpenClaw on remote server
- Creates systemd service with user `openclaw`
- **Review** install.sh before running as root
- Change default passwords immediately after install

### hermes-tutorial skill
- Installs hermes-agent via pip
- Long-term memory stored locally in SQLite
- Local-only operation

## Reporting Dependency Vulnerabilities

We use GitHub Dependabot. If you find a vulnerability:

1. Check [GitHub Security Advisories](https://github.com/fast1188/ai-agent-skills/security/advisories)
2. Or open a private security issue

## Acknowledgments

We thank security researchers who responsibly disclose vulnerabilities.

## Updates to This Policy

This policy may be updated. Last updated: 2026-06-11.