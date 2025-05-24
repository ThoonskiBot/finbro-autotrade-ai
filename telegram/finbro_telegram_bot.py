import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import telebot
from dotenv import load_dotenv

from tools.gpt_trade_explainer import explain_skipped_trade
from tools.gpt_summary_generator import generate_summary
from tools.chart_sender import generate_dummy_chart
from tools.log_sender import get_latest_log_file
from tools.gpt_trade_coach import coach_trades
from tools.weekly_drift_gpt import summarize_drift
from tools.signal_scorer import score_signal
from tools.cloud_backup import backup_logs_to_local_cloud
from tools.eod_gpt_reflection import reflect_on_day
from tools.strategy_promoter import promote_strategy

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, (
        "👋 Welcome to FINBRO Bot!\n\n"
        "Available Commands:\n"
        "/summary – GPT trade summary for today\n"
        "/why <TICKER> – Why a trade was skipped\n"
        "/status – Check system status\n"
        "/pnl – View profit/loss (coming soon)\n"
        "/chart – Weekly PnL chart\n"
        "/logs – Download latest trade log\n"
        "/coach – GPT trade coaching\n"
        "/week – Weekly strategy drift report\n"
        "/evaluate – Run full GPT Phase 77–80 evaluation"
    ))

@bot.message_handler(commands=['summary'])
def send_summary(message):
    try:
        summary = generate_summary()
        bot.reply_to(message, f"🧠 GPT Summary:\n\n{summary}")
    except Exception as e:
        bot.reply_to(message, f"❌ Error generating summary:\n{e}")

@bot.message_handler(commands=['why'])
def handle_why_command(message):
    parts = message.text.strip().split()
    if len(parts) < 2:
        bot.reply_to(message, "❌ Usage: /why AAPL")
        return
    ticker = parts[1].upper()
    try:
        reason = explain_skipped_trade(ticker)
        bot.reply_to(message, f"📉 Reason for skipping {ticker}:\n\n{reason}")
    except Exception as e:
        bot.reply_to(message, f"❌ Error analyzing {ticker}:\n{e}")

@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, "📡 FINBRO Bot is live and listening!")

@bot.message_handler(commands=['pnl'])
def send_pnl(message):
    bot.reply_to(message, "💰 PnL tracking module coming soon!")

@bot.message_handler(commands=['chart'])
def send_chart(message):
    try:
        chart_path = generate_dummy_chart()
        with open(chart_path, "rb") as photo:
            bot.send_photo(message.chat.id, photo)
    except Exception as e:
        bot.reply_to(message, f"❌ Chart error:\n{e}")

@bot.message_handler(commands=['logs'])
def send_logs(message):
    try:
        log_file = get_latest_log_file()
        if not log_file:
            bot.reply_to(message, "⚠️ No logs found.")
            return
        with open(log_file, "rb") as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        bot.reply_to(message, f"❌ Log error:\n{e}")

@bot.message_handler(commands=['coach'])
def send_trade_coaching(message):
    try:
        feedback = coach_trades()
        bot.reply_to(message, f"📚 GPT Trade Coach:\n\n{feedback}")
    except Exception as e:
        bot.reply_to(message, f"❌ Coaching error:\n{e}")

@bot.message_handler(commands=['week'])
def send_weekly_drift(message):
    try:
        drift = summarize_drift()
        bot.reply_to(message, f"📈 Weekly Drift:\n\n{drift}")
    except Exception as e:
        bot.reply_to(message, f"❌ Drift error:\n{e}")

@bot.message_handler(commands=['evaluate'])
def evaluate_all(message):
    try:
        bot.reply_to(message, "🛠 Running GPT evaluation...")

        context = "Signal triggered by RSI < 30 and SPY trend confirmation."
        score = score_signal("AAPL", context)
        backup = backup_logs_to_local_cloud()
        reflection = reflect_on_day()
        strategy = promote_strategy()

        result = (
            f"📊 Phase 77–80 Results:\n\n"
            f"🧠 Score: {score}\n"
            f"☁️ Backup Location: {backup}\n"
            f"📘 Reflection Log: {reflection}\n"
            f"📈 Strategy Pick: {strategy}"
        )
        bot.reply_to(message, result)
    except Exception as e:
        bot.reply_to(message, f"❌ Error:\n{e}")

print("🤖 FINBRO Telegram Bot is online!")
bot.polling()