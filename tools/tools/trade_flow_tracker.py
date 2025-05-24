# Phase 86 – Trade Flow Tracker
def track_flows(trades):
    result = {'buy': 0, 'sell': 0}
    for trade in trades:
        action = trade.get('action')
        if action in result:
            result[action] += 1
    return result