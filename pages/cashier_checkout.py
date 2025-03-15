import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

dummy_data = {'description':['blueband','bread','egg'],
              'price':[12000,18000,15000],
              'quantity':[1,2,3]}

df = pd.DataFrame(dummy_data)
df['amount'] = df['price'] * df['quantity']

def printreceipt():
  content = f'my shop\n'
  content = f'----------\n'
  content = f'----------\n'
  return content 

leftcolumn,rightcolumn = st.columns(2)

with leftcolumn:
  pass
  with st.container(border=True):
    st.write("Check-out items:")
    st.dataframe(df)

  with st.container(border=True):
    st.write("Total:")
    total_amount = df['amount'].sum()
    st.write(f'{total_amount}')

  with st.container(border=True):
    st.write("Payment:")
    payment_received = st.number_input("Enter payment amount",min_value=0,step=1)

  with st.container(border=True):
    st.write("Return:")
    return_amount = payment_received - total_amount
    st.write(f'{return_amount}')

  with st.container():
    if st.button("print receipt"):
      if return_amount >= 0:
        printreceipt()
      else:
        st.warning('payment must be more or equal than the purchase')

with rightcolumn:
  pass
  with st.container(border=True):
    c = printreceipt()
    st.write(c)
