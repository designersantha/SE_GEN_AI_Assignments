import streamlit as st

st.title("Age Category Determiner")

def age_category(age: int) -> str:
    if age < 0:
        return "Invalid age"
    if age <= 12:
        return "Child"
    if age <= 19:
        return "Teenager"
    if age <= 59:
        return "Adult"
    return "Senior"

age = st.number_input("Enter an age to categorize:", min_value=0, step=1, format="%d")
if st.button("Categorize Age"):
    st.info(f"Age {age} ➜ **{age_category(age)}**")

st.subheader("Batch Categorization")
ages_line = st.text_area("Enter multiple ages separated by spaces:")
if st.button("Categorize List"):
    try:
        ages = [int(a) for a in ages_line.split()]
        results = [f"Age {a} ➜ {age_category(a)}" for a in ages]
        st.write("\n".join(results))
    except ValueError:
        st.error("Please enter valid integers separated by spaces.")
