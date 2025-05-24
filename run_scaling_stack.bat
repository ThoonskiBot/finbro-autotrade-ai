@echo off
cd /d C:\FINBRO
py tools\multi_account_router.py
py tools\broker_mirroring_engine.py
py tools\strategy_cloner.py
py tools\alpha_api_exporter.py