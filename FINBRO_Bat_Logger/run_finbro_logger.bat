@echo off
set LOGFILE=C:\FINBRO\logs\finbro_output_%date:~10,4%-%date:~4,2%-%date:~7,2%_%time:~0,2%%time:~3,2%.txt
cd /d C:\FINBRO\FINBRO_Phase_16_Complete
python finbro_runner.py > %LOGFILE% 2>&1
