import streamlit as st

import os
import pyedflib

from sklearn import datasets

import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)


def app():
    st.title('Submit')

    st.write('Run the model with new datasource.')

    st.write('Please, send a new EEG file and check the results.')

    file_result = st.file_uploader("Upload an EDF file", type=([".edf"]))

    # if file_result:
    #st.write('You selected `%s`' % file_result)
    # realizar teste com novo arquivo
