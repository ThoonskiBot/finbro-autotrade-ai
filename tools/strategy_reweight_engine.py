
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.strategy_pnl_tracker import generate_strategy_pnl_summary

def get_strategy_weights():
    pnl = generate_strategy_pnl_summary()
    total = sum(abs(v) for v in pnl.values()) or 1
    weights = {k: round((abs(v) / total) * 100, 1) for k, v in pnl.items()}
    return weights

if __name__ == "__main__":
    weights = get_strategy_weights()
    for strat, weight in weights.items():
        print(f"{strat}: {weight}% weight")
