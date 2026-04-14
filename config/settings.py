import os

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
VECTOR_DB_DIR = os.path.join(DATA_DIR, "chroma_db")

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

VECTOR_DB_DIR = os.path.join(DATA_DIR, "chroma_db")