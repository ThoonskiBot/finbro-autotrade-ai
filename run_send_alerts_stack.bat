@echo off
py -3.11 tools\gpt_stack_commentary_generator.py
py -3.11 tools\send_telegram_stack_summary.py
