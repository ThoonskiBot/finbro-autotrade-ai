# Phase 122 – Signal Lag Detector
def detect_lag(signal_time, execution_time, threshold=2):
    from datetime import datetime
    fmt = "%Y-%m-%d %H:%M:%S"
    signal_dt = datetime.strptime(signal_time, fmt)
    exec_dt = datetime.strptime(execution_time, fmt)
    lag = (exec_dt - signal_dt).total_seconds()
    return lag > threshold, lag