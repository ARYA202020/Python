import streamlit as st

from datetime import datetime

st.set_page_config(page_title="My Streamlit App")

st.title("Welcome to my Streamlit App")

blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

name = st.text_input("Please Enter Your Name:")
phone = st.text_input("Please Enter Your Phone Number:")
dob = st.date_input("Enter your date of birth", datetime.today())
b_grp = st.selectbox("Select your blood group", blood_groups)


button_clicked = st.button("Submit")

if button_clicked:

    dict = {
        'Your Name Is': name,
        'Your Phone Number Is': phone,
        'Your DOB Is': dob,
        'Your Blood Group Is': b_grp
    }
    st.write(dict)

