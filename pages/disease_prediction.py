import streamlit as st
import numpy as np
from typing import Dict, Any
from utils.model_loader import load_models  # Updated import

from utils.style_loader import load_css

def disease_prediction():
    load_css()
    st.markdown("<h1 class='animated-text'>🔍 Disease Prediction By Report</h1>", 
                unsafe_allow_html=True)
    
    # Rest of your code...

def disease_prediction():
    load_css()
    st.markdown("<h1 class='animated-text'>🔍 Disease Prediction By Report</h1>", unsafe_allow_html=True)
    
    disease = st.selectbox("Select Disease", ["Heart Disease", "Parkinson's Disease", "Diabetes"])
    
    if disease == "Heart Disease":
        predict_heart_disease()
    elif disease == "Parkinson's Disease":
        predict_parkinsons()
    elif disease == "Diabetes":
        predict_diabetes()

def predict_heart_disease():
    # Your heart disease prediction code...
        st.subheader("Heart Disease Prediction")
        age = st.number_input("Age", min_value=1)
        sex = st.selectbox("Sex", ["Female", "Male"])
        cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)
        trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200)
        chol = st.number_input("Serum Cholesterol", min_value=100, max_value=600)
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
        restecg = st.number_input("Resting ECG (0-2)", min_value=0, max_value=2)
        thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220)
        exang = st.selectbox("Exercise Induced Angina", [0, 1])
        oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=6.0)
        slope = st.number_input("Slope of the Peak Exercise ST Segment", min_value=0, max_value=2)
        ca = st.number_input("Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4)
        thal = st.selectbox("Thalassemia (1-3)", [1, 2, 3])

        if st.button("Predict Heart Disease"):
            if age == 1 or trestbps == 80 or chol == 100 or thalach == 60:
                st.warning("⚠️ Please enter all required values before predicting.")
            else:
                try:
                    input_data = np.array([[age, 1 if sex == "Male" else 0, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
                    prediction = models["heart"].predict(input_data)
                    result = "Has Heart Disease. Consult a doctor!" if prediction[0] == 1 else "No Heart Disease detected."
                    st.success(result)
                    # Show hospital suggestion button only if disease is detected
                    if prediction[0] == 1:
                        st.markdown("---")
                        st.markdown("### Need help finding medical care?")
                        if st.button("🏥 Find Nearby Hospitals", key="heart_hospitals"):
                            st.session_state.show_hospital_search = True

                except ValueError:
                    st.error("You entered the wrong input, please enter the correct input.")
    
                pass

def predict_parkinsons():
    # Your Parkinson's prediction code...
        st.subheader("Parkinson's Disease Prediction")

        age = st.number_input("Age", min_value=0, step=1)
        gender = st.selectbox("Gender", ["Male", "Female"])  # Convert to binary later
        ethnicity = st.number_input("Ethnicity", min_value=0, step=1)
        bmi = st.number_input("BMI", min_value=0.0, format="%f")
        smoking = st.number_input("Smoking", min_value=0, step=1)
        alcohol = st.number_input("Alcohol Consumption", min_value=0.0, format="%f")
        physical_activity = st.number_input("Physical Activity", min_value=0.0, format="%f")
        diet_quality = st.number_input("Diet Quality", min_value=0.0, format="%f")
        sleep_quality = st.number_input("Sleep Quality", min_value=0.0, format="%f")
        family_history = st.number_input("Family History of Parkinson's", min_value=0, step=1)
        brain_injury = st.number_input("Traumatic Brain Injury", min_value=0, step=1)
        diabetes = st.number_input("Diabetes", min_value=0, step=1)
        depression = st.number_input("Depression", min_value=0, step=1)
        stroke = st.number_input("Stroke", min_value=0, step=1)
        systolic_bp = st.number_input("Systolic Blood Pressure", min_value=0, step=1)
        diastolic_bp = st.number_input("Diastolic Blood Pressure", min_value=0, step=1)
        cholesterol = st.number_input("Cholesterol Total", min_value=0.0, format="%f")
        tremor = st.number_input("Tremor", min_value=0, step=1)
        rigidity = st.number_input("Rigidity", min_value=0, step=1)
        bradykinesia = st.number_input("Bradykinesia", min_value=0, step=1)
        postural_instability = st.number_input("Postural Instability", min_value=0, step=1)
        speech_problems = st.number_input("Speech Problems", min_value=0, step=1)
        sleep_disorders = st.number_input("Sleep Disorders", min_value=0, step=1)
        constipation = st.number_input("Constipation", min_value=0, step=1)
        
        gender_binary = 1 if gender == "Male" else 0

        if st.button("Predict Parkinson's Disease"):
            if age == 0 or bmi == 0.0 or sleep_quality == 0.0 or cholesterol == 0.0:
                st.warning("⚠️ Please provide all necessary inputs before predicting.")
            else:
                try:
                    input_data = np.array([[age, gender_binary, ethnicity, bmi, smoking, alcohol, physical_activity, diet_quality, 
                                            sleep_quality, family_history, brain_injury, diabetes, depression, stroke, systolic_bp, 
                                            diastolic_bp, cholesterol, tremor, rigidity, bradykinesia, postural_instability, 
                                            speech_problems, sleep_disorders, constipation]])
                    prediction = models["parkinsons"].predict(input_data)
                    result = "Parkinson's Detected. Consult a specialist!" if prediction[0] == 1 else "No Parkinson's detected."
                    st.success(result)
                    # Show hospital suggestion button only if disease is detected
                    if prediction[0] == 1:
                        st.markdown("---")
                        st.markdown("### Need help finding medical care?")
                        if st.button("🏥 Find Nearby Hospitals", key="heart_hospitals"):
                            st.session_state.show_hospital_search = True

                    
                except ValueError:
                    st.error("You entered the wrong input, please enter the correct input.")

def predict_diabetes():
    # Your diabetes prediction code...
        st.subheader("Diabetes Prediction")
        sex = st.selectbox("Sex", ["Female", "Male"])
        
        pregnancies = 0 if sex == "Male" else st.number_input("Number of Pregnancies", min_value=0)
        glucose = st.number_input("Glucose Level", min_value=0)
        blood_pressure = st.number_input("Blood Pressure Level", min_value=0)
        skin_thickness = st.number_input("Skin Thickness", min_value=0)
        insulin = st.number_input("Insulin Level", min_value=0)
        bmi = st.number_input("BMI", min_value=0.0)
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
        age = st.number_input("Age", min_value=0)

        if st.button("Predict Diabetes"):
            if glucose == 0 or blood_pressure == 0 or bmi == 0.0 or age == 0:
                st.warning("⚠️ Please fill in all required fields before predicting.")
            else:
                try:
                    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
                    prediction = models["diabetes_best"].predict(input_data)
                    result = "Positive for Diabetes. Consult a doctor!" if prediction[0] == 1 else "No Diabetes detected."
                    st.success(result)
                    if 'show_hospitals' not in st.session_state:
                        st.session_state.show_hospitals = False

# After disease prediction (in each disease section):
                    if prediction[0] == 1:  # If disease is detected
                        st.markdown("---")
                        st.markdown("### Need help finding medical care?")
                        if st.button("🏥 Find Nearby Hospitals", key="unique_key_for_disease"):
                            st.session_state.show_hospitals = True

                    # Show hospital search if button was clicked
                    if st.session_state.show_hospitals:
                        suggest_hospitals()
                except ValueError:
                    st.error("You entered the wrong input, please enter the correct input.")
                pass