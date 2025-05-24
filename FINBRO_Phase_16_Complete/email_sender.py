# FINBRO email sender using existing .env variable names (FAILSAFE_EMAIL_...)

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from pathlib import Path
from dotenv import load_dotenv

# --- Load environment variables from .env ---
load_dotenv()

sender_email = os.getenv("FAILSAFE_EMAIL_SENDER")
receiver_email = os.getenv("FAILSAFE_EMAIL_RECEIVER")
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = sender_email
smtp_password = os.getenv("FAILSAFE_EMAIL_PASSWORD")

# --- Create the Email ---
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "📊 FINBRO Daily Trade Report + Preview"

# --- Body ---
body_text = "Attached: your daily FINBRO trade summary and chart preview."
msg.attach(MIMEText(body_text, "plain"))

# --- Attach PDF ---
pdf_path = Path("reports/daily_trade_summary_chart_2025-05-21.pdf")
if pdf_path.exists():
    with open(pdf_path, "rb") as f:
        part = MIMEApplication(f.read(), _subtype="pdf")
        part.add_header("Content-Disposition", "attachment", filename=pdf_path.name)
        msg.attach(part)

# --- Attach Preview Image ---
jpg_path = Path("reports/previews/daily_trade_summary_chart_2025-05-21_preview.jpg")
if jpg_path.exists():
    with open(jpg_path, "rb") as f:
        image = MIMEImage(f.read())
        image.add_header("Content-Disposition", "attachment", filename=jpg_path.name)
        msg.attach(image)

# --- Send It ---
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        print("✅ Email sent successfully.")
except Exception as e:
    print(f"❌ Email failed: {e}")
