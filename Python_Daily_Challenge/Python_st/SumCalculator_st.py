import streamlit as st

st.title("Sum Calculator (1 to n)")

n = st.number_input("Enter a positive integer n:", min_value=1, step=1, format="%d")

if st.button("Calculate Sum"):
    total = sum(range(1, n + 1))
    st.success(f"The sum of numbers from 1 to {n} is {total}")
