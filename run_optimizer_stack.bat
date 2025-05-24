@echo off
cd /d C:\FINBRO
py tools\signal_roi_tracker.py
py tools\strategy_reweighting_engine.py
py tools\alpha_redistribution.py
py tools\gpt_profit_estimator.py