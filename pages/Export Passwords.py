import streamlit as st
title = st.text_input("Entry Title")
username = st.text_input("Username")
password = st.text_input("Password")
data = f'''Title,URL,Username,Password,Notes,OTPAuth
{title},,{username},{password},,'''
st.download_button("Export Passwords", data, file_name="exported_password.csv", mime=None, key=10, use_container_width=True)