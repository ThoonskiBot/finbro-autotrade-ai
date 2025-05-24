import streamlit as st
import pandas as pd
import glob

st.title("📡 Live Signal Log Viewer")

signal_files = sorted(glob.glob("signals/*.csv"), reverse=True)
if signal_files:
    df = pd.read_csv(signal_files[0])
    st.dataframe(df)
    for sig in df['signal'].unique():
        st.subheader(f"🔍 {sig} signals")
        st.dataframe(df[df['signal'] == sig])
else:
    st.warning("No signal files found.")