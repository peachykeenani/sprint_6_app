"""Module for Sprint 6 project"""

import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels as sm

# Loaded the used cars dataset.
df = pd.read_csv('vehicles_us.csv')
# Created new column 'manufacturer' 
# by getting the first word from the 'model' column.
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])
# Replaced all missing values from 'is_4wd' column with 0.
df['is_4wd'] = df['is_4wd'].fillna(0)
# Renamed 'price' column to 'price_$'.
df.rename(columns={'price':'price_$'}, inplace=True)


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


# Created a histogram of vehicle types by manufacturer.
st.header('Vehicle types by manufacturer')
# Created a Plotly histogram figure.
fig = px.histogram(df, x='manufacturer',
                   color='type')
# Displayed the figure with Streamlit.
st.write(fig)
st.divider()


# Created a histogram that explores the relationship
# between condition and model_year.
st.header('Histogram of `condition` vs `model_year`')
# Created a Plotly histogram figure.
fig = px.histogram(df, x='model_year', 
                   color='condition')
# Displayed the figure with Streamlit.
st.write(fig)
st.divider()


# Created a histogram that compares the price distribution
# between two manufacturers.
st.header('Compare price distribution between manufacturers')
# Get a list of car manufacturers.
manufac_list = sorted(df['manufacturer'].unique())
# Get user's inputs from a dropdown menu.
manufacturer_1 = st.selectbox(
                            label='Select manufacturer 1', # Title of the select box
                            options=manufac_list, # Options listed in the select box
                            index=manufac_list.index('chevrolet') # Default pre-selected option  
                            )
# Repeat for the second dropdown menu.
manufacturer_2 = st.selectbox(
                            label='Select manufacturer 2',
                            options=manufac_list,
                            index=manufac_list.index('hyundai')
                            )
# Filter the dataframe.
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]

# Add a checkbox if a user wants to normalize the histogram.
# Pass a unique key argument to st.selectbox.
counter = 0
normalize = st.checkbox('Normalize histogram', value=True, key=counter)
counter += 1
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

# Created a plotly histogram figure.
fig = px.histogram(df_filtered,
                   x='price_$',
                   nbins=30,
                   color='manufacturer',
                   histnorm=histnorm,
                   barmode='overlay'
                   )
# Displayed figure with Streamlit.
st.write(fig)
st.divider()


# Created a histogram of vehicle condition by manufacturer.
st.header('Vehicle condition by manufacturer')
# Created a Plotly histogram figure.
fig = px.histogram(df, x='manufacturer',
                   color='condition'
                   )
# Displayed the figure with Streamlit.
st.write(fig)
st.divider()


# Created a histogram of sales totals by vehicle condition.
st.header('Total sales by vehicle condition')
# Created a Plotly histogram figure.
fig = px.histogram(df, x='condition',
             y='price_$',
             color='condition',
             # Sorted bar chart by 'condition' in descending order.
             category_orders={'condition':['excellent',
                                           'good',
                                           'like new',
                                           'fair',
                                           'new',
                                           'salvage'
                                           ]
                            },
             labels={'price_$':'sales USD'}
             )
# Displayed the figure with Streamlit.
st.write(fig)
st.divider()


# Created a scatter plot that displays the relationship between vehicle price and condition.
st.header('Explore relationship between vehicle `price` and `condition`')
# Created a Plotly scatter plot figure.
fig = px.scatter(df, x='condition',
                 y='price_$',
                 color='condition'
                 )
# Displayed the figure with Streamlit.
st.write(fig)
st.divider()


# Created a box plot that compares price distribution of fuel types by vehicle transmission.
st.header('Comparing the price distribution of `fuel` types by vehicle `transmission`')
# Created a Plotly box plot figure.
fig = px.box(df, x='transmission',
             y='price_$',
             color='fuel',
             points='suspectedoutliers'
             )
# Excluded the median to divide the ordered dataset into tow halves.
fig.update_traces(quartilemethod='exclusive')
# Displayed the figure with Streamlit.
st.write(fig)
st.divider()


# Created a box plot that compares price distribution of 4WD vs. non-4WD vehicles by transmission.
st.header('Comparing the price distribution of `is_4wd` vehicles by `transmission`')
# Created a Plotly box plot figure.
fig = px.box(df, x='transmission',
             y='price_$',
             color='is_4wd',
             points='suspectedoutliers'
             )
# Excluded the median to divide the ordered dataset into tow halves.
fig.update_traces(quartilemethod='exclusive')
# Displayed the figure with Streamlit.
st.write(fig)
st.divider()


# Created a scatter plot that displays the relationship between days listed and price.
# Add a checkbox if a user wants to show trendline.
show_trend_ln = st.checkbox('Show trendline', value=True, key=counter)
if show_trend_ln:
    trendline = 'ols'
else:
    trendline = None

st.header('Explore relationship between vehicle `price` and `days_listed`')
# Created a Plotly scatter plot figure.
fig = px.scatter(df, x='price_$',
                 y='days_listed',
                 trendline=trendline
                 )
# Displayed the figure with Streamlit.
st.write(fig)
st.divider()