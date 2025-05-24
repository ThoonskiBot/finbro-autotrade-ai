
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import smtplib
from email.message import EmailMessage
from datetime import datetime
from core.config import (
    EMAIL_USER, EMAIL_PASS, EMAIL_RECEIVER, EMAIL_ENABLED,
    REPORTS_PATH
)

def send_daily_report():
    if not EMAIL_ENABLED:
        print("❌ Email sending is disabled in .env")
        return

    today_str = datetime.now().strftime("%Y-%m-%d")
    subject = f"FINBRO Daily Report - {today_str}"

    # Find latest GPT summary
    summary_path = None
    for file in os.listdir(REPORTS_PATH):
        if file.startswith("gpt_trade_summary_") and today_str in file:
            summary_path = os.path.join(REPORTS_PATH, file)
            break

    if not summary_path:
        print("❌ GPT summary not found.")
        return

    # Find matching chart
    chart_path = os.path.join(REPORTS_PATH, f"daily_trade_summary_chart_{today_str.replace('-', '')}.pdf")
    if not os.path.exists(chart_path):
        chart_path = None

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_RECEIVER

    with open(summary_path, "r", encoding="utf-8") as f:
        msg.set_content(f.read())

    if chart_path:
        with open(chart_path, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=os.path.basename(chart_path))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
        print("✅ Email report sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    send_daily_report()
