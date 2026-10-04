import streamlit as st
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("crop_recommendation_model.pkl")

# -----------------------------
# Header
# -----------------------------
st.title("🌾 Crop Recommendation System")

st.markdown(
    "### Smart agriculture using Machine Learning"
)

st.write(
    "Enter the soil and weather conditions below to get "
    "a suitable crop recommendation."
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🌱 About Project")

st.sidebar.info(
    """
    This project uses Machine Learning to recommend
    suitable crops based on soil and weather conditions.

    Algorithm:
    Random Forest Classifier
    """
)

st.sidebar.success(
    "Developed using Python, Machine Learning and Streamlit."
)

# -----------------------------
# Input Section
# -----------------------------
st.subheader("🌱 Enter Soil & Weather Details")

col1, col2 = st.columns(2)

with col1:

    N = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        max_value=150.0,
        value=50.0
    )

    P = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        max_value=150.0,
        value=50.0
    )

    K = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        max_value=210.0,
        value=50.0
    )

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=50.0,
        value=25.0
    )

with col2:

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

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("🌱 Recommend Crop", use_container_width=True):

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

    crop = prediction[0].upper()

    st.success(
        f"🌾 Recommended Crop: **{crop}**"
    )

    st.balloons()

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "Crop Recommendation System | Machine Learning Project | MCA"
)
