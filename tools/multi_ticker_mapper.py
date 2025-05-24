# Phase 123 – Multi-Ticker Strategy Mapper
def map_strategy_to_tickers(strategy_output, tickers):
    return [{**strategy_output, "ticker": t} for t in tickers]