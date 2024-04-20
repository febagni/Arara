import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


# Create two columns
col1, col2 = st.columns(2)

# Input fields for the first column
pdf_viewer("CS.pdf",width=700, height=500, pages_to_render=[1])

# Input fields for the second column
button = col2.button('fodase?')

