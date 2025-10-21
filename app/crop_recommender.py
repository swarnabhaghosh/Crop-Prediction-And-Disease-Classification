import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Model Loading ---
def load_model(model_path):
    """Load the pre-trained model from a pickle file."""
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error(f"Error: Model file not found at {model_path}. Please make sure the model file is in the correct directory.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        return None

# Use a relative path for the model file
model_filename = '../models/NBClassifier.pkl'
model = load_model(model_filename)


# --- UI Design ---
# Main Title
st.title("🌾 Crop Recommendation System")
st.markdown("Enter the soil and weather conditions to get a recommendation for the most suitable crop to cultivate.")

# Sidebar for User Input
st.sidebar.header("Input Parameters")

def user_input_features():
    """Create number inputs in the sidebar for user input."""
    # The st.number_input widget provides a text box with increment/decrement buttons
    n = st.sidebar.number_input('Nitrogen (N)', min_value=5, max_value=140, value=50, help="Enter the ratio of Nitrogen content in the soil (e.g., 50)")
    p = st.sidebar.number_input('Phosphorus (P)', min_value=5, max_value=145, value=50, help="Enter the ratio of Phosphorus content in the soil (e.g., 50)")
    k = st.sidebar.number_input('Potassium (K)', min_value=5, max_value=300, value=50, help="Enter the ratio of Potassium content in the soil (e.g., 50)")
    temp = st.sidebar.number_input('Temperature (°C)', min_value=9.0, max_value=43.0, value=25.0, step=0.1, format="%.1f", help="Enter the temperature in Celsius (e.g., 25.5)")
    humidity = st.sidebar.number_input('Humidity (%)', min_value=15.0, max_value=99.0, value=70.0, step=0.1, format="%.1f", help="Enter the relative humidity in % (e.g., 70.0)")
    ph = st.sidebar.number_input('pH Level', min_value=3.6, max_value=9.9, value=6.5, step=0.1, format="%.1f", help="Enter the pH value of the soil (e.g., 6.5)")
    rainfall = st.sidebar.number_input('Rainfall (mm)', min_value=21.0, max_value=298.0, value=100.0, step=0.1, format="%.1f", help="Enter the rainfall in mm (e.g., 100.0)")
    
    data = {
        'N': n, 'P': p, 'K': k,
        'temperature': temp, 'humidity': humidity,
        'ph': ph, 'rainfall': rainfall
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display user input in the main area
st.subheader("Your Input Parameters")
st.dataframe(input_df, use_container_width=True)

# --- Prediction and Display ---
if model:
    if st.button("Get Crop Recommendation", key="predict_button"):
        try:
            # The model expects a 2D numpy array
            prediction_features = input_df.values
            prediction = model.predict(prediction_features)
            
            # Display the result
            st.success(f"**The recommended crop is: {prediction[0].capitalize()}**")
            
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
else:
    st.warning("Model is not loaded. Please check the file path and integrity.")

# Adding some informative text at the bottom
st.markdown("---")
st.info(
    "**Disclaimer:** This recommendation is based on a machine learning model trained on a standard dataset. "
    "Always consult with local agricultural experts for final decisions."
)

