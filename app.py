
import streamlit as st
import pickle
import numpy as np

# Charging the trained model
model = pickle.load(open('model.pkl', 'rb'))

st.title("CO2 Emissions Prediction")

# Criating inputs for user insert the data
engine_size = st.number_input("Motor Size (L)", min_value=0.5, max_value=7.0, value=2.0)
cylinders = st.number_input("Number of Cilinders", min_value=2, max_value=16, value=4)
fuel_consumption = st.number_input("Fuel Comsumption (L/100 km)", min_value=1.0, max_value=30.0, value=8.5)

# Doing predictions
if st.button("CO2 Emissions Prediction"):
    input_data = np.array([[engine_size, cylinders, fuel_consumption]])
    prediction = model.predict(input_data)
    st.success(f"Estimation of CO2 Emissions: {prediction[0]:,.2f} g/km")
    