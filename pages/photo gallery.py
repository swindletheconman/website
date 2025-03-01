import streamlit as st
import os

folder = os.listdir('images')
length_of_images = len(folder)
ncolumns = 5

for i in range(length_of_images):
  for c in range(ncolumns):
    if i%ncolumns == c:
      col == columns[c]
      with col:
        with st.container(border=True):
          st.image(r'./images/'+folder[i])
