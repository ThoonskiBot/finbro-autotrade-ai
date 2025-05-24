# tools/signal_fusion.py

def fuse_signals(signals):
    if not signals or not isinstance(signals, list):
        return []
    # Example fusion logic: only keep tickers that appear in at least 2 strategies
    from collections import Counter
    flat = [sig['ticker'] for sig in signals if 'ticker' in sig]
    ticker_counts = Counter(flat)
    fused = [sig for sig in signals if ticker_counts[sig['ticker']] >= 2]
    return fused