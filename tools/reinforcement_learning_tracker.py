# Phase 97 – Reinforcement Learning Tracker

def log_rl_outcome(signal, result, tracker):
    key = signal.get('ticker') + "|" + signal.get('strategy')
    if key not in tracker:
        tracker[key] = {'wins': 0, 'losses': 0}
    if result == 'win':
        tracker[key]['wins'] += 1
    elif result == 'loss':
        tracker[key]['losses'] += 1
    return tracker