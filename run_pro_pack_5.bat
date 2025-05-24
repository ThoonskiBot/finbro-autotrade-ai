@echo off
echo Running Pro Pack 5...
py tools\eod_gpt_journal.py
py tools\strategy_roi_profiler.py
py tools\gpt_weekly_playbook.py
py tools\alert_sound_engine.py
py tools\signal_archiver.py