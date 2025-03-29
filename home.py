import streamlit as st

st.header("Welcome to Haadi's WebApp")
st.write("Choose the app on the side bar")
st.write("Thank you, hope you enjoy it")

st.write("Security: uploaded data is not stored in github repository")

pages = {
    "Prodjects" : [
        st.Page("./pages/Conversion.py", title = "Converter"),
        st.Page("./pages/market.py", title = "Online Store"),
        st.Page("./pages/cashier_checkout.py", title = "Cashier"),
        st.Page("./pages/Triangle.py", title = "Triangle")
    ],
    "Tools" : [
        st.Page("./pages/photo gallery.py", title = "Rotate PDF"),
        st.Page("./pages/newapp.py", title = "Inventory Simulation"),
    ],
}

pg = st.navigation(pages)
pg.run()
