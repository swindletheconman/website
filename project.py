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

pages = {
    "Prodjects" : [
        st.Page("./pages/Convsion.py", title = "Converter"),
        st.Page("./pages/Market.py", title = "Online Store"),
        st.Page("./pages/Cashier_checkout.py", title = "Cashier"),
        st.Page("./pages/04_Triangle.py", title = "Triangle")
    ],
    "Tools" : [
        st.Page("./pages/photo gallery.py", title = "Rotate PDF"),
        st.Page("./pages/newapp.py", title = "Inventory Simulation"),
    ],
}

pg = st.navigation(pages)
pg.run()
