@echo off
cd /d C:\FINBRO
py -3.11 finbro_runner.py

cd tools
py -3.11 send_daily_email_report.py
