import streamlit as st
import emoji

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .title {
            color: #ff4b4b;
            text-align: center;
            font-size: 40px;
        }
        .result {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
        }
        .stButton > button {
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit App Title
st.markdown("<h1 class='title'>💪 BMI Calculator</h1>", unsafe_allow_html=True)

# User Input
weight = st.number_input(emoji.emojize("🏋️ **Enter weight (kg):**"), min_value=1.0, format="%.2f")
height = st.number_input(emoji.emojize("📏 **Enter height (m):**"), min_value=0.5, format="%.2f")

# Calculate BMI
if st.button("✨ Calculate BMI ✨"):
    if height > 0:
        bmi = weight / (height ** 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "🥦 Underweight"
            color = "blue"
        elif 18.5 <= bmi < 24.9:
            category = "😊 Normal"
            color = "green"
        elif 25 <= bmi < 29.9:
            category = "🍔 Overweight"
            color = "orange"
        else:
            category = "⚠️ Obese"
            color = "red"

        # Display Result with Styling
        st.markdown(f"<h3 class='result' style='color: green;'>📊 Your BMI: {bmi:.2f}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3 class='result' style='color: {color};'>🏷️ Category: {category}</h3>", unsafe_allow_html=True)

        # Progress Bar for BMI Range
        st.progress(min(bmi / 40, 1.0))
    else:
        st.error("❌ Height must be greater than zero!")