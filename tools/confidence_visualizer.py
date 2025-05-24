# Phase 105 – Confidence Visualizer (matrix format)
def visualize_confidence_matrix(confidences):
    tickers = list(confidences.keys())
    output = "Confidence Matrix\n"
    output += "\n".join([f"{ticker}: {confidences[ticker]}" for ticker in tickers])
    return output