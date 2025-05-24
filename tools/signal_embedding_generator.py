# Phase 85 – Signal Embedding for GPT Insight

def generate_signal_embedding(signal):
    import hashlib
    summary = f"{signal.get('ticker')}|{signal.get('strategy')}|{signal.get('score', 0)}"
    embedding = hashlib.sha256(summary.encode('utf-8')).hexdigest()
    return embedding