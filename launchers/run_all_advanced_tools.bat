@echo off
py tools\anomaly_detector.py
py tools\execution_review_gpt.py
py tools\alpha_attribution_engine.py
py tools\auto_zip_purge.py
py tools\gpt_trade_context_generator.py