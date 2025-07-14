import streamlit as st

st.title("Grade Average Calculator")

PASS_MARK = 50
scores = []
with st.form("score_form"):
    for i in range(1, 6):
        score = st.number_input(f"Enter score {i}:", min_value=0.0, max_value=100.0, step=0.1, format="%.1f", key=f"score_{i}")
        scores.append(score)
    submitted = st.form_submit_button("Calculate")

if submitted:
    average = sum(scores) / len(scores)
    status = "PASS ✅" if average >= PASS_MARK else "FAIL ❌"

    st.write(f"**Average score:** {average:.2f}")
    st.success(f"Result: {status}")
