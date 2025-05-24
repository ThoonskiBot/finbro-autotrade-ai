@echo off
echo Running full Pro Utility Stack...
py tools\replay_simulator.py
py tools\signal_reweighting_engine.py
py tools\signal_purity_filter.py
py tools\gpt_drift_monitor.py
py tools\dashboard_toggle_patch.py
py tools\gpt_voice_narrator.py