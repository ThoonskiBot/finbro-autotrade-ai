import os
import pandas as pd
from datetime import datetime

LOG_DIR = "C:/FINBRO/logs"
REPORT_DIR = "C:/FINBRO/reports"
files = sorted([f for f in os.listdir(LOG_DIR) if f.startswith("order_log") and f.endswith(".txt")], reverse=True)[:30]

data = []
for fname in files:
    with open(os.path.join(LOG_DIR, fname), "r", encoding="utf-8") as f:
        for line in f:
            if "|" in line:
                parts = [p.strip() for p in line.strip().split("|")]
                if len(parts) >= 3:
                    strategy = parts[0]
                    ticker = parts[1]
                    result = parts[-1]
                    data.append((strategy, ticker, result))

df = pd.DataFrame(data, columns=["strategy", "ticker", "result"])
if df.empty:
    print("❌ No data to analyze.")
    exit()

recap = df.groupby(["strategy", "result"]).size().unstack(fill_value=0)
recap["Total"] = recap.sum(axis=1)
recap["WinRate"] = recap.get("win", 0) / recap["Total"]
recap = recap.sort_values("WinRate", ascending=False)

csv_path = os.path.join(REPORT_DIR, f"strategy_alpha_recap_{datetime.now().strftime('%Y-%m-%d')}.csv")
recap.to_csv(csv_path)
print(f"✅ Alpha recap saved to: {csv_path}")
