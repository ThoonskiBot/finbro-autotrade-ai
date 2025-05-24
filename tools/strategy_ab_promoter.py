
import os
import csv
from collections import Counter

def pick_best_strategy(log_path="ab_test_winners.txt"):
    if not os.path.exists(log_path):
        print("❌ No AB test log found.")
        return None

    with open(log_path, "r") as f:
        reader = csv.reader(f)
        winners = [row[0] for row in reader if row]

    if not winners:
        print("❌ No strategy records found in AB test log.")
        return None

    count = Counter(winners)
    best = count.most_common(1)
    print(f"🏆 Most Successful Strategy: {best[0][0]} with {best[0][1]} wins")
    return best[0][0]

if __name__ == "__main__":
    pick_best_strategy()
