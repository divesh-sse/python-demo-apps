import streamlit as st

st.title("🎬 Simple Movie Booking System")
st.write("This app demonstrates the use of Python Tuples")

# ------------------------------------
# FIXED DATA USING TUPLES
# ------------------------------------

movies = ("Avengers", "Inception", "Interstellar", "Jawan")
seats = ("A1", "A2", "A3", "A4", "A5")

# ------------------------------------
# DISPLAY AVAILABLE OPTIONS
# ------------------------------------

st.subheader("🎥 Available Movies")
st.write(movies)

st.subheader("💺 Available Seats")
st.write(seats)

# ------------------------------------
# USER INPUT
# ------------------------------------

movie_choice = st.text_input("Which movie do you want to watch?")
seat_choice = st.text_input("Choose your seat")

# ------------------------------------
# BOOKING LOGIC
# ------------------------------------

if st.button("Book Ticket"):
    if movie_choice in movies:
        if seat_choice in seats:
            st.success("✅ Booking Confirmed!")
            st.write("🎬 Movie:", movie_choice)
            st.write("💺 Seat:", seat_choice)
        else:
            st.error("❌ Invalid seat number")
    else:
        st.error("❌ Movie not available")
