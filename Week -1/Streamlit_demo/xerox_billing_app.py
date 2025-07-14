import streamlit as st

st.title("🖨️ Xerox Shop Billing System")

# Services with their fixed prices
SERVICES = {
    "B/W Single Side Xerox - Rs.2": 2,
    "B/W Double Side Xerox - Rs.3": 3,
    "B/W ID Card Xerox - Rs.3": 3,
    "B/W A3 Single Side - Rs.7": 7,
    "B/W A3 Double Side - Rs.12": 12,
    "B/W A3 to A4 Single Side - Rs.5": 5
}

# Dropdown to select a service
selected_service = st.selectbox("Select Xerox Service", list(SERVICES.keys()))

# Quantity input
quantity = st.number_input("Enter quantity", min_value=0, step=1)

# Calculate total
if st.button("Calculate Bill"):
    price = SERVICES[selected_service]
    total = quantity * price

    st.subheader("🧾 Bill Summary")
    st.write(f"Selected Service: {selected_service}")
    st.write(f"Quantity: {quantity}")
    st.write(f"Unit Price: Rs.{price}")
    st.success(f"Total Amount: Rs.{total}")
