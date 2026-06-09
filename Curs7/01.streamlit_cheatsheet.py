## Pentru instalare
##  pip install streamlit

## Pentru rulare
## streamlit run numele_fisierului.py
import streamlit as st

## Text

st.title("Acesta este titlul paginii")

st.header("Acesta este un header...")

st.subheader("Acesta este un subheader...")

st.text("Acesta este un text")

st.write("Acesta este tot un text")


## Linkuri
st.markdown("https://www.link-academy.com/")
st.markdown("[Website ul companiei](https://www.link-academy.com/)")

## HTML Direct
EXEMPLU_HTML = """   <div>
        <p style="color:blue;background-color:red;">
            Acesta este un exemplu de HTML clasic
        </p>
    </div>"""

st.markdown(EXEMPLU_HTML, unsafe_allow_html=True)


## Status
st.success("Acesta este un mesaj de success!")
st.error("Acesta este un mesaj de eroare!")
st.info("Acesta este un mesaj de info!")
st.warning("Acesta este un mesaj de warning!")

## Multimedia
st.video("https://www.youtube.com/shorts/_Ocd0RaX5Hg")

from PIL import Image
cat_image = Image.open("cat.jpeg")
st.image(cat_image)


## Interactiune
## # 1. Butoane
if st.button("Apasa"):
    st.text("Butonul a fost apasat")

## # 2. Radio Button
radio_button = st.radio("Alege dintre variantele", ["Spania", "Portugalia", "Franta", "Germania"]) 

if radio_button == "Spania":
    st.info("Ai ales spania")
elif radio_button == "Portugalia":
    st.info("Ai ales Portugalia")


## # 3. Select Box
select_box = st.selectbox("Alege dintre variantele", ["Spania", "Portugalia", "Franta", "Germania"]) 

if select_box == "Spania":
    st.info("Ai ales spania")
elif select_box == "Portugalia":
    st.info("Ai ales Portugalia")



## # 4. Multi Select Box
multi_select_box = st.multiselect("Alege dintre variantele", ["Spania", "Portugalia", "Franta", "Germania"]) 


## # 5. Input Text
input_text = st.text_input("Insereaza textul tau", "")
if input_text:
    st.write("Textul scris de tine este:", input_text)



## # 6. Number Text
input_number = st.number_input("Insereaza textul tau", min_value=10, max_value=123)
if input_number:
    st.write("Numarul scris de tine este:", input_number)


## # 7. Text Area
text_mai_mare = st.text_area("Insereaza textul tau")
if text_mai_mare:
    st.write("Textul tau scris de tine este:", text_mai_mare)