import streamlit as st
import joblib
import numpy as np
st.title("House Price Prediction")

st.image("/Users/shaikmujeeburrahman/Downloads/nit_git_eda/naresh_it.jpeg")

model = joblib.load("house.pkl")

house_size = st.number_input("enter house size")
bedrooms = st.number_input("enter the number")
if st.button("predict"):
    features = np.array([[house_size,bedrooms]])
    price = model.predict(features)
    st.write(f"The house price is {price[0]}")


