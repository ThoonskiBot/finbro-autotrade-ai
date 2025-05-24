import os
import glob
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import requests

# === Load FINBRO .env ===
load_dotenv(dotenv_path="C:/FINBRO/.env")

# === Email Settings ===
EMAIL_ENABLED = os.getenv("FINBRO_EMAIL_ENABLED", "false").lower() == "true"
EMAIL_SENDER = os.getenv("FAILSAFE_EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("FAILSAFE_EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("FAILSAFE_EMAIL_RECEIVER")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))

# === Telegram Settings ===
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# === Paths ===
REFLECTION_PATH = os.getenv("REFLECTION_PATH", "reports")
summary_files = glob.glob(f"{REFLECTION_PATH}/gpt_trade_summary_*.txt")
latest_file = max(summary_files, key=os.path.getctime) if summary_files else None

if not latest_file:
    print("❌ No GPT summary file found.")
    exit(1)

with open(latest_file, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"📨 Preparing to send GPT summary from: {latest_file}")

# === Send Email ===
if EMAIL_ENABLED and EMAIL_SENDER and EMAIL_PASSWORD and EMAIL_RECEIVER:
    try:
        msg = MIMEText(content, "plain", "utf-8")
        msg["Subject"] = f"GPT Trade Summary – {os.path.basename(latest_file)}"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("📧 Email sent.")
    except Exception as e:
        print(f"❌ Email failed: {e}")

# === Send Telegram ===
if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": content[:4096]
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("📲 Telegram message sent.")
        else:
            print(f"❌ Telegram failed: {response.text}")
    except Exception as e:
        print(f"❌ Telegram error: {e}")
