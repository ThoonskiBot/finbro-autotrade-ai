# Phase 111 – Order Clustering Manager

def cluster_orders(orders):
    clusters = {}
    for order in orders:
        key = f"{order['ticker']}_{order['strategy']}"
        if key not in clusters:
            clusters[key] = []
        clusters[key].append(order)
    return clusters