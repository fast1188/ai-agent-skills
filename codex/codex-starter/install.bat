@echo off
REM install.bat - Install codex-starter skill

set CODEX_DIR=%USERPROFILE%\.codex
set SKILL_DIR=%CODEX_DIR%\skills\codex-starter
set SCRIPT_DIR=%~dp0

echo ====================================
echo  codex-starter skill installer
echo ====================================
echo.

if not exist "%CODEX_DIR%" (
    echo [INFO] Creating ~/.codex directory...
    mkdir "%CODEX_DIR%"
    mkdir "%CODEX_DIR%\prompts"
)

if exist "%SKILL_DIR%" (
    echo [INFO] Updating existing installation...
    rmdir /s /q "%SKILL_DIR%"
)

mkdir "%SKILL_DIR%"
copy "%SCRIPT_DIR%SKILL.md" "%SKILL_DIR%\SKILL.md" >nul

REM Copy config (don't overwrite existing)
if not exist "%CODEX_DIR%\config.toml" (
    copy "%SCRIPT_DIR%config.toml" "%CODEX_DIR%\config.toml" >nul
    echo [OK] Copied config.toml
) else (
    echo [INFO] config.toml already exists, skipped.
)

REM Copy prompts
if not exist "%CODEX_DIR%\prompts" mkdir "%CODEX_DIR%\prompts"
copy "%SCRIPT_DIR%\prompts\*.md" "%CODEX_DIR%\prompts\" >nul
echo [OK] Copied prompt templates

echo.
echo ====================================
echo  Installed to: %SKILL_DIR%
echo  Prompts: %CODEX_DIR%\prompts\
echo ====================================
echo.
pause