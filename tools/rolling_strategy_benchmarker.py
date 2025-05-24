# Phase 126 – Rolling Strategy Benchmarker

def benchmark_strategy_rollout(performance_log, new_result):
    performance_log.append(new_result)
    if len(performance_log) > 10:
        performance_log.pop(0)
    avg = round(sum(performance_log) / len(performance_log), 2)
    return avg, performance_log