
import os
from collections import defaultdict
from core.config import LOG_PATH

def alpha_attribution():
    alpha = defaultdict(int)
    for file in os.listdir(LOG_PATH):
        if file.startswith("order_log_"):
            with open(os.path.join(LOG_PATH, file), "r", encoding="utf-8") as f:
                for line in f:
                    if "Executing" in line:
                        strategy = line.split("|")[2].split(":")[1].strip()
                        action = line.split("|")[1].strip().upper()
                        alpha[strategy] += 1 if action == "SELL" else -1
    return dict(alpha)

if __name__ == "__main__":
    result = alpha_attribution()
    for strat, score in result.items():
        print(f"{strat}: {score}")
