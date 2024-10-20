import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

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
  X_raw = df.drop('species',axis=1)
  X_raw
  st.write('**y**')
  y_raw = df.species
  y_raw
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

data = {'island': island,
        'bill_length_mm': bill_length_mm,
        'bill_depth_mm': bill_depth_mm,
        'flipper_length_mm': flipper_length_mm,
        'body_mass_g': body_mass_g,
        'sex': sex}
input_df = pd.DataFrame(data, index=[0])
input_penguins = pd.concat([input_df, X_raw],axis=0)

with st.expander('input features'):
  st.write('**input penguins**')
  input_df
  st.write('**input combined data**')
  input_penguins
  
 # encode x
encode = ['island','sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
X = df_penguins[1:]
input_row = df_penguins[:1]
# encode y
target_mapper = {'Adelie':0,
                 'Chinstrap':1, 
                 'Gentoo':2}
def target_encode(val):
  return target_mapper[val]
y = y_raw.apply(target_encode)

with st.expander('Data preparation'):
  st.write('**Encoded X (input penguins)**')
  input_row
  st.write('**Encoded y**')
  y

rf = RandomForestClassifier()
rf.fit(X, y)

prediction = rf.predict(input_row)
pred_proba = rf.predict_proba(input_row)

pred_proba

df.pred_prob = pd.DataFrame(pred_proba)
df.pred_prob.columns = ['Adelie', 'Chinstrap', 'Gentoo']
df.pred_prob.rename({0:'Adelie',
                     1:'Chinstrap',
                     2:'Gentoo'})
#df.pred_prob

st.subset('Predictated Species')
penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.success(str(penguins_species[prediction][0]))








  
  






