import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("crop_recommendation_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌾",
    layout="centered"
)

# Title
st.title("🌾 Crop Recommendation System")

st.write(
    "Enter the soil and weather conditions to get a suitable crop recommendation."
)

# Input fields
N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=150.0, value=50.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=150.0, value=50.0)
K = st.number_input("Potassium (K)", min_value=0.0, max_value=210.0, value=50.0)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=0.0,
    max_value=50.0,
    value=25.0
)

humidity = st.number_input(
    "Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

ph = st.number_input(
    "Soil pH",
    min_value=0.0,
    max_value=14.0,
    value=6.5
)

rainfall = st.number_input(
    "Rainfall (mm)",
    min_value=0.0,
    max_value=500.0,
    value=100.0
)

# Prediction
if st.button("🌱 Recommend Crop"):

    input_data = [[
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    ]]

    prediction = model.predict(input_data)

    st.success(
        f"Recommended Crop: **{prediction[0].upper()}** 🌾"
    )