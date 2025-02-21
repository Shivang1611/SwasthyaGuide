import re
import requests
import streamlit as st
from utils.style_loader import load_css
from typing import Optional
import time

def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def send_email(user_email: str, query_message: str) -> bool:
    """
    Send email using Formspree.
    
    Args:
        user_email: User's email address
        query_message: Query content
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    FORMSPREE_URL = "https://formspree.io/f/mbldkzjl"
    
    try:
        response = requests.post(
            FORMSPREE_URL,
            data={
                "email": user_email,
                "message": query_message
            },
            timeout=10  # Add timeout
        )
        return response.status_code == 200
    except requests.RequestException as e:
        st.error(f"Network error: {str(e)}")
        return False

def Query() -> None:
    """Handle query form submission."""
    load_css()
    
    st.markdown("<h1 class='animated-text'>Send Query</h1>", 
                unsafe_allow_html=True)
    
    # Rate limiting check
    if 'last_submission' in st.session_state:
        time_diff = time.time() - st.session_state.last_submission
        if time_diff < 60:  # 1 minute cooldown
            st.warning(f"Please wait {60 - int(time_diff)} seconds before submitting again.")
            return
    
    with st.form(key='query_form'):
        user_email = st.text_input(
            "Your Email",
            key="query_email",
            help="Enter a valid email address"
        )
        
        query_message = st.text_area(
            "Your Query",
            key="query_message",
            help="Describe your query in detail"
        )
        
        submit_button = st.form_submit_button(
            "Send Query",
            help="Submit your query via email"
        )

        if submit_button:
            if not user_email or not query_message:
                st.warning("⚠️ Please fill in both fields.")
                return
                
            if not validate_email(user_email):
                st.error("⚠️ Please enter a valid email address.")
                return
                
            with st.spinner("Sending your query..."):
                success = send_email(user_email, query_message)
                
            if success:
                st.success("✅ Query sent successfully!")
                st.session_state.last_submission = time.time()
            else:
                st.error("❌ Failed to send query. Please try again later.")