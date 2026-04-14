import os

CHUNK_SIZE = 500
CHUNK_OVERLAP = 150

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
VECTOR_DB_DIR = os.path.join(DATA_DIR, "chroma_db")

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

VECTOR_DB_DIR = os.path.join(DATA_DIR, "chroma_db")

LLM_MODEL_NAME = "llama3.2:1b"
OLLAMA_BASE_URL = "http://host.docker.internal:11434"

RETRIEVAL_K = 2

PROMPT_TEMPLATE = """You are an assistant that helps answer
                    questions based on the following document
                    chunks. Use the provided chunks to answer
                    the question as accurately as possible. If
                    you don't know the answer, say you don't know, 
                    DO NOT make up an answer. Always use the 
                    provided chunks to answer the question.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""