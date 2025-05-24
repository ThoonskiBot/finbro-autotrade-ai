@echo off
py tools\order_clustering_manager.py
py tools\smart_exit_refiner.py
py tools\trade_retry_manager.py