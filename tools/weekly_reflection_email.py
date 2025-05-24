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
files = sorted([f for f in os.listdir(REPORTS_DIR) if f.startswith("gpt_weekly_reflection_")], reverse=True)
if not files:
    print("❌ No weekly reflection found.")
    exit()

latest_file = files[0]
report_path = os.path.join(REPORTS_DIR, latest_file)

msg = EmailMessage()
msg['Subject'] = f"FINBRO Weekly GPT Reflection - {datetime.now().strftime('%Y-%m-%d')}"
msg['From'] = EMAIL_ADDRESS
msg['To'] = TO_EMAIL
msg.set_content("Attached is your weekly GPT-generated market reflection.")

with open(report_path, 'rb') as f:
    msg.add_attachment(f.read(), maintype='text', subtype='plain', filename=latest_file)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print(f"✅ Weekly GPT reflection emailed: {latest_file}")
