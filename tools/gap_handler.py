# Phase 110 – Gap Detection & Handling Logic

def detect_price_gap(prev_close, current_open, threshold=0.03):
    if prev_close == 0:
        return False
    gap = abs(current_open - prev_close) / prev_close
    return gap >= threshold