# Phase 112 – Smart Exit Refinement Module

def refine_exit_price(entry_price, price_data):
    if price_data.get('volatility') > 0.03:
        return round(entry_price * 1.01, 2)
    elif price_data.get('trend_strength') > 0.7:
        return round(entry_price * 1.02, 2)
    else:
        return round(entry_price * 1.005, 2)