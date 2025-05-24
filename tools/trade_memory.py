
import os
from datetime import datetime
from core.config import LOG_PATH

def get_recent_trades(days=1):
    recent_trades = {}
    today = datetime.now().strftime("%Y%m%d")
    for file in sorted(os.listdir(LOG_PATH), reverse=True):
        if not file.startswith("order_log_") or not file.endswith(".txt"):
            continue
        file_date = file.split("_")[2][:8]
        if file_date != today:
            continue
        with open(os.path.join(LOG_PATH, file), "r", encoding="utf-8") as f:
            for line in f:
                if "Executing" in line:
                    parts = line.strip().split("|")
                    ticker = parts[0].replace("✅ Executing", "").strip()
                    action = parts[1].strip()
                    recent_trades[ticker] = action.upper()
    return recent_trades
