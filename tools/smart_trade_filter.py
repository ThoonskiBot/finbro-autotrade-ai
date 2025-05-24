
import os
from core.config import MAX_POSITION_PER_TICKER
from tools.alpaca_position_sync import get_live_positions

# Simulated signal structure: {ticker, action, strategy, confidence, risk_level}
def should_execute_trade(signal):
    positions = get_live_positions()
    ticker = signal.get("Ticker")
    action = signal.get("Action").upper()
    strategy = signal.get("Strategy", "Unknown")
    confidence = float(signal.get("Confidence", 1.0))  # Optional
    risk_level = signal.get("Risk", "Normal")  # Optional

    qty_held = int(positions.get(ticker, 0))
    max_allowed = MAX_POSITION_PER_TICKER

    # Rule: avoid duplicate long entries
    if action == "BUY" and qty_held >= max_allowed:
        return False, f"Position cap reached on {ticker} ({qty_held}/{max_allowed})"

    # Rule: avoid excessive shorting
    if action == "SELL" and qty_held <= -max_allowed:
        return False, f"Short limit hit on {ticker} ({qty_held})"

    # Rule: skip low-confidence trades
    if confidence < 0.5:
        return False, f"Low confidence trade rejected ({confidence})"

    # Rule: skip flagged risky trades
    if risk_level == "High":
        return False, "Risk level 'High' blocked by filter"

    return True, "Approved"
