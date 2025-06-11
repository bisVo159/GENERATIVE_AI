import streamlit as st

st.title("Chapter 2: Streamlit Widgets")
st.header("Interactive Widgets in Streamlit")
st.subheader("Explore various input widgets")
st.text("This section demonstrates different input widgets in Streamlit.")
st.markdown("**Select your favorite fruit:**")
fruits = st.selectbox("Choose a fruit:", ["Apple", "Banana", "Cherry", "Date", "Elderberry"])
st.write(f"You selected: {fruits}")

ingredients = st.multiselect("Select ingredients for your smoothie:",
                            ["Strawberry", "Spinach", "Yogurt", "Honey","Almonds","Milk","Water"])

# st.write(ingredients)
for ingredient in ingredients:
    st.write(f"You added: {ingredient}")

st.slider("Sugar level (Spoon):", 0,5,2, step=1)

cups=st.number_input("Enter the number of servings:", min_value=1, max_value=10, value=1)
st.write("You selected", cups, "servings.")

name=st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

dob=st.date_input("Select your date of birth:")
st.write(f"Your date of birth is: {dob}")

juicer=st.checkbox("Do you have a juicer?", value=False)
if juicer:
    st.write("Great! You can make fresh juice with your fruits.")

if st.button("Submit"):
    st.success("Thank you for your submission!")


st.markdown("**Choose your favorite color:**")
colors = st.radio("Select a color:", ["Red", "Green", "Blue", "Yellow", "Purple"])
st.write(f"You chose: {colors}")
st.markdown("**Enter your feedback:**")
feedback = st.text_area("Your feedback here:")
st.write(f"Your feedback: {feedback}")