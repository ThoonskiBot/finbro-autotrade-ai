
import json
import os

def log_signal_result(ticker, action, result, log_path='signal_scores.json'):
    if not os.path.exists(log_path):
        scores = {}
    else:
        with open(log_path, "r") as f:
            scores = json.load(f)

    key = f"{ticker}:{action}"
    scores.setdefault(key, {"wins": 0, "losses": 0})
    if result > 0:
        scores[key]["wins"] += 1
    else:
        scores[key]["losses"] += 1

    with open(log_path, "w") as f:
        json.dump(scores, f, indent=2)
