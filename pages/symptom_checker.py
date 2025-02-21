import streamlit as st
import numpy as np
import pandas as pd
from typing import Dict, List, Any
from utils.model_loader import load_models # This matches the function name
import time

from utils.style_loader import load_css


def symptom_checker(model=None, label_encoder=None, symptom_list=None):
    st.title("🔍 Symptom Checker")
    
    # Define default symptom list
    default_symptoms = [
        "Fever", "Cough", "Fatigue", "Difficulty Breathing", 
        "Body Ache", "Headache", "Sore Throat", "Nausea",
        "Diarrhea", "Loss of Taste/Smell", "Chest Pain",
        "Runny Nose", "Joint Pain", "Dizziness", "Vomiting"
    ]
    
    # Use default symptoms if no model is loaded
    symptoms_to_show = symptom_list if symptom_list else default_symptoms
    
    # Create two columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Select Your Symptoms")
        selected_symptoms = st.multiselect(
            "What symptoms are you experiencing?",
            options=symptoms_to_show,
            help="Select all symptoms that apply"
        )
        
        severity = st.slider(
            "Rate the severity of your symptoms",
            min_value=1,
            max_value=10,
            value=5,
            help="1 = Very Mild, 10 = Very Severe"
        )
        
        duration = st.number_input(
            "How many days have you had these symptoms?",
            min_value=0,
            max_value=30,
            value=1,
            help="Enter number of days"
        )
    
    with col2:
        st.markdown("### Additional Information")
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        
        # Additional risk factors
        st.markdown("### Risk Factors")
        smoking = st.checkbox("Smoking")
        diabetes = st.checkbox("Diabetes")
        heart_disease = st.checkbox("Heart Disease")
        hypertension = st.checkbox("Hypertension")
    
    # Check symptoms button
    if st.button("Check Symptoms", type="primary"):
        if not selected_symptoms:
            st.warning("Please select at least one symptom.")
            return
            
        # Show analysis results
        st.markdown("### Analysis Results")
        
        # Create progress bar for analysis
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.01)
        
        # Display results
        st.success("Analysis Complete!")
        
        # Show possible conditions
        st.markdown("### Possible Conditions")
        if len(selected_symptoms) > 0:
            conditions = get_possible_conditions(selected_symptoms)
            for condition, probability in conditions.items():
                st.write(f"- {condition}: {probability}%")
        
        # Recommendations
        st.markdown("### Recommendations")
        show_recommendations(selected_symptoms, severity)
        
        # Warning for severe symptoms
        if severity > 7 or any(s in selected_symptoms for s in ["Difficulty Breathing", "Chest Pain"]):
            st.error("""
                ⚠️ **Urgent Medical Attention Recommended**
                Some of your symptoms suggest a potentially serious condition. 
                Please seek immediate medical care.
            """)
        
        # General advice
        st.markdown("### General Advice")
        st.info("""
            👉 Monitor your symptoms closely
            👉 Stay hydrated and get plenty of rest
            👉 Follow up with your healthcare provider
            👉 Keep track of any new symptoms
        """)
        
        # Disclaimer
        st.warning("""
            ⚠️ **Medical Disclaimer**: This is not a substitute for professional medical advice. 
            If you're experiencing severe symptoms, please consult a healthcare provider immediately.
        """)

def get_possible_conditions(symptoms):
    """
    Return possible conditions based on symptoms.
    This is a simplified demo version.
    """
    conditions = {
        "Common Cold": 85,
        "Seasonal Allergies": 70,
        "Viral Infection": 65,
        "Flu": 60
    }
    return conditions

def show_recommendations(symptoms, severity):
    """
    Show recommendations based on symptoms and severity
    """
    recommendations = [
        "Rest and stay hydrated",
        "Monitor your symptoms",
        "Practice good hygiene",
        "Consider over-the-counter medications for symptom relief"
    ]
    
    if severity > 5:
        recommendations.append("Consider scheduling a medical appointment")
    
    if "Fever" in symptoms:
        recommendations.append("Take temperature regularly")
    
    if "Cough" in symptoms:
        recommendations.append("Use cough suppressants if needed")
    
    for rec in recommendations:
        st.write(f"✅ {rec}")