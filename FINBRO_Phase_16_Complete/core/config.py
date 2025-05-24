import os
from dotenv import load_dotenv
load_dotenv()

### === ALPACA PAPER TRADING === ###
APCA_API_KEY_ID = os.getenv("APCA_API_KEY_ID")
APCA_API_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
ALPACA_ENDPOINT = os.getenv("ALPACA_ENDPOINT", "https://paper-api.alpaca.markets")

### === TELEGRAM ALERTS (OPTIONAL BUT STRONGLY RECOMMENDED) === ###
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

### === TWELVEDATA (for Fundamentals/Indicators) === ###
TWELVEDATA_API_KEY = os.getenv("TWELVEDATA_API_KEY")

### === OPENAI (for GPT-based logic or summaries) === ###
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

### === EMAIL FAILSAFE (for crash alerts/logs) === ###
FAILSAFE_EMAIL_SENDER = os.getenv("FAILSAFE_EMAIL_SENDER")
FAILSAFE_EMAIL_PASSWORD = os.getenv("FAILSAFE_EMAIL_PASSWORD")
FAILSAFE_EMAIL_RECEIVER = os.getenv("FAILSAFE_EMAIL_RECEIVER")
FINBRO_EMAIL_ENABLED = os.getenv("FINBRO_EMAIL_ENABLED", "true").lower() == "true"

### === GENERAL CONFIGS === ###
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
TIMEZONE = os.getenv("TIMEZONE", "America/Los_Angeles")
TRADING_ENABLED = os.getenv("TRADING_ENABLED", "true").lower() == "true"
MAX_POSITION_PER_TICKER = int(os.getenv("MAX_POSITION_PER_TICKER", 100))
DAILY_TRADE_LIMIT = int(os.getenv("DAILY_TRADE_LIMIT", 5))

### === INTERNAL PATHS === ###
TRADE_LEDGER_PATH = "ledger/trade_log.csv"
POSITIONS_FILE = "ledger/positions.csv"
PDF_REPORT_PATH = "reports/daily_trade_summary.pdf"

### === ACTIVE TRADING FLAG === ###
LIVE_MODE = os.getenv("LIVE_TRADING_ENABLED", "false").lower() == "true"
