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
    options = [
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
       
