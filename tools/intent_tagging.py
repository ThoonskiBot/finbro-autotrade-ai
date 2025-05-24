
def tag_trade_intent(signal):
    # Dummy logic for tagging signal intent
    ticker = signal.get("Ticker", "")
    strategy = signal.get("Strategy", "").lower()
    if "momentum" in strategy:
        return "Breakout Pullback"
    elif "reversal" in strategy:
        return "Mean Reversion Dip"
    return "General Trend Signal"
