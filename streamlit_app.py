import streamlit as st
import pandas as pd

st.title('🤖 WEATHER PREDICTION APP')

st.write('This app is meant to predict weather conditions in your area')
with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/penguins.csv')
  df
with st.expander('Clean Data'):
  st.write('**clean data**')
  df.dropna(subset=['sex'],inplace=True)
  df
  st.write('**X**')
  X = df.drop('species',axis=1)
  X
  st.write('**y**')
  y = df.species
  y
with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x="bill_length_mm", y="body_mass_g",color="species")

with st.sidebar:
  st.header('input features')
  # island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
  island = st.selectbox('island',('Torgersen','Biscoe','Dream'))
  bill_length_mm = st.slider('bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('bill depth (mm)', 13.1, 21.5, 17.1)
  flipper_length_mm = st.slider('flipper length (mm)', 172.0, 231.0, 200.9)
  body_mass_g = st.slider('body mass (g)', 2700.0, 6300.0, 4207.0)
  sex = st.selectbox('Sex', ('MALE','FEMALE'))



  
  






