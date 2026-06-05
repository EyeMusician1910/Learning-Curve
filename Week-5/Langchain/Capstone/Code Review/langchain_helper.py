import os
import sys
import io
from pathlib import Path
from dotenv import load_dotenv

# Core Modern LangChain & Tools
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyMuPDFLoader # ◄ Make sure this import is here

# Advanced Search Imports
from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever

load_dotenv()

# Initialize Llama 3.1 and Embeddings
llm = ChatOllama(model="llama3.1", temperature=0.1)
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# ─── ADD THIS: PDF PROCESSING FUNCTION (For ingest.py) ──────────────
def process_all_pdfs(pdf_directory: str):
    """Loads all PDFs in the data folder cleanly using PyMuPDF."""
    all_documents = []
    pdf_dir = Path(pdf_directory)
    pdf_files = list(pdf_dir.glob("**/*.pdf"))
    
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

# ─── ADD THIS: VECTOR STORE INITIALIZER (For ingest.py) ─────────────
def create_hybrid_vector_store(documents, faiss_path: str):
    """Splits text chunks and builds the base FAISS Vector Index."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    print(f"Split data into {len(chunks)} text chunks.")
    
    print("Building Core FAISS Vector Store...")
    faiss_db = FAISS.from_documents(chunks, embeddings)
    faiss_db.save_local(faiss_path)
    return faiss_db

# --- HELPER: RAW CHUNK REBUILDER FOR RUNTIME BM25 ---
def _get_raw_chunks():
    DATA_DIR = Path(os.getcwd()) / "data"
    all_documents = []
    if DATA_DIR.exists():
        for pdf_file in DATA_DIR.glob("**/*.pdf"):
            try:
                all_documents.extend(PyMuPDFLoader(str(pdf_file)).load())
            except:
                pass
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(all_documents)
# --- MODERN TOOL 1: HYBRID MATRIX RETRIEVER ---
@tool
def search_knowledge_base(query: str) -> str:
    """Useful when you need to search for programming concepts, specific code terms, 
    variable names, syntax, or rules directly from the loaded textbooks."""
    DB_INDEX_PATH = Path(os.getcwd()) / "faiss_index"
    if not DB_INDEX_PATH.exists():
        return "Knowledge base index missing. Run ingest.py first."
        
    faiss_db = FAISS.load_local(str(DB_INDEX_PATH), embeddings, allow_dangerous_deserialization=True)
    vector_retriever = faiss_db.as_retriever(search_kwargs={"k": 3})
    
    chunks = _get_raw_chunks()
    if not chunks:
        return "No text documents found in data folder to search."
    bm25_retriever = BM25Retriever.from_documents(chunks)
    bm25_retriever.k = 3
    
    hybrid_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, vector_retriever], 
        weights=[0.5, 0.5]
    )
    
    docs = hybrid_retriever.invoke(query)
    return "\n\n".join([f"[Source: {d.metadata.get('source_file', 'Unknown')}] {d.page_content}" for d in docs])

# --- MODERN TOOL 2: INTERNAL PYTHON SANDBOX EXECUTOR ---
@tool
def execute_python_code(code: str) -> str:
    """Useful to test, run, or verify Python code snippets. Pass raw valid Python code strings 
    to this tool to see their console outputs."""
    output_buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = output_buffer
    try:
        exec(code, {}, {})
        sys.stdout = old_stdout
        val = output_buffer.getvalue()
        return val if val.strip() else "Executed successfully with no printable output."
    except Exception as e:
        sys.stdout = old_stdout
        return f"Execution Error: {e}"

# --- THE MODERN RUNTIME LOOP (Replaces AgentExecutor) ---
class ModernAgentRunner:
    def __init__(self, model, tools, system_prompt: str):
        self.model = model.bind_tools(tools)
        self.tools = {t.name: t for t in tools}
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])

    def invoke(self, inputs: dict) -> dict:
        # Formulate prompt and run through LLM
        chain = self.prompt | self.model
        ai_msg = chain.invoke(inputs)
        
        # Check if the LLM decided it needs to call a tool
        if ai_msg.tool_calls:
            for tool_call in ai_msg.tool_calls:
                selected_tool = self.tools[tool_call["name"]]
                # Execute the tool dynamically
                tool_output = selected_tool.invoke(tool_call["args"])
                
                # Feed the tool output back into the model to get a final conversational answer
                final_prompt = ChatPromptTemplate.from_messages([
                    ("system", "Analyze the following tool output data to answer the user's request accurately."),
                    ("human", f"User Request: {inputs['input']}\n\nTool Results:\n{tool_output}")
                ])
                final_chain = final_prompt | llm
                final_msg = final_chain.invoke({})
                return {"output": final_msg.content}
                
        return {"output": ai_msg.content}

def get_agent_executor():
    """Initializes our modern, non-deprecated custom execution engine."""
    tools = [search_knowledge_base, execute_python_code]
    system_prompt = (
        "You are an advanced Agentic Code Reviewer. You have access to tools.\n"
        "If a user asks about programming, rules, or explanations, use 'search_knowledge_base' to pull facts.\n"
        "If a user asks you to write or verify scripts, run them using 'execute_python_code' to check for errors."
    )
    return ModernAgentRunner(llm, tools, system_prompt)