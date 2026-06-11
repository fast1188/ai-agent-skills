@echo off
REM install.bat - Install cursor-rules-pack skill

set SKILL_DIR=%USERPROFILE%\.claude\skills\cursor-rules-pack
set SCRIPT_DIR=%~dp0

echo ====================================
echo  cursor-rules-pack skill installer
echo ====================================
echo.

if not exist "%USERPROFILE%\.claude\skills" (
    mkdir "%USERPROFILE%\.claude\skills"
)

if exist "%SKILL_DIR%" (
    echo [INFO] Updating existing installation...
    rmdir /s /q "%SKILL_DIR%"
)

mkdir "%SKILL_DIR%"
mkdir "%SKILL_DIR%\rules"
copy "%SCRIPT_DIR%SKILL.md" "%SKILL_DIR%\SKILL.md" >nul
copy "%SCRIPT_DIR%.cursorrules-template" "%SKILL_DIR%\.cursorrules-template" >nul
copy "%SCRIPT_DIR%\rules\*.md" "%SKILL_DIR%\rules\" >nul

echo [OK] Installed to: %SKILL_DIR%
echo.
echo Usage:
echo   1. Copy .cursorrules-template to your project root
echo   2. Rename to .cursorrules
echo   3. Customize for your project type
echo.
pause