@echo off
cd /d C:\FINBRO
py tools\gpt_summary_generator.py
py tools\gpt_pnl_commentary.py
py tools\send_gpt_email.py
py tools\send_gpt_telegram.py
powershell Compress-Archive -Path reports\* -DestinationPath archive\gpt_summary_%date:~10,4%%date:~4,2%%date:~7,2%.zip -Force
echo ✅ 6PM GPT Summary Delivery Complete.