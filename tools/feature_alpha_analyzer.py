
import os
from collections import defaultdict
from core.config import LOG_PATH

def analyze_feature_alpha():
    alpha = defaultdict(int)
    for file in os.listdir(LOG_PATH):
        if file.startswith("order_log_"):
            with open(os.path.join(LOG_PATH, file), "r", encoding="utf-8") as f:
                for line in f:
                    if "Executing" in line:
                        if "Momentum" in line:
                            alpha["momentum"] += 1
                        if "Reversal" in line:
                            alpha["reversal"] += 1
                        if "Neutral" in line:
                            alpha["neutral"] += 0
    return dict(alpha)

if __name__ == "__main__":
    results = analyze_feature_alpha()
    for k, v in results.items():
        print(f"{k}: {v}")
