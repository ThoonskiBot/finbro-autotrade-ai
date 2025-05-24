@echo off
cd /d C:\FINBRO

REM === Send Weekly Reflection ===
py -3.11 tools\weekly_reflection_email.py
py -3.11 tools\weekly_reflection_telegram.py

exit
