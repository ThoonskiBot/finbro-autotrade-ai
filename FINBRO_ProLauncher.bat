@echo off
echo ===============================
echo     FINBRO PRO LAUNCHER
echo ===============================
echo [1] Run GPT Weekly Journal
echo [2] Run Alpha Recap
echo [3] Run Strategy Tracker
echo [4] Run Heatmap Generator
echo [5] Build Weekly PDF
echo [6] Send Full Weekly Report (Email + Telegram)
echo [7] Run GPT Strategy Coach
echo [8] GPT Drift Summary
echo [9] GPT Key Check
echo [10] Zip Full Backup
echo [11] System Health Check
echo [0] Exit
echo.

set /p choice="Select task: "

if "%choice%"=="1" py -3.11 tools\gpt_weekly_reflector.py
if "%choice%"=="2" py -3.11 tools\strategy_alpha_recap.py
if "%choice%"=="3" py -3.11 tools\strategy_score_tracker.py
if "%choice%"=="4" py -3.11 tools\strategy_heatmap_generator.py
if "%choice%"=="5" py -3.11 tools\generate_weekly_pdf_report.py
if "%choice%"=="6" py -3.11 tools\send_full_weekly_report.py
if "%choice%"=="7" py -3.11 tools\gpt_strategy_coach.py
if "%choice%"=="8" py -3.11 tools\gpt_drift_summary.py
if "%choice%"=="9" py -3.11 tools\verify_gpt_key_from_env.py
if "%choice%"=="10" PowerShell -ExecutionPolicy Bypass -File "C:\Users\Matthew\Downloads\FINBRO_System_Backup_Kit\zip_finbro_backup.ps1"
if "%choice%"=="11" py -3.11 tools\finbro_system_check.py
if "%choice%"=="0" exit

pause
