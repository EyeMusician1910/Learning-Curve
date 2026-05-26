import langchain_helper as lch
from pathlib import Path
import os

if __name__ == "__main__":
    BASE_DIR = Path(os.getcwd())
    DATA_DIR = BASE_DIR / "data"
    DB_INDEX_PATH = BASE_DIR / "faiss_index"

    # Ensure data directory exists
    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Created a blank 'data/' folder. Please drop your PDFs into: {DATA_DIR}")
        exit()

    print("🚀 Starting High-Speed Data Ingestion Pipeline...")
    documents = lch.process_all_pdfs(DATA_DIR)

    if documents:
        # This streams directly to your GPU via Ollama
        db = lch.create_vector_store(documents)
        
        # Save the vectors locally to disk
        db.save_local(str(DB_INDEX_PATH))
        print(f"\n🎉 Success! Vector Database built and saved to disk at: {DB_INDEX_PATH}")
        print("You can now safely run your Streamlit UI!")
    else:
        print(f"❌ Error: No PDF files found inside your data directory: {DATA_DIR}")