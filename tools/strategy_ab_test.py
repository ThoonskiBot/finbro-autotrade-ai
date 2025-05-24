
import random

def pick_strategy_for_day():
    return random.choice(["StrategyA", "StrategyB"])

def record_winner(strategy, pnl_log):
    with open("ab_test_winners.txt", "a") as f:
        f.write(f"{strategy},{pnl_log}\n")
