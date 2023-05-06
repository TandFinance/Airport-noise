import streamlit as st
import pandas as pd
# Set page title and background image
st.set_page_config(page_title="IFP NOISE", page_icon=None, layout="wide", initial_sidebar_state="expanded")
bg_image = "background.png"
st.markdown(f'<style>body{{background-image: url("{bg_image}");background-size: cover;}}</style>', unsafe_allow_html=True)

# Define function to convert degree, minute, second to decimal degrees
def dms_to_dd(d: float, m: float, s: float, dir: str) -> float:
    dd = d + m / 60 + s / 3600
    if dir in ["S", "W"]:
        dd = -dd
    return dd

# Define function to convert decimal degrees to degree, minute, second
def dd_to_dms(dd: float) -> tuple:
    d = int(dd)
    md = abs(dd - d) * 60
    m = int(md)
    s = (md - m) * 60
    return d, m, s

# Define function to validate latitude or longitude input
def validate_lat_long(d: int, m: int, s: int, dir: str) -> bool:
    if not (0 <= d <= 90):
        return False
    if not (0 <= m < 60):
        return False
    if not (0 <= s < 60):
        return False
    if dir not in ["N", "S", "E", "W"]:
        return False
    return True

# Define function to validate other inputs
def validate_input(val: str, min_val: float, max_val: float, decimal_places: int) -> bool:
    try:
        val = float(val)
    except ValueError:
        return False
    if not (min_val <= val <= max_val):
        return False
    if round(val, decimal_places) != val:
        return False
    return True

# Load aircraft options from CSV file
aircraft_options = st.cache(pd.read_csv)("aircraft_option.csv")["Type"].tolist()

# Define UI layout
with st.sidebar:
    st.header("IFP NOISE")
    st.subheader("Paramètres")
    with st.beta_expander("Coordonnées de points de référence"):
        col1, col2 = st.beta_columns(2)
        with col1:
            st.write("Latitude")
            lat_deg = st.selectbox("Degré", range(0, 91))
            lat_min = st.selectbox("Minute", range(0, 60))
            lat_sec = st.selectbox("Seconde", range(0, 60))
            lat_dir = st.selectbox("Direction", ["N", "S"])
        with col2:
            st.write("Longitude")
            lon_deg = st.selectbox("Degré", range(0, 181))
            lon_min = st.selectbox("Minute", range(0, 60))
            lon_sec = st.selectbox("Seconde", range(0, 60))
            lon_dir = st.selectbox("Direction", ["E", "W"])
    with st.beta_expander("Autres paramètres"):
        rayon = st.slider("Rayon (m)", 100, 1000, 100, 20)
        pas = st.slider("Pas (m)", 50, 500, 100)
        temp = st.number_input("Température (°C)", step=0.1, min_value=-273.15, max_value=100, value=15)
       

