import streamlit as st

with st.sidebar:
    st.write("Choose Web App")

st.title("Hello This is my Brand New Website")
st.header("Written with 100% Python code")
st.write("click the button for fun surprise")

if st.button("Snowflake"):
    st.snow()
    
if st.button("Balloon"):
    st.balloons()
    
st.write("I'll put something great here so stay tunned")
