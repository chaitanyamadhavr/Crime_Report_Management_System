import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        criminal_id = st.number_input("Criminal ID:")
        criminal_name = st.text_input("Criminal Name:")
        criminal_nickname = st.text_input("Criminal NickName:")
    with col2:
        criminal_type = st.selectbox("Criminal Type", ["SERIAL KILLER", "MURDERER", "ROBBER","THIEF","OTHER"])
        crime_location = st.selectbox("Crime Location", ["Bengaluru", "Dwarka", "Mangaluru","Mandya","Nasik","Delhi","Mumbai"])
        crime_date = st.date_input("Crime Date:")

    if st.button("Add"):
        add_data(criminal_id, criminal_name, criminal_nickname, criminal_type, crime_location, crime_date)
        st.success("Successfully Added Crime Details : {}".format(criminal_name))

        