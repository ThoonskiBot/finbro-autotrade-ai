
def taper_strategy_weight(alpha_dict, base_weight=100):
    adjusted = {}
    for strat, alpha in alpha_dict.items():
        if alpha < 0:
            adjusted[strat] = int(base_weight * 0.75)
        elif alpha == 0:
            adjusted[strat] = base_weight
        else:
            adjusted[strat] = int(base_weight * 1.1)
    return adjusted
