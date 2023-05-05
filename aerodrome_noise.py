import streamlit as st

def main():
    st.set_page_config(page_title="Noise", page_icon=":sound:", layout="wide")
    st.markdown(
        """
        <style>
        .main {
            background-image: url('background.png');
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
            height: 200px;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align: center;
        }
        .main h1 {
            font-size: 4em;
            font-weight: bold;
            color: blue;
            text-shadow: 2px 2px 4px white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    with st.container():
        st.markdown("<div class='main'><h1>IFP NOISE</h1></div>", unsafe_allow_html=True)
    field_parameters()
    aircraft()

def field_parameters():
    st.header("Field Parameters")
    ref_point = st.text_input("Reference point coordinates (DD-MM-SS)")
    rayon = st.number_input("Rayon (Km)", value=0.0, step=0.1)
    pas = st.number_input("Pas (m)", value=0, step=1)
    temp = st.number_input("T°C", value=0, step=1)
    densite = st.number_input("Densité", value=0.0, step=0.1)

def aircraft():
    st.header("Aircraft")
    aircraft_options = [
        "1900D",
        "707",
        "707120",
        "707320",
        "707QN",
        "717200",
        "720",
        "720B",
        "727100",
        "727200",
        "727D15",
        "727D17",
        "727EM1",
        "727EM2",
        "727Q15",
        "727Q7",
        "727Q9",
        "727QF",
        "737",
        "737300",
        "7373B2",
        "737400",
        "737500",
        "737700",
        "737800",
        "7378MAX",
        "737D17",
        "737N17",
        "737N9",
        "737QN",
        "747100",
        "74710Q",
        "747200",
        "74720A",
        "74720B",
        "747400",
        "7478",
        "747SP",
        "757300",
        "757PW",
        "757RR",
        "767300",
        "767400",
        "767CF6",
        "767JT9",
        "777200",
        "777300",
        "7773ER",
        "7878R",
        "A300-622R",
        "A300B4-203",
        "A310-304",
        "A319-131",
        "A320-211",
        "A320-232",
        "A321-232",
        "A330-301",
        "A330-343",
        "A340-211",
        "A340-642",
        "A350-941",
        "A380-841",
        "A380-861",
        "BAC111",
        "BAE146",
        "BAE300",
        "BEC58P",
        "C130",
        "C130E",
        "CIT3",
        "CL600",
        "CNA172",
        "CNA182",
        "CNA206",
        "CNA208",
        "CNA20T",
        "CNA441", 
        "CNA500", 
        "CNA510", 
        "CNA525C",
        "CNA55B",
        "CNA560E",
         "CNA560U", 
        "CNA560XL",
        "CNA680",
        "CNA750",
        "CONCRD",
        "CRJ9-ER",
    "CRJ9-LR",
        "CVR580",
        "DC1010",
        "DC1030", 
        "DC1040", 
        "DC3",
        "DC6",
    "DC820",
        "DC850",
        "DC860",
        "DC870", 
        "DC8QN",
        "DC910",
        "DC930",
    "DC93LW", 
        "DC950",
        "DC95HW",
        "DC9Q7",
        "DC9Q9",
        "DHC6",
        "DHC6QP",
        "DHC7",
        "DHC8",
        "DHC830",
         "DO228",
        "DO328",
        "ECLIPSE500",
        "EMB120",
        "EMB145",
         "EMB14L",
        "EMB170",
        "EMB175",
        "EMB190",
        "EMB195",
        "F10062",
         "F10065",
         "F28MK2",
         "F28MK4",
         "FAL20",
         "GII",
"GIIB",
"GIV",
"GV",
"HS748A",
"IA1125",
"L1011",
"L10115",
"L188",
"LEAR25",
"LEAR35",
"MD11GE",
"MD11PW",
"MD81",
"MD82",
"MD83",
"MD9025",
"MD9028",
"MU3001",
"PA28",
"PA30",
"PA31",
"PA42",
"SABR80",
"SD330",
"SF340", 
    # add remaining aircraft options here
]
aircraft = st.sidebar.selectbox("Select an Aircraft", aircraft_options)

# Add some text to the page
st.write("You selected the following field parameters:")
st.write(f"- Reference Point Coordinates: {ref_point}")
st.write(f"- Rayon (Km): {rayon_km}")
st.write(f"- Pas (m): {pas_m}")
st.write(f"- T°C: {temp_c}")
st.write(f"- Densité: {density}")
st.write("")
st.write(f"You selected the following aircraft: {aircraft}")
