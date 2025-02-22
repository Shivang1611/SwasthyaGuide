import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize food database
FOOD_DATABASE = {
    "Fruits": {
        "Apple": 52,
        "Banana": 89,
        "Orange": 47,
        "Grapes (1 cup)": 62,
        "Mango": 60,
        "Strawberries (1 cup)": 49,
        "Pineapple (1 cup)": 82
    },
    "Vegetables": {
        "Carrot": 41,
        "Broccoli (1 cup)": 55,
        "Spinach (1 cup)": 7,
        "Potato": 163,
        "Tomato": 22,
        "Green Beans (1 cup)": 31,
        "Sweet Potato": 103
    },
    "Proteins": {
        "Chicken Breast (100g)": 165,
        "Egg": 72,
        "Salmon (100g)": 208,
        "Tuna (100g)": 116,
        "Tofu (100g)": 76,
        "Greek Yogurt (100g)": 59,
        "Chickpeas (1 cup)": 269
    },
    "Grains": {
        "White Rice (1 cup cooked)": 205,
        "Brown Rice (1 cup cooked)": 216,
        "Bread (1 slice)": 79,
        "Oatmeal (1 cup cooked)": 158,
        "Quinoa (1 cup cooked)": 222,
        "Pasta (1 cup cooked)": 221,
        "Cereal (1 cup)": 307
    },
    "Snacks": {
        "Almonds (1 oz)": 164,
        "Chocolate Bar": 235,
        "Potato Chips (1 oz)": 152,
        "Popcorn (1 cup)": 31,
        "Cookie": 148,
        "Mixed Nuts (1 oz)": 173,
        "Granola Bar": 190
    }
}

# Set page configuration
st.set_page_config(page_title="Food Calorie Calculator", layout="wide")

# Initialize session state for storing selected foods
if 'selected_foods' not in st.session_state:
    st.session_state.selected_foods = []

def add_food_item(food_name, calories, quantity):
    """Add food item to selected foods list"""
    total_calories = calories * quantity
    st.session_state.selected_foods.append({
        "food_name": food_name,
        "quantity": quantity,
        "calories_per_unit": calories,
        "total_calories": total_calories,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# App title and description
st.title("🍎 Food Calorie Calculator")
st.markdown("Calculate the calories of your meals using our food database")

# Create two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Add Food Items")
    
    # Food category selection
    category = st.selectbox("Select Food Category", list(FOOD_DATABASE.keys()))
    
    # Food item selection
    food_item = st.selectbox("Select Food Item", list(FOOD_DATABASE[category].keys()))
    
    # Quantity input
    quantity = st.number_input("Quantity", min_value=0.25, max_value=10.0, value=1.0, step=0.25)
    
    # Display calories for selected item
    calories = FOOD_DATABASE[category][food_item]
    st.write(f"Calories per unit: {calories}")
    st.write(f"Total calories: {calories * quantity:.1f}")
    
    # Add button
    if st.button("Add to Meal"):
        add_food_item(food_item, calories, quantity)
        st.success(f"Added {quantity} {food_item}(s) to your meal")

with col2:
    st.subheader("Your Meal Summary")
    
    if st.session_state.selected_foods:
        # Create DataFrame from selected foods
        df = pd.DataFrame(st.session_state.selected_foods)
        
        # Display total calories
        total_calories = df["total_calories"].sum()
        st.metric("Total Calories", f"{total_calories:.1f}")
        
        # Display selected foods table
        st.write("Selected Foods:")
        display_df = df[["food_name", "quantity", "calories_per_unit", "total_calories"]]
        display_df.columns = ["Food Item", "Quantity", "Calories/Unit", "Total Calories"]
        st.dataframe(display_df)
        
        # Add clear button
        if st.button("Clear All"):
            st.session_state.selected_foods = []
            st.experimental_rerun()
        
        # Add download button
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Meal Data",
            data=csv,
            file_name="meal_data.csv",
            mime="text/csv"
        )
    else:
        st.info("Start adding food items to see your meal summary")

# Display database information
st.markdown("---")
st.subheader("📚 Food Database")

# Create tabs for each category
tabs = st.tabs(list(FOOD_DATABASE.keys()))
for tab, category in zip(tabs, FOOD_DATABASE.keys()):
    with tab:
        # Convert category data to DataFrame
        category_df = pd.DataFrame.from_dict(
            FOOD_DATABASE[category], 
            orient='index', 
            columns=['Calories']
        ).reset_index()
        category_df.columns = ['Food Item', 'Calories']
        st.dataframe(category_df, use_container_width=True)

# Add nutritional information disclaimer
st.markdown("---")
st.markdown("""
### ℹ️ Disclaimer
- Calorie values are approximate and based on standard serving sizes
- Actual calories may vary based on preparation method and specific brands
- This calculator is for educational purposes only
- Consult with a healthcare professional for personalized dietary advice
""")