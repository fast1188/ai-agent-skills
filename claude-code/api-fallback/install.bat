@echo off
REM install.bat - Install api-fallback skill for Claude Code

set SKILL_DIR=%USERPROFILE%\.claude\skills\api-fallback
set SCRIPT_DIR=%~dp0

echo ====================================
echo  api-fallback skill installer
echo ====================================
echo.

REM Check Python
py --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Install from https://www.python.org/
    pause
    exit /b 1
)

REM Create skills dir
if not exist "%USERPROFILE%\.claude\skills" (
    mkdir "%USERPROFILE%\.claude\skills"
)

REM Remove old version
if exist "%SKILL_DIR%" (
    echo [INFO] Updating existing installation...
    rmdir /s /q "%SKILL_DIR%"
)

mkdir "%SKILL_DIR%"
copy "%SCRIPT_DIR%SKILL.md" "%SKILL_DIR%\SKILL.md" >nul
copy "%SCRIPT_DIR%monitor.py" "%SKILL_DIR%\monitor.py" >nul
copy "%SCRIPT_DIR%requirements.txt" "%SKILL_DIR%\requirements.txt" >nul

REM Install Python deps
echo Installing Python dependencies...
py -m pip install -r "%SKILL_DIR%\requirements.txt" -i https://pypi.tuna.tsinghua.edu.cn/simple
if errorlevel 1 (
    echo [WARN] Some deps failed to install. Monitor may not work fully.
)

REM Create start script
echo @echo off > "%SKILL_DIR%\start.bat"
echo py "%SKILL_DIR%\monitor.py" >> "%SKILL_DIR%\start.bat"

REM Create desktop shortcut
echo Creating desktop shortcut...
powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%USERPROFILE%\Desktop\Claude API Fallback Monitor.lnk'); $s.TargetPath = '%SKILL_DIR%\start.bat'; $s.WorkingDirectory = '%SKILL_DIR%'; $s.Save()"

echo.
echo ====================================
echo  Installed!
echo ====================================
echo.
echo Skill location: %SKILL_DIR%
echo Start menu:     Desktop - "Claude API Fallback Monitor"
echo.
echo Next:
echo   1. Configure: edit %SKILL_DIR%\config.json
echo   2. Add api.skillai.top API key
echo   3. Double-click desktop shortcut to start
echo   4. Keep running while using Claude Code
echo.
pause