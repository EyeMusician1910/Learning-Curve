from dotenv import load_dotenv
load_dotenv()
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama

# Initialization
embeddings = OllamaEmbeddings(model="nomic-embed-text")

llm=ChatOllama(
    model="llama3.1",
    temperature=0.1,
)

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

docs= [WebBaseLoader(url).load() for url in urls]
docs_list=[item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250,chunk_overlap=0
)

docs_split= text_splitter.split_documents(docs_list)

# vectorstore= Chroma.from_documents(
#     documents=docs_split,
#     collection_name="rag-chroma",
#     embedding=embeddings,
#     persist_directory="./.chroma",
# )

retriever = Chroma(
    collection_name="rag-chroma",
    embedding_function=embeddings,  #  Fixed
    persist_directory="./.chroma",
).as_retriever()