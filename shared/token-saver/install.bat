@echo off
REM install.bat - Install token-saver skill

set SKILL_DIR=%USERPROFILE%\.claude\skills\token-saver
set SCRIPT_DIR=%~dp0

echo ====================================
echo  token-saver skill installer
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
copy "%SCRIPT_DIR%compress.py" "%SKILL_DIR%\compress.py" >nul
copy "%SCRIPT_DIR%requirements.txt" "%SKILL_DIR%\requirements.txt" >nul

echo [INFO] Installed to: %SKILL_DIR%
echo.
echo Test:
echo   py "%SKILL_DIR%\compress.py" "请你帮我编写一个 Python 函数,这个函数的作用是接收一个列表作为输入参数,然后计算并返回这个列表中所有数字元素的总和。"
echo.
pause