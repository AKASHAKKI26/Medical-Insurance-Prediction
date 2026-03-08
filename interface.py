import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("insurance_model.pkl", "rb"))
st.title("⚕️ Medical Insurance Charges Prediction")
age = st.selectbox("Select Age",list(range(18,65)))
bmi = st.selectbox("Select BMI",list(range(15,50)))
children = st.selectbox("Number of Children",[0,1,2,3,4,5])
smoker = st.selectbox("Smoker",["Yes","No"])
if smoker=="Yes":
    smoker_val=1
else:
    smoker_val=0

interaction=smoker_val*bmi

if st.button("Predict Insurance Charges"):
    prediction=model.predict([[age,bmi,children,smoker_val,interaction]])
    st.success(f"The Insurance Charges are:{prediction[0]:.2f}")




