
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from tools.strategy_pnl_tracker import generate_strategy_pnl_summary
from core.config import OPENAI_API_KEY, REPORTS_PATH

def evaluate_strategy_with_gpt():
    try:
        import openai
        openai.api_key = OPENAI_API_KEY
    except ImportError:
        print("❌ OpenAI not installed.")
        return

    pnl = generate_strategy_pnl_summary()
    summary = f"📊 Strategy PnL Review ({datetime.now().strftime('%Y-%m-%d')}):\n"
    for strat, pnl_value in pnl.items():
        summary += f"- {strat}: {'+' if pnl_value >= 0 else ''}{pnl_value}\n"

    prompt = "Given the following strategy PnL performance, recommend which to scale up, pause, or tune:\n" + summary

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a trading coach analyzing strategy performance."},
                {"role": "user", "content": prompt}
            ]
        )
        advice = response['choices'][0]['message']['content']
    except Exception as e:
        advice = f"GPT error: {e}"

    out_path = os.path.join(REPORTS_PATH, f"strategy_eval_gpt_{datetime.now().strftime('%Y-%m-%d_%H%M')}.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(summary + "\n" + advice)

    print(f"✅ Strategy evaluation saved to: {out_path}")

if __name__ == "__main__":
    evaluate_strategy_with_gpt()
