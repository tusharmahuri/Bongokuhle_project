import streamlit as st
import pandas as pd
import pickle

# Load the trained model from the pickle file
with open('best_tree_model.pkl', 'rb') as file:
    model = pickle.load(file)

# App Title
st.title("Vehicle Telemetry Fuel Consumption Prediction")

# App description
st.write("""
### Predict fuel consumption based on vehicle telemetry data
Enter the following details to predict the fuel consumption.
""")

# Input fields for the telemetry data (no maximum values defined)
Records_GpsSpeed = st.number_input('GPS Speed (km/h)', min_value=0.0, value=37.097629)
Records_RPM = st.number_input('RPM (Revolutions per Minute)', min_value=0.0, value=1071.772664)
altitude = st.number_input('Altitude (m)', min_value=0.0, value=1381.087855)
engine_output_kw = st.number_input('Engine Output (kw)', min_value=0, value=344)
gross_vehicle_mass_kg = st.number_input('Gross Vehicle Mass (kg)', min_value=0, value=26855)
gross_combination_mass_kg = st.number_input('Gross Combination Mass (kg)', min_value=0, value=72357)
trip_duration_hours = st.number_input('Trip Duration (hours)', min_value=0.0, value=3.845347)
distance_travelled = st.number_input('Distance Travelled (km)', min_value=0.0, value=142.653265)

# Button to make the prediction
if st.button('Predict Fuel Usage'):
    # Step 1: Prepare the input data as a DataFrame
    input_data = {
        'Records_GpsSpeed': [Records_GpsSpeed],
        'Records_RPM': [Records_RPM],
        'altitude': [altitude],
        'engine_output(kw)': [engine_output_kw],
        'gross_vehicle_mass(kg)': [gross_vehicle_mass_kg],
        'gross_combination_mass(kg)': [gross_combination_mass_kg],
        'trip_duration_hours': [trip_duration_hours],
        'distance_travelled': [distance_travelled]
    }

    input_df = pd.DataFrame(input_data)

    # Step 2: Use the loaded model to predict fuel consumption
    prediction = model.predict(input_df)

    # Step 3: Display the prediction result
    st.success(f"Predicted Fuel Usage: {prediction[0]:.2f} units")
