import streamlit as st
import pandas as pd

# Read aircraft options from file
aircraft_options = pd.read_csv("aircraft_option.csv")["Type"].tolist()

# Set page title and background image
st.set_page_config(page_title="IFP NOISE", page_icon=":sound:", layout="wide", initial_sidebar_state="expanded")
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: url("background.png") no-repeat center center fixed;
            -webkit-background-size: cover;
            -moz-background-size: cover;
            -o-background-size: cover;
            background-size: cover;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Add parameters group
with st.beta_container():
    st.markdown("# Parameters")
    with st.beta_container():
        st.markdown("## Coordonnées de points de réference")
        col1, col2 = st.beta_columns(2)
        with col1 :
            st.markdown("## Latitude")
            lat_deg = st.number_input("Latitude (degrés)", value=0, step=1, key="lat_deg")
            lat_min = st.number_input("Latitude (minutes)", value=0, step=1, key="lat_min")
            lat_sec = st.number_input("Latitude (secondes)", value=0, step=1, key="lat_sec")
            lat_dir = st.selectbox("Latitude (direction)", ["Nord", "Sud"], key="lat_dir")
         with col2 :
            st.markdown("## Longitude")
            lon_deg = st.number_input("Longitude (degrés)", value=0, step=1, key="lon_deg")
            lon_min = st.number_input("Longitude (minutes)", value=0, step=1, key="lon_min")
            lon_sec = st.number_input("Longitude (secondes)", value=0, step=1, key="lon_sec")
            lon_dir = st.selectbox("Longitude (direction)", ["Est", "Ouest"], key="lon_dir")

    with st.beta_container():
        st.markdown("## Autres paramètres")
        rayon = st.slider("Rayon (m)", min_value=100, max_value=1000, step=20, value=100)
        pas = st.slider("Pas (m)", min_value=50, max_value=500, step=10, value=100)
        temp = st.number_input("Température (°C)", value=0.0, step=0.1, format="%.1f")
        densite = st.number_input("Densité", min_value=0.7, max_value=2.0, step=0.1, value=1.0, format="%.1f")

    with st.beta_container():
        st.markdown("## Type d'avion")
        aircraft_type = st.selectbox("Type", aircraft_options)

    with st.beta_container():
        st.markdown("## Mouvements")
        mouvements = st.selectbox("Mouvements", ["Arrivée", "Départ"])
