import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.write("page x de fodase")

pdf_viewer("CS.pdf",width=700, height=500, pages_to_render=[1])

st.button("Previous")
st.button("Next")

st.write("summary")

st.write("ask me about it")
