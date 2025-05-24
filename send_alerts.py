
import os
import smtplib
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="C:/FINBRO/.env")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

EMAIL_USER = os.getenv("FAILSAFE_EMAIL_SENDER")
EMAIL_PASS = os.getenv("FAILSAFE_EMAIL_PASSWORD")
EMAIL_TO = os.getenv("FAILSAFE_EMAIL_RECEIVER")
EMAIL_ENABLED = os.getenv("FINBRO_EMAIL_ENABLED", "false").lower() == "true"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587

def read_pnl_threshold(log_file="C:/FINBRO/logs/order_log_test_2025-05-26.txt"):
    pnl = 0
    try:
        with open(log_file, "r") as f:
            for line in f:
                if "win" in line:
                    pnl += 100
                elif "loss" in line:
                    pnl -= 100
    except Exception as e:
        print("Error reading log:", e)
    return pnl

def send_telegram_alert(msg):
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        try:
            requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", data={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": msg
            })
        except Exception as e:
            print("Telegram error:", e)

def send_email_alert(subject, msg):
    if EMAIL_ENABLED and EMAIL_USER and EMAIL_PASS and EMAIL_TO:
        try:
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.starttls()
                server.login(EMAIL_USER, EMAIL_PASS)
                message = f"Subject: {subject}\n\n{msg}"
                server.sendmail(EMAIL_USER, EMAIL_TO, message)
        except Exception as e:
            print("Email error:", e)

def run_alerts():
    pnl = read_pnl_threshold()
    print(f"Current PnL: ${pnl}")
    if pnl >= 1000:
        message = f"🚀 FINBRO ALERT: Daily PnL hit ${pnl}!"
        send_telegram_alert(message)
        send_email_alert("FINBRO PnL Alert", message)

if __name__ == "__main__":
    run_alerts()
