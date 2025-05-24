
import os
from datetime import datetime
from collections import defaultdict
from core.config import LOG_PATH

def parse_logs_for_strategy_pnl():
    strategy_pnl = defaultdict(int)

    for filename in os.listdir(LOG_PATH):
        if filename.startswith("order_log_") and filename.endswith(".txt"):
            try:
                with open(os.path.join(LOG_PATH, filename), "r", encoding="utf-8") as f:
                    for line in f:
                        if "BUY" in line:
                            strategy = line.split("Strategy:")[1].strip()
                            strategy_pnl[strategy] -= 1
                        elif "SELL" in line:
                            strategy = line.split("Strategy:")[1].strip()
                            strategy_pnl[strategy] += 1
            except:
                continue
    return dict(strategy_pnl)
