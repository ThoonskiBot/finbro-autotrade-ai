
ENABLED_STRATEGIES = {
    "Momentum": True,
    "Reversal": True,
    "Neutral": False
}

def is_strategy_enabled(strategy):
    return ENABLED_STRATEGIES.get(strategy, False)
