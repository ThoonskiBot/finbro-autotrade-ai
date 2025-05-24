@echo off
cd /d C:\FINBRO
py tools\cloud_runner.py
py tools\remote_git_sync.py
py tools\dashboard_launcher.py