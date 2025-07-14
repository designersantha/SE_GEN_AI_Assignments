import streamlit as st

st.title("Shopping Bill Calculator")

prices = [st.number_input(f"Price for item {i + 1} (Rs):", min_value=0.0, step=0.1, format="%.2f") for i in range(3)]
tax_pct = st.number_input("Tax percentage (%):", min_value=0.0, step=0.1, format="%.2f")

if st.button("Calculate Total"):
    subtotal = sum(prices)
    tax_amount = subtotal * tax_pct / 100
    total = subtotal + tax_amount

    st.write(f"**Subtotal:** Rs.{subtotal:.2f}")
    st.write(f"**Tax ({tax_pct}%):** Rs.{tax_amount:.2f}")
    st.success(f"**Total:** Rs.{total:.2f}")
