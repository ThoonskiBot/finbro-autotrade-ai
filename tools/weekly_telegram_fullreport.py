import os
import requests
from dotenv import load_dotenv

load_dotenv("C:/FINBRO/.env")

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
REPORTS_DIR = "C:/FINBRO/reports"

journal = sorted([f for f in os.listdir(REPORTS_DIR) if f.startswith("gpt_weekly_reflection_")], reverse=True)
recap = sorted([f for f in os.listdir(REPORTS_DIR) if f.startswith("strategy_alpha_recap_")], reverse=True)

def send_file(filename, caption):
    path = os.path.join(REPORTS_DIR, filename)
    with open(path, 'rb') as f:
        response = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
            data={"chat_id": CHAT_ID, "caption": caption},
            files={"document": f}
        )
    return response.ok

if BOT_TOKEN and CHAT_ID:
    if journal:
        send_file(journal[0], f"📊 GPT Weekly Journal: {journal[0]}")
    if recap:
        send_file(recap[0], f"📈 Alpha Recap: {recap[0]}")
    print("✅ Journal + recap sent via Telegram.")
else:
    print("❌ Missing Telegram credentials.")
