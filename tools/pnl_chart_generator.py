
import matplotlib.pyplot as plt
import os

# Path to trade log (replace with actual dynamic file if needed)
log_path = "C:/FINBRO/logs/pnl_log_sample.txt"
chart_output = "C:/FINBRO/ui/static/pnl_chart.png"

timestamps = []
pnls = []

# Parse log file
if os.path.exists(log_path):
    with open(log_path, "r") as f:
        for line in f:
            if "|" in line:
                try:
                    time, pnl = line.strip().split("|")
                    timestamps.append(time.strip())
                    pnls.append(float(pnl.strip()))
                except:
                    continue

# Generate chart
plt.figure(figsize=(10, 4))
plt.plot(timestamps, pnls, marker="o", color="#00FF88")
plt.title("PnL Over Time")
plt.xlabel("Time")
plt.ylabel("PnL ($)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save image
plt.savefig(chart_output)
print(f"✅ PnL chart saved to {chart_output}")
