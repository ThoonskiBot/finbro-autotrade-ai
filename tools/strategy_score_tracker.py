import os
import pandas as pd
from datetime import datetime

LOG_DIR = "C:/FINBRO/logs"
REPORT_DIR = "C:/FINBRO/reports"
files = sorted([f for f in os.listdir(LOG_DIR) if f.startswith("order_log")], reverse=True)[:30]

records = []
for fname in files:
    with open(os.path.join(LOG_DIR, fname), "r", encoding="utf-8") as f:
        for line in f:
            if "|" in line:
                parts = [p.strip() for p in line.strip().split("|")]
                if len(parts) >= 3:
                    strategy = parts[0]
                    result = parts[-1].lower()
                    win = 1 if result == "win" else 0
                    records.append((fname, strategy, win))

df = pd.DataFrame(records, columns=["file", "strategy", "win"])
if df.empty:
    print("❌ No data found.")
    exit()

summary = df.groupby("strategy")["win"].agg(["count", "sum"])
summary["win_rate"] = summary["sum"] / summary["count"]
summary = summary.rename(columns={"count": "total_trades", "sum": "wins"})
summary.reset_index(inplace=True)

out_file = os.path.join(REPORT_DIR, f"strategy_score_tracker_{datetime.now().strftime('%Y-%m-%d')}.csv")
summary.to_csv(out_file, index=False)

print(f"✅ Weekly strategy tracker saved to: {out_file}")
