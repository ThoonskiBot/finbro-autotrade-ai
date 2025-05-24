# Parses local trade logs or Alpaca for building PnL line chart
import csv
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def load_pnl_from_logs(log_folder="logs"):
    pnl_by_date = defaultdict(float)

    for csv_file in Path(log_folder).rglob("*.csv"):
        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    date_str = row.get("date") or row.get("timestamp", "").split("T")[0]
                    pnl = float(row.get("pnl", 0) or row.get("PnL", 0))
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                    pnl_by_date[date_obj.date()] += pnl
                except:
                    continue

    sorted_dates = sorted(pnl_by_date)
    return {
        "dates": [d.strftime("%Y-%m-%d") for d in sorted_dates],
        "values": [round(pnl_by_date[d], 2) for d in sorted_dates]
    }
