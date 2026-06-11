@echo off
REM install.bat - Install chinese-dev-helper skill

set SKILL_DIR=%USERPROFILE%\.claude\skills\chinese-dev-helper
set SCRIPT_DIR=%~dp0

echo ====================================
echo  chinese-dev-helper skill installer
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
copy "%SCRIPT_DIR%helper.py" "%SKILL_DIR%\helper.py" >nul

echo [INFO] Installed to: %SKILL_DIR%
echo.
echo Test:
echo   py "%SKILL_DIR%\helper.py" "帮我部署到 k8s 集群"
echo.
pause