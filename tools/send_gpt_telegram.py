import os, requests
token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")
with open("reports/gpt_trade_summary_2025-05-21_2102.txt", "r", encoding="utf-8") as f:
    summary = f.read()
requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": chat_id, "text": summary})
print("✅ GPT Summary sent via Telegram.")