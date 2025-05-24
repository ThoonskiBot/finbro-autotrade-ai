import matplotlib.pyplot as plt

strategies = ["StrategyA", "StrategyB", "StrategyC"]
roi = [0.12, 0.08, 0.15]

plt.bar(strategies, roi)
plt.title("Strategy ROI Comparison")
plt.ylabel("ROI")
plt.savefig("reports/strategy_roi_chart.png")
print("✅ Strategy ROI chart saved to reports/strategy_roi_chart.png")