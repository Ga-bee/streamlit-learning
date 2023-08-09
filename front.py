import streamlit as st
import pandas as pd
import numpy as np


st.title("Olá mundo")
#df = pd.DataFrame({'Nomes':['Gabriela', 'Julia', 'Bruno', 'Sara'],'Idades': [22,23,45,26]})
#st.write(df)
#st.table(df)
#df
#st.dataframe(df.style.highlight_max())

#map_data = pd.DataFrame(np.random.randn(1000,2) / [50,50] + [37.76, 0122.4],
#                       columns = [ 'lat', 'lon'] )

#st.map(map_data)

x = st.slider('x')
st.write(x, 'squared is', x * x)

st.text_input('Your name', key = 'name')
st.session_state.name

if st.checkbox('Show dataframe'):
  chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']  ) 
  chart_data

df = pd.DataFrame({
  'first column': [1,2,3,4],
  'secind column': [10,20,30,40]})

option = st.selectbox('Wich number do you like best?',df['first column'])

'You selected: ', option

add_selectbox = st.sidebar.selectbox('How would you like to be contacted',('Email','Home phone', 'Mobile phone'))

add_slider = st.sidebar.slider('Select a range of values',
                               0.0, 100.0, (25.0,75.0))

import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
