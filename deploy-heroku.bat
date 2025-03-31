@echo off
cd /d %~dp0
git init
git add .
git commit -m "Deploy UI Colour Connect"
heroku git:remote -a hlc-colour-atlas-xl-app
git push heroku main --force
pause
