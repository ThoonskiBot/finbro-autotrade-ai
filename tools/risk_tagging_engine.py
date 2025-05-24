# Phase 102 – Risk Tagging Engine
def tag_trade_risk(trade):
    tags = []
    if trade.get("leverage", 1) > 2:
        tags.append("overleveraged")
    if trade.get("volatility", 0) > 0.05:
        tags.append("high volatility")
    if trade.get("stop_loss") is None:
        tags.append("no stop loss")
    return tags