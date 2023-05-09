import streamlit as st
import pandas as pd
from github import Github

# Authenticate with your GitHub access token
g = Github("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")
# Functions
# Define function to convert degree, minute, second to decimal degrees
def dms_to_dd(d: float, m: float, s: float, dir: str) -> float:
    dd = d + m / 60 + s / 3600
    if dir in ["Sud", "Ouest"]:
        dd = -dd
    return dd
# Read aircraft options from file
aircraft_options = pd.read_csv("aircraft_option.csv")["Type"].tolist()
Para=pd.read_csv("parameters.csv")
Lat=float(Para.loc["Lat"].values[0])
Lon=float(Para.loc["Lon"].values[0])
R=int(Para.loc["R"].values[0])
P=int(Para.loc["P"].values[0])
T=float(Para.loc["T"].values[0])
d=float(Para.loc["d"].values[0])
ac=Para.loc["ac"].values[0]
Mvt=Para.loc["Mvt"].values[0]
#Lat Degr, Min, Sec
if Lat>0:
    Lato=["Nord","Sud"]
else:
    Lato=["Sud","Nord"]
    Lat=-Lat
Latd=int(Lat)
Latm1=(Lat-Latd)*60
Latm=int(Latm1)
Lats=int((Latm1-Latm)*60)
#Lon Degr, Min, Sec
if Lon>0:
    Lono=["Est","Ouest"]
else:
    Lono=["Ouest","Est"]
    Lon=-Lon
Lond=int(Lon)
Lonm1=(Lon-Lond)*60
Lonm=int(Lonm1)
Lons=int((Lonm1-Lonm)*60)
# Set page title and background image
st.set_page_config(page_title="IFP NOISE", page_icon=":sound:", layout="wide", initial_sidebar_state="expanded")
Title="IFP NOISE"
Profil="background.png"
with st.container ():
    st.title(Title)
    st.image(Profil)
    Para
    Latm
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
                    lat_deg = st.number_input("Latitude (°)",min_value=0, max_value=90,  value=Latd, step=1, key="lat_deg")
                with col[1] :
                    lat_min = st.number_input("Latitude (min)",min_value=0, max_value=90, value=Latm, step=1, key="lat_min")
                with col[2] :
                    lat_sec = st.number_input("Latitude (sec)",min_value=0, max_value=90, value=Lats, step=1, key="lat_sec")
                with col[3] :
                    lat_dir = st.selectbox("Latitude (direction)", Lato, key="lat_dir")
        st.markdown("""<style> .verticalLine {border-left: 2px solid blue; height: 100%; position:absolute;left: 50%;margin-left: -3px;} </style> """, unsafe_allow_html=True)
        with colb :
            st.markdown('<div class="verticalLine"></div>', unsafe_allow_html=True)
        with col2 :
            st.markdown("## Longitude")
            with st.beta_container():
                colg = st.beta_columns(4)
                with colg[0]:
                    lon_deg = st.number_input("Longitude (°)",min_value=0, max_value=90, value=Lond, step=1, key="lon_deg")
                with colg[1]:
                    lon_min = st.number_input("Longitude (min)",min_value=0, max_value=90, value=Lonm, step=1, key="lon_min")
                with colg[2]:
                    lon_sec = st.number_input("Longitude (sec)",min_value=0, max_value=90, value=Lons, step=1, key="lon_sec")
                with colg[3]:
                    lon_dir = st.selectbox("Longitude (direction)", Lono, key="lon_dir")
    st.markdown("<hr style='border-top: 2px solid blue;'>", unsafe_allow_html=True)
    with st.beta_container():
        st.markdown("## Autres paramètres")
        rayon = st.slider("Rayon (m)", min_value=5, max_value=50, value=R)
        pas = st.slider("Pas (m)", min_value=50, max_value=500, step=10, value=P)
        temp = st.number_input("Température (°C)", value=T, step=0.1, format="%.1f")
        densite = st.number_input("Densité", min_value=0.7, max_value=2.0, step=0.1, value=d, format="%.1f")
   
    st.markdown("<hr style='border-top: 2px solid blue;'>", unsafe_allow_html=True)
    with st.beta_container():
        st.markdown("## Type d'avion")
        aircraft_type = st.selectbox("Type", aircraft_options)

    with st.beta_container():
        st.markdown("## Mouvements")
        mouvements = st.selectbox("Mouvements", ["Arrivée", "Départ"])
# Save changes
with st.container():
    if st.button("Calculate Noise"):
        # Perform action here
        Lat=dms_to_dd(d=lat_deg, m=lat_min, s=lat_sec, dir=lat_dir)
        Lon=dms_to_dd(d=lon_deg, m=lon_min, s=lon_sec, dir=lon_dir)
        Para["Param"]=[Lat,Lon,rayon,pas,temp,aircraft_type,mouvements,densite]
        Para.to_csv("parameters.csv")
        # Get the repo you want to commit to
        repo = g.get_user().get_repo("TandFinance/Airport-noise")

        # Get the contents of the file you want to update
        file = repo.get_contents("parameters.csv")
        # Commit the changes to the file
        repo.update_file(file.path,"Commit message",Para.to_csv(index=False),file.sha)
        # Success message
        st.success("File saved successfully to GitHub!")
        st.markdown("**Saved**)
