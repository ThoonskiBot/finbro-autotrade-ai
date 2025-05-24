# Generates a simple pnl_by_date.csv from trade log files
import csv
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def generate_pnl_log(log_dir="logs", output_file="logs/pnl_by_date.csv", qty_per_trade=1, mock_exit_price=610.0):
    pnl_by_date = defaultdict(float)

    for file in Path(log_dir).rglob("*.csv"):
        if "pnl_by_date" in str(file.name):
            continue  # skip output files

        with open(file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    ts = row.get("Timestamp") or row.get("timestamp")
                    entry = float(row["EntryPrice"])
                    pnl = (mock_exit_price - entry) * qty_per_trade

                    date = datetime.fromisoformat(ts).date()
                    pnl_by_date[str(date)] += pnl
                except Exception as e:
                    continue

    # Ensure the output directory exists
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["date", "pnl"])
        for date_str in sorted(pnl_by_date):
            writer.writerow([date_str, round(pnl_by_date[date_str], 2)])

    print(f"✅ PnL log written to: {output_file}")

if __name__ == "__main__":
    generate_pnl_log()
