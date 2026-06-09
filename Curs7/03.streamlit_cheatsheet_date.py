## Pentru instalare
##  pip install streamlit

## Pentru rulare
## streamlit run numele_fisierului.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

### Streamlit functioneaza cu pandas, matplotlib, seaborn

df = pd.read_csv("teams.csv")
st.dataframe(df)

st.table(df.head(10))

## Plotting
st.bar_chart(df[["id", "team_name"]])


fig, axes = plt.subplots()
st.pyplot(fig)


code_de_aratat = """df = pd.read_csv("teams.csv")
st.dataframe(df)

st.table(df.head(10))"""

st.code(code_de_aratat)