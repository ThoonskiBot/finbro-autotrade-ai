import os
import smtplib
from email.message import EmailMessage

def send_trade_summary(log_path):
    sender = os.getenv("FAILSAFE_EMAIL_SENDER")
    password = os.getenv("FAILSAFE_EMAIL_PASSWORD")
    receiver = os.getenv("FAILSAFE_EMAIL_RECEIVER")

    print("📬 FAILSAFE_EMAIL_SENDER:", sender)
    print("📬 FAILSAFE_EMAIL_RECEIVER:", receiver)
    print("🔑 FAILSAFE_EMAIL_PASSWORD (first 4 chars):", password[:4] if password else "None")

    msg = EmailMessage()
    msg['Subject'] = '📊 FINBRO Daily Trade Summary'
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content("FINBRO completed its daily run. Logs and signals have been updated.")

    try:
        signals = sorted([f for f in os.listdir('signals') if f.endswith('.csv')], key=lambda x: os.path.getctime(f'signals/{x}'), reverse=True)
        if signals:
            with open(f'signals/{signals[0]}', 'rb') as f:
                msg.add_attachment(f.read(), maintype='text', subtype='csv', filename=signals[0])
    except Exception as e:
        print(f"⚠️ Could not attach signals: {e}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
            print("📧 Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
