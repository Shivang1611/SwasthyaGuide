import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Calorie Calculator", layout="wide")

def calculate_bmr(weight, height, age, gender):
    """
    Calculate BMR using the Mifflin-St Jeor Equation
    """
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return round(bmr)

def calculate_tdee(bmr, activity_level):
    """
    Calculate Total Daily Energy Expenditure based on activity level
    """
    activity_multipliers = {
        "Sedentary (little or no exercise)": 1.2,
        "Lightly active (light exercise 1-3 days/week)": 1.375,
        "Moderately active (moderate exercise 3-5 days/week)": 1.55,
        "Very active (hard exercise 6-7 days/week)": 1.725,
        "Super active (very hard exercise & physical job)": 1.9
    }
    tdee = bmr * activity_multipliers[activity_level]
    return round(tdee)

# App title and description
st.title("🔢 Calorie Calculator")
st.markdown("""
This calculator helps you determine your:
- Basal Metabolic Rate (BMR)
- Total Daily Energy Expenditure (TDEE)
- Calorie needs for different goals
""")

# Create two columns for input and results
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Enter Your Details")
    
    # Personal Information
    gender = st.radio("Gender", ["Male", "Female"])
    age = st.number_input("Age (years)", min_value=15, max_value=100, value=30)
    
    # Weight input with unit selection
    weight_unit = st.selectbox("Weight Unit", ["Kilograms", "Pounds"])
    if weight_unit == "Kilograms":
        weight = st.number_input("Weight", min_value=30, max_value=200, value=70)
    else:
        weight_lbs = st.number_input("Weight", min_value=66, max_value=440, value=154)
        weight = weight_lbs * 0.453592  # Convert pounds to kg
    
    # Height input with unit selection
    height_unit = st.selectbox("Height Unit", ["Centimeters", "Feet/Inches"])
    if height_unit == "Centimeters":
        height = st.number_input("Height", min_value=130, max_value=230, value=170)
    else:
        feet = st.number_input("Feet", min_value=4, max_value=7, value=5)
        inches = st.number_input("Inches", min_value=0, max_value=11, value=7)
        height = (feet * 30.48) + (inches * 2.54)  # Convert to cm
    
    # Activity Level
    activity_level = st.selectbox(
        "Activity Level",
        [
            "Sedentary (little or no exercise)",
            "Lightly active (light exercise 1-3 days/week)",
            "Moderately active (moderate exercise 3-5 days/week)",
            "Very active (hard exercise 6-7 days/week)",
            "Super active (very hard exercise & physical job)"
        ]
    )

# Calculate BMR and TDEE
bmr = calculate_bmr(weight, height, age, gender)
tdee = calculate_tdee(bmr, activity_level)

# Display Results
with col2:
    st.subheader("Your Results")
    
    # Display BMR
    st.markdown("### Basal Metabolic Rate (BMR)")
    st.info(f"{bmr:.0f} calories/day")
    st.markdown("*This is the number of calories your body burns at rest*")
    
    # Display TDEE
    st.markdown("### Total Daily Energy Expenditure (TDEE)")
    st.success(f"{tdee:.0f} calories/day")
    st.markdown("*This is your maintenance calories based on your activity level*")
    
    # Display calorie targets for different goals
    st.markdown("### Calorie Targets for Different Goals")
    
    goals_df = pd.DataFrame({
        "Goal": [
            "Weight Loss (0.5kg/week)",
            "Moderate Weight Loss (0.25kg/week)",
            "Maintenance",
            "Moderate Weight Gain (0.25kg/week)",
            "Weight Gain (0.5kg/week)"
        ],
        "Daily Calories": [
            tdee - 500,
            tdee - 250,
            tdee,
            tdee + 250,
            tdee + 500
        ]
    })
    
    # Style the dataframe
    st.dataframe(goals_df.style.format({"Daily Calories": "{:.0f}"}))

# Additional Information
st.markdown("---")
st.markdown("""
### 📝 Notes:
- BMR is calculated using the Mifflin-St Jeor Equation
- TDEE includes your activity level multiplier
- Weight loss/gain targets are based on the assumption that 3,500 calories = 1 pound of fat
- These are estimates and should be adjusted based on your personal results
- Consult with a healthcare professional before starting any diet or exercise program
""")