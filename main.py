import os
from app import *

def main():
    with open('key.txt', 'r') as file: 
        line = file.readline()
    os.environ["OPENAI_API_KEY"] = line
    
    handle_streamlit_config()
    uploaded_file = handle_side_bar()

    
    # handle_user_question(pdf_reader, current_page)
    if uploaded_file:
            
            # Read the PDF file
            pdf_bytes = uploaded_file.read()
            
            # Create a PDF reader object
            pdf_reader = PdfReader(BytesIO(pdf_bytes))
            
            # Current page state
            current_page = st.session_state.get('current_page', 0)

            column1, column2 = st.columns([.1,1])

            # Navigation buttons
            if current_page > 0:
                # Previous Page button
                if column1.button(":arrow_left:"):
                    st.session_state.current_page = current_page - 1
            
            # Next Page button
            if current_page < len(pdf_reader.pages) - 1:
                if column2.button(":arrow_right:"):
                    st.session_state.current_page = current_page + 1
            
            # Display the current page
            display_pdf_page(pdf_reader, current_page, uploaded_file)
            

if __name__ == '__main__':
    main()
