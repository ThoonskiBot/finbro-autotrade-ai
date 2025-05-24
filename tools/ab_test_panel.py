import streamlit as st
import pandas as pd

st.title("🧪 A/B Strategy Tester")

df = pd.read_csv("logs/pnl_log_sample.txt", sep="|", header=None, names=["Strategy", "Ticker", "Result"])
pivot = df.pivot_table(index="Strategy", columns="Result", aggfunc="size", fill_value=0)

st.subheader("📈 Performance Breakdown")
st.dataframe(pivot)

st.subheader("🏆 Top Strategy")
if not pivot.empty:
    win_rates = pivot["win"] / (pivot["win"] + pivot["loss"])
    top_strategy = win_rates.idxmax()
    st.success(f"🔥 {top_strategy} has the highest win rate: {win_rates[top_strategy]*100:.2f}%")