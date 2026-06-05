import streamlit as st

st.header("Streamlit chat")

mesaj = st.chat_input("Ce vrei sa afli astazi?")
print("mesajul venit este", mesaj)

st.session_state.messages = []

print("st.session_state:", st.session_state)


if mesaj:
    st.session_state.messages.append(mesaj)
    print("st.session_state:", st.session_state)

    with st.chat_message("human"):
        st.markdown(mesaj)

    with st.chat_message("ai"):
        st.markdown("Foarte buna intrebarea...")