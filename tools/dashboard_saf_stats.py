import streamlit as st
import pandas as pd
data = {
    "Executed": 9,
    "Skipped": 3,
    "Win": 6,
    "Loss": 3
}
st.title("📊 SAF Statistics")
df = pd.DataFrame.from_dict(data, orient='index', columns=["Count"])
st.bar_chart(df)