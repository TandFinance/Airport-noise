import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="Noise.py")

# Load aircraft options from CSV file
aircraft_options = pd.read_csv("aircraft_option.csv", usecols=["Type"])

# Define input fields
with st.form(key="input_form"):
    # Group for parameters
    st.write("Parameters:")
    col1, col2, col3, col4 = st.beta_columns(4)
    with col1:
        latitude_degree = st.number_input("Latitude (°)", min_value=-90, max_value=90, value=0)
    with col2:
        latitude_minute = st.number_input("Minutes", min_value=0, max_value=59, value=0)
    with col3:
        latitude_seconde = st.number_input("Seconds", min_value=0, max_value=59, value=0)
    with col4:
        latitude_orientation = st.selectbox("Orientation", ["N", "S"])

    col1, col2 = st.beta_columns(2)
    with col1:
        rayon = st.slider("Rayon (m)", min_value=100, max_value=10000, step=20, value=500)
    with col2:
        pas = st.number_input("Pas (m)", min_value=50, value=100)

    temperature = st.number_input("Temperature (°C)", value=20.0)

    densite = st.number_input("Densité", min_value=0.7, max_value=2.0, value=1.0)

    # Group for aircraft options
    st.write("Aircraft:")
    aircraft_choice = st.selectbox("Mouvements", aircraft_options["Type"])

    # Submit button
    submitted = st.form_submit_button(label="Submit")

# Show results if submitted
if submitted:
    st.write("Parameters:")
    st.write(f"Latitude: {latitude_degree}° {latitude_minute}' {latitude_seconde}\" {latitude_orientation}")
    st.write(f"Rayon: {rayon}m")
    st.write(f"Pas: {pas}m")
    st.write(f"Temperature: {temperature}°C")
    st.write(f"Densité: {densite}")

    st.write("Aircraft:")
    st.write(f"Type: {aircraft_choice}")

