import joblib
import streamlit as st
import numpy as np

model = joblib.load("iris_model1.pkl")

st.title("Iris Flower Classification")
# Define the Streamlit app

# Input fields for features
sepal_length = st.number_input('Sepal Length (cm)', min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input('Sepal Width (cm)', min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input('Petal Length (cm)', min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input('Petal Width (cm)', min_value=0.0, max_value=10.0, step=0.1)

# Prediction button
if st.button('Predict'):
    # Make a prediction
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    if prediction[0] ==2:
        st.write("setosa")
    
    # Output the result
    st.write(f"The predicted class is: {prediction[0]}")