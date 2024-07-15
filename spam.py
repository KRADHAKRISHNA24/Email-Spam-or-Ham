import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


st.image(r"inno logo png.png")
st.title('EMAIL SPAM OR HAM CLASSIFIER')

model=pickle.load(open(r"model.pkl", 'rb'))
model1=pickle.load(open(r"model1.pkl","rb"))
email=st.text_area("Please Enter Your Email Text to Classify")

Evaluating=model1.transform([email])
prediction=model.predict(Evaluating)[0]

if st.button("Classify"):
    if prediction=='spam':
        st.write("This email is Spam")
        st.image(r"spam png.jpeg")
    else:
        st.write("This email is Ham")
        st.image(r"ham png.png")
