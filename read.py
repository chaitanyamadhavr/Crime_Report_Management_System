import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data


def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['criminal_id','criminal_name','criminal_nickname' ,'criminal_type' ,'crime_location','crime_date'])
    with st.expander("View all CRIME DETAILS"):
        st.dataframe(df)
    with st.expander("CRIME Details"):
        train_df = df['crime_date'].value_counts().to_frame()
        train_df = train_df.reset_index()
        st.dataframe(train_df)
        p1 = px.pie(train_df, names='index', values='crime_date')
        st.plotly_chart(p1)