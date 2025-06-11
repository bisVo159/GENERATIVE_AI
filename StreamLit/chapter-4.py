import streamlit as st
import pandas as pd

st.title("Chapter 4: Streamlit Data Display")

df=pd.DataFrame({
    "Name": ["Anik", "Sayak", "Ayan", "Sayan", "Sourav"],
    "Ratings": [5, 6, 4, 7, 8],
    "City": ["Dhaka", "Kolkata", "Mumbai", "Delhi", "Chennai"]
})

file=st.file_uploader("Upload a CSV file", type=["csv"])
if file:
    df=pd.read_csv(file)
st.write("Data from uploaded CSV file:")
st.subheader("Data Preview")
st.dataframe(df)

st.subheader("Summary Statistics")
st.write("This is a summary of the data:")
st.write(df.describe())

