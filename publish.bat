@echo off

git add .

set /p message=输入上传消息:

git commit -m "%message%"

pause