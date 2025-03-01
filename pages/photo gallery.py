import streamlit as st
import os

folder = os.listdir('images')
length_of_images = len(folder)

ncolumns = st.number_input("Column Configuration",min_value = 1, value = 4,step = 1)
columns = st.columns(ncolumns)

for i in range(length_of_images):
  for c in range(ncolumns):
    if i%ncolumns == c:
      col = columns[c]
      with col:
        with st.container(border=True):
          st.image(r'./images/'+folder[i])
