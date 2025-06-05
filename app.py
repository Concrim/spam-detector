import streamlit as st
import pickle
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC


def predict_spam(phrase):
    phrase_vec = vectorizer.transform([phrase])
    phrase_pred = svm.predict(phrase_vec)
    if phrase_pred[0] == 0:
        return 'ham'
    else:
        return 'spam'


svm = pickle.load(open('svm.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.header('Spam Detection')
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.pexels.com/photos/5605061/pexels-photo-5605061.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1');
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
textbox = st.text_area("Please enter the text that you'd like to test")
if st.button('Enter'):
    st.text(predict_spam(textbox))
