@echo off
REM install.bat - OpenClaw deploy for Windows
REM Note: Windows doesn't have systemd, this is a simpler setup

echo ====================================
echo  OpenClaw Deploy v1.0 (Windows)
echo ====================================
echo.

where node >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js not found. Install from https://nodejs.org/
    pause
    exit /b 1
)

echo Installing OpenClaw...
call npm install -g @openclaw/cli
if errorlevel 1 (
    echo [FAIL] OpenClaw install failed
    pause
    exit /b 1
)

echo Creating config directory...
if not exist "%USERPROFILE%\.openclaw" mkdir "%USERPROFILE%\.openclaw"

echo Generating config...
(
    echo server:
    echo   port: 3000
    echo   host: 127.0.0.1
    echo auth:
    echo   jwt_secret: REPLACE_ME
    echo proxy:
    echo   api_base: https://api.skillai.top
    echo   api_key: REPLACE_ME
) > "%USERPROFILE%\.openclaw\config.yaml"

echo.
echo [OK] Installed!
echo.
echo Start OpenClaw:
echo   openclaw serve
echo.
echo Then open: http://localhost:3000
echo.
pause