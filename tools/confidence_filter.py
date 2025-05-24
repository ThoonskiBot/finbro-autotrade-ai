"""
Signal Confidence Filter - Filters out signals below confidence threshold.
"""
def filter_signals(signals, threshold=0.7):
    return [s for s in signals if s.get('confidence', 1.0) >= threshold]
