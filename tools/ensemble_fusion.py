
def blend_ensemble_signals(*strategy_lists):
    from collections import defaultdict
    votes = defaultdict(lambda: {"BUY": 0, "SELL": 0, "HOLD": 0, "meta": {}})

    for strategy_signals in strategy_lists:
        for signal in strategy_signals:
            t = signal["Ticker"]
            a = signal["Action"].upper()
            votes[t][a] += 1
            votes[t]["meta"] = signal

    blended = []
    for ticker, result in votes.items():
        action = max(["BUY", "SELL", "HOLD"], key=lambda x: result[x])
        fused_signal = result["meta"].copy()
        fused_signal["FusedAction"] = action
        blended.append(fused_signal)
    return blended
