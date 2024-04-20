import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def display_pdf_page(pdf_reader, current_page):
    # Get the total number of pages in the PDF file
    num_pages = len(pdf_reader.pages)
    
    # Display the current page number
    st.write(f"Page {current_page + 1} of {num_pages}")
    
    # Extract text from the current page and display it
    page = pdf_reader.pages[current_page]
    text = page.extract_text()
    st.text(text)
    
    # Provide an option to save the current page as a separate PDF file
    if st.button(f"Save Page {current_page + 1} as PDF"):
        save_page_as_pdf(pdf_reader, current_page)

def save_page_as_pdf(pdf_reader, current_page):
    # Create a new PDF writer object
    pdf_writer = PdfWriter()
    
    # Add the current page to the writer
    pdf_writer.add_page(pdf_reader.pages[current_page])
    
    # Define the output file path for the current page
    output_file_path = f"page_{current_page + 1}.pdf"
    
    # Write the current page to a new PDF file
    with open(output_file_path, 'wb') as output_file:
        pdf_writer.write(output_file)
    
    # Display a success message
    st.success(f"Page {current_page + 1} saved as '{output_file_path}'")

def main():
    # File uploader for PDF
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    if uploaded_file:
        # Read the PDF file
        pdf_bytes = uploaded_file.read()
        
        # Create a PDF reader object
        pdf_reader = PdfReader(BytesIO(pdf_bytes))
        
        # Current page state
        current_page = st.session_state.get('current_page', 0)
        
        # Display the current page
        display_pdf_page(pdf_reader, current_page)
        
        # Navigation buttons
        if current_page > 0:
            # Previous Page button
            if st.button("Previous Page"):
                st.session_state.current_page = current_page - 1
        
        # Next Page button
        if current_page < len(pdf_reader.pages) - 1:
            if st.button("Next Page"):
                st.session_state.current_page = current_page + 1

# Run the app
if __name__ == "__main__":
    main()
