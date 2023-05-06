import streamlit as st
import pandas as pd

# Load aircraft options from file
aircraft_options = pd.read_csv("aircraft_option.csv")["Type"].tolist()

# Set page title and background image
st.set_page_config(page_title="IFP NOISE", page_icon=None, layout="wide")
st.markdown(
    """
    <style>
        .main {
            background-image: url("background.png");
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create parameter groups
st.markdown("<h1 style='color:blue; font-weight:bold;'>IFP NOISE</h1>", unsafe_allow_html=True)
with st.beta_container():
    st.markdown("<h2 style='color:white; font-weight:bold;'>Parameters</h2>", unsafe_allow_html=True)

    with st.beta_container():
        st.markdown("<h3 style='color:white;'>Coordonnées de points de réference</h3>", unsafe_allow_html=True)
        lat_deg = st.number_input("Latitude (degré)", value=0, step=1)
        lat_min = st.number_input("Latitude (minute)", value=0, step=1)
        lat_sec = st.number_input("Latitude (seconde)", value=0, step=1)
        lat_dir = st.selectbox("Latitude (direction)", ("Nord", "Sud"))

        lon_deg = st.number_input("Longitude (degré)", value=0, step=1)
        lon_min = st.number_input("Longitude (minute)", value=0, step=1)
        lon_sec = st.number_input("Longitude (seconde)", value=0, step=1)
        lon_dir = st.selectbox("Longitude (direction)", ("Est", "Ouest"))

    with st.beta_container():
        st.markdown("<h3 style='color:white;'>Rayon (m)</h3>", unsafe_allow_html=True)
        rayon = st.slider("Rayon", min_value=100, max_value=2000, step=20, value=100)

    with st.beta_container():
        st.markdown("<h3 style='color:white;'>Pas (m)</h3>", unsafe_allow_html=True)
        pas = st.slider("Pas", min_value=50, max_value=1000, step=10, value=100)

    with st.beta_container():
        st.markdown("<h3 style='color:white;'>T°C</h3>", unsafe_allow_html=True)
        temperature = st.number_input("T°C", value=0)

    with st.beta_container():
        st.markdown("<h3 style='color:white;'>Densité</h3>", unsafe_allow_html=True)
        densite = st.slider("Densité", min_value=0.7, max_value=2.0, step=0.1, value=1.0)

    with st.beta_container():
        st.markdown("<h3 style='color:white;'>Aircraft</h3>", unsafe_allow_html=True)
        aircraft_type = st.selectbox("Type", options=aircraft_options)
        mouvement = st.selectbox("Mouvements", options=["Arrivée", "Départ"])

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    with st.beta_container():
        st.button("Calculate Noise")
