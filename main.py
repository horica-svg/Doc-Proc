import os
import config.settings as settings
from src.document_processor import DocumentProcessor
from src.vector_store import VectorStoreManager
from src.query_manager import QueryManager
from src.llm_manager import LLMManager

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def main():
    doc_processor = DocumentProcessor()
    vs_manager = VectorStoreManager()
    llm_manager = LLMManager()

    vector_db = vs_manager.load_database()
    
    if not vector_db:
        pdf_path = os.path.join(settings.DATA_DIR, "Scrisoare_Intentie_Zafiu_Horia.pdf")
        if os.path.exists(pdf_path):
            chunks = doc_processor.load_and_split_pdf(pdf_path)
            vector_db = vs_manager.create_database(chunks)
        else:
            print(f"ERROR: PDF file not found at:{settings.DATA_DIR}")
            return

    query_manager = QueryManager(vector_db)

    user_query = "Pentru ce firma este destinata aceasta scrisoare?"
    print(f"\n--- User Question: {user_query} ---")

    final_prompt = query_manager.build_prompt(user_query)
    
    answer = llm_manager.generate_answer(final_prompt)
    
    print("\n" + "="*50)
    print("GENERATED RESPONSE (Ollama):")
    print("="*50)
    print(answer)
    print("="*50)

if __name__ == "__main__":
    main()