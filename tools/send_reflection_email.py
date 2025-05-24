
import os, smtplib
from email.message import EmailMessage
from datetime import datetime
from core.config import EMAIL_USER, EMAIL_PASS, EMAIL_RECEIVER, EMAIL_ENABLED, REPORTS_PATH

def send_gpt_reflection():
    if not EMAIL_ENABLED:
        print("❌ Email sending is disabled.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    path = os.path.join(REPORTS_PATH, f"gpt_reflection_{today}.txt")
    if not os.path.exists(path):
        print("❌ No GPT reflection file for today.")
        return

    msg = EmailMessage()
    msg["Subject"] = f"FINBRO GPT Reflection - {today}"
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_RECEIVER

    with open(path, "r", encoding="utf-8") as f:
        msg.set_content(f.read())

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
        print("✅ Reflection email sent.")
    except Exception as e:
        print(f"❌ Email error: {e}")

if __name__ == "__main__":
    send_gpt_reflection()
