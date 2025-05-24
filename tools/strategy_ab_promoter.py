
def pick_best_strategy(log_path="ab_test_winners.txt"):
    import csv
    from collections import Counter

    if not os.path.exists(log_path):
        return None

    with open(log_path, "r") as f:
        reader = csv.reader(f)
        winners = [row[0] for row in reader]

    count = Counter(winners)
    best = count.most_common(1)
    return best[0][0] if best else None
