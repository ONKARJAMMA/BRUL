import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Load model
model = joblib.load('models/xgb_rul_model.pkl')

# App config
st.set_page_config(page_title="Battery RUL Predictor", layout="centered")
st.title("🔋 Battery RUL (Remaining Useful Life) Predictor")

st.markdown(
    """
    Predict how many cycles a battery has left based on real-time sensor inputs.  
    Adjust the sliders to simulate sensor readings.
    """
)

st.sidebar.header("📊 Sensor Settings")

# Define input features
features = [f'op_set{i}' for i in range(1, 4)] + [f'sensor{i}' for i in range(1, 22)]
user_input = {}

# Sliders in sidebar
for col in features:
    user_input[col] = st.sidebar.slider(col, 0.0, 1.0, 0.5, step=0.01)

# Convert input to DataFrame
input_df = pd.DataFrame([user_input])

# Show input preview
with st.expander("🔍 View Input Sensor Data"):
    st.dataframe(input_df)

# Predict
if st.button("🔮 Predict RUL"):
    prediction = model.predict(input_df)[0]
    st.success(f"📈 Predicted Remaining Useful Life: **{prediction:.2f} cycles**")
    st.balloons()

# Optional: Add footer
st.markdown(
    """
    <hr>
    <center>Built for DevifyX Battery Health Assignment | 🔧 Model: XGBoost | UI: Streamlit</center>
    """,
    unsafe_allow_html=True
)
