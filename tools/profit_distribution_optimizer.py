# Phase 113 – Profit Distribution Optimizer

def distribute_profits(total_profit, allocations):
    total_weight = sum(allocations.values())
    return {k: round((v / total_weight) * total_profit, 2) for k, v in allocations.items()}