
# tools/chart_sender.py

import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path

load_dotenv()
LOG_DIR = os.getenv("LOG_PATH", "logs")
CHART_PATH = os.getenv("CHART_OUTPUT_PATH", "reports/finbro_pnl_chart.png")

def generate_dummy_chart():
    dates = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    pnl = [1200, 1400, 1100, 1500, 1700]

    plt.figure(figsize=(8, 4))
    plt.plot(dates, pnl, marker="o")
    plt.title("Weekly PnL")
    plt.xlabel("Day")
    plt.ylabel("PnL ($)")
    plt.grid(True)
    plt.tight_layout()

    output_path = Path(CHART_PATH)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    return str(output_path)
