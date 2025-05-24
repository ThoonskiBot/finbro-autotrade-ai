@echo off
echo Running FINBRO Stabilization Tools...
py tools\health_check_dashboard.py
py tools\signal_audit_logger.py
py tools\daily_run_logger.py
py tools\failsafe_recovery.py
py tools\gpt_audit_me.py
echo ✅ Stabilization tools executed.