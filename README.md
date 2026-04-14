# Doc_Proc: Local RAG Document Processor

**Doc-Proc** is a specialized document processing application that leverages **Retrieval-Augmented Generation (RAG)** to enable natural language interaction with unstructured data (PDFs). The system is designed for **100% local execution**, ensuring total data privacy by utilizing quantized Large Language Models (LLMs) and on-premise vector databases.

## Key Features

- **End-to-End RAG Pipeline:** Seamless flow from raw PDF upload to context-aware response generation.
- **Semantic Retrieval:** Uses **Transformer-based embeddings** to perform similarity searches based on intent and context rather than simple keyword matching.
- **Local Intelligence:** Integrated with Llama 3.2 (via Ollama) to provide high-quality generative responses without external API calls.
- **Data Sanitization:** Includes custom text cleaning heuristics to handle PDF encoding artifacts (e.g., fragmented words), significantly improving indexing accuracy for small-scale models.
- **Privacy-First:** No data ever leaves the local machine, making it suitable for sensitive or proprietary documents.

## System Architecture

The application follows a modular architecture designed for scalability and maintainability:

1. **Ingestion**: Extracts raw text from PDFs using `PyPDF`.
2. **Cleaning & Chunking:** Sanitizes text and applies a **Recursive Character Splitting** strategy with overlap to preserve semantic boundaries.
3. **Embedding:** Transforms text chunks into high-dimensional vectors using the `all-MiniLM-L6-v2` sentence transformer.
4. **Vector Storage:** Manages persistent storage and indexing of embeddings via **ChromaDB**.
5. **Query Logic:** Retrieves the top-K most relevant chunks using cosine similarity.
6. **Response Generation:** Injects the retrieved context into a specialized prompt for the local LLM.

## Technologies Stack

**AI & MachineLearning:**

- **Python 3.10+**
- **LangChain:** For orchestrating the RAG pipeline.
- **Sentence-Transformers:** Deep Learning models for embedding generation.
- **Ollama:** Local serving of LLMs (optimized for Llama 3.2).
- **ChromaDB:** High-performance vector database for semantic search.

**Supporting skills and deployment:**

- **Streamlit:** For building the interactive web interface.
- **Docker:** Containerization for easy deployment and environment consistency.
- **Regular Expressions:** Custom text cleaning to handle PDF-specific formatting issues.

## Installation & Setup

**1. Prerequisites**

- Install Ollama and pull the lightweight model:
  ```bash
  ollama pull llama3.2:1b
  ```

**2. Enviroment Setup**:

- Run the following command to install the required Python libraries:
  ```bash
    pip install -r requirements.txt
  ```

**3. Running the Application**:

- Start the Streamlit app:
  ```bash
    streamlit run app.py
  ```

## Docker Deployment

- Build the Docker image:
  ```bash
    docker build -t doc-proc .
    docker run -p 8501:8501 doc-proc
  ```
