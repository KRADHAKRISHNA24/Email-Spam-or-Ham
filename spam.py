import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


st.image(r"C:\Users\G0d\Pictures\inno logo png.png")
st.title('EMAIL SPAM OR HAM CLASSIFIER')

model=pickle.load(open(r"C:\Users\G0d\Machine Learning\model.pkl", 'rb'))
model1=pickle.load(open(r"C:\Users\G0d\Machine Learning\model1.pkl","rb"))
email=st.text_area("Please Enter Your Email Text to Classify")

Evaluating=model1.transform([email])
prediction=model.predict(Evaluating)[0]

if st.button("Classify"):
    if prediction=='spam':
        st.write("This email is Spam")
        st.image(r"C:\Users\G0d\Pictures\spam png.jpeg")
    else:
        st.write("This email is Ham")
        st.image(r"C:\Users\G0d\Downloads\ham png.png")
