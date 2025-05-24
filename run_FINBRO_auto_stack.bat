
@echo off
cd /d C:\FINBRO

echo 🔁 Starting FINBRO Full Auto Run...
py -3.11 finbro_runner.py

echo 🧠 Generating GPT Summary...
py -3.11 tools\gpt_summary_generator.py

echo 📬 Sending Email Report...
py -3.11 tools\send_gpt_email_report.py

echo 📲 Sending Telegram Report...
py -3.11 tools\send_gpt_to_telegram.py

echo ✅ FINBRO Full Auto Run Complete.
