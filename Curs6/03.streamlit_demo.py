
import streamlit as st

st.header("Acesta este un header")

st.sidebar.write("Acesta este un side bar")

st.sidebar.date_input("Alege o data")

st.date_input("Alege o data")


st.slider("Alege o valoare", min_value=123, max_value=456)

st.text_input("Introdu un text")


st.chat_input("Introdu un text ca de chat")