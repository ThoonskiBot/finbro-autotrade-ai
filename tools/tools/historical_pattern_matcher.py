# Phase 83 – Historical Pattern Matcher
def match_patterns(signal_history, current_signal):
    matches = [entry for entry in signal_history if entry['pattern'] == current_signal['pattern']]
    return matches