@echo off
REM === FINBRO 6PM FULL CHAIN + LOGGER + JOURNAL ===
cd /d C:\FINBRO

REM Step 1: Generate GPT Risk Review
py -3.11 tools\gpt_risk_reviewer.py

REM Step 2: Send Email Report
py -3.11 tools\email_gpt_risk_report.py

REM Step 3: Send Telegram Report
py -3.11 tools\telegram_send_risk_report.py

REM Step 4: Write to chain log
py -3.11 tools\chain_logger.py

REM Step 5: Generate GPT market journal entry
py -3.11 tools\gpt_journal_writer.py

exit
