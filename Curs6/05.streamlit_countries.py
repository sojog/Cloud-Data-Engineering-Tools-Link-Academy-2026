import boto3
from botocore.config import Config
from botocore import UNSIGNED
import streamlit as st
import random

s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))

BUCKET_NAME = "noaa-ghcn-pds"

# file_dict = s3.list_objects_v2(Bucket=BUCKET_NAME)['Contents']
# print(file_dict)


countries = {}

with open("ghcnd-countries.txt", "r") as file_reader:
    file_lines = file_reader.readlines()
    for line in file_lines:
        abbr, country =  line.split(" ", 1)
        countries[abbr] = country.replace("\n", "")

print(countries)

st.header("Ghiceste tara")



# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


print("st.session_state:", st.session_state)


next_guess = random.choice(list(countries.keys()))

with st.chat_message("ai"):
    st.markdown(next_guess)

if mesaj := st.chat_input("Cum se numeste tara urmatoare?"):
   
    print("mesajul venit este", mesaj)

    st.session_state.messages.append({"role": "ai", "content": next_guess})

    print("st.session_state:", st.session_state)

    with st.chat_message("human"):
        st.session_state.messages.append({"role": "user", "content": mesaj})
        st.markdown(mesaj)

    with st.chat_message("ai"):
        if mesaj.lower() == countries[next_guess].lower():
            # st.session_state.messages.append(("ai", "Ai raspuns corect..."))
            st.session_state.messages.append({"role": "ai", "content": "Ai raspuns corect"})
            st.markdown("Ai raspuns corect...")
        else:
            
            # st.session_state.messages.append(("ai", f"Nu ai raspuns raspuns corect...Raspunsul corect era: {countries[next_guess]}"))
            st.session_state.messages.append({"role": "ai", "content":  f"Nu ai raspuns raspuns corect...Raspunsul corect era: {countries[next_guess]}"})
            st.markdown(f"Nu ai raspuns raspuns corect...Raspunsul corect era: {countries[next_guess]}")

    