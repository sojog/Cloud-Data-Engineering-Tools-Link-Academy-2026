## Pentru instalare
##  pip install streamlit

## Pentru rulare
## streamlit run numele_fisierului.py
import streamlit as st
import requests


st.title("Calculeaza procent din pretul Bitcoin")

SYMBOLS = ["EUR", "USDT"]

def get_prices(symbols:list[str]):
    responses = []
    for currency in symbols:
        response = requests.get(f"https://api.binance.com/api/v3/avgPrice?symbol=BTC{currency}")
        responses.append((currency, float(response.json().get("price",0))))
    return responses

responses = get_prices(SYMBOLS)
for currency, price in  responses:
    st.json({"price":price, "currency": currency})


input_number = st.number_input("Insereaza textul tau si apoi apasă ENTER", min_value=0.01, max_value=100.0, value=0.07)
if input_number:
    text = f"{input_number} % dintr-un Bitcoin este: "
    for currency, price in  responses:
        valoare_procentuala = price * input_number 
        text += f"{round(valoare_procentuala, 2)} {currency}  "
    st.write(text)

 