import streamlit as st

st.title("🛒 Simple Shopping Cart Demo")
st.write("This demo shows how to use Python lists in Streamlit to manage a shopping cart.")

# Initialize cart list in Streamlit session state
if "cart" not in st.session_state:
    st.session_state.cart = []

# Input for adding items
item_to_add = st.text_input("Add an item to the cart:")

if st.button("Add Item"):
    if item_to_add.strip():
        st.session_state.cart.append(item_to_add.strip())
        st.success(f"Added: {item_to_add}")
    else:
        st.warning("Please enter an item name.")

st.subheader("🛍️ Current Cart Items")
if st.session_state.cart:
    st.write(st.session_state.cart)
else:
    st.write("Your cart is empty.")

# Remove items
item_to_remove = st.selectbox(
    "Select an item to remove:", 
    st.session_state.cart if st.session_state.cart else ["(cart empty)"]
)

if st.button("Remove Item"):
    if st.session_state.cart:
        st.session_state.cart.remove(item_to_remove)
        st.success(f"Removed: {item_to_remove}")
    else:
        st.warning("No items to remove.")

# Clear cart
if st.button("Clear Cart"):
    st.session_state.cart.clear()
    st.success("Cart cleared!")
