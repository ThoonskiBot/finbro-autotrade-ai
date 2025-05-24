import os
from dotenv import load_dotenv
load_dotenv()

TRADE_LEDGER_PATH = "ledger/trade_log.csv"
POSITIONS_FILE = "ledger/positions.csv"
PDF_REPORT_PATH = "reports/daily_trade_summary.pdf"
LIVE_MODE = os.getenv("LIVE_TRADING_ENABLED", "false").lower() == "true"
