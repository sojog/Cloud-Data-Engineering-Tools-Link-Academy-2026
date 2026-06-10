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
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(f"https://api.binance.com/api/v3/avgPrice?symbol=BTC{currency}", headers=headers, timeout=10, verify=False)
        responses.append((currency, float(response.json().get("price",response.status_code))))
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

 