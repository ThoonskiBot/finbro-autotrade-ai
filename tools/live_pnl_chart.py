
import os
import pandas as pd
import matplotlib.pyplot as plt
from core.config import LOG_PATH, REPORTS_PATH
from datetime import datetime

def generate_live_pnl_chart():
    records = []

    for file in sorted(os.listdir(LOG_PATH), reverse=True):
        if file.startswith("order_log_"):
            date_str = file.split("_")[2][:8]
            with open(os.path.join(LOG_PATH, file), "r", encoding="utf-8") as f:
                pnl = 0
                for line in f:
                    if "Executing" in line:
                        if "BUY" in line:
                            pnl -= 1
                        elif "SELL" in line:
                            pnl += 1
                records.append((date_str, pnl))

    df = pd.DataFrame(records, columns=["Date", "PnL"])
    df = df.groupby("Date").sum().reset_index()

    plt.figure(figsize=(8, 4))
    plt.plot(df["Date"], df["PnL"], marker="o")
    plt.title("Live Session PnL")
    plt.xlabel("Date")
    plt.ylabel("PnL")
    plt.grid(True)
    plt.tight_layout()

    os.makedirs(REPORTS_PATH, exist_ok=True)
    out_path = os.path.join(REPORTS_PATH, f"live_pnl_chart_{datetime.now().strftime('%Y%m%d_%H%M')}.png")
    plt.savefig(out_path)
    plt.close()
    print(f"✅ Live PnL chart saved to: {out_path}")

if __name__ == "__main__":
    generate_live_pnl_chart()
