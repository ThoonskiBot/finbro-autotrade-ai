@echo off
py -3.11 tools\gpt_trade_explainer.py
py -3.11 tools\pnl_heatmap_generator.py
py -3.11 tools\send_explainer_to_telegram.py
