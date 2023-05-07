import streamlit as st
import sys
sys.path.append("..")
from aerodrome_noise import aircraft_type
st.set_page_config(page_title="IFP NOISE", page_icon=":sound:", layout="wide", initial_sidebar_state="expanded")
Title="IFP NOISE"
Profil="background.png"
with st.container ():
    st.title(Title)
    st.image(Profil)
with st.container():
  st.markdown(aircraft_type)
