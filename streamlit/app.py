import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV dataset
data = pd.read_csv('dataset.csv')

# Set up Streamlit layout
st.set_page_config(page_title='Personalized Dashboard', layout='wide')
st.title('Personalized Dashboard')

# Add logo to the right top corner using st.sidebar
st.sidebar.image('logo.png')

# Create a category filter in the sidebar
selected_categories = st.sidebar.multiselect('Select Category', data['Category'].unique())

# Filter the data based on the selected categories
filtered_data = data[data['Category'].isin(selected_categories)] if selected_categories else data

# Calculate the KPI
kpi = filtered_data['Value'].sum()

# Display the KPI in a square card
st.markdown('## Key Performance Indicator')
st.info(f'Total Value: {kpi}')

# Create a bar chart using Plotly
st.markdown('## Bar Chart')
bar_data = filtered_data.groupby('Category')['Value'].sum().reset_index()
fig = px.bar(bar_data, x='Category', y='Value', labels={'Category': 'Category', 'Value': 'Value'})
st.plotly_chart(fig)

# Create a line chart for time series analysis using Plotly
st.markdown('## Time Series Analysis')
time_series_data = filtered_data[['Date', 'Value']]
time_series_data['Date'] = pd.to_datetime(time_series_data['Date'])
fig = px.line(time_series_data, x='Date', y='Value', labels={'Date': 'Date', 'Value': 'Value'})
st.plotly_chart(fig)
