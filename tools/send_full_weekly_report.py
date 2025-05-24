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
files_to_send = []

# Pull latest files
for prefix in [
    "gpt_weekly_reflection_",
    "strategy_alpha_recap_",
    "strategy_score_tracker_",
    "strategy_heatmap_",
    "FINBRO_Weekly_Report_"
]:
    matches = sorted([f for f in os.listdir(REPORTS_DIR) if f.startswith(prefix)], reverse=True)
    if matches:
        files_to_send.append(matches[0])

# Email setup
if EMAIL_ADDRESS and EMAIL_PASSWORD and TO_EMAIL:
    try:
        msg = EmailMessage()
        msg['Subject'] = f"FINBRO Full Weekly Report - {datetime.now().strftime('%Y-%m-%d')}"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = TO_EMAIL
        msg.set_content("Attached are all key weekly FINBRO files.")

        for filename in files_to_send:
            full_path = os.path.join(REPORTS_DIR, filename)
            maintype = 'application'
            subtype = 'octet-stream'
            if filename.endswith(".txt"):
                maintype, subtype = "text", "plain"
            elif filename.endswith(".csv"):
                maintype, subtype = "text", "csv"
            elif filename.endswith(".pdf"):
                maintype, subtype = "application", "pdf"
            elif filename.endswith(".png"):
                maintype, subtype = "image", "png"
            with open(full_path, "rb") as f:
                msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=filename)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print(f"✅ Full report emailed to {TO_EMAIL}")
    except Exception as e:
        print(f"❌ Email failed: {e}")
else:
    print("❌ Email settings incomplete.")

# Telegram delivery
if BOT_TOKEN and CHAT_ID:
    for filename in files_to_send:
        path = os.path.join(REPORTS_DIR, filename)
        with open(path, 'rb') as f:
            try:
                resp = requests.post(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
                    data={"chat_id": CHAT_ID, "caption": f"{filename}"},
                    files={"document": f}
                )
                if resp.status_code == 200:
                    print(f"✅ {filename} sent to Telegram.")
                else:
                    print(f"❌ Telegram send failed for {filename}: {resp.text}")
            except Exception as e:
                print(f"❌ Telegram error on {filename}: {e}")
else:
    print("❌ Telegram settings incomplete.")
