# Phase 108 – Trade Timing Profiler

def profile_trade_timing(trades):
    from collections import Counter
    hours = [int(t['timestamp'].split(' ')[1].split(':')[0]) for t in trades]
    return dict(Counter(hours))