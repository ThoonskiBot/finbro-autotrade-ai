def fuse_signals(signals):
    if not signals or not isinstance(signals, list):
        return []
    from collections import Counter
    flat = [sig['ticker'] for sig in signals if 'ticker' in sig]
    ticker_counts = Counter(flat)
    fused = [sig for sig in signals if ticker_counts[sig['ticker']] >= 2]
    return fused
