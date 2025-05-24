@echo off
echo Running Pro Pack 3...
py tools\pnl_heatmap_generator.py
py tools\cloud_sync_backup.py
py tools\gpt_reflection_logger_v2.py
py tools\dashboard_login_patch.py