## Pentru instalare
##  pip install streamlit

## Pentru rulare
## streamlit run numele_fisierului.py
import streamlit as st
import requests



st.title("Calculeaza procent din pretul Bitcoin")
response = requests.get("https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT")
st.json(response.json())


input_number = st.number_input("Insereaza textul tau si apoi apasă ENTER", min_value=0.01, max_value=100.0, value=0.07)
if input_number:
    bitcoin = float(response.json()["price"])
    valoare_procentuala = bitcoin * input_number 
    st.write(f"{input_number} % dintr-un Bitcoin este:", round(valoare_procentuala, 2), "dolari")

 