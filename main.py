import os
from app import *

def main():
    with open('key.txt', 'r') as file: 
        line = file.readline()
    os.environ["OPENAI_API_KEY"] = line
    
    current_page = 0
    handle_streamlit_config()
    handle_user_question(current_page)
    handle_side_bar()

if __name__ == '__main__':
    main()
