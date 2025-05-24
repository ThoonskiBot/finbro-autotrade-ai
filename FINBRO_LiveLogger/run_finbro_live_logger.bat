@echo off
setlocal EnableDelayedExpansion

:: Create log folder if it doesn't exist
if not exist C:\FINBRO\logs mkdir C:\FINBRO\logs

:: Generate timestamp
for /f %%A in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd_HHmm"') do set timestamp=%%A

:: Define log path
set LOGFILE=C:\FINBRO\logs\finbro_output_!timestamp!.txt

:: Run and live log
cd /d C:\FINBRO\FINBRO_Phase_16_Complete
python finbro_runner.py | tee %LOGFILE%
pause
