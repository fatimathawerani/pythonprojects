import streamlit as st
import pandas as pd
import time

# ✅ Set page config at the very top
st.set_page_config(page_title="Enhanced Streamlit App", layout="wide")

# Custom Styles
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { background-color: #4CAF50; color: white; }
    </style>
""", unsafe_allow_html=True)

def main():
    # Sidebar Navigation
    with st.sidebar:
        st.header("Navigation")
        page = st.radio("Go to:", ["Home", "About"])
    
    if page == "Home":
        st.title("🚀 My Styled Streamlit Web App")

        # Text input
        name = st.text_input("Enter your name:")
        if name:
            st.success(f"Hello, {name}!")

        # Number input
        age = st.slider("Select your age:", 1, 100, 25)
        st.write(f"You are **{age} years old**!")

        # Progress Bar Simulation
        if st.button("Start Process"):
            with st.spinner("Processing..."):
                time


try:
    import streamlit as st
except ModuleNotFoundError:
    raise ImportError("The 'streamlit' module is not installed. Install it using 'pip install streamlit'.")

def main():
    st.title("My First Streamlit Web App")
    
    # Text input
    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}!")
    
    # Number input
    age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1)
    if age:
        st.write(f"You are {age} years old!")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file:
        st.write("File uploaded successfully!")
    
    # Button example
    if st.button("Click me"):
        st.success("Button clicked!")
    
if __name__ == "__main__":
    main()
