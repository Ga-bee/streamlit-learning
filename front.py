import streamlit as st
import pandas a pd

st.title("Olá mundo")
df = pd.DataFrame({'Nomes':['Gabriela', 'Julia', 'Bruno', 'Sara'],'Idades': [22,23,45,26]})
st.write(df)
