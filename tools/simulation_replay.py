
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from core.config import LOG_PATH

def replay_latest_log(delay=1.0):
    logs = sorted([f for f in os.listdir(LOG_PATH) if f.startswith("order_log_")], reverse=True)
    if not logs:
        print("❌ No logs found.")
        return

    with open(os.path.join(LOG_PATH, logs[0]), "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            print("▶", line.strip())
            time.sleep(delay)

if __name__ == "__main__":
    replay_latest_log(0.8)
