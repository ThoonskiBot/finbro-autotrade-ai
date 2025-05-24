# Phase 96 – Feature Evolution Optimizer

def track_feature_evolution(feature_logs):
    evolution = {}
    for day, features in feature_logs.items():
        for k, v in features.items():
            if k not in evolution:
                evolution[k] = []
            evolution[k].append(v)
    return evolution