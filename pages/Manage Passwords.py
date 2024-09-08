import streamlit as st
import pandas as pd
import io
data = '''Title,URL,Username,Password,Notes,OTPAuth
{title},,{username},{password},,'''
data = io.StringIO(data)
data = pd.read_csv(data)
st.data_editor(data=data, num_rows="dynamic")
st.write("Unfortunately, Firestore is not working correctly and responds 5 minutes later than it should, so we are unable to save your passwords.")