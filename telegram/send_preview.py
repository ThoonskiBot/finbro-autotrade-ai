# Sends a preview image to Telegram using bot token & chat ID from .env
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_preview_via_telegram(image_path="reports/previews/daily_trade_summary_chart_2025-05-21_preview.jpg"):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_id:
        print("❌ Telegram bot token or chat ID not set in .env.")
        return

    try:
        with open(image_path, 'rb') as photo:
            resp = requests.post(
                f"https://api.telegram.org/bot{bot_token}/sendPhoto",
                data={"chat_id": chat_id},
                files={"photo": photo}
            )
        if resp.status_code == 200:
            print("📲 Telegram preview sent.")
        else:
            print(f"❌ Telegram error: {resp.text}")
    except Exception as e:
        print(f"❌ Telegram send failed: {e}")

if __name__ == "__main__":
    send_preview_via_telegram()
