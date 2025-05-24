
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import smtplib
from email.message import EmailMessage
from datetime import datetime
from core.config import EMAIL_USER, EMAIL_PASS, EMAIL_RECEIVER, EMAIL_ENABLED, REPORTS_PATH

def send_gpt_email_report():
    if not EMAIL_ENABLED:
        print("❌ Email sending is disabled.")
        return

    today_str = datetime.now().strftime("%Y-%m-%d")
    raw_date = datetime.now().strftime("%Y%m%d")

    msg = EmailMessage()
    msg["Subject"] = f"FINBRO Daily GPT Summary - {today_str}"
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_RECEIVER

    gpt_path = None
    for file in os.listdir(REPORTS_PATH):
        if file.startswith("gpt_trade_summary_") and today_str in file:
            gpt_path = os.path.join(REPORTS_PATH, file)
            break

    chart_path = os.path.join(REPORTS_PATH, f"daily_trade_summary_chart_{raw_date}.pdf")

    if gpt_path:
        with open(gpt_path, "r", encoding="utf-8") as f:
            msg.set_content(f.read())

    if os.path.exists(chart_path):
        with open(chart_path, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=os.path.basename(chart_path))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
        print("✅ Email with GPT summary and chart sent.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    send_gpt_email_report()
