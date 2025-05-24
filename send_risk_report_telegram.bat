@echo off
REM Send FINBRO GPT Risk Report via Telegram
cd /d C:\FINBRO
py -3.11 tools\telegram_send_risk_report.py
exit
