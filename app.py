from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain-community
from langchain-text-splitters
from langchain-core
from langchain-chroma
from langchain_groq import ChatGroq
from pypdf
import os

API_KEY = os.environ.get("GROQ_API_KEY"):

dados = "FaqSuportSaas.csv"
loader = PyPDFLoader(dados)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=15
)
chunks = text_splitter.split_documents(documentos)


embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="/tmp/chroma_db"
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


interface = gr.ChatInterface(
    fn=responder_chat,
    title="Agente de faq de SaaS",
    description="Quero que voce responde as duvida dos usuarios",
    examples=[
        "Como trocar meu plano",
        "como funciona a plataforma",
        "Como cancelar meu plano",
    ],
)






