import streamlit as st

st.title("Simple Password Validator")

MIN_LENGTH = 8
password = st.text_input("Enter a password:", type="password")

if st.button("Validate"):
    if len(password) >= MIN_LENGTH:
        st.success("Password accepted ✅")
    else:
        st.error(f"Password too short. Must be at least {MIN_LENGTH} characters long ❌")
