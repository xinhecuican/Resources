
git add .

@echo off

set /p message=enter commit message:

@echo on

git commit -m "%message%"

git push origin master

@echo off

pause