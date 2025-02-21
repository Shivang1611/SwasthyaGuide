import streamlit as st
import os
from pathlib import Path

def load_css() -> None:
    """Load and inject custom CSS styles"""
    try:
        # Get the absolute path to the static directory
        current_dir = Path(__file__).parent.parent
        css_file = current_dir /'static'/'styles.css'
        
        # Check if file exists
        if not css_file.exists():
            raise FileNotFoundError(f"CSS file not found at {css_file}")
            
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Warning: Could not load custom styles. Using default styles. Error: {str(e)}")