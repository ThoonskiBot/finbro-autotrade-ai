# Phase 98 – GPT Coaching Loop

def generate_gpt_coaching_feedback(trade_log):
    import openai, os
    from dotenv import load_dotenv
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if not trade_log:
        return "⚠️ No trade log provided."

    prompt = (
        "You're a professional trading coach. Review this trade log and provide feedback "
        "on what worked, what didn't, and how the trader can improve tomorrow:\n\n"
        f"{trade_log}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT Error: {e}"