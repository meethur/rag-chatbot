import pdfplumber
import streamlit as st

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# ⚠️ Use environment variable instead in real apps
OPENAI_API_KEY="give your APIKEY"

st.title("RAG Chatbot")

file = st.file_uploader("Upload a PDF", type="pdf")

if file is not None:
    # ✅ Extract text
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"

    # ✅ Split text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_text(text)

    # ✅ Create embeddings
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=OPENAI_API_KEY
    )

    # ✅ Create vector store
    vector_store = FAISS.from_texts(chunks, embeddings)

    # ✅ Retriever
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})

    # ✅ LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3,
        openai_api_key=OPENAI_API_KEY
    )

    # ✅ Prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Answer using only the context:\n{context}"),
        ("human", "{question}")
    ])

    # ✅ Helper
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # ✅ Chain
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # ✅ User input
    user_question = st.text_input("Ask a question")

    if user_question:
        response = chain.invoke(user_question)
        st.write(response)

else:
    st.info("Please upload a PDF to start.")