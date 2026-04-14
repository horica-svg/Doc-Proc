import os

import config.settings as settings
from src.document_processor import DocumentProcessor
from src.vector_store import VectorStoreManager
from src.query_manager import QueryManager

def main():
    if not os.path.exists(settings.DATA_DIR):
        os.makedirs(settings.DATA_DIR)
    
    processor = DocumentProcessor()
    vs_manager = VectorStoreManager()
    vector_db = vs_manager.load_database()
    
    if not vector_db:
        pdf_path = os.path.join(settings.DATA_DIR, "manual_tehnic.pdf")
        if os.path.exists(pdf_path):
            chunks = processor.load_and_split_pdf(pdf_path)
            vector_db = vs_manager.create_database(chunks)
        else:
            print("Eroare: Baza de date nu există și nici fișierul PDF pentru indexare.")
            return

    query_manager = QueryManager(vector_db)
    
    user_query = "Cum se realizează mentenanța sistemului?"
    print(f"\n--- Întrebare utilizator: {user_query} ---")
    
    final_prompt = query_manager.build_prompt(user_query)
    
    print("\n" + "="*50)
    print("PROMPT FINAL PREGĂTIT PENTRU LLM")
    print("="*50)
    print(final_prompt)

if __name__ == "__main__":
    main()