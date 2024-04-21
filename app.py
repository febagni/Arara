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
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    if(st.session_state.vector_store_created==False):
        st.error("The PDFs where not loaded properly..... please try reloading them again",  icon="🚨")
        return

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in reversed(list(enumerate(st.session_state.chat_history))):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
            
def handle_streamlit_config():
    st.set_page_config(page_title="Chat with Arara",
                       page_icon=":parrot:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "vector_store_created" not in st.session_state:
        st.session_state.vector_store_created = False
    st.header("Chat with Arara :parrot:")
    logo = open('images/logo.png', 'rb').read()
    st.image(logo)

def call_pdf_render(page, name):
    pdf_viewer(name, width=700, height=500, pages_to_render=[page])
    handle_user_question()

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
    
    st.write("summary")
    
    user_question = st.text_input("Ask a question about your documents:  (Model: GPT-3.5-turbo · Generated content may be inaccurate or false)")
    if user_question:
        handle_userinput(user_question)

def handle_side_bar():
    flag = False
    with st.sidebar:
        st.subheader("Your documents")
        # uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
        uploaded_file = st.file_uploader(
            "Upload your PDF here: ", type="pdf")
        # if st.button("Process"):
        #     with st.spinner("Processing"):

                # # get pdf text
                # raw_text = get_pdf_text(uploaded_file)

                # # get the text chunks
                # text_chunks = get_text_chunks(raw_text)

                # # create vector store
                # vectorstore = get_vectorstore(text_chunks)
                # st.session_state.vector_store_created = True

                # # create conversation chain
                # st.session_state.conversation = get_conversation_chain(vectorstore)
    return uploaded_file
