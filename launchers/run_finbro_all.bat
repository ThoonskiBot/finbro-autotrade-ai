
@echo off
set PYTHON_EXE=C:\Users\Matthew\AppData\Local\Programs\Python\Python311\python.exe

echo 🔁 FINBRO: Starting stack with strategy toggle routing...

%PYTHON_EXE% -c "import tools.strategy_toggle_router as r; exit(0) if not r.should_run('StrategyAlpha') else None" && %PYTHON_EXE% tools\signal_fusion_engine.py
%PYTHON_EXE% -c "import tools.strategy_toggle_router as r; exit(0) if not r.should_run('StrategyBeta') else None" && %PYTHON_EXE% tools\strategy_blender_engine.py

%PYTHON_EXE% tools\gpt_strategy_console.py
%PYTHON_EXE% tools\strategy_fatigue_monitor.py
%PYTHON_EXE% tools\multi_objective_optimizer.py
%PYTHON_EXE% tools\voice_alert_system.py

echo ✅ FINBRO stack completed.
pause
