# Phase 118 – Confidence Backtest Simulator

def simulate_confidence_accuracy(logs):
    correct = 0
    total = 0
    for log in logs:
        if "confidence" in log and "outcome" in log:
            total += 1
            if (log["confidence"] >= 0.5 and log["outcome"] == "win") or (log["confidence"] < 0.5 and log["outcome"] == "loss"):
                correct += 1
    return round(correct / total, 2) if total else 0.0