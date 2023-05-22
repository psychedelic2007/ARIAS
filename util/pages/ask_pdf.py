from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


def arias_ask():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"]{
            background-color: #b388eb;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    load_dotenv()
    st.header("Ask ARIAS 💬")

    # upload file
    st.subheader("Please upload your Research Paper")
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    api_key = st.text_input("Please enter your OpenAI API Key:")

    with st.form("question form"):
        user_question = st.text_input("Ask a question about your PDF:")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        if api_key:
            with st.spinner("ARIAS is scanning the document and preparing your anaswer....."):
                # extract the text
                if pdf is not None:
                    pdf_reader = PdfReader(pdf)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text()

                    # split into chunks
                    text_splitter = CharacterTextSplitter(
                        separator="\n",
                        chunk_size=1000,
                        chunk_overlap=200,
                        length_function=len
                    )
                    chunks = text_splitter.split_text(text)

                    # create embeddings
                    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
                    knowledge_base = FAISS.from_texts(chunks, embeddings)

                    # show user input
                    if user_question:
                        docs = knowledge_base.similarity_search(user_question)

                        llm = OpenAI()
                        chain = load_qa_chain(llm, chain_type="stuff")
                        with get_openai_callback() as cb:
                            response = chain.run(input_documents=docs, question=user_question)
                            print(cb)

                        st.write(response)
         else:
            st.error("Please enter your OPENAI API Key")
