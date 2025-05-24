
import os
from datetime import datetime
from collections import defaultdict

def read_pnl_from_logs(log_dir="logs"):
    pnl_by_date = defaultdict(float)
    for filename in os.listdir(log_dir):
        if not filename.startswith("order_log_") or not filename.endswith(".txt"):
            continue
        date_str = filename.replace("order_log_", "").replace(".txt", "")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except:
            continue
        path = os.path.join(log_dir, filename)
        with open(path, "r") as f:
            for line in f:
                if "win" in line:
                    pnl_by_date[date.date()] += 100
                elif "loss" in line:
                    pnl_by_date[date.date()] -= 100
    result = [{"date": str(k), "pnl": v} for k, v in sorted(pnl_by_date.items())]
    return result
