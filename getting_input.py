import pandas as pd
import streamlit as st

from datetime import datetime

st.set_page_config(page_title="My Streamlit App")

st.title("Welcome to Arya's App")

blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
min_date = datetime(1940, 1, 1)
max_date = datetime(2040, 12, 31)

name = st.text_input("Please Enter Your Name:")
phone = st.text_input("Please Enter Your Phone Number:")
dob = st.date_input("Enter your date of birth", min_value=min_date, max_value=max_date)
b_grp = st.selectbox("Select your blood group", blood_groups)
street = st.text_input("Street")
city = st.text_input("City")
state = st.text_input("State")
pin_code = st.text_input("Pin Code")


button_clicked = st.button("Submit")

if button_clicked:

    dict = {
        'Your Name Is': name,
        'Your Phone Number Is': phone,
        'Your DOB Is': dob,
        'Your Blood Group Is': b_grp,
        'Your Street is': street,
        'Your City is': city,
        'Your State is': state,
        'Your Pin Code is': pin_code
    }


    st.write(dict)
