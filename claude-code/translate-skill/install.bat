@echo off
REM install.bat — 把 translate skill 装到 ~/.claude/skills/
chcp 65001 >nul
setlocal

set SKILL_NAME=translate
set SKILL_DIR=%USERPROFILE%\.claude\skills\%SKILL_NAME%

if exist "%SKILL_DIR%" (
    echo skill 已存在,跳过: %SKILL_DIR%
    echo 如要重装,先删除 %SKILL_DIR%
) else (
    mkdir "%SKILL_DIR%"
    copy "%~dp0SKILL.md" "%SKILL_DIR%\SKILL.md" >nul
    copy "%~dp0translate.py" "%SKILL_DIR%\translate.py" >nul
    copy "%~dp0test_translate.py" "%SKILL_DIR%\test_translate.py" >nul
    echo √ 已装到: %SKILL_DIR%
)
echo.
echo 验证: py %SKILL_DIR%\test_translate.py
endlocal
pause
