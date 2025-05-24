
import os
from dotenv import load_dotenv
import smtplib
import requests

load_dotenv(dotenv_path="C:/FINBRO/.env")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

EMAIL_USER = os.getenv("FAILSAFE_EMAIL_SENDER")
EMAIL_PASS = os.getenv("FAILSAFE_EMAIL_PASSWORD")
EMAIL_TO = os.getenv("FAILSAFE_EMAIL_RECEIVER")
EMAIL_ENABLED = os.getenv("FINBRO_EMAIL_ENABLED", "false").lower() == "true"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587

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

def get_latest_gpt_summary():
    try:
        report_dir = "C:/FINBRO/reports"
        summaries = sorted(
            [f for f in os.listdir(report_dir) if f.startswith("gpt_trade_summary_") and f.endswith(".txt")],
            reverse=True
        )
        if summaries:
            with open(os.path.join(report_dir, summaries[0]), "r") as f:
                return f.read()
    except Exception as e:
        print("Summary load error:", e)
    return None

def run_summary_alert():
    summary = get_latest_gpt_summary()
    if summary:
        send_telegram_alert(f"🧠 FINBRO GPT Summary:\n{summary[:400]}...")
        send_email_alert("🧠 FINBRO Daily GPT Summary", summary)
    else:
        print("No GPT summary found.")

if __name__ == "__main__":
    run_summary_alert()
