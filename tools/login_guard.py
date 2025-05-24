import streamlit as st
import json

with open("config/login_config.json") as f:
    cfg = json.load(f)

username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    if username == cfg["username"] and password == cfg["password"]:
        st.success("✅ Access granted")
    else:
        st.error("❌ Access denied")