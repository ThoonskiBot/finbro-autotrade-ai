
import os
import requests
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv("C:/FINBRO/.env")

# Paths
summary_path = "C:/FINBRO/reports/gpt_summary.txt"
pnl_path = "C:/FINBRO/reports/gpt_pnl_summary.txt"

# Load content
with open(summary_path, "r", encoding="utf-8") as f:
    trade_summary = f.read()
with open(pnl_path, "r", encoding="utf-8") as f:
    pnl_summary = f.read()

full_message = f"🧠 FINBRO Daily Report\n\nGPT Trade Summary:\n{trade_summary}\n\nPnL Summary:\n{pnl_summary}"

# Telegram
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")
if bot_token and chat_id:
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": full_message})

# Email
sender = os.getenv("FAILSAFE_EMAIL_SENDER")
password = os.getenv("FAILSAFE_EMAIL_PASSWORD")
receiver = os.getenv("FAILSAFE_EMAIL_RECEIVER")
if sender and password and receiver:
    msg = MIMEText(full_message)
    msg["Subject"] = "🧠 FINBRO Daily Summary"
    msg["From"] = sender
    msg["To"] = receiver
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

print("✅ GPT summary sent to Telegram + Email.")
