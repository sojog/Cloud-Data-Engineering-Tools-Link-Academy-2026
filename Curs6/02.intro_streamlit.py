## pip install streamlit

import streamlit as st


x = st.slider("Select a value from 0 to 100")
st.write(x, "squared is", x * x)