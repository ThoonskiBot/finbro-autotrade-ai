@echo off
REM Activate FINBRO GPT Risk Review @ 6PM
cd /d C:\FINBRO
py -3.11 tools\gpt_risk_reviewer.py
exit
