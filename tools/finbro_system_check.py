import os
from dotenv import load_dotenv
import openai
import requests

load_dotenv("C:/FINBRO/.env")

# Core .env pulls
api_key = os.getenv("OPENAI_API_KEY")
telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
email_sender = os.getenv("FAILSAFE_EMAIL_SENDER")
email_password = os.getenv("FAILSAFE_EMAIL_PASSWORD")
email_receiver = os.getenv("FAILSAFE_EMAIL_RECEIVER")

print("=== FINBRO SYSTEM HEALTH CHECK ===")

# 1. GPT Key Check
print("\n[GPT API]")
if not api_key or api_key.strip() == "":
    print("❌ OPENAI_API_KEY is missing or blank.")
else:
    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Say: ✅ GPT key working"}]
        )
        print("✅", response["choices"][0]["message"]["content"])
    except Exception as e:
        print("❌ GPT test failed:", e)

# 2. Telegram Check
print("\n[Telegram Credentials]")
if not telegram_token or not telegram_chat_id:
    print("❌ Telegram bot credentials missing.")
else:
    print("✅ Telegram bot key and chat ID present (send test manually if needed).")

# 3. Email Check
print("\n[Email Credentials]")
if email_sender and email_password and email_receiver:
    print(f"✅ Email credentials loaded for {email_receiver}")
else:
    print("❌ Missing or incomplete email credentials.")

# 4. FINBRO Logs Check
print("\n[Log Directory Scan]")
log_dir = "C:/FINBRO/logs"
if os.path.isdir(log_dir):
    logs = [f for f in os.listdir(log_dir) if f.startswith("order_log")]
    print(f"✅ Found {len(logs)} order log(s).")
else:
    print("❌ Log directory missing.")

# 5. Report Directory Check
print("\n[Report Directory Scan]")
report_dir = "C:/FINBRO/reports"
if os.path.isdir(report_dir):
    reports = [f for f in os.listdir(report_dir) if f.endswith(".txt") or f.endswith(".csv")]
    print(f"✅ Found {len(reports)} report file(s).")
else:
    print("❌ Report directory missing.")

print("\n✅ System check complete.")
