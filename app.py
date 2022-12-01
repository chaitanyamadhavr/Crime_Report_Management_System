import streamlit as st
import mysql.connector

from create import create
from database import create_table
from delete import delete
from read import read
from update import update

def main():
    st.title("Crime Report Management System")
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Add":
        st.subheader("Enter Crime Details:")
        create()

    elif choice == "View":
        st.subheader("View Details:")
        read()

    elif choice == "Edit":
        st.subheader("Edited Details:")
        update()

    elif choice == "Remove":
        st.subheader("Delete Details:")
        delete()

    else:
        st.subheader("")


if __name__ == '__main__':
    main()