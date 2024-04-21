import os
from app import *

def main():
    with open('key.txt', 'r') as file: 
        line = file.readline()
    os.environ["OPENAI_API_KEY"] = line
    
    handle_streamlit_config()
    # handle_user_question()
    handle_side_bar()

if __name__ == '__main__':
    main()
