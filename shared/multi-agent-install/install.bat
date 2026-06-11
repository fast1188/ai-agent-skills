@echo off
REM install.bat - Install multi-agent-install skill (helper only)

set SKILL_DIR=%USERPROFILE%\.claude\skills\multi-agent-install
set SCRIPT_DIR=%~dp0

echo ====================================
echo  multi-agent-install skill installer
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
copy "%SCRIPT_DIR%SKILL.md" "%SKILL_DIR%\SKILL.md" >nul
copy "%SCRIPT_DIR%install-all.bat" "%SKILL_DIR%\install-all.bat" >nul
copy "%SCRIPT_DIR%install-all.sh" "%SKILL_DIR%\install-all.sh" >nul

echo [INFO] Installed to: %SKILL_DIR%
echo.
echo To install all AI agents, run:
echo   %SKILL_DIR%\install-all.bat
echo.
pause