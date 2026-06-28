import streamlit as st
import numpy as np
import pandas as pd
import pickle as pkl

st.title("Car Price Prediction App")

pipe = pkl.load(open("pipe.pkl","rb+"))
df = pd.read_csv("final_data.csv")
companies = sorted(df["company"].unique())
years = range(2000,2027)

company = st.sidebar.selectbox("Select company",companies)

names = sorted(df[df['company'] == company]["name"].unique())

name = st.sidebar.selectbox("Select name",names)
year = st.sidebar.selectbox("Select year",years)
kms_driven = st.sidebar.number_inputs("Enter km driven", value=50000, min_value=1000,max_va=200000)
fuel = st.sidebar.selectbox("Select fuel type",["Petrol","Disel"])

if st.sidebar.button("Predict Price"):
    st.write("You have selected:")
    st.write("Company:{company}")
    st.write("Name: {name}")
    st.write("Year: {year}")
    st.write("Kilometers Driven: {km_driven}")
    st.write("Fuel Type: {furl}")

    #check for user input
    myinput = [[company, name, year, km_driven, fuel]]
    columns = ['company','name','year','kms_driven','furl_type']
    myinput = pd.DataFreame(data = myinput, colunms = columns)
    result = pipe.predict(myinput)

    if result[0,0] < 0:
        st.write("Sorry, the predicted price is negative. Please check your input values.")
    else:
        st.write("Predicted Price is:", str(round(result[0,0])))
