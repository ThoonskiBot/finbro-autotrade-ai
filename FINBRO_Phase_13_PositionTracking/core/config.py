import os
from dotenv import load_dotenv
load_dotenv()

LOG_PATH = "logs"
PDF_OUTPUT_DIR = "logs"
TRADE_LEDGER_PATH = "ledger/trade_log.csv"
POSITIONS_FILE = "ledger/positions.csv"
LIVE_MODE = os.getenv("LIVE_TRADING_ENABLED", "false").lower() == "true"
