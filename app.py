"""Module for Sprint 6 project"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Loaded the used cars dataset.
df = pd.read_csv('vehicles_us.csv')
# Created new column 'manufacturer' 
# by getting the first word from the 'model' column.
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# Added project title.
st.title('Sprint 6 Project')
# Added a project summary.
st.write('This application refers to the vehicles_us.csv dataset.')
# Added a divider.
st.header('', divider='rainbow')
st.header('')

# Created a text header above the DataFrame.
st.header('Data viewer')
# Displayed the DataFrame with Streamlit.
st.dataframe(df)
st.divider()

st.header('Vehicle types by manufacturer')
# Created a Plotly histogram figure.
fig = px.histogram(df, x='manufacturer',
                   color='type')
# Displayed the figure with Streamlit.
st.write(fig)
st.divider()