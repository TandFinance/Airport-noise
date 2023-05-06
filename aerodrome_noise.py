import streamlit as st
import pandas as pd

# Load aircraft options from CSV
aircraft_options = pd.read_csv('aircraft_option.csv')['Type'].tolist()

# Set up page layout and background image
st.set_page_config(page_title="Noise", page_icon=":sound:", layout="wide")
bg_image = "background.png"
page_bg_img = '''
<style>
body {
background-image: url("https://cdn.pixabay.com/photo/2017/08/30/12/45/girl-2696947_960_720.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Add page title
st.markdown("<h1 style='text-align: center; color: blue;'>IFP NOISE</h1>", unsafe_allow_html=True)

# Add field parameters group
with st.beta_container():
    st.header("Field Parameters")
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        lat_deg = st.number_input("Latitude (deg)", min_value=0, max_value=90)
    with col2:
        lat_min = st.number_input("Latitude (min)", min_value=0, max_value=59)
    with col3:
        lat_sec = st.number_input("Latitude (sec)", min_value=0, max_value=59)
    with col4:
        rayon = st.number_input("Rayon (km)", min_value=0, max_value=999)
    with col5:
        pas = st.number_input("Pas (m)", min_value=0, max_value=999)

    st.number_input("T°C", min_value=0, max_value=999)
    st.number_input("Densité", min_value=0, max_value=999)

# Add aircraft group with movement combobox
with st.beta_container():
    st.header("Aircraft")
    mouvements = st.selectbox("Mouvements", ["Arrivée", "Départ"])
    aircraft_type = st.selectbox("Aircraft Type", aircraft_options)

# Add a button to submit the form
if st.button("Submit"):
    # Combine latitude inputs into single value
    latitude = lat_deg + (lat_min / 60) + (lat_sec / 3600)

    # Print form values to console
    print("Latitude:", latitude)
    print("Rayon:", rayon)
    print("Pas:", pas)
    print("T°C:", st.session_state["T°C"])
    print("Densité:", st.session_state["Densité"])
    print("Mouvements:", mouvements)
    print("Aircraft Type:", aircraft_type)
