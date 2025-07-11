import streamlit as st
import numpy as np
import joblib

# Load saved models and preprocessors
value_model = joblib.load('fifa_value_model.pkl')
position_model = joblib.load('rf_position_classifier.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

st.title("FIFA 21 Player Value & Position Predictor")

# Input sliders for features used by both models
pace = st.slider("Pace", 1, 99, 50)
shooting = st.slider("Shooting", 1, 99, 50)
passing = st.slider("Passing", 1, 99, 50)
dribbling = st.slider("Dribbling", 1, 99, 50)
defending = st.slider("Defending", 1, 99, 50)
physic = st.slider("Physic", 1, 99, 50)

# Other features to help with prediction
age = st.slider("Age", 16, 45, 25)
overall = st.slider("Overall", 40, 99, 70)
potential = st.slider("Potential", 40, 99, 75)

# Arrays that handle value and position
features_value = np.array([[age, overall, potential, pace, shooting, passing, dribbling, defending, physic]])
features_position = np.array([[pace, shooting, passing, dribbling, defending, physic]])

# Scale for position prediction
features_position_scaled = scaler.transform(features_position)

if st.button("Predict"):
    # Predict value
    value_pred = value_model.predict(features_value)[0]

    # Predict position
    pos_pred_encoded = position_model.predict(features_position_scaled)[0]
    pos_pred = label_encoder.inverse_transform([pos_pred_encoded])[0]

    st.write(f"**Predicted Player Value:** €{value_pred:,.2f}")
    st.write(f"**Predicted Player Position:** {pos_pred}")
