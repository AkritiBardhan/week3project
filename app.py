import streamlit as st
from datetime import datetime

# Set page background color
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to right,#FC5C7D,#6A82FB);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Container with background color black and smooth edges
container_style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=DynaPuff:wght@400..700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Playwrite+NZ:wght@100..400&display=swap');

    h2 {
    font-family: "DynaPuff", system-ui;
        color: orange;
        font-weight: bold;
        text-shadow: 2px 2px 2px black;
        font-size: 40px;
    }
    .stTextInput label {
        color: yellow !important;
        font-family: "Playwrite NZ", cursive;
        font-weight: bold;
    }
    .stDateInput label {
        color: yellow !important;
        font-weight: bold;
    }
    .stTimeInput label {
        color: yellow !important;
        font-weight: bold;
        font-size: 30px;
    }
    .container input[type="submit"] {
        background-color: orange;
        width: 100px;
        height: 50px;
        border: none;
        border-radius: 5px;
        color: white;
        font-weight: bold;
    }
</style>
<div class="container">
"""
st.markdown(container_style, unsafe_allow_html=True)

# Actual email and password
actual_email = "ak@gmail.com"
actual_pass = "ak123"

# Form inputs
st.markdown('<h2>Student Admission Form</h2>', unsafe_allow_html=True)
email = st.text_input("Email")
password = st.text_input("Password", type="password")
date_of_admission = st.date_input("Date of Admission")
current_time = st.time_input("Current Time")

# Submit button
submitted = st.button("Submit")

# Form submission logic
if submitted:
    if email == actual_email and password == actual_pass:
        st.success("Login successfully")
    else:
        st.error("Username or password is not correct")

# End the container
st.markdown("</div>", unsafe_allow_html=True)