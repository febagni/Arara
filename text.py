import streamlit as st
from PyPDF2 import PdfReader
from io import BytesIO

def display_pdf_page(pdf_bytes, current_page):
    # Create a PDF reader object
    pdf_reader = PdfReader(BytesIO(pdf_bytes))
    num_pages = len(pdf_reader.pages)
    
    # Display current page
    st.write(f"Page {current_page + 1} of {num_pages}")
    page = pdf_reader.pages[current_page]
    text = page.extract_text()
    st.text(text)

def main():
    # File uploader for PDF
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    if uploaded_file:
        # Read the PDF file
        pdf_bytes = uploaded_file.read()
        
        # Current page state
        current_page = st.session_state.get('current_page', 0)
        
        # Display the current page
        display_pdf_page(pdf_bytes, current_page)
        
        # Navigation buttons
        if current_page > 0:
            if st.button("Previous Page"):
                st.session_state.current_page = current_page - 1
        
        num_pages = len(PdfReader(BytesIO(pdf_bytes)).pages)
        if current_page < num_pages - 1:
            if st.button("Next Page"):
                st.session_state.current_page = current_page + 1

# Run the app
if __name__ == '__main__':
    main()