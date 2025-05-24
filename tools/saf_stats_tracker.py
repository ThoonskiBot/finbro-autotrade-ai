
import glob

log_files = glob.glob("C:/FINBRO/logs/order_log*.txt")
executed, skipped = 0, 0
strategy_stats = {}

for f in log_files[-5:]:
    with open(f, "r") as file:
        for line in file:
            if "accepted" in line:
                executed += 1
                strategy = line.split("|")[0].strip()
                strategy_stats[strategy] = strategy_stats.get(strategy, 0) + 1
            elif "skipped" in line:
                skipped += 1

with open("C:/FINBRO/ui/static/saf_stats.txt", "w") as out:
    out.write(f"Executed Trades: {executed}\nSkipped Trades: {skipped}\n")
    for k, v in strategy_stats.items():
        out.write(f"{k}: {v} trades\n")

print("📊 SAF stats written.")
