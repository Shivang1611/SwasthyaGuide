import streamlit as st
import numpy as np
import pickle
import joblib
import pandas as pd
import requests 
import time
import sys
from typing import Dict, Any, Optional
from pathlib import Path
st.set_page_config(
    
    page_title="SwasthyaGuide",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/yourusername/your-repo',
        'Report a bug': "https://github.com/yourusername/your-repo/issues",
        'About': "# Multiple Disease Prediction System\n This is a comprehensive health prediction system."
    }
)

app_dir = Path(__file__).parent.parent
sys.path.append(str(app_dir))

# Import all pages
from pages.disease_prediction import disease_prediction
from pages.symptom_checker import symptom_checker
from pages.query import Query
from pages.report_upload import create_report_upload_page
from pages.about import about_page
from pages.first_aid import show_first_aid_page
from pages.suggesthospital import find_healthcare_providers
from pages.govt_schemes import show_govt_schemes


# Import utilities
from utils.style_loader import load_css
from utils.model_loader import load_models

# Page configuration



# Load CSS
load_css()

# Initialize session state for page management
if 'page' not in st.session_state:
    st.session_state.page = 'home'  # Set default page to home
if 'initialized' not in st.session_state:
    st.session_state.initialized = False



def reset_to_home():
    st.session_state.page = 'home'
    st.experimental_rerun()
    
    
# Initialize models with error handling
def load_all_models() -> None:
    """Initialize and load all required models and data"""
    try:
        if not st.session_state.initialized:
            with st.spinner("Loading models... Please wait."):
                models, label_encoder, symptom_list = load_models()
                if all([models, label_encoder, symptom_list]):
                    st.session_state.models = models
                    st.session_state.label_encoder = label_encoder
                    st.session_state.symptom_list = symptom_list
                    st.session_state.initialized = True
                else:
                    raise Exception("Failed to load one or more components")
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        st.session_state.initialized = False

# Sidebar configuration
def sidebar_menu():
    """Configure sidebar navigation"""
    with st.sidebar:
        st.markdown(""" <div class="sidebar-title"> 🏥 Menu </div> """, unsafe_allow_html=True)
        
        # Navigation buttons in a single column
        if st.button("🏠 Home", key='home', help="Go to Home page", use_container_width=True):
            st.session_state.page = "home"
        
        if st.button("🔍 Symptoms", key='symptoms', help="Check Symptoms", use_container_width=True):
            st.session_state.page = "symptoms"
        
        if st.button("📊 Reports", key='report', help="Disease Prediction by Report", use_container_width=True):
            st.session_state.page = "report"
        
        if st.button("📁 Upload", key='upload', help="Upload Medical Reports", use_container_width=True):
            st.session_state.page = "upload"
        
        if st.button("🚑 First Aid", key='firstaid', help="First Aid Guide", use_container_width=True):
            st.session_state.page = "firstaid"
        
        if st.button("❓ Query", key='query', help="Send Query", use_container_width=True):
            st.session_state.page = "query"
        
        
            
        if st.button("Suggest Hospitals", key='suggest', help="Suggest Hospitals", use_container_width=True):
            st.session_state.page = "suggest"
            
        if st.button("Govt Schemes", key='govt', help="Govt Schemes", use_container_width=True):
            st.session_state.page = "govt"
        if st.button("ℹ️ About", key='about', help="About Us", use_container_width=True):
            st.session_state.page = "about"
            
def home_content():
    # Hero Section
    st.markdown("""
        <div class="hero-section">
            <h1 class="animated-text">🏥 SwasthyaGuide</h1>
            <p class="hero-subtitle">Your Personal Health Assistant & Disease Prediction System</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Main Features Section
    st.markdown("## 🎯 Our Services")
    
    col1, col2,col3 = st.columns(3)
    
    
    with col1:
        st.markdown("""
            <div class="feature-card">
                <h3>🚑 Emergency Aid</h3>
                <p>
                    First aid guide  
                    Emergency procedure  
                    Quick response tip  
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Button inside the box
        if st.button("Get First Aid", key="first_aid"):
            st.session_state.page = "firstaid"  # Navigate to First Aid Page
            st.experimental_rerun()

    with col2:
            st.markdown("""
                <div class="feature-card">
                    <h3>💬 Health Assistant</h3>
                    <p>
                        24/7 chat support  
                        Health advice  
                        Medical guidance  
                    </p>
                </div>
            """, unsafe_allow_html=True)

            # Button inside the box 
            if st.button("Chat with Assistant", key="chat"):
                st.session_state.page = "query"
                st.experimental_rerun()
                

    # Button inside the box
    

        
    col4,col5 = st.columns(2)
    
    with col3:
        st.markdown("""
            
            <div class="feature-card">
                <h3>🔍 Disease Prediction</h3>
                <p>
                    Symptom-based analysis  
                    Medical report analysis 
                    Quick health assessment 
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Button inside the box
        if st.button("Predict Disease", key="predict"):
            st.session_state.page = "symptoms"
            st.experimental_rerun()
            

        
        
        
        
    with col4:
        st.markdown("""
            <div class="feature-card" style="background-color: white; border-radius: 15px; padding: 25px; margin: 15px 0; 
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center;">
                <h3 style="color: #1976d2;">Govt. Schemes</h3>
                <p>
                    Comprehensive health coverage<br>
                    Financial protection for families<br>
                    Access to quality healthcare services  
                </p>
                
            </div>
            
        """, unsafe_allow_html=True)

        if st.button("View Schemes", key="govt_schemes"):
            st.session_state.page = "govt"  # Set session state for navigation
            st.experimental_rerun()
        
    with col5:
        st.markdown("""
            <div class="feature-card" style="background-color: white; border-radius: 15px; padding: 25px; margin: 15px 0; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                <h3 style="color: #1976d2;">Suggest Hospitals</h3>
                <p>
                    Find nearby healthcare providers<br>
                    Locate hospitals and clinics<br>
                    Get medical assistance   
                </p>
            </div>
        """, unsafe_allow_html=True)

    # Add the button below the card content
         # Update the session state to navigate to the govt schemes page
        if st.button("Find Hospitals", key="find_hospitals"):
            st.session_state.page = "suggest"
            st.experimental_rerun()
    # How It Works Section
    st.markdown("## 🔄 How It Works")
    
    steps = {
        "1️⃣ Enter Information": "Add your symptoms or upload medical reports",
        "2️⃣ Get Analysis": "Our AI analyzes your health data",
        "3️⃣ Receive Results": "Get detailed health insights and recommendations",
        "4️⃣ Take Action": "Follow personalized health advice and recommendations"
    }
    
    for step, description in steps.items():
        st.markdown(f"""
            <div class="step-card">
                <h4>{step}</h4>
                <p>{description}</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Quick Access Section
   
            
            
def main():
    # Initialize session state
    """ i handles the page routing"""
    
    # Show sidebar
   
    
    # Display content based on current page
    try:
        # Show sidebar
        sidebar_menu()
        
        if st.session_state.page == "home":
            home_content()
            
        elif st.session_state.page == "symptoms":
            # Pass None for now, but this will work with the enhanced symptom checker
            symptom_checker()
        elif st.session_state.page == "report":
            disease_prediction()
            
        elif st.session_state.page == "upload":
            create_report_upload_page()
            
        elif st.session_state.page == "firstaid":
            show_first_aid_page()
            
        elif st.session_state.page == "query":
            Query()
            
        elif st.session_state.page == "about":
            
            about_page()
        elif st.session_state.page == "suggest":
            find_healthcare_providers()
        elif st.session_state.page == "govt":
            show_govt_schemes()
        
        
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        if st.button("Return to Home"):
            st.session_state.page = "home"
            st.experimental_rerun()

if __name__ == "__main__":
    main()