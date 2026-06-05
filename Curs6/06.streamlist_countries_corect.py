import random
import streamlit as st

# Încarcă țările
countries = {}

with open("ghcnd-countries.txt", "r") as file_reader:
    for line in file_reader:
        abbr, country = line.split(" ", 1)
        countries[abbr] = country.strip()

st.header("Ghiceste tara")

# Inițializare stare
if "messages" not in st.session_state:
    st.session_state.messages = []

    # Prima întrebare
    first_guess = random.choice(list(countries.keys()))

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": first_guess,
        }
    )

# Afișează istoricul
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input utilizator
if user_answer := st.chat_input("Cum se numeste tara urmatoare?"):

    # Ultima întrebare AI (codul țării)
    current_guess = st.session_state.messages[-1]["content"]

    # Salvează răspunsul utilizatorului
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_answer,
        }
    )

    # Verifică răspunsul
    if user_answer.strip().lower() == countries[current_guess].lower():
        ai_response = "Ai raspuns corect ✅"
    else:
        ai_response = (
            f"Nu ai raspuns corect ❌\n\n"
            f"Raspunsul corect era: **{countries[current_guess]}**"
        )

    # Salvează feedback-ul AI
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_response,
        }
    )

    # Generează următoarea întrebare
    next_guess = random.choice(list(countries.keys()))

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": next_guess,
        }
    )

    st.rerun()