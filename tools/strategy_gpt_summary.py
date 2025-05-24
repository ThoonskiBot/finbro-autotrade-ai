
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from core.config import REPORTS_PATH, OPENAI_API_KEY
from tools.strategy_pnl_tracker import generate_strategy_pnl_summary

def generate_strategy_gpt_summary():
    try:
        import openai
        openai.api_key = OPENAI_API_KEY
    except ImportError:
        print("❌ OpenAI module not found.")
        return

    pnl = generate_strategy_pnl_summary()
    summary = f"📊 Strategy PnL Summary for {datetime.now().strftime('%Y-%m-%d')}\n"
    for strat, profit in pnl.items():
        summary += f"- {strat}: {'+' if profit >= 0 else ''}{profit}\n"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial analyst reviewing trading strategies."},
                {"role": "user", "content": summary}
            ]
        )
        gpt_output = response['choices'][0]['message']['content']
    except Exception as e:
        gpt_output = f"GPT error: {e}"

    out_path = os.path.join(REPORTS_PATH, f"strategy_gpt_summary_{datetime.now().strftime('%Y-%m-%d_%H%M')}.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(summary + "\n" + gpt_output)

    print(f"✅ Strategy GPT summary saved to: {out_path}")

if __name__ == "__main__":
    generate_strategy_gpt_summary()
