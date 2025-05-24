@echo off
py tools\phase_25101_stress_test_engine.py
py tools\phase_25102_multi_model_tuner.py
py tools\phase_25201_drawdown_monitor.py
py tools\phase_25202_panic_stop.py
py tools\phase_25301_error_logger.py
py tools\phase_25302_gpt_error_explainer.py
py tools\phase_25401_shadow_engine.py