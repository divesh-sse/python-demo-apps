import streamlit as st

st.title("🎧 Student Music Interest Analyzer")
st.write("This app demonstrates Python SETS using music preferences")

# ------------------------------------
# INPUT FROM STUDENTS
# ------------------------------------

st.header("🎵 Enter Music Genres")

genres1 = st.text_input(
    "Student 1 - Enter genres (comma separated)",
    "Rock, Pop, Jazz, Hip Hop"
)

genres2 = st.text_input(
    "Student 2 - Enter genres (comma separated)",
    "Pop, Classical, Jazz, EDM"
)

# ------------------------------------
# CONVERT INPUT TO SETS
# ------------------------------------

student1 = set(genres1.split(","))
student2 = set(genres2.split(","))

# Remove extra spaces
student1 = {g.strip() for g in student1}
student2 = {g.strip() for g in student2}

# ------------------------------------
# DISPLAY SETS
# ------------------------------------

st.subheader("🎧 Student Sets (Unique Genres Only)")
st.write("Student 1 Genres:", student1)
st.write("Student 2 Genres:", student2)

# ------------------------------------
# SET OPERATIONS
# ------------------------------------

st.header("🔍 Set Operations Results")

common = student1 & student2
all_genres = student1 | student2
only_student1 = student1 - student2
only_student2 = student2 - student1

st.write("🤝 Common Genres:", common)
st.write("🌍 All Unique Genres:", all_genres)
st.write("🎯 Only Student 1 Likes:", only_student1)
st.write("🎯 Only Student 2 Likes:", only_student2)

st.success("✅ SET concepts demonstrated successfully!")
