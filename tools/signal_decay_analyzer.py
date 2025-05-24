# Phase 88 – Signal Decay Analyzer

def analyze_signal_decay(signals):
    from statistics import mean
    scores = [s.get('confidence', 0) for s in signals]
    return mean(scores) if scores else 0