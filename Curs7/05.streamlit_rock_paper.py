import streamlit as st
import random

OPTIONS = ["🪨", "📄", "✂"]


user_choice =st.radio("Your choice", OPTIONS)

if st.button("Play"):
    computer_choice = random.choice(OPTIONS)

    if user_choice == computer_choice:
        st.info("Egalitate")
    elif (user_choice == "🪨" and computer_choice == "✂") or (user_choice == "📄" and computer_choice == "🪨") or (user_choice == "✂" and computer_choice == "📄"):
        st.success("Ai castigat") 
    else:
        st.error("Ai pierdut")
        

