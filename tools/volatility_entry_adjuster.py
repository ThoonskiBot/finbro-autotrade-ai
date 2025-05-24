# Phase 109 – Volatility-Aware Entry Adjuster

def adjust_entry_price(base_price, volatility, direction='long'):
    offset = base_price * volatility
    return round(base_price - offset, 2) if direction == 'long' else round(base_price + offset, 2)