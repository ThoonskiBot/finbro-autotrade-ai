import os
import smtplib
import requests
from datetime import datetime
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv("C:/FINBRO/.env")

EMAIL_ADDRESS = os.getenv("FAILSAFE_EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("FAILSAFE_EMAIL_PASSWORD")
TO_EMAIL = os.getenv("FAILSAFE_EMAIL_RECEIVER")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

REPORTS_DIR = "C:/FINBRO/reports"
coach_files = sorted([f for f in os.listdir(REPORTS_DIR) if f.startswith("gpt_coach_feedback_") and f.endswith(".txt")], reverse=True)

if not coach_files:
    print("❌ No GPT Coach feedback file found.")
    exit()

latest_coach_file = coach_files[0]
file_path = os.path.join(REPORTS_DIR, latest_coach_file)

# === Email ===
if EMAIL_ADDRESS and EMAIL_PASSWORD and TO_EMAIL:
    try:
        msg = EmailMessage()
        msg['Subject'] = f"FINBRO GPT Strategy Coach Feedback - {datetime.now().strftime('%Y-%m-%d')}"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = TO_EMAIL
        msg.set_content("Attached is this week's GPT strategy coaching feedback.")

        with open(file_path, 'rb') as f:
            msg.add_attachment(f.read(), maintype='text', subtype='plain', filename=latest_coach_file)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print(f"✅ Coach feedback emailed to {TO_EMAIL}")
    except Exception as e:
        print(f"❌ Email failed: {e}")

# === Telegram ===
if BOT_TOKEN and CHAT_ID:
    try:
        with open(file_path, 'rb') as f:
            response = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
                data={"chat_id": CHAT_ID, "caption": f"GPT Coach Feedback: {latest_coach_file}"},
                files={"document": f}
            )
        if response.status_code == 200:
            print("✅ Coach feedback sent to Telegram.")
        else:
            print(f"❌ Telegram failed: {response.text}")
    except Exception as e:
        print(f"❌ Telegram error: {e}")
else:
    print("❌ Missing Telegram credentials.")
