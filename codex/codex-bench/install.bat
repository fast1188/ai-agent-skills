@echo off
REM install.bat - Install codex-bench
set SKILL_DIR=%USERPROFILE%\.claude\skills\codex-bench
set SCRIPT_DIR=%~dp0
if not exist "%USERPROFILE%\.claude\skills" mkdir "%USERPROFILE%\.claude\skills"
if exist "%SKILL_DIR%" rmdir /s /q "%SKILL_DIR%"
mkdir "%SKILL_DIR%"
copy "%SCRIPT_DIR%SKILL.md" "%SKILL_DIR%\SKILL.md" >nul
echo [OK] Installed to %SKILL_DIR%
pause