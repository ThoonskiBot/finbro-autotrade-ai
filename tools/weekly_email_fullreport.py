import os
import smtplib
from datetime import datetime
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv("C:/FINBRO/.env")

EMAIL_ADDRESS = os.getenv("FAILSAFE_EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("FAILSAFE_EMAIL_PASSWORD")
TO_EMAIL = os.getenv("FAILSAFE_EMAIL_RECEIVER")

REPORTS_DIR = "C:/FINBRO/reports"
journal = sorted([f for f in os.listdir(REPORTS_DIR) if f.startswith("gpt_weekly_reflection_")], reverse=True)
recap = sorted([f for f in os.listdir(REPORTS_DIR) if f.startswith("strategy_alpha_recap_")], reverse=True)

msg = EmailMessage()
msg['Subject'] = f"FINBRO Weekly Report - {datetime.now().strftime('%Y-%m-%d')}"
msg['From'] = EMAIL_ADDRESS
msg['To'] = TO_EMAIL
msg.set_content("Attached are this week's GPT journal and alpha recap.")

if journal:
    with open(os.path.join(REPORTS_DIR, journal[0]), 'rb') as f:
        msg.add_attachment(f.read(), maintype='text', subtype='plain', filename=journal[0])

if recap:
    with open(os.path.join(REPORTS_DIR, recap[0]), 'rb') as f:
        msg.add_attachment(f.read(), maintype='text', subtype='csv', filename=recap[0])

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("✅ Weekly journal + alpha recap emailed.")
