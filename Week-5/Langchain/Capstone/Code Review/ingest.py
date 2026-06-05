import langchain_helper as lch
from pathlib import Path
import os

if __name__ == "__main__":
    BASE_DIR = Path(os.getcwd())
    DATA_DIR = BASE_DIR / "data"
    DB_INDEX_PATH = BASE_DIR / "faiss_index"

    # Safety check for target data directories
    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Created blank data folder. Please drop your PDFs into: {DATA_DIR}")
        exit()

    print("🚀 Starting High-Speed Local Hybrid Data Ingestion Pipeline...")
    documents = lch.process_all_pdfs(DATA_DIR)

    if documents:
        # Calls the updated hybrid vector function from langchain_helper
        lch.create_hybrid_vector_store(documents, str(DB_INDEX_PATH))
        print(f"\n🎉 Success! Local Base Vector Index compiled at: {DB_INDEX_PATH}")
        print("You can now safely run your UI dashboard layout using 'streamlit run main.py'!")
    else:
        print(f"❌ Error: Please ensure you drop your PDF textbooks inside: {DATA_DIR}")