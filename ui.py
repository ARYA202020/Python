import streamlit as st

# Set page title
st.set_page_config(page_title="My Streamlit App")

# Add a title to the app
st.title("Welcome to my Streamlit App")

# Add a text box to the app
user_input = st.text_input("Enter your name:")
user_input = st.text_input("Please Enter Your Phone Number:")

# Add a button to the app
button_clicked = st.button("Submit")

# Display a message if the button is clicked
if button_clicked:
    st.write(f"Hello, {user_input}!")
    st.write(f"Phone number is  {user_input}!")
