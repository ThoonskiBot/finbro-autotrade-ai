# Phase 103 – Market Regime Detector
def detect_regime(data):
    if data.get("trend_strength") > 0.7:
        return "Trending"
    elif data.get("volatility") > 0.05:
        return "Choppy"
    elif data.get("momentum") > 1.5:
        return "Breakout"
    else:
        return "Sideways/Undefined"