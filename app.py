import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from html_template import css, bot_template, user_template
from langchain.llms import HuggingFaceHub
from streamlit_pdf_viewer import pdf_viewer
import os
from io import BytesIO

def get_pdf_text(pdf):
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(temperature=0)
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
    )
    return conversation_chain


def handle_userinput(user_question, show_user = False):
    if(st.session_state.vector_store_created==False):
        st.error("The PDFs where not loaded properly..... please try reloading them again",  icon="🚨")
        return

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in reversed(list(enumerate(st.session_state.chat_history))):
        if i % 2 == 0 and show_user:
            pass
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        elif i % 2 == 1:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
            
def handle_streamlit_config():
    st.set_page_config(page_title="Chat with Arara",
                       page_icon="images/icon.png")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "vector_store_created" not in st.session_state:
        st.session_state.vector_store_created = False
    st.header("Chat with Arara :parrot:")

def call_pdf_render(page, name):
    pdf_viewer(name, width=700, height=500, pages_to_render=[page])
    #handle_user_question()

def display_pdf_page(pdf_reader, current_page, uploaded_file):
    # Get the total number of pages in the PDF file
    num_pages = len(pdf_reader.pages)
    
    # Display the current page number
    st.write(f"Page {current_page + 1} of {num_pages}")
    
    # Display pdf
    call_pdf_render(current_page + 1, uploaded_file.name)

    process_pdf(uploaded_file)

def process_pdf(uploaded_file):
     # get pdf text
    raw_text = get_pdf_text(uploaded_file)

    # get the text chunks
    text_chunks = get_text_chunks(raw_text)

    # create vector store
    vectorstore = get_vectorstore(text_chunks)
    st.session_state.vector_store_created = True

    # create conversation chain
    st.session_state.conversation = get_conversation_chain(vectorstore)


def handle_user_question(): # edit here

    b1 = st.button("Let's start learning!")

    b2 = st.button("I want to build flashcards!")

# TODOS: histórico das respostas, esconder as perguntas de prompt, take a look on this matter of the memory

    follow_up = "Give me topics to make flashcards about this material. Start by saying that you are happy for the journey with me and that I should keep up, say it's all about the analyzed pdf and that you are here to help on enhancing the understanding, without shortcuts"

    initial_question = "Start saying hello and being cordial. Explaining why is it important to understand this concept for a computer scientist, say that you can comment slide by slide and enrich the experience using an iteractive apporach, say that you can ask any question for help as well, start by making a opening question to me to grasp by attention. Show me as well the main bullet points of the material"


    if b1:
        handle_userinput(initial_question)

    if b2:
        handle_userinput(follow_up)
    
    user_question = st.text_input("Ask me aditional questions about this material: ") + ". Be friendly and act as a tutor and try making me engage with the material to help me understand and try making questions when possible"
    if user_question:
        handle_userinput(user_question)

def handle_side_bar():
    with st.sidebar:
        logo = open('images/logo.png', 'rb').read()
        st.image(logo)
        st.subheader("Your documents")
        uploaded_file = st.file_uploader("Upload your PDF here: ", type="pdf")

    return uploaded_file
