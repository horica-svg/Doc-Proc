import os

import config.settings as settings
from src.document_processor import DocumentProcessor
from src.vector_store import VectorStoreManager

def main():
    if not os.path.exists(settings.DATA_DIR):
        os.makedirs(settings.DATA_DIR)
    
    processor = DocumentProcessor()
    pdf_path = os.path.join(settings.DATA_DIR, "Scrisoare_Intentie_Zafiu_Horia.pdf")
    
    if not os.path.exists(pdf_path):
        print(f"Sample PDF not found at {pdf_path}.")
        return
    
    chunks = processor.load_and_split(pdf_path)
    
    if chunks:
        vs_manager = VectorStoreManager()
        vector_db = vs_manager.create_database(chunks)
        
        query = "What are the main topics covered in the document?"
        results = vector_db.similarity_search(query, k=2)
        
        print("Search results:")
        for i, res in enumerate(results):
            print(f"Result {i+1}: (Page {res.metadata.get('page', 'N/A')}):")
            print(res.page_content[:150] + "...\n")

if __name__ == "__main__":
    main()