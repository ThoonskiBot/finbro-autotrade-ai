import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

LOG_DIR = "C:/FINBRO/logs"
REPORT_DIR = "C:/FINBRO/reports"
files = sorted([f for f in os.listdir(LOG_DIR) if f.startswith("order_log") and f.endswith(".txt")])

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
                    win = 1 if result.lower() == "win" else 0
                    data.append((strategy, ticker, win))

df = pd.DataFrame(data, columns=["strategy", "ticker", "win"])
if df.empty:
    print("❌ No data found for heatmap.")
    exit()

pivot = df.pivot_table(index="strategy", columns="ticker", values="win", aggfunc="mean").fillna(0)
plt.figure(figsize=(10, 6))
sns.heatmap(pivot, annot=True, cmap="YlGnBu", fmt=".2f", linewidths=.5)
plt.title("Strategy vs Ticker Win Rate Heatmap")

heatmap_path = os.path.join(REPORT_DIR, f"strategy_heatmap_{datetime.now().strftime('%Y-%m-%d')}.png")
plt.savefig(heatmap_path)
plt.close()

print(f"✅ Heatmap saved to: {heatmap_path}")
