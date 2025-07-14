import streamlit as st

st.title("Count Numbers")

numbers_line = st.text_area("Enter integers separated by spaces:")

if st.button("Count"):
    try:
        nums = [int(n) for n in numbers_line.split()]
        positives = sum(1 for n in nums if n > 0)
        negatives = sum(1 for n in nums if n < 0)
        zeros = sum(1 for n in nums if n == 0)

        st.write(f"**Positives:** {positives}")
        st.write(f"**Negatives:** {negatives}")
        st.write(f"**Zeros:** {zeros}")
    except ValueError:
        st.error("Please enter integers only, separated by spaces.")
