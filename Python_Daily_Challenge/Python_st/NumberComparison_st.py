import streamlit as st

st.title("Number Comparison")

a = st.number_input("Enter first number:", value=0.0, format="%f")
b = st.number_input("Enter second number:", value=0.0, format="%f")

if st.button("Compare"):
    if a > b:
        st.info(f"{a} is larger than {b}")
    elif a < b:
        st.info(f"{a} is smaller than {b}")
    else:
        st.success(f"{a} and {b} are equal")
