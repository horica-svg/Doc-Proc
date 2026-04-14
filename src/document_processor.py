import os
import re
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import config.settings as settings

class DocumentProcessor:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            length_function=len,
            add_start_index=True
        )
    def clean_text(self, text):
        text = re.sub(r'(\w)\s(?\w)', r'\1', text)
        return re.sub(r'\s+', ' ', text).strip()
    def load_and_split(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at: {file_path}")
        
        try:
            print(f"Loading document from: {file_path}")
            loader = PyPDFLoader(file_path)
            
            pages = loader.load()
            for page in pages:
                page.page_content = self.clean_text(page.page_content)
            
            chunks = self.splitter.split_documents(pages)
            print(f"Document loaded and split into {len(chunks)} chunks.")
            return chunks
        except Exception as e:
            print(f"Ingestion error processing document: {str(e)}")
            return []