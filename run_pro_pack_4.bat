@echo off
echo Running Pro Pack 4...
py tools\gpt_strategy_namer.py
py tools\telegram_trade_flow.py
py tools\trade_anomaly_explainer.py
py tools\multi_strategy_router.py
py tools\strategy_context_builder.py