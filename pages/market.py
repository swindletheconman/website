import streamlit as st
import pandas as pd

data = pd.read_excel('./pages/source.xlsx')
#st.dataframe(data)

category_values = data['category'].unique()
selected_category = st.multiselect("Seclect Category", options=category_values,default=category_values)

store_values = data['store_name'].unique()
selected_store = st.multiselect("Seclect store", options=store_values,default=store_values)

minimum_price = data['price'].min()
maximum_price = data['price'].max()

price_range = st.slider("Price range",min_value=minimum_price,max_value=maximum_price)

#develop search criteria
criteria1 = data['category'].isin(selected_category)
criteria2 = data['store_name'].isin(selected_store)
criteria3 = data['price'] <= price_range

join_criteria = (criteria1) & (criteria2) & (criteria3)

#display the picture
st.image('./images/sabun_cuci_piring.jpeg')

criteria4 = data['price'] >= 10000
criteria5 = data['price'] <= 30000
criteria6 = (criteria4) & (criteria5)

#to apply the criteria
#st.dataframe(data[criteria1])
#st.dataframe(data[criteria2])
st.dataframe(data[criteria3])
#st.dataframe(data[criteria4])
#st.dataframe(data[criteria5])
#st.dataframe(data[criteria6])
