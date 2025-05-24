
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from core.config import LOG_PATH, REPORTS_PATH

def build_strategy_heatmap():
    trade_data = []

    for file in os.listdir(LOG_PATH):
        if not file.startswith("order_log_") or not file.endswith(".txt"):
            continue

        file_date = file.split("_")[2][:8]
        readable_date = datetime.strptime(file_date, "%Y%m%d").strftime("%Y-%m-%d")

        with open(os.path.join(LOG_PATH, file), "r", encoding="utf-8") as f:
            for line in f:
                if "Executing" in line:
                    parts = line.strip().split("|")
                    strat = parts[2].split(":")[1].strip()
                    trade_data.append((readable_date, strat, 1))
                elif "Skipping" in line:
                    parts = line.strip().split("|")
                    strat = parts[1].split(":")[1].strip()
                    trade_data.append((readable_date, strat, 0))

    if not trade_data:
        print("❌ No trade data found.")
        return

    df = pd.DataFrame(trade_data, columns=["Date", "Strategy", "Executed"])
    pivot = df.pivot_table(index="Strategy", columns="Date", values="Executed", aggfunc="sum", fill_value=0)

    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot, cmap="YlGnBu", annot=True, fmt="d", linewidths=0.5)
    plt.title("📊 Strategy Trade Heatmap (Executed = Count)")
    plt.tight_layout()

    os.makedirs(REPORTS_PATH, exist_ok=True)
    output_path = os.path.join(REPORTS_PATH, f"strategy_trade_heatmap_{datetime.now().strftime('%Y%m%d_%H%M')}.png")
    plt.savefig(output_path)
    plt.close()
    print(f"✅ Strategy heatmap saved to: {output_path}")

if __name__ == "__main__":
    build_strategy_heatmap()
