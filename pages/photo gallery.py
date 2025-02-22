import streamlit as st
import os

folder = os.listdir('images')
length_of_images = len(folder)

for i in range(ncolumns):
  for c in range(ncolumns):
    if i%ncolumns == c:
      col == columns[c]
      with col:
        with st.container(border=True):
