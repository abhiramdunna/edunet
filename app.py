# app.py
import streamlit as st
from chatbot import chatbot_response

# Set Streamlit page configuration
st.set_page_config(page_title="NLP Chatbot", layout="centered")

# App title
st.title("🤖 Simple NLP Chatbot")

# User input field
user_input = st.text_input("You:", placeholder="Type your message here...")

# Display the chatbot response
if st.button("Send"):
    if user_input.strip():
        response = chatbot_response(user_input)
        st.text_area("Chatbot:", response, height=100, max_chars=None)
    else:
        st.warning("Please enter a message.")
