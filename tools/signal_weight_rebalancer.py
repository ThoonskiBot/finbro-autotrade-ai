# Phase 100 – Signal Weight Rebalancer

def rebalance_signal_weights(performance, current_weights):
    total_perf = sum(performance.values())
    if total_perf == 0:
        return current_weights  # no change if no performance data
    new_weights = {
        strat: round((perf / total_perf), 2)
        for strat, perf in performance.items()
    }
    return new_weights