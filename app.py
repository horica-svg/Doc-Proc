import streamlit as st
import os
import config.settings as settings
from src.document_processor import DocumentProcessor
from src.vector_store import VectorStoreManager
from src.query_manager import QueryManager
from src.llm_manager import LLMManager

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

st.set_page_config(page_title="Doc-Proc", page_icon="📄")
st.title("📄 DocProc")

@st.cache_resource
def load_system():
    return DocumentProcessor(), VectorStoreManager(), LLMManager()

doc_proc, vs_manager, llm_manager = load_system()

with st.sidebar:
    st.header("Configure")
    uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])
    
    if uploaded_file:
        if not os.path.exists(settings.DATA_DIR):
            os.makedirs(settings.DATA_DIR)
            
        path = os.path.join(settings.DATA_DIR, uploaded_file.name)
        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        if st.button("Index Document"):
            with st.spinner("Processing..."):
                chunks = doc_proc.load_and_split(path)
                vs_manager.create_database(chunks)
                st.success("Document indexed!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask me something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    vector_db = vs_manager.load_database()
    if vector_db:
        query_mgr = QueryManager(vector_db)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                final_prompt = query_mgr.build_prompt(prompt)
                response = llm_manager.generate_answer(final_prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.warning("Please upload and index a document first.")