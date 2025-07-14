import streamlit as st

st.title("Even or Odd Checker")

number = st.number_input("Enter a number to check if it's Even or Odd:", step=1, format="%d")
if st.button("Check Single Number"):
    result = "Even" if number % 2 == 0 else "Odd"
    st.info(f"{int(number)} is **{result}**")

st.subheader("Batch Check")
numbers_line = st.text_area("Enter multiple integers separated by spaces:")
if st.button("Check List"):
    try:
        nums = [int(n) for n in numbers_line.split()]
        results = [f"{n} ➜ {'Even' if n % 2 == 0 else 'Odd'}" for n in nums]
        st.write("\n".join(results))
    except ValueError:
        st.error("Please enter integers only, separated by spaces.")
