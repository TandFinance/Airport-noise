import streamlit as st
import pandas as pd
# Read aircraft options from file
aircraft_options = pd.read_csv("aircraft_option.csv")["Type"].tolist()
Para=pd.read_csv("parameters.csv")
# Set page title and background image

st.set_page_config(page_title="IFP NOISE", page_icon=":sound:", layout="wide", initial_sidebar_state="expanded")
Title="IFP NOISE"
Profil="background.png"
with st.container ():
    st.title(Title)
    st.image(Profil)
    Para.loc["Lat"]
# Add parameters group
with st.beta_container():
    st.markdown("# Parameters")
    with st.beta_container():
        st.markdown("## Coordonnées de points de réference")
        st.markdown("<hr style='border-top: 2px solid blue;'>", unsafe_allow_html=True)
        col1, colb, col2 = st.beta_columns([3, 0.5, 3])
        with col1 :
            st.markdown("## Latitude")
            with st.beta_container():
                col = st.beta_columns(4)
                with col[0] :
                    lat_deg = st.number_input("Latitude (°)",min_value=0, max_value=90,  value=0, step=1, key="lat_deg")
                with col[1] :
                    lat_min = st.number_input("Latitude (min)",min_value=0, max_value=90, value=0, step=1, key="lat_min")
                with col[2] :
                    lat_sec = st.number_input("Latitude (sec)",min_value=0, max_value=90, value=0, step=1, key="lat_sec")
                with col[3] :
                    lat_dir = st.selectbox("Latitude (direction)", ["Nord", "Sud"], key="lat_dir")
        st.markdown("""<style> .verticalLine {border-left: 2px solid blue; height: 100%; position:absolute;left: 50%;margin-left: -3px;} </style> """, unsafe_allow_html=True)
        with colb :
            st.markdown('<div class="verticalLine"></div>', unsafe_allow_html=True)
        with col2 :
            st.markdown("## Longitude")
            with st.beta_container():
                colg = st.beta_columns(4)
                with colg[0]:
                    lon_deg = st.number_input("Longitude (°)",min_value=0, max_value=90, value=0, step=1, key="lon_deg")
                with colg[1]:
                    lon_min = st.number_input("Longitude (min)",min_value=0, max_value=90, value=0, step=1, key="lon_min")
                with colg[2]:
                    lon_sec = st.number_input("Longitude (sec)",min_value=0, max_value=90, value=0, step=1, key="lon_sec")
                with colg[3]:
                    lon_dir = st.selectbox("Longitude (direction)", ["Est", "Ouest"], key="lon_dir")
    st.markdown("<hr style='border-top: 2px solid blue;'>", unsafe_allow_html=True)
    with st.beta_container():
        st.markdown("## Autres paramètres")
        rayon = st.slider("Rayon (m)", min_value=100, max_value=1000, step=20, value=100)
        pas = st.slider("Pas (m)", min_value=50, max_value=500, step=10, value=100)
        temp = st.number_input("Température (°C)", value=0.0, step=0.1, format="%.1f")
        densite = st.number_input("Densité", min_value=0.7, max_value=2.0, step=0.1, value=1.0, format="%.1f")
   
    st.markdown("<hr style='border-top: 2px solid blue;'>", unsafe_allow_html=True)
    with st.beta_container():
        st.markdown("## Type d'avion")
        aircraft_type = st.selectbox("Type", aircraft_options)

    with st.beta_container():
        st.markdown("## Mouvements")
        mouvements = st.selectbox("Mouvements", ["Arrivée", "Départ"])
