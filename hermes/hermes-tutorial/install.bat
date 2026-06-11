@echo off
REM install.bat - Install hermes-tutorial skill

set SKILL_DIR=%USERPROFILE%\.hermes\skills\hermes-tutorial
set SCRIPT_DIR=%~dp0

echo ====================================
echo  hermes-tutorial skill installer
echo ====================================
echo.

REM Check Python
py --version >nul 2>&1
if errorlevel 1 (
    echo [WARN] Python not found. Hermes needs Python 3.10+
    echo        Install from https://www.python.org/
)

if not exist "%USERPROFILE%\.hermes\skills" (
    echo [INFO] Creating ~/.hermes/skills directory...
    mkdir "%USERPROFILE%\.hermes\skills"
)

if exist "%SKILL_DIR%" (
    echo [INFO] Updating existing installation...
    rmdir /s /q "%SKILL_DIR%"
)

mkdir "%SKILL_DIR%"
copy "%SCRIPT_DIR%SKILL.md" "%SKILL_DIR%\SKILL.md" >nul
copy "%SCRIPT_DIR%config.toml" "%SKILL_DIR%\config.toml" >nul

REM Try to install hermes-agent
echo Installing hermes-agent...
py -m pip install hermes-agent -i https://pypi.tuna.tsinghua.edu.cn/simple
if errorlevel 1 (
    echo [WARN] hermes-agent install failed. Install manually with: pip install hermes-agent
)

echo.
echo ====================================
echo  Installed!
echo ====================================
echo.
echo Try:
echo   py -m hermes init
echo   py -m hermes chat
echo.
pause