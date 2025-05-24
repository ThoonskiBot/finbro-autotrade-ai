
import os
import pandas as pd
from collections import defaultdict
from core.config import LOG_PATH

def analyze_saf_logs():
    skipped = defaultdict(int)
    executed = defaultdict(int)
    reasons = defaultdict(lambda: defaultdict(int))

    latest_file = sorted([f for f in os.listdir(LOG_PATH) if f.startswith("order_log_")], reverse=True)[0]
    log_path = os.path.join(LOG_PATH, latest_file)

    with open(log_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if "Skipping" in line:
            parts = line.strip().split("|")
            strategy = parts[1].split(":")[1].strip()
            reason = parts[2].split(":")[1].strip()
            skipped[strategy] += 1
            reasons[strategy][reason] += 1
        elif "Executing" in line:
            parts = line.strip().split("|")
            strategy = parts[2].split(":")[1].strip()
            executed[strategy] += 1

    return executed, skipped, reasons
