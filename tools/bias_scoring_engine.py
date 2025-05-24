# Phase 104 – Bias Scoring Engine
def score_bias(log):
    from collections import Counter
    counts = Counter([t["ticker"] for t in log])
    max_count = max(counts.values())
    return {ticker: round(c / max_count, 2) for ticker, c in counts.items()}