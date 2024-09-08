import streamlit as st
if st.button("Generate Passwords"):
    st.switch_page("./pages/Generate Passwords.py")
if st.button("Export Passwords"):
    st.switch_page("./pages/Export Passwords.py")
if st.button("Manage Passwords"):
    st.switch_page("./pages/Manage Passwords.py")
if st.button("Ask a question to ChatGPT"):
    st.switch_page("./pages/AI.py")