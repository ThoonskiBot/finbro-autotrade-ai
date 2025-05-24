# Phase 95 – GPT-Based Signal Arbitration
def arbitrate_signals(signals):
    import openai, os
    from dotenv import load_dotenv
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = "Given these signals, decide which one(s) should be executed:\n\n"
    for s in signals:
        prompt += f"- {s.get('ticker')} ({s.get('strategy')}): {s.get('summary', 'no summary')}\n"
    prompt += "\nSelect the best signal(s) based on clarity and alignment."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT Error: {e}"