# Phase 120 – Ticker Fatigue Detector

def detect_fatigue(trades, threshold=3):
    from collections import Counter
    counts = Counter(t['ticker'] for t in trades)
    return [ticker for ticker, count in counts.items() if count >= threshold]