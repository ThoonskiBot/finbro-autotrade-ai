import os
import requests
from dotenv import load_dotenv

load_dotenv("C:/FINBRO/.env")

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
REPORTS_DIR = "C:/FINBRO/reports"

files = sorted([f for f in os.listdir(REPORTS_DIR) if f.startswith("gpt_weekly_reflection_")], reverse=True)
if not BOT_TOKEN or not CHAT_ID:
    print("❌ Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID")
    exit()

if not files:
    print("❌ No weekly reflection found.")
    exit()

latest_file = files[0]
file_path = os.path.join(REPORTS_DIR, latest_file)

with open(file_path, 'rb') as f:
    response = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
        data={"chat_id": CHAT_ID, "caption": f"📊 FINBRO Weekly Reflection: {latest_file}"},
        files={"document": f}
    )

if response.status_code == 200:
    print(f"✅ Weekly reflection sent to Telegram: {latest_file}")
else:
    print(f"❌ Telegram send failed: {response.text}")
