@echo off
echo Running FINBRO Phase 22001–22100 Block...
py tools\phase_22001_rl_optimizer.py
py tools\phase_22002_signal_embedding.py
py tools\phase_22003_roi_time_profiler.py
py tools\phase_22004_alpha_attribution_map.py
py tools\phase_22005_retraining_orchestrator.py
py tools\phase_22006_bias_detector.py
py tools\phase_22007_trade_narrator.py
py tools\phase_22008_dashboard_replay.py
py tools\phase_22009_multi_market_router.py
py tools\phase_22010_alpha_memory_builder.py