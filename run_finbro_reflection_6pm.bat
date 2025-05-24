
@echo off
cd /d C:\FINBRO

echo 🧠 Generating GPT Reflection...
py -3.11 tools\gpt_reflection_log.py

echo 📬 Sending Reflection Email...
py -3.11 tools\send_reflection_email.py

echo 📲 Sending Reflection to Telegram...
py -3.11 tools\send_gpt_to_telegram.py

echo ✅ FINBRO Reflection Report Dispatched.
pause
