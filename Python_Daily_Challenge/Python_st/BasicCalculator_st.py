import streamlit as st

st.title("Basic Calculator")

a = st.number_input("Enter the first number:", value=0.0, format="%.4f")
b = st.number_input("Enter the second number:", value=0.0, format="%.4f")
operator = st.selectbox("Choose an operation:", ["+", "-", "*", "/"])

def calculate(x, y, op):
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    if op == "/":
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return x / y
    raise ValueError("Unsupported operation")

if st.button("Calculate"):
    try:
        result = calculate(a, b, operator)
        st.success(f"{a} {operator} {b} = {result}")
    except ZeroDivisionError as zde:
        st.error(str(zde))
    except Exception as e:
        st.error(f"Error: {e}")
