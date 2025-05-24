@echo off
py tools\signal_router.py
py tools\strategy_fallback_logic.py
py tools\live_error_catch.py
py tools\drawdown_guard.py
py tools\trade_failsafe_loop.py
py tools\confidence_scorer.py
