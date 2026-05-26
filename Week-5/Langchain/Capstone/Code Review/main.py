import streamlit as st
import langchain_helper as lch
from langchain_community.vectorstores import FAISS
from pathlib import Path
import os

st.set_page_config(layout="wide")
st.title("📚 Codey Q")

BASE_DIR = Path(os.getcwd())
DB_INDEX_PATH = BASE_DIR / "faiss_index"

# Load the completed index directly from disk in under 1 second
@st.cache_resource
def load_knowledge_base():
    if DB_INDEX_PATH.exists():
        embeddings = lch.get_embeddings_model()
        # allow_dangerous_deserialization is required to load local pickle/FAISS binaries safely
        return FAISS.load_local(str(DB_INDEX_PATH), embeddings, allow_dangerous_deserialization=True)
    return None

vector_db = load_knowledge_base()

# Sidebar Setup
with st.sidebar:
    st.header("App Management")
    if vector_db is not None:
        st.success("⚡ Database Loaded Successfully (On GPU)!")
        k_slider = st.slider("Context chunks to retrieve (k)", min_value=1, max_value=8, value=4)
    else:
        st.error("⚠️ Local Database Index Not Found!")
        st.info("Please stop this app and run 'python ingest.py' in your terminal first to process your PDFs.")

# Main Application Window
if vector_db is not None:
    # Change st.text_input to st.text_area
    user_query = st.text_area(
    "Ask a question about your 3,700 pages:", 
    placeholder="Paste your code or text here and press Ctrl+Enter to submit...",
    height=150  # Sets a nice initial box height (approx 3 lines tall)
)
    
    if user_query:
        with st.spinner("Searching database and generating response..."):
            try:
                answer = lch.get_response_from_query(vector_db, user_query, k=k_slider)
                st.subheader("💡 Answer:")
                st.write(answer)
            except Exception as e:
                st.error(f"An execution error occurred: {e}")