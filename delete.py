import pandas as pd
import streamlit as st
from database import view_all_data, view_only_criminal_names, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['criminal_id','criminal_name','criminal_nickname' ,'criminal_type' ,'crime_location','crime_date'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_crime_details = [i[0] for i in view_only_criminal_names()]
    selected_crime_details = st.selectbox("Crime Details to Delete", list_of_crime_details)
    st.warning("Do you want to delete ::{}".format(selected_crime_details))
    if st.button("Delete crime_details"):
        delete_data(selected_crime_details)
        st.success("CRIME DETAILS has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['criminal_id','criminal_name','criminal_nickname' ,'criminal_type' ,'crime_location','crime_date'])
    with st.expander("Updated data"):
        st.dataframe(df2)