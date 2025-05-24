
import os
from collections import defaultdict
from core.config import LOG_PATH

def generate_strategy_pnl_summary():
    pnl_by_strategy = defaultdict(int)

    for file in sorted(os.listdir(LOG_PATH), reverse=True):
        if file.startswith("order_log_") and file.endswith(".txt"):
            with open(os.path.join(LOG_PATH, file), "r", encoding="utf-8") as f:
                for line in f:
                    if "Executing" in line:
                        parts = line.strip().split("|")
                        strategy = parts[2].split(":")[1].strip()
                        action = parts[1].strip().lower()
                        if "buy" in action:
                            pnl_by_strategy[strategy] -= 1
                        elif "sell" in action:
                            pnl_by_strategy[strategy] += 1
    return dict(pnl_by_strategy)
