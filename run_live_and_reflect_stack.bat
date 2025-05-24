@echo off
cd /d C:\FINBRO
call run_signal_fusion_stack.bat
call run_model_inferencer_stack.bat
call run_strategy_selector_stack.bat
call run_live_trade_executor_stack.bat
call run_post_trade_summary_stack.bat
call run_trade_explainer.bat
call run_pnl_heatmap.bat
call run_cloud_backup.bat
