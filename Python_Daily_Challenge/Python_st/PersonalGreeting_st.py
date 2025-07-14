import streamlit as st

st.title("Personal Greeting")

name = st.text_input("👋 What's your name?")
age = st.number_input("🎂 How old are you?", min_value=0, step=1, format="%d")
color = st.text_input("🎨 What's your favorite color?")

if st.button("Generate Greeting"):
    if name and color:
        st.success(
            f"Hi {name}! At {int(age)} years young, your love for {color} shows you have a vibrant personality. "
            "Wishing you a colorful day ahead! 😊"
        )
    else:
        st.warning("Please enter both your name and favorite color.")
