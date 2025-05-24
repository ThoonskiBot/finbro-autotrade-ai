import os
import smtplib
from email.message import EmailMessage
from core.config import PDF_REPORT_PATH, EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

def send_pdf_email():
    msg = EmailMessage()
    msg['Subject'] = '📊 FINBRO Daily Trade Summary'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg.set_content("Attached is your daily FINBRO trade summary.")

    try:
        with open(PDF_REPORT_PATH, 'rb') as f:
            msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename='daily_trade_summary.pdf')
    except Exception as e:
        print(f"❌ Failed to attach PDF: {e}")
        return

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("📧 PDF email sent successfully.")
    except Exception as e:
        print(f"❌ Email send failed: {e}")
