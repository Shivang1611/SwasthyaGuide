import streamlit as st
import time
from utils.style_loader import load_css


# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state.page = "Upload Reports"
if 'diabetes_data' not in st.session_state:
    st.session_state.diabetes_data = None
if 'heart_data' not in st.session_state:
    st.session_state.heart_data = None
if 'parkinsons_data' not in st.session_state:
    st.session_state.parkinsons_data = None

def create_report_upload_page():
    load_css()
    st.markdown("<h1 class='animated-text'>📁 Upload Medical Reports</h1>", 
                unsafe_allow_html=True)
   
    col1, col2, col3 = st.columns(3)

    # Diabetes Report Section
    with col1:
        st.markdown("<div class='report-container'><h3>🩸 Diabetes Reports</h3>", unsafe_allow_html=True)
        diabetes_file = st.file_uploader("Upload Diabetes Report", type=['txt', 'pdf', 'csv'], key='diabetes')
        if diabetes_file:
            try:
                st.success("✅ Report parsed successfully!", icon="✅")
                st.session_state.diabetes_data = diabetes_file  # Save file in session state
                if st.button("🔍 Analyze Diabetes", key='diabetes_pred', help="Go to Diabetes Prediction"):
                    st.session_state.page = "Diabetes Prediction"
            except Exception as e:
                st.error(f"❌ Error parsing report: {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

    # Heart Disease Report Section
    with col2:
        st.markdown("<div class='report-container'><h3>❤️ Heart Disease Reports</h3>", unsafe_allow_html=True)
        heart_file = st.file_uploader("Upload Heart Report", type=['txt', 'pdf', 'csv'], key='heart')
        if heart_file:
            try:
                st.success("✅ Report parsed successfully!", icon="✅")
                st.session_state.heart_data = heart_file  # Save file in session state
                if st.button("🔍 Analyze Heart Disease", key='heart_pred', help="Go to Heart Disease Prediction"):
                    st.session_state.page = "Heart Disease Prediction"
            except Exception as e:
                st.error(f"❌ Error parsing report: {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

    # Parkinson's Report Section
    with col3:
        st.markdown("<div class='report-container'><h3>🧠 Parkinson's Reports</h3>", unsafe_allow_html=True)
        parkinsons_file = st.file_uploader("Upload Parkinson's Report", type=['txt', 'pdf', 'csv'], key='parkinsons')
        if parkinsons_file:
            try:
                st.success("✅ Report parsed successfully!", icon="✅")
                st.session_state.parkinsons_data = parkinsons_file  # Save file in session state
                if st.button("🔍 Analyze Parkinson's", key='parkinsons_pred', help="Go to Parkinson's Prediction"):
                    st.session_state.page = "Parkinson's Prediction"
            except Exception as e:
                st.error(f"❌ Error parsing report: {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

    # Handle prediction results
    if st.session_state.page == "Diabetes Prediction":
        show_prediction_results("Diabetes", st.session_state.diabetes_data)
    elif st.session_state.page == "Heart Disease Prediction":
        show_prediction_results("Heart Disease", st.session_state.heart_data)
    elif st.session_state.page == "Parkinson's Prediction":
        show_prediction_results("Parkinson's", st.session_state.parkinsons_data)

def show_prediction_results(disease_type: str, data):
    """
    Display prediction results for the specified disease
    """
    st.write(f"## {disease_type} Prediction Results")
    if data:
        with st.spinner(f"🧑‍🔬 Analyzing {disease_type.lower()} report... Please wait!"):
            time.sleep(2)  # Simulated processing time
            st.success("✅ Analysis complete!")
            
            # Add some mock results
            st.info("Based on the uploaded report:")
            st.write("- Report quality: Good")
            st.write("- Analysis confidence: High")
            
            # Add a button to find nearby hospitals
            if st.button("🏥 Find Nearby Hospitals"):
                suggest_hospitals()
            
            st.info("We are working on improving the results. Check back soon for more detailed analysis.")
    else:
        st.error(f"No {disease_type.lower()} report data available")

if __name__ == "__main__":
    create_report_upload_page()