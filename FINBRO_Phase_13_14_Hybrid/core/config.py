import os
from dotenv import load_dotenv
load_dotenv()

ALPACA_API_KEY = os.getenv("APCA_API_KEY_ID")
ALPACA_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
ALPACA_BASE_URL = os.getenv("ALPACA_ENDPOINT", "https://paper-api.alpaca.markets")

TRADE_LEDGER_PATH = "ledger/trade_log.csv"
POSITIONS_FILE = "ledger/positions.csv"
LIVE_MODE = os.getenv("LIVE_TRADING_ENABLED", "false").lower() == "true"
