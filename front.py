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
