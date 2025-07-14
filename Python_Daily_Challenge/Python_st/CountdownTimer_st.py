import streamlit as st
import time

st.title("Countdown Timer")

start_count = st.number_input("Start countdown from:", min_value=1, max_value=100, step=1, value=10, format="%d")

if st.button("Start Countdown"):
    placeholder = st.empty()
    for i in range(int(start_count), -1, -1):
        placeholder.markdown(f"<h2 style='text-align:center'>{i}</h2>", unsafe_allow_html=True)
        time.sleep(1)
    placeholder.markdown("<h2 style='text-align:center'>Blast off! 🚀</h2>", unsafe_allow_html=True)
