import streamlit as st
from langdetect import detect, LangDetectException

st.title('Language Detection App')

text = st.text_area("Enter text:", "")

if st.button('Detect Language'):
    if text:
        try:
            language = detect(text)
            st.write(f"The detected language is: {language}")
        except LangDetectException as e:
            st.write("Error: Unable to detect language. Please enter more text.")
    else:
        st.write("Please enter some text to detect the language.")
