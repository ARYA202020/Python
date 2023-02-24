import streamlit as st

# Set page title
st.set_page_config(page_title="My Streamlit App")

# Add a title to the app
st.title("Welcome to my Streamlit App")

# Add a slider to the app
value = st.slider("Select a value", 0, 100)

# Display the value
st.write("You selected:", value)
