@echo off
cd /d C:\FINBRO
py tools\model_selector.py
streamlit run tools\dashboard_ui.py