# Phase 84 – Strategy Time-of-Day Profiler
def profile_signal_times(trades):
    from collections import Counter
    import datetime
    times = [datetime.datetime.strptime(t['timestamp'], "%Y-%m-%d %H:%M:%S").hour for t in trades]
    return dict(Counter(times))