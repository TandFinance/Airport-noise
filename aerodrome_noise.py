import streamlit as st
import pandas as pd
# Set page config
st.set_page_config(page_title="IFP NOISE", page_icon=":sound:", layout="wide")

# Set background image
main_bg = "background.png"
st.markdown(f"""
    <style>
        .reportview-container {{
            background: url({main_bg}) no-repeat center center fixed;
            background-size: cover;
        }}
    </style>
""", unsafe_allow_html=True)

# Add title
st.markdown("<h1 style='text-align: center; color: blue; font-weight: bold;'>IFP NOISE</h1>", unsafe_allow_html=True)

# Add groups
parameters = st.beta_expander("Parameters")
mouvements = st.beta_expander("Mouvements")

# Add inputs to parameters group
with parameters:
    st.subheader("Reference Coordinate")
    col1, col2 = st.beta_columns(2)
    with col1:
        lat = st.number_input("Latitude (deg)", value=0, step=1)
    with col2:
        lon = st.number_input("Longitude (deg)", value=0, step=1)

    st.number_input("Rayon (km)", value=0, step=1)
    st.number_input("Pas (m)", value=0, step=1)
    st.number_input("T°C", value=0, step=1)
    st.number_input("Densité", value=0, step=1)

# Add combobox to mouvements group
with mouvements:
    st.subheader("Aircraft")
    # Read the CSV file using Pandas
    aircraft_options = pd.read_csv("aircraft_options.csv")["Type"].tolist()
    aircraft_choice = st.selectbox("Mouvements", ["Arrivée", "Départ"])
    aircraft_type = st.selectbox("Type", aircraft_options)
