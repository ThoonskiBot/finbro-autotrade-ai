# Phase 114 – Order Latency Diagnostic Tool

def calculate_latency(signal_time, fill_time):
    from datetime import datetime
    fmt = "%Y-%m-%d %H:%M:%S"
    signal_dt = datetime.strptime(signal_time, fmt)
    fill_dt = datetime.strptime(fill_time, fmt)
    return (fill_dt - signal_dt).total_seconds()