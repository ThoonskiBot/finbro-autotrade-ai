
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.config import *

print("=== ALPACA SETTINGS ===")
print("ALPACA_KEY:", ALPACA_KEY)
print("ALPACA_SECRET:", ALPACA_SECRET)
print("ALPACA_ENDPOINT:", ALPACA_ENDPOINT)

print("\n=== TELEGRAM SETTINGS ===")
print("TELEGRAM_BOT_TOKEN:", TELEGRAM_BOT_TOKEN)
print("TELEGRAM_CHAT_ID:", TELEGRAM_CHAT_ID)

print("\n=== TWELVEDATA ===")
print("TWELVEDATA_API_KEY:", TWELVEDATA_API_KEY)

print("\n=== OPENAI ===")
print("GPT_API_KEY:", GPT_API_KEY)

print("\n=== EMAIL FAILSAFE ===")
print("EMAIL_USER:", EMAIL_USER)
print("EMAIL_PASS:", EMAIL_PASS)
print("EMAIL_RECEIVER:", EMAIL_RECEIVER)
print("EMAIL_ENABLED:", EMAIL_ENABLED)

print("\n=== GENERAL CONFIGS ===")
print("LOG_LEVEL:", LOG_LEVEL)
print("TIMEZONE:", TIMEZONE)
print("TRADING_ENABLED:", TRADING_ENABLED)
print("MAX_POSITION_PER_TICKER:", MAX_POSITION_PER_TICKER)
print("DAILY_TRADE_LIMIT:", DAILY_TRADE_LIMIT)
