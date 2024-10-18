import streamlit as st
import pandas as pd

st.title('🤖 WEATHER PREDICTION APP')

st.write('This app is meant to predict weather conditions in your area')

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/penguins.csv')
df
df.isnull()

