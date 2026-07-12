import streamlit as st

# Regular Text Input
name = st.text_input(
    "Enter Your Name"
)

# Numbers only as Input
age = st.number_input(
    "Enter Age"
)

# Password Field
password = st.text_input(
    "Password",
    type="password"
)

# Text Area (Multi line Text Input to write feeback/suggestions etc)
feedback = st.text_area(
    "Enter Feedback"
)

# Buttons
if st.button("Submit"):
    st.write("Submitted Successfully")
    
# Select Box (Select any one of the dropdown box element)
city = st.selectbox(
    "Select City",
    ["New York", "Chicago", "Los Angeles"]
)

# Radio Buttons
gender = st.radio(
    "Gender",
    ["Male", "Female"]
)
# Checkboxes
agree = st.checkbox(
    "Accept Terms"
)

# Sliders (Slide the bar, you can see number changing)
salary = st.slider(
    "Salary",
    10000,
    100000
)

# Multiselect (Select multiple elements)
skills = st.multiselect(
    "Skills",
    ["Python", "SQL", "AI", "ML"]
)

# Date Input (Select Date from Date Selection Window)
joining_date = st.date_input(
    "Joining Date"
)
