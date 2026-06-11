@echo off
REM install-all.bat - Install all major AI coding agents on Windows

setlocal enabledelayedexpansion

echo ======================================
echo  multi-agent-install v1.0
echo ======================================
echo.

REM Detect OS
echo Detecting system...
for /f "tokens=*" %%i in ('ver') do set OS_VER=%%i
echo   OS: %OS_VER%
where node >nul 2>&1 && (
    for /f "tokens=*" %%v in ('node --version') do echo   Node.js: %%v
) || (
    echo   [WARN] Node.js not found. CLI tools will fail.
)
where python >nul 2>&1 && (
    for /f "tokens=*" %%v in ('python --version') do echo   Python: %%v
) || (
    where py >nul 2>&1 && (
        for /f "tokens=*" %%v in ('py --version') do echo   Python: %%v
    ) || (
        echo   [WARN] Python not found. Hermes will fail.
    )
)
echo.

REM Check existing
echo Checking existing tools...
where claude >nul 2>&1 && echo   [OK] Claude Code || echo   [MISS] Claude Code
where codex >nul 2>&1 && echo   [OK] Codex || echo   [MISS] Codex
where cursor >nul 2>&1 && echo   [OK] Cursor || echo   [MISS] Cursor
where openclaw >nul 2>&1 && echo   [OK] OpenClaw || echo   [MISS] OpenClaw
where hermes >nul 2>&1 && echo   [OK] Hermes Agent || echo   [MISS] Hermes Agent
echo.

REM Ask user
echo Install which tools? (default: all)
set /p INSTALL_CLAUDE="  Claude Code [Y/n]: "
set /p INSTALL_CODEX="  Codex [Y/n]: "
set /p INSTALL_OPENCLAW="  OpenClaw [Y/n]: "
set /p INSTALL_HERMES="  Hermes Agent [Y/n]: "

if "%INSTALL_CLAUDE%"=="" set INSTALL_CLAUDE=Y
if "%INSTALL_CODEX%"=="" set INSTALL_CODEX=Y
if "%INSTALL_OPENCLAW%"=="" set INSTALL_OPENCLAW=Y
if "%INSTALL_HERMES%"=="" set INSTALL_HERMES=Y
echo.

REM Install Claude Code
if /i "%INSTALL_CLAUDE%"=="Y" (
    echo Installing Claude Code...
    call npm install -g @anthropic-ai/claude-code
    if errorlevel 1 (
        echo   [FAIL] Claude Code install failed
    ) else (
        echo   [OK] Claude Code installed
    )
)

REM Install Codex
if /i "%INSTALL_CODEX%"=="Y" (
    echo Installing Codex...
    call npm install -g @openai/codex
    if errorlevel 1 (
        echo   [FAIL] Codex install failed
    ) else (
        echo   [OK] Codex installed
    )
)

REM Install OpenClaw
if /i "%INSTALL_OPENCLAW%"=="Y" (
    echo Installing OpenClaw...
    call npm install -g @openclaw/openclaw
    if errorlevel 1 (
        echo   [FAIL] OpenClaw install failed
    ) else (
        echo   [OK] OpenClaw installed
    )
)

REM Install Hermes
if /i "%INSTALL_HERMES%"=="Y" (
    echo Installing Hermes Agent...
    call pip install hermes-agent
    if errorlevel 1 (
        echo   [FAIL] Hermes install failed
    ) else (
        echo   [OK] Hermes installed
    )
)

echo.
echo ======================================
echo  Installation complete!
echo ======================================
echo.
echo Next steps:
echo   1. Configure API keys for each tool
echo   2. See ai-agent-skills README.md
echo.
pause