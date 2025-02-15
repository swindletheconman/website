import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

data = pd.read_excel('./pages/source.xlsx')
#st.dataframe(data)
column1,column2,column3 = st.columns(3)

with column1:
  category_values = data['category'].unique()
  selected_category = st.multiselect("Seclect Category", options=category_values,default=category_values)

with column2:
  store_values = data['store_name'].unique()
  selected_store = st.multiselect("Seclect store", options=store_values,default=store_values)

with column3:
  minimum_price = data['price'].min()
  maximum_price = data['price'].max()
  price_range = st.slider("Price range",min_value=minimum_price,max_value=maximum_price)

#develop search criteria
criteria1 = data['category'].isin(selected_category)
criteria2 = data['store_name'].isin(selected_store)
criteria3 = data['price'] <= price_range

join_criteria = (criteria1) & (criteria2) & (criteria3)

#display the picture
columns = st.columns(4)

row_number = len(data[join_criteria])
for i in range(row_number):
  if i%4==0: #for even number
    col = columns[0]
  elif i%4 == 1:
    col = columns[1]
  elif i%4 == 2:
    col = columns[2]
  else:
    col = columns[3]
    
  with col:
    with st.container(border=True):
      st.image(data.iloc[i]['picture'])
      st.write(data.iloc[i]['name'])
      st.write(data.iloc[i]['price'])
      st.write(data.iloc[i]['store_name'])
      if st.button("Add to Cart", key= str(i)):
        st.write("item added to cart")
      if st.button("Purchase item", key= "a"+str(i)):
        st.write("Thank you for buying from us!")
        
#criteria4 = data['price'] >= 10000
#criteria5 = data['price'] <= 30000
#criteria6 = (criteria4) & (criteria5)

#to apply the criteria
#st.dataframe(data[criteria1])
#st.dataframe(data[criteria2])
#st.dataframe(data[criteria3])
#st.dataframe(data[criteria4])
#st.dataframe(data[criteria5])
#st.dataframe(data[criteria6])
