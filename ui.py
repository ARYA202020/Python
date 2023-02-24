import streamlit as st
from datetime import datetime
# Set page title
st.set_page_config(page_title="My Streamlit App")

# Add a title to the app
st.title("Welcome to my Streamlit App")

blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

# Add a text box to the app
user_input = st.text_input("Please Enter Your Name:")
user_input = st.text_input("Please Enter Your Phone Number:")
dob = st.date_input("Enter your date of birth", datetime.today())
selected_bg = st.selectbox("Select your blood group", blood_groups)


# Add a button to the app
button_clicked = st.button("Submit")

# Display a message if the button is clicked
if button_clicked:
    st.write(f"Hello, {user_input}!")
    st.write(f"Phone number is  {user_input}!")
    st.write(f"Your date of birth is: {dob}")
    st.write("Your selected blood group is:", selected_bg)