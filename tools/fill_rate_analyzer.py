# Phase 107 – Fill Rate Analyzer

def analyze_fill_rate(fills, orders):
    if orders == 0:
        return 0.0
    return round((fills / orders) * 100, 2)