## Pentru rulare
## streamlit run numele_fisierului.py
import streamlit as st
import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("kkhandekar/calories-in-food-items-per-100-grams", output_dir="calories", force_download=True)

print("Path to dataset files:", path)

@st.cache_data
def load_calories_data():
    df = pd.read_csv("calories/calories.csv")
    return df


df = load_calories_data()



print("sesiunea utilizatorului:", st.session_state)

if "food_list" not in st.session_state:
    st.session_state.food_list = []

print("sesiunea utilizatorului:", st.session_state)

st.table(df.head())

selected_food = st.selectbox("Alege un element pe care sa il folosesti", df["FoodItem"]) 


grams = st.number_input("Alege cantitatea (in grame)", min_value=0, value=100)

add_button = st.button("Adaugă în listă")

if add_button:
    print("Butonul a fost apasat")
    print("Selected food", selected_food)
    print("Gramaj", grams)

    food_row = df[df["FoodItem"] == selected_food].iloc[0]
    calories = int(food_row["Cals_per100grams"].split(" ")[0]) * grams / 100


    st.session_state.food_list.append({
        "Aliment":selected_food,
        "Gramaj": grams,
        "Calorii": calories
    })

    print("sesiunea utilizatorului:", st.session_state)


st.divider()

if st.session_state.food_list:
    food_df = pd.DataFrame(st.session_state.food_list)
    st.dataframe(food_df)

    total = food_df["Calorii"].sum()
    st.write(f"Totalul caloriilor {total}")


if st.button("X Sterge toate inregistrarile"):
    st.session_state.food_list = []