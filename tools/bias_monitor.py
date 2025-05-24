# Phase 99 – Bias Monitor

def detect_strategy_bias(trade_log):
    from collections import Counter
    tickers = [entry['ticker'] for entry in trade_log if 'ticker' in entry]
    return dict(Counter(tickers))