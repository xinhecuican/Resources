
git add .

@echo off

set /p message=输入上传消息:

@echo on

git commit -m "%message%"

git push origin master

@echo off

pause