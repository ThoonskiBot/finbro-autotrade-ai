
import os
from datetime import datetime, timedelta
from core.config import LOG_PATH

def collect_weekly_logs():
    today = datetime.now()
    summaries = []

    for file in sorted(os.listdir(LOG_PATH), reverse=True):
        if file.startswith("order_log_"):
            file_date = file.split("_")[2][:8]
            log_date = datetime.strptime(file_date, "%Y%m%d")
            if (today - log_date).days <= 7:
                with open(os.path.join(LOG_PATH, file), "r", encoding="utf-8") as f:
                    summaries.append(f.read())

    return "\n\n--- NEXT LOG ---\n\n".join(summaries)
