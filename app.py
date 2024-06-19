import streamlit as st
from langdetect import detect, LangDetectException

# Dictionary to map language codes to full names
LANGUAGES = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'bn': 'Bengali',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'zh': 'Chinese',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'et': 'Estonian',
    'fr': 'French',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'id': 'Indonesian',
    'it': 'Italian',
    'ja': 'Japanese',
    'kn': 'Kannada',
    'ko': 'Korean',
    'lt': 'Lithuanian',
    'lv': 'Latvian',
    'mk': 'Macedonian',
    'ml': 'Malayalam',
    'mr': 'Marathi',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'pa': 'Punjabi',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sr': 'Serbian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'es': 'Spanish',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'zu': 'Zulu',
    'yo': 'Yoruba'
}

st.title('Language Detection App')

text = st.text_area("Enter text:", "")

if st.button('Detect Language'):
    if text:
        try:
            language_code = detect(text)
            language_name = LANGUAGES.get(language_code, "Unknown")
            st.write(f"The detected language is: {language_name} ({language_code})")
        except LangDetectException as e:
            st.write("Error: Unable to detect language. Please enter more text.")
    else:
        st.write("Please enter some text to detect the language.")

