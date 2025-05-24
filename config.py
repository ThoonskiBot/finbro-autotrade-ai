
import os
from dotenv import load_dotenv

# Always load environment variables every time the module is imported
load_dotenv(override=True)

# === API Keys ===
ALPACA_API_KEY = os.getenv("APCA_API_KEY_ID")
ALPACA_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
ALPACA_ENDPOINT = os.getenv("ALPACA_ENDPOINT", "https://paper-api.alpaca.markets")

# === Trading Parameters ===
DEFAULT_TICKER = os.getenv("DEFAULT_TICKER", "SPY")
DEFAULT_QTY = int(os.getenv("DEFAULT_QTY", 10))
TP_PERCENT = float(os.getenv("TP_PERCENT", 3.0))
SL_PERCENT = float(os.getenv("SL_PERCENT", 2.0))

# === File Paths ===
LOG_PATH = os.getenv("LOG_PATH", "logs/trade_log.csv")
SIGNALS_DIR = os.getenv("SIGNALS_DIR", "signals/")
PDF_OUTPUT_DIR = os.getenv("PDF_OUTPUT_DIR", "logs/")

# === Test Print Block ===
print("🔑 ALPACA_API_KEY:", ALPACA_API_KEY)
print("📦 DEFAULT_QTY:", DEFAULT_QTY)
print("📍 TP %:", TP_PERCENT)
print("🛡️ SL %:", SL_PERCENT)
print("📄 LOG PATH:", LOG_PATH)
