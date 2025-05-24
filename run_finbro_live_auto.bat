@echo off
cd /d C:\FINBRO
SETLOCAL

SET LIVE_MODE=1
SET SIGNAL_DIR=C:\FINBRO\signals
SET SIGNAL_FILE=%SIGNAL_DIR%\signals_%DATE:~10,4%%DATE:~4,2%%DATE:~7,2%.csv

IF NOT EXIST %SIGNAL_FILE% (
  echo ? No signal file found for today: %SIGNAL_FILE%
  EXIT /B
)

py tools\ml_feature_generator.py
py tools\train_model_sl.py
py tools\evaluate_model_results.py
py tools\model_live_swapper.py

py finbro_runner.py
py tools\gpt_summary_generator.py
py tools\gpt_pnl_commentary.py
py tools\gpt_risk_reviewer.py
py tools\strategy_roi_chart.py
py tools\log_delta_comparator.py
py tools\multi_strategy_router.py
py tools\economic_filter.py
py tools\event_voice_alert.py

echo ? FINBRO Full Intelligence Stack Complete
ENDLOCAL
