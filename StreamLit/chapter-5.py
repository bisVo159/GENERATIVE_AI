import streamlit as st
import requests
st.title("Chapter 5: Live Currency Converter")

url="https://api.exchangerate-api.com/v4/latest/INR"
amount=st.number_input("Enter amount in INR:", min_value=1, value=1000)

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    st.write("Exchange Rates Data:")
    selected_currency=st.selectbox(options=list(data['rates'].keys()), label="Convert to", key="currency")
    if st.button("Convert"):
        rate = data['rates'].get(selected_currency,1)
        converted_amount = amount * rate
        st.success(f"{amount} INR is equal to {converted_amount:.2f} {selected_currency}.")
    else:
        st.info("Click the button to convert the amount.")

else:
    st.error("Failed to fetch convertion rates. Please try again later.")
