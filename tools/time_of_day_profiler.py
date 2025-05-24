# Phase 84 – Strategy Time-of-Day Profiler

def profile_signal_times(trades):
    from collections import Counter
    import datetime
    try:
        times = [datetime.datetime.strptime(t['timestamp'], "%Y-%m-%d %H:%M:%S").hour for t in trades]
        return dict(Counter(times))
    except Exception as e:
        return f"❌ Error processing timestamps: {e}"