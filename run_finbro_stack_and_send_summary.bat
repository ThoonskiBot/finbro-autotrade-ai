@echo off
cd /d C:\FINBRO
py -3.11 tools\ml_feature_generator.py
py -3.11 tools\train_model_sl.py
py -3.11 tools\evaluate_model_results.py
py -3.11 tools\model_live_swapper.py
py -3.11 finbro_runner.py
py -3.11 tools\gpt_summary_generator.py
py -3.11 tools\send_gpt_summary_email.py
py -3.11 tools\send_gpt_summary_telegram.py
