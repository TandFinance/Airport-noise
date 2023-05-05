import streamlit as st

def main():
    st.title('IFP NOISE')

    st.header('PARAMETERS')
    reference_point = st.beta_container()
    with reference_point:
        st.subheader('REFERENCE POINT')
        longitude = st.number_input('Longitude (X)', value=0.0, step=0.01)
        latitude = st.number_input('Latitude (Y)', value=0.0, step=0.01)
        radius = st.number_input('Radius (km)', value=0.0, step=0.01)
        step = st.number_input('Step (m)', value=0.0, step=0.01)

    aircraft = st.beta_container()
    with aircraft:
        st.subheader('AIRCRAFT TYPE')
        aircraft_type = st.selectbox('Select the aircraft type', ['A', 'B', 'C'])

    flight = st.beta_container()
    with flight:
        st.subheader('FLIGHT INFORMATION')
        arrival_departure = st.selectbox('Select the arrival or departure', ['Arrival', 'Departure'])
        temperature = st.number_input('Temperature (°C)', value=0.0, step=0.1)
        density = st.number_input('Density', value=0.0, step=0.1)

    st.header('TRAJECTORY EVALUATION')
    evaluation = st.beta_container()
    with evaluation:
        st.subheader('TRAJECTORY EVALUATION')
        upload_files = st.file_uploader('Upload the flight procedure and traffic files')
        if upload_files:
            uploaded_files = upload_files.getvalue()
            st.write(uploaded_files)

        add_evaluation = st.button('Add an evaluation trajectory')
        compile_impacts = st.button('Compile evaluated impacts')

    st.header('INSTRUCTIONS')
    st.markdown('''
        1. Load the traffic and flight procedure files
        2. Enter the parameters for the reference point, aircraft type, and flight information
        3. Add an evaluation trajectory
        4. Compile evaluated impacts
    ''')

if __name__ == '__main__':
    main()
