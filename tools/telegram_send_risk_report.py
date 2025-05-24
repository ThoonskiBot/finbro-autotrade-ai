import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="C:/FINBRO/.env")

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
REPORTS_DIR = "C:/FINBRO/reports"

if not BOT_TOKEN or not CHAT_ID:
    print("❌ Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID in .env")
    exit(1)

# Find latest report file
files = sorted([f for f in os.listdir(REPORTS_DIR) if f.startswith("gpt_risk_review_")], reverse=True)
if not files:
    print("❌ No risk review files found.")
    exit(1)

latest_file = files[0]
file_path = os.path.join(REPORTS_DIR, latest_file)

# Send document
with open(file_path, 'rb') as f:
    response = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
        data={"chat_id": CHAT_ID, "caption": f"📊 FINBRO GPT Risk Report: {latest_file}"},
        files={"document": f}
    )

if response.status_code == 200:
    print(f"✅ Report sent to Telegram: {latest_file}")
else:
    print(f"❌ Failed to send: {response.text}")
