import streamlit as st
import pandas as pd

st.title("Olá mundo")
df = pd.DataFrame({'Nomes':['Gabriela', 'Julia', 'Bruno', 'Sara'],'Idades': [22,23,45,26]})
st.write(df)
st.table(df)
df
