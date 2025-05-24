"""
AB Strategy Tester - Compares multiple strategy versions and promotes the winner.
"""
import pandas as pd

def run_ab_test(strategy_logs):
    scores = {}
    for name, log in strategy_logs.items():
        df = pd.read_csv(log)
        total_pnl = df['PnL'].sum()
        win_rate = (df['PnL'] > 0).mean()
        scores[name] = total_pnl * win_rate
    winner = max(scores, key=scores.get)
    print(f"🏆 AB Test Winner: {winner}")
    return winner
