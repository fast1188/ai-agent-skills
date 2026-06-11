@echo off
REM install.bat - Install recommended VSCode AI extensions

echo ====================================
echo  vscode-extension-pack installer
echo ====================================
echo.

REM Check VSCode is installed
where code >nul 2>&1
if errorlevel 1 (
    echo [ERROR] VSCode not found in PATH.
    echo        Open VSCode, press Ctrl+Shift+P, type "shell command", run "Install 'code' command in PATH"
    pause
    exit /b 1
)

echo Installing AI extensions...
echo.

set EXTENSIONS=(
    "cline.cline"
    "Continue.continue"
    "GitHub.copilot"
    "Codeium.codeium"
    "Anthropic.claude-code"
)

for %%e in (%EXTENSIONS%) do (
    echo [INSTALL] %%e
    call code --install-extension %%e
)

echo.
echo Done! Reload VSCode to activate.
pause