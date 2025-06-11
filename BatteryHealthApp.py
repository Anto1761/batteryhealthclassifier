import streamlit as st
import pickle
import numpy as np

# Set the title
st.title("🔋 Battery Health Prediction")

# Load the model
try:
    with open("BatteryClassifier.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Input sliders
temperature = st.number_input("Enter Temperature (°C):", min_value=-10.0, max_value=100.0, step=0.1)
voltage = st.number_input("Enter Voltage (V):", min_value=0.0, max_value=10.0, step=0.01)
current = st.number_input("Enter Current (A):", min_value=0.0, max_value=5.0, step=0.01)

# Predict button
if st.button("Predict"):
    input_data = np.array([[temperature, voltage, current]])

    try:
        prediction = model.predict(input_data)[0]

        label_mapping = {0: "Good", 1: "Moderate", 2: "Poor"}
        result = label_mapping.get(prediction, "Unknown")

        st.success(f"✅ Predicted Battery Health: **{result}**")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
