import os
import pandas as pd
from datetime import datetime, timedelta

log_dir = "C:/FINBRO/logs"
files = sorted([f for f in os.listdir(log_dir) if f.startswith("order_log") and f.endswith(".txt")])

data = []
for fname in files[-30:]:  # last 30 logs
    with open(os.path.join(log_dir, fname), "r", encoding="utf-8") as f:
        for line in f:
            if "|" in line:
                parts = line.strip().split("|")
                if len(parts) >= 3:
                    strategy = parts[0].strip()
                    result = parts[-1].strip()
                    data.append((fname, strategy, result))

df = pd.DataFrame(data, columns=["file", "strategy", "result"])
if df.empty:
    print("❌ No data found.")
    exit()

summary = df.groupby(["strategy", "result"]).size().unstack(fill_value=0)
summary["Total"] = summary.sum(axis=1)
summary["WinRate"] = summary.get("win", 0) / summary["Total"]

out_path = os.path.join("C:/FINBRO/reports", f"strategy_drift_report_{datetime.now().strftime('%Y-%m-%d')}.csv")
summary.to_csv(out_path)
print(f"📉 Drift report saved to: {out_path}")
