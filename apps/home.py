import streamlit as st
from PIL import Image


def app():

    image = Image.open('Images/Home_image.png')
    st.image(image)

    header = st.beta_container()
    dataset = st.beta_container()
    features = st.beta_container()

    with header:
        st.title('Home')
        st.text(
            'In this project I look into the detection of epilepsy seizure using ML models.')

    with dataset:
        st.header('The EEG dataset')
        st.text('I found this dataset at blablabla.com')

    with features:
        st.header('The features I created')
