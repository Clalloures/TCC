import streamlit as st
from multiapp import MultiApp
from apps import home, data, model, new_file_submit  # import your app modules here


# st.markdown("""
# Epileptic Seizure Detection
# Development of an epilepsy seizure detection system using machine learning models
# """)


st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox(
    'Select page', ['Home', 'Description', 'Models', 'New File Submition'])


if(paginaSelecionada == 'Home'):
    home.app()

elif(paginaSelecionada == 'Description'):
    data.app()

elif(paginaSelecionada == 'Models'):
    model.app()

elif(paginaSelecionada == 'New File Submition'):
    new_file_submit.app()

# Add all your application here

# The main app
# app.run()
