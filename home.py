import streamlit as st

st.header("Welcome to Haadi's WebApp")
st.write("Choose the app on the side bar")
st.write("Thank you, hope you enjoy it")

st.write("Security: uploaded data is not stored in github repository")

pages = {
    "Prodjects" : [
        st.Page("./pages/01_Unit Converter.py", title = "Converter"),
        st.Page("./pages/02_Online Marketplace.py", title - "Online Store"),
        st.Page("./pages/03_Cashier Webpp.py", title - "Cashier"),
        st.Page("./pages/04_Triangle Calculator.py", title = "Triangle")
    ],
    "Tools" : [
        st.Page("./pages/05_PDF Rotator.py", title = "Rotate PDF"),
        st.Page("./pages/06_Inventory Simulation.py", title = "Inventory Simulation"),
        st.Page("./pages/07_Batch Inventory Simulation.py", title = "Batch Inventory Simulation"),
        st.Page("./pages/09_Led Matrix Simulation.py", title = "Led Matrix Simulation")
    ],
}

pg = st.navigation(pages)
pg.run()
