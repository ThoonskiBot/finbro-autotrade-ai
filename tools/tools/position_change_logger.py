# Phase 87 – Position Change Logger
def log_position_change(prev, curr):
    changes = {}
    for ticker, curr_qty in curr.items():
        prev_qty = prev.get(ticker, 0)
        diff = curr_qty - prev_qty
        if diff != 0:
            changes[ticker] = diff
    return changes