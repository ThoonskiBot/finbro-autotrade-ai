
import random
from datetime import datetime

def select_strategy():
    weekday = datetime.now().weekday()
    strategies = ["Momentum", "Reversal", "Breakout"]

    if weekday == 0:
        return "Breakout"
    elif weekday in [1, 2]:
        return "Momentum"
    else:
        return random.choice(strategies)
