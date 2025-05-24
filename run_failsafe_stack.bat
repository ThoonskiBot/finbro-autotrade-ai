@echo off
cd /d C:\FINBRO
py tools\loss_streak_auto_pause.py
py tools\reversal_pattern_detector.py
py tools\trade_confidence_heatmap.py
py tools\gpt_anomaly_narrator.py
py tools\max_drawdown_lock.py
