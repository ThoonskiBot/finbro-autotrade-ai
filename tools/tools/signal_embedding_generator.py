# Phase 85 – Signal Embedding for GPT Insight
def generate_signal_embedding(signal):
    import hashlib
    summary = f"{signal['ticker']}|{signal['strategy']}|{signal.get('score', 0)}"
    embedding = hashlib.sha256(summary.encode()).hexdigest()
    return embedding