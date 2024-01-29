"""Module for Sprint 6 project"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Loaded the used cars dataset.
df = pd.read_csv('vehicles_us.csv')
"""Created new column 'manufacturer' \
    by getting the first word from the 'model' column.
    """
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

st.header('Sprint 6 Project', divider='rainbow')

st.write('It is not a functional application yet. Under construction.')