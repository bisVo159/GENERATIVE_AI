import streamlit as st

st.title("Chapter 3: Streamlit Dashboards")
st.markdown("## Welcome to voting dashboard")

col1,col2=st.columns(2)

with col1:
    st.header("Anik Biswas")
    st.image("https://images.pexels.com/photos/2854693/pexels-photo-2854693.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width=200)
    vote1=st.button("Vote for Anik")

with col2:
    st.header("Sayak Basu")
    st.image("https://images.pexels.com/photos/28245748/pexels-photo-28245748/free-photo-of-superman-chinatown-san-francisco.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width=200)
    vote2=st.button("Vote for Sayak")

if vote1:
    st.success("You voted for Anik Biswas!")
elif vote2:
    st.success("You voted for Sayak Basu!")
else:
    st.info("Please cast your vote!")

name=st.sidebar.text_input("Enter your name:")
vote=st.sidebar.selectbox("Enter your favorite:",["Anik", "Sayak", "Ayan", "Sayan", "Sourav"])
st.write(f"Hello, {name}! You voted for {vote}.")

with st.expander("See more details"):
    st.write('''This is an example of a Streamlit dashboard with two columns,
              each containing a profile picture and a vote button.
              You can vote for your favorite person, and the result will be displayed 
             below the buttons. Additionally, you can enter your name and select your favorite 
             person from the sidebar.''')
    
st.markdown("**Thank you for participating!**")