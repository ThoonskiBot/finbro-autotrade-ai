import streamlit as st

st.title("🕵️ Trade Replay Viewer")

try:
    with open("logs/order_log_test_2025-05-26.txt") as f:
        lines = f.readlines()
    index = st.slider("Scroll through trades", 0, len(lines)-1)
    st.code(lines[index])
except:
    st.warning("No valid trade log available.")