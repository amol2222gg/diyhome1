import streamlit as st
import google.generativeai as genai
import random
import traceback  # For debugging

# Configure Gemini API
GEMINI_API_KEY = "your_api_key_here"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# Sample DIY home improvement responses
diy_responses = {
    "painting": [
        "For painting walls, start by cleaning the surface and applying painter's tape to edges.",
        "Use a primer before applying paint for better coverage and durability.",
        "When painting, work from top to bottom and maintain a wet edge to avoid lap marks."
    ],
    "plumbing": [
        "Always turn off the water supply before starting any plumbing work.",
        "Use plumber's tape on threaded connections to prevent leaks.",
        "Keep a bucket handy when disconnecting pipes to catch residual water."
    ],
    "flooring": [
        "Acclimate wood flooring in your home for at least 72 hours before installation.",
        "Start laying tiles from the center of the room and work outward for the best appearance.",
        "Use spacers between tiles to ensure even grout lines."
    ],
    "electrical": [
        "Always turn off power at the breaker before working on electrical projects.",
        "Use a voltage tester to confirm power is off before touching any wires.",
        "Follow local electrical codes when installing new fixtures or outlets."
    ],
    "default": [
        "What DIY project are you working on? I can help with painting, plumbing, flooring, or electrical work.",
        "Try asking about specific home improvement tasks like wall painting or fixing a leaky faucet.",
        "I can provide step-by-step instructions for many home improvement projects. What are you interested in?"
    ]
}

def get_gemini_response(prompt):
    """Get response from Gemini API using the official client library."""
    try:
        # Create a model instance
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Generate content
        response = model.generate_content(prompt)
        
        return response.text
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return "Sorry, I couldn't process your request at the moment."

# Streamlit UI
st.title("DIY Home Improvement Guide 🏠")

st.write("Hello! I'm your DIY assistant. Ask me about painting, plumbing, flooring, or electrical projects!")

# User Input
user_input = st.text_input("Ask about a DIY project...")

if st.button("Send"):
    if user_input:
        response = get_gemini_response(user_input)
        st.write("### Response:")
        st.write(response)
    else:
        st.warning("Please enter a question.")
