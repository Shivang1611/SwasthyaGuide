import streamlit as st
import numpy as np
import pandas as pd
from typing import Dict, List, Any
from pages.suggesthospital import find_healthcare_providers
from utils.model_loader import load_models
import time

from utils.style_loader import load_css


def symptom_checker(model=None, label_encoder=None, symptom_list=None):
    st.title("🔍 Symptom Checker")
    st.markdown("---")  # Divider for better separation

    # Default symptoms
    default_symptoms = [
        "Fever", "Cough", "Fatigue", "Difficulty Breathing",
        "Body Ache", "Headache", "Sore Throat", "Nausea",
        "Diarrhea", "Loss of Taste/Smell", "Chest Pain",
        "Runny Nose", "Joint Pain", "Dizziness", "Vomiting"
    ]
    
    symptoms_to_show = symptom_list if symptom_list else default_symptoms

    # 🟢 Input Section (Organized into Two Columns)
    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.markdown("### Select Your Symptoms")
        selected_symptoms = st.multiselect(
            "What symptoms are you experiencing?",
            options=symptoms_to_show,
            help="Select all symptoms that apply",
        )

        severity = st.slider(
            "Rate the severity of your symptoms",
            min_value=1, max_value=10, value=5,
            help="1 = Very Mild, 10 = Very Severe"
        )

        duration = st.number_input(
            "How many days have you had these symptoms?",
            min_value=0, max_value=30, value=1,
            help="Enter number of days"
        )

    with col2:
        st.markdown("### Additional Information")
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

        # Risk Factors
        st.markdown("### Risk Factors")
        col_risk1, col_risk2 = st.columns(2)
        with col_risk1:
            smoking = st.checkbox("Smoking")
            diabetes = st.checkbox("Diabetes")
        with col_risk2:
            heart_disease = st.checkbox("Heart Disease")
            hypertension = st.checkbox("Hypertension")

    st.markdown("---")  # Divider

    # 🟢 Check Symptoms Button (with Centering)
    col_center = st.columns([1, 2, 1])  # Centering the button
    with col_center[1]:
        if st.button("🔍 Check Symptoms", type="primary"):
            if not selected_symptoms:
                st.warning("⚠️ Please select at least one symptom.")
                return

            # Show analysis results
            st.markdown("### 📊 Analysis Results")
            progress_bar = st.progress(0)
            for i in range(100):
                progress_bar.progress(i + 1)
                time.sleep(0.01)

            st.success("✅ Analysis Complete!")

            # Display Possible Conditions
            st.markdown("### Possible Conditions")
            conditions = get_possible_conditions(selected_symptoms)
            for condition, probability in conditions.items():
                st.write(f"- **{condition}**: {probability}%")

            # Show Recommendations
            st.markdown("---")  # Divider
            st.markdown("### 🏥 Recommendations")
            show_recommendations(selected_symptoms, severity)


# 🔹 Function to Simulate Possible Conditions
def get_possible_conditions(symptoms):
    conditions = {
        "Common Cold": 85,
        "Seasonal Allergies": 70,
        "Viral Infection": 65,
        "Flu": 60
    }
    return conditions


# 🔹 Initialize session state





# 🔹 Show Recommendations & Hospital Finder
def show_recommendations(symptoms, severity):
    recommendations = [
        "✅ Rest and stay hydrated",
        "✅ Monitor your symptoms",
        "✅ Practice good hygiene",
        "✅ Consider over-the-counter medications for symptom relief"
    ]

    if severity > 5:
        recommendations.append("⚠️ Consider scheduling a medical appointment")

    if "Fever" in symptoms:
        recommendations.append("🌡️ Take your temperature regularly")

    if "Cough" in symptoms:
        recommendations.append("💊 Use cough suppressants if needed")

    for rec in recommendations:
        st.write(rec)

    # Hospital Suggestion Button (Centered Inside the Box)
    if "show_hospitals" not in st.session_state:
        st.session_state.show_hospitals = False

# Hospital Suggestion Button (Centered Inside the Box)
    st.markdown("---")
    st.markdown("### 🏥 Need Medical Assistance?")

    if st.button("Find Hospitals", key="find_hospitals"):
            st.session_state.page = "sugges"
            st.experimental_rerun() # **Correct way to refresh the UI**

    # Check session state & call function **after rerun**
    if st.session_state.page == "sugges":
            find_healthcare_providers()  # **Thi
