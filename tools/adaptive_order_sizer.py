# Phase 106 – Adaptive Order Sizing Engine

def calculate_order_size(balance, risk_percent, stop_distance):
    if stop_distance == 0:
        return 0
    risk_amount = balance * risk_percent
    size = risk_amount / stop_distance
    return round(size, 2)