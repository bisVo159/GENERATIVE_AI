import streamlit as st

st.title("My First Streamlit App")
st.header("Welcome to Streamlit")
st.subheader("This is a subheader")
st.text("This is a simple text display.")
st.markdown("**This is bold text**")
st.code("print('Hello, World!')", language='python')
st.latex(r"E = mc^2")
st.write("Hello, Streamlit!")


names=st.selectbox("Choose an option:", ["Anik", "Sayak", "Ayan", "Sayan", "Sourav"])
options=st.radio("Select an option:", ["Option 1", "Option 2", "Option 3"])
slide_value=st.slider("Select a value:", 0, 100, 50)
st.write(f"You selected: {names}")
st.write(f"You chose: {options}")   
st.write(f"Slider value: {slide_value}")
st.text_input("Enter your name:")
st.text_area("Enter your message:")
st.checkbox("Check me out!")    

st.success("This is a success message!")