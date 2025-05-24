
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
import requests
from datetime import datetime
from subprocess import run, CalledProcessError
from core.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, REPORTS_PATH, LOG_PATH, ALPACA_ENDPOINT
from core.config import APCA_API_KEY_ID as ALPACA_KEY, APCA_API_SECRET_KEY as ALPACA_SECRET
from core.strategy_filter import select_strategy

try:
    from alpaca_trade_api.rest import REST
except ImportError:
    REST = None

API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

def send_telegram_message(text):
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    try:
        requests.post(f"{API_URL}/sendMessage", data=payload)
    except Exception as e:
        print(f"❌ Telegram message failed: {e}")

def send_telegram_file(filepath, caption=""):
    try:
        with open(filepath, "rb") as f:
            requests.post(
                f"{API_URL}/sendDocument",
                data={"chat_id": TELEGRAM_CHAT_ID, "caption": caption},
                files={"document": f}
            )
    except Exception as e:
        print(f"❌ Telegram file send failed: {e}")

def get_price(ticker):
    try:
        r = requests.get(f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={ticker}")
        data = r.json()["quoteResponse"]["result"][0]
        price = data["regularMarketPrice"]
        change = data["regularMarketChangePercent"]
        return f"📈 {ticker.upper()} = ${price:.2f} ({change:+.2f}%)"
    except Exception as e:
        return f"❌ Could not fetch {ticker}: {e}"

def get_positions():
    if not (ALPACA_KEY and ALPACA_SECRET and ALPACA_ENDPOINT):
        return "❌ Alpaca credentials not set in .env"
    try:
        api = REST(ALPACA_KEY, ALPACA_SECRET, ALPACA_ENDPOINT)
        positions = api.list_positions()
        if not positions:
            return "📭 No open positions."
        msg = "📊 Current Positions:\n"
        for p in positions:
            msg += f"{p.symbol}: {p.qty} shares at ${p.avg_entry_price}\n"
        return msg
    except Exception as e:
        return f"❌ Failed to fetch positions: {e}"

def handle_command(command):
    today = datetime.now().strftime("%Y-%m-%d")
    raw_date = datetime.now().strftime("%Y%m%d")

    if command == "/run":
        send_telegram_message("🧠 FINBRO is running now...")
        try:
            result = run(["py", "-3.11", "finbro_runner.py"], capture_output=True, text=True, check=True)
            send_telegram_message("✅ FINBRO finished.\n\n" + result.stdout[-4000:])
        except CalledProcessError as e:
            send_telegram_message("❌ Error during FINBRO run:\n\n" + e.stderr[-4000:])
    elif command == "/strategy":
        strat = select_strategy()
        send_telegram_message(f"🧠 Today's strategy: {strat}")
    elif command == "/summary":
        for file in os.listdir(REPORTS_PATH):
            if file.startswith("gpt_trade_summary_") and today in file:
                send_telegram_file(os.path.join(REPORTS_PATH, file), caption="🧠 GPT Summary")
                return
        send_telegram_message("❌ No GPT summary found for today.")
    elif command == "/pnl":
        chart_path = os.path.join(REPORTS_PATH, f"daily_trade_summary_chart_{raw_date}.pdf")
        if os.path.exists(chart_path):
            send_telegram_file(chart_path, caption="📈 Daily PnL Chart")
        else:
            send_telegram_message("❌ No PnL chart found.")
    elif command == "/logs":
        for file in sorted(os.listdir(LOG_PATH), reverse=True):
            if file.startswith("order_log_") and file.endswith(".txt"):
                send_telegram_file(os.path.join(LOG_PATH, file), caption="📋 Latest Order Log")
                return
        send_telegram_message("❌ No logs found.")
    elif command == "/positions":
        send_telegram_message(get_positions())
    elif command.startswith("/price"):
        ticker = command.split(" ")[-1].strip().upper()
        send_telegram_message(get_price(ticker))
    elif command == "/status":
        send_telegram_message("✅ FINBRO is online and listening. Ready for commands.")
    else:
        send_telegram_message("❌ Unknown command. Try /run /summary /pnl /logs /positions /price TICKER /strategy /status")

def poll_telegram():
    offset = None
    print("📡 FINBRO Telegram bot listening...")
    while True:
        try:
            resp = requests.get(f"{API_URL}/getUpdates", params={"offset": offset}, timeout=60)
            updates = resp.json().get("result", [])
            for update in updates:
                offset = update["update_id"] + 1
                message = update.get("message", {}).get("text")
                if message:
                    handle_command(message)
        except Exception as e:
            print(f"⚠️ Polling error: {e}")

if __name__ == "__main__":
    poll_telegram()
