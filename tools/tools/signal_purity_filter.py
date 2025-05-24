# Phase 82 – Signal Purity Filter
def filter_pure_signals(signals, min_confidence=0.7):
    return [s for s in signals if s.get('confidence', 0) >= min_confidence]