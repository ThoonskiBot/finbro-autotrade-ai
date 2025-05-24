# Phase 81 – Feature Correlation Tracker
def correlate_features(signals):
    from pandas import DataFrame
    if not signals:
        return "⚠️ No signals provided."
    df = DataFrame(signals)
    corr = df.corr(numeric_only=True)
    return corr.to_string()