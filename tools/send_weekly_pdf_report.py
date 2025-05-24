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
pdfs = sorted([f for f in os.listdir(REPORTS_DIR) if f.startswith("FINBRO_Weekly_Report_") and f.endswith(".pdf")], reverse=True)

if not pdfs:
    print("❌ No weekly PDF report found.")
    exit()

latest_pdf = pdfs[0]
pdf_path = os.path.join(REPORTS_DIR, latest_pdf)

# === Email ===
if EMAIL_ADDRESS and EMAIL_PASSWORD and TO_EMAIL:
    try:
        msg = EmailMessage()
        msg['Subject'] = f"FINBRO Weekly PDF Report - {datetime.now().strftime('%Y-%m-%d')}"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = TO_EMAIL
        msg.set_content("Attached is this week's FINBRO intelligence report (PDF).")

        with open(pdf_path, 'rb') as f:
            msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=latest_pdf)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print(f"✅ PDF emailed to {TO_EMAIL}")
    except Exception as e:
        print(f"❌ Email failed: {e}")

# === Telegram ===
if BOT_TOKEN and CHAT_ID:
    try:
        with open(pdf_path, 'rb') as f:
            response = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
                data={"chat_id": CHAT_ID, "caption": f"FINBRO Weekly PDF Report: {latest_pdf}"},
                files={"document": f}
            )
        if response.status_code == 200:
            print("✅ PDF sent to Telegram.")
        else:
            print(f"❌ Telegram failed: {response.text}")
    except Exception as e:
        print(f"❌ Telegram error: {e}")
else:
    print("❌ Missing Telegram credentials.")
