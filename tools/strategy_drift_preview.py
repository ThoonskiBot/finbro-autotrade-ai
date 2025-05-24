import os
import pandas as pd
from datetime import datetime

LOG_DIR = "C:/FINBRO/logs"
files = sorted([f for f in os.listdir(LOG_DIR) if f.startswith("order_log")], reverse=True)[:5]

rows = []
for file in files:
    with open(os.path.join(LOG_DIR, file), "r", encoding="utf-8") as f:
        for line in f:
            if "|" in line:
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 3:
                    rows.append((file, parts[0], parts[2]))

df = pd.DataFrame(rows, columns=["file", "strategy", "result"])
if df.empty:
    print("❌ No recent logs to analyze.")
    exit()

pivot = df.groupby(["strategy", "file"]).agg({"result": lambda x: (x == "win").mean()})
pivot = pivot.unstack().fillna(0).round(2)

print("Strategy Drift Summary:\n")
print(pivot)
