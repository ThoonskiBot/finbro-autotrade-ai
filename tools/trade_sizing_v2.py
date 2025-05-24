
def get_dynamic_position_size(base_size, win_streak=0, volatility=1.0):
    multiplier = 1.0
    if win_streak >= 3:
        multiplier += 0.25
    if win_streak <= -2:
        multiplier -= 0.25
    if volatility > 2.0:
        multiplier -= 0.25
    return max(1, int(base_size * multiplier))
