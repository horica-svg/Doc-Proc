import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import config.settings as settings

class VectorStoreManager:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL_NAME)
        
    def create_database(self, chunks):
        vector_db = Chroma.from_documents(
            documents = chunks,
            embedding = self.embeddings,
            persist_directory = settings.VECTOR_DB_DIR
        )
        print(f"Creating vector database with {len(chunks)} chunks...")
        
        return vector_db
    
    def load_database(self):
        if os.path.exists(settings.VECTOR_DB_DIR):
            print("Loading existing vector database...")
            return Chroma(
                persist_directory=settings.VECTOR_DB_DIR,
                embedding_function=self.embeddings)
        print("No existing vector database found.")
        return None