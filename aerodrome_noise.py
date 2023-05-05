import streamlit as st
import pandas as pd

# Load aircraft options from csv file
aircraft_options = pd.read_csv("aircraft_option.csv")["Type"].tolist()

# Set page title and background image
st.set_page_config(page_title="Noise", page_icon=None, layout="wide", initial_sidebar_state="auto")
st.markdown(f"""
    <style>
        .reportview-container {{
            background: url("background.png");
            background-size: cover;
        }}
        .title {{
            font-size: 50px;
            font-weight: bold;
            color: blue;
            text-shadow: 2px 2px 4px #000000;
        }}
    </style>
    <div class="title">IFP NOISE</div>
    """, unsafe_allow_html=True)

# Define input fields
ddmmss = st.text_input("Reference point coordinates (DD-MM-SS)")
rayon = st.number_input("Rayon (Km)", value=0, step=1)
pas = st.number_input("Pas (m)", value=0, step=1)
temp = st.number_input("T°C", value=0, step=1)
densite = st.number_input("Densité", value=0, step=1)
aircraft = st.selectbox("Aircraft", aircraft_options)

# Define submit button
if st.button("Submit"):
    # Do something with the input data
    st.write("Input data:")
    st.write(f"Reference point coordinates: {ddmmss}")
    st.write(f"Rayon (Km): {rayon}")
    st.write(f"Pas (m): {pas}")
    st.write(f"T°C: {temp}")
    st.write(f"Densité: {densite}")
    st.write(f"Aircraft: {aircraft}")

