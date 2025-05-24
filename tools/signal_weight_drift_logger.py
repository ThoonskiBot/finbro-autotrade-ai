# Phase 125 – Signal Weight Drift Logger
def log_weight_drift(history, current_weights):
    history.append(current_weights)
    if len(history) > 5:
        history.pop(0)
    return history