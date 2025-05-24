with open("logs/order_log_test_2025-05-26.txt") as f:
    lines = f.readlines()

skipped = [line for line in lines if "skipped" in line.lower()]
explanation = "🧠 Skipped Trade Analysis\n---\n" + "\n".join(skipped) if skipped else "No skipped trades today."

with open("reports/skipped_trade_gpt_explanation.txt", "w") as f:
    f.write(explanation)

print("✅ GPT skipped trade explanation saved.")