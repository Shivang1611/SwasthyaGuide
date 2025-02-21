import streamlit as st
from utils.style_loader import load_css 

def about_page():
    load_css()
    st.markdown("<h1 class='animated-text'>ℹ️ About the Team</h1>", unsafe_allow_html=True)
                
                
                

    # Team and Background Details
    st.markdown("""
    Project on **SwasthyaGuide** using machine learning models.

    ### Team Members:
    - **<span class="hover-shadow">Nikhil Verma </span>**
    - **<span class="hover-shadow">Sukhwinder Singh</span>**
    - **<span class="hover-shadow">Aayush Singh</span>**
    - **<span class="hover-shadow">Shivang Shukla</span>**

    Together, we are working to harness the power of AI to predict health risks and provide valuable insights to users.
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Our Vision
    Our vision is to use cutting-edge machine learning techniques to predict health conditions, enabling early detection and intervention. We aim to make healthcare more accessible by leveraging technology for better outcomes.
    """, unsafe_allow_html=True)

    # Contact Information
    st.markdown("""
    ### Contact Information
    For any queries or feedback, feel free to reach out to us:

    - Email: [shivangshukla306@gmail.com](mailto:shivangshukla306@gmail.com)
    - GitHub: [Shivang1611](https://github.com/Shivang1611)
    """, unsafe_allow_html=True)

    # Add some styling
    
pass

    # ... rest of your about page code ...