import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="IFP NOISE", page_icon=":sound:", layout="wide")

# Load aircraft options from file
aircraft_options = pd.read_csv("aircraft_options.csv")["Type"].tolist()

# Define function to convert degree-minute-second coordinates to decimal degrees
def dms_to_dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes) / 60 + float(seconds) / (60 * 60)
    if direction == "S" or direction == "W":
        dd *= -1
    return dd

# Define sidebar content
st.sidebar.image("background.png", use_column_width=True)
st.sidebar.subheader("Parameters")

# Add reference point coordinates
ref_lat_deg = st.sidebar.number_input("Latitude (degrees)", value=48)
ref_lat_min = st.sidebar.number_input("Latitude (minutes)", value=50)
ref_lat_sec = st.sidebar.number_input("Latitude (seconds)", value=0)
ref_lat_dir = st.sidebar.selectbox("Latitude direction", ["N", "S"])
ref_lon_deg = st.sidebar.number_input("Longitude (degrees)", value=2)
ref_lon_min = st.sidebar.number_input("Longitude (minutes)", value=20)
ref_lon_sec = st.sidebar.number_input("Longitude (seconds)", value=0)
ref_lon_dir = st.sidebar.selectbox("Longitude direction", ["E", "W"])

# Convert reference point coordinates to decimal degrees
ref_lat = dms_to_dd(ref_lat_deg, ref_lat_min, ref_lat_sec, ref_lat_dir)
ref_lon = dms_to_dd(ref_lon_deg, ref_lon_min, ref_lon_sec, ref_lon_dir)

# Add radius, pas, temperature, and density inputs
st.sidebar.subheader("Field parameters")
radius = st.sidebar.slider("Radius (m)", 100, 1000, 100, 20)
pas = st.sidebar.slider("Pas (m)", 50, 1000, 100, 50)
temp = st.sidebar.number_input("Temperature (°C)", value=20.0, format="%.1f")
density = st.sidebar.number_input("Density", value=1.2, min_value=0.7, max_value=2.0, format="%.2f")

# Add aircraft movement selection
st.sidebar.subheader("Aircraft")
aircraft_movement = st.sidebar.selectbox("Movement", ["Arrivée", "Départ"], key="aircraft_movement")
aircraft_type = st.sidebar.selectbox("Type", aircraft_options)

# Define main content
st.image("background.png", use_column_width=True)
st.markdown("# IFP NOISE")

# Display field parameters
st.subheader("Field parameters")
parameters_col1, parameters_col2 = st.columns(2)
with parameters_col1:
    st.markdown(f"**Reference point coordinates:** ({ref_lat_deg}° {ref_lat_min}' {ref_lat_sec}\" {ref_lat_dir}, {ref_lon_deg}° {ref_lon_min}' {ref_lon_sec}\" {ref_lon_dir})")
    st.markdown(f"**Radius:** {radius} m")
with parameters_col2:
    st.markdown(f"**Pas:** {pas} m")
    st.markdown(f"**Temperature:** {temp} °C")
    st.markdown(f"**Density:** {density}")

# Display aircraft information
st.subheader("Aircraft")
st.markdown(f"**Movement:** {aircraft_movement}")
st.markdown(f"**Type:** {aircraft_type}")
