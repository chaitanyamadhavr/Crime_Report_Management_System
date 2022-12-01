import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_criminal_names, get_details, edit_details


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['criminal_id','criminal_name','criminal_nickname' ,'criminal_type' ,'crime_location','crime_date'])
    with st.expander("Current CRIME DETAILS"):
        st.dataframe(df)
    list_of_crime_details = [i[0] for i in view_only_criminal_names()]
    selected_crime_details = st.selectbox("DETAILS to Edit", list_of_crime_details)
    selected_result = get_details(selected_crime_details)
    # st.write(selected_result)
    if selected_result:
        criminal_id = selected_result[0][0]
        criminal_name = selected_result[0][1]
        criminal_nickname = selected_result[0][2]
        criminal_type = selected_result[0][3]
        crime_location = selected_result[0][4]
        crime_date = selected_result[0][5]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_criminal_id = st.number_input("CRIMINAL ID:", criminal_id)
            new_criminal_name = st.text_input("CRIMINAL Name:", criminal_name)
            new_criminal_type = st.text_input("CRIMINAL TYPE:",criminal_type)
        with col2:
            new_criminal_nickname = st.text_input("CRIMINAL NICKNAME:",criminal_nickname)
            new_crime_location = st.selectbox(crime_location, ["Bengaluru", "Dwarka", "Mangaluru","Mandya","Nasik","Delhi","Mumbai"])
            new_crime_date = st.date_input("Crime Date:")

        if st.button("Update Details"):
            edit_details(new_criminal_id, new_criminal_name, new_criminal_nickname, new_criminal_type, new_crime_location, new_crime_date, criminal_id,criminal_name,criminal_nickname,criminal_type,crime_location,crime_date)
            st.success("Successfully updated:: {} to ::{}".format(criminal_name, new_criminal_name))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['new_criminal_id', 'new_criminal_name', 'new_criminal_nickname', 'new_criminal_type', 'new_crime_location', 'new_crime_date'])
    with st.expander("Updated data"):
        st.dataframe(df2)





































