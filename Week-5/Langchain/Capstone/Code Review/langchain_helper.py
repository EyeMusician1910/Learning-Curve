import os
from pathlib import Path
from dotenv import load_dotenv # ◄ New import

# LangChain core imports
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate  
from langchain_community.vectorstores import FAISS  
from langchain_core.output_parsers import StrOutputParser

# Gemini imports
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# ─── LOAD ENVIRONMENT VARIABLES ─────────────────────────────────
# This finds the .env file and injects GEMINI_API_KEY into your system variables
load_dotenv() 

# 1. Initialize Gemini Model (It automatically picks up GEMINI_API_KEY from os.environ)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.5
)

# 2. Update the helper embeddings model function
def get_embeddings_model():
    return GoogleGenerativeAIEmbeddings(
        model="text-embedding-004"
    )

def process_all_pdfs(pdf_directory):
    """Fast extraction of raw text from PDFs using PyMuPDF"""
    all_documents = []
    pdf_dir = Path(pdf_directory)
    pdf_files = list(pdf_dir.glob("**/*.pdf"))
    
    if not pdf_files:
        return []
        
    print(f"Found {len(pdf_files)} PDF files to process.")
    for pdf_file in pdf_files:
        try:
            loader = PyMuPDFLoader(str(pdf_file))
            documents = loader.load()
            
            for doc in documents:
                doc.metadata['source_file'] = pdf_file.name
                doc.metadata['file_type'] = 'pdf'
            
            all_documents.extend(documents)
        except Exception as e:
            print(f"Error loading {pdf_file.name}: {e}")
            
    return all_documents

def create_vector_store(documents) -> FAISS:
    """Splits documents and embeds them natively into your RTX A500 GPU VRAM"""
    if not documents:
        return None
        
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split data into {len(chunks)} text chunks.")
    
    embeddings = get_embeddings_model()
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store

def get_response_from_query(vectore_store, query, k=4):
    """Retrieves context and streams it to Llama3.1 for an answer"""
    docs = vectore_store.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])
    
    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template=(
            "You are a helpful assistant that answers questions based on the provided documents.\n\n"
            "CONTEXT DOCUMENTS:\n"
            "{docs}\n\n"
            "USER QUESTION:\n"
            "{question}\n\n"
            "Instructions: Answer the user's question accurately using only the facts found in the context documents above. "
            "If the answer cannot be found in the documents, say 'I cannot find the answer in the provided documents.'"
        )
    )
    
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"question": query, "docs": docs_page_content})
    return response