# Phase 124 – Trade Streak Analyzer
def analyze_trade_streaks(trade_log):
    streak = {"win": 0, "loss": 0}
    current = ""
    for trade in trade_log:
        outcome = trade.get("outcome")
        if outcome == current:
            streak[outcome] += 1
        else:
            current = outcome
            streak[outcome] = 1
    return streak