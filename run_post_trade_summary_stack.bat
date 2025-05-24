@echo off
py -3.11 tools\gpt_stack_commentary_generator.py
py -3.11 tools\gpt_risk_reviewer.py
py -3.11 tools\strategy_roi_tracker.py
py -3.11 tools\generate_daily_pnl_chart.py
py -3.11 tools\log_delta_analyzer.py
py -3.11 tools\send_telegram_stack_summary.py
