import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets


def app():
    st.title('Data')

    st.write("In this page I will discripe the dataset used in this project.")

    st.write("The TUEP dataset is a subset of TUEG (The TUH EEG Epilepsy Corpus) that contains 100 subjects epilepsy and 100 subjects without epilepsy, as determined by a certified neurologist. The data was developed in collaboration with a number of partners including NIH. .")
    st.write("The following is the DataFrame of the `TUEP` dataset.")

    iris = datasets.load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    Y = pd.Series(iris.target, name='class')
    df = pd.concat([X, Y], axis=1)
    df['class'] = df['class'].map(
        {0: "setosa", 1: "versicolor", 2: "virginica"})

    st.write(df)
