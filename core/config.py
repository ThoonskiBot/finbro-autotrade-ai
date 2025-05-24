
import os
from dotenv import load_dotenv
load_dotenv()

# === ALPACA PAPER TRADING (ENV MAPPED) ===
APCA_API_KEY_ID = os.getenv("APCA_API_KEY_ID")
APCA_API_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
ALPACA_ENDPOINT = os.getenv("ALPACA_ENDPOINT")

# === TELEGRAM ALERTS ===
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# === OPENAI / GPT ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# === EMAIL FAILSAFE ===
EMAIL_USER = os.getenv("FAILSAFE_EMAIL_SENDER")
EMAIL_PASS = os.getenv("FAILSAFE_EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("FAILSAFE_EMAIL_RECEIVER")
EMAIL_ENABLED = os.getenv("FINBRO_EMAIL_ENABLED", "false").lower() == "true"

# === GENERAL CONFIGS ===
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
TIMEZONE = os.getenv("TIMEZONE", "America/Los_Angeles")
TRADING_ENABLED = os.getenv("TRADING_ENABLED", "false").lower() == "true"
MAX_POSITION_PER_TICKER = int(os.getenv("MAX_POSITION_PER_TICKER", "100"))
DAILY_TRADE_LIMIT = int(os.getenv("DAILY_TRADE_LIMIT", "5"))

# === PATHS ===
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORTS_PATH = os.path.join(ROOT, "reports")
LOG_PATH = os.path.join(ROOT, "logs")
SIGNALS_PATH = os.path.join(ROOT, "signals")
