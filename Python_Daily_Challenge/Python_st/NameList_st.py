import streamlit as st

st.title("Name List with Lengths")

names = []
with st.form("name_form"):
    for i in range(1, 6):
        name = st.text_input(f"Enter name {i}:", key=f"name_{i}")
        names.append(name)
    submitted = st.form_submit_button("Submit")

if submitted:
    if all(names):
        for name in names:
            st.write(f"{name} ({len(name)} characters)")
    else:
        st.warning("Please fill in all 5 names.")
