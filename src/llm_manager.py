from langchain_ollama import ChatOllama
import config.settings as settings

class LLMManager:
    def __init__(self):
        self.llm = None
        try:
            self.llm = ChatOllama(
                model = settings.LLM_MODEL_NAME,
                Base_url = settings.OLLAMA_BASE_URL,
                temerature = 0
            )
            print(f"Local LLM initialized with model: {settings.LLM_MODEL_NAME}")
        except Exception as e:
            print(f"Error initializing local LLM: {str(e)} ---")
        
    def generate_answer(self, final_prompt):
        try:
            response = self.llm.invoke(final_prompt)
            return response.content
        except Exception as e:
            return f"Error generating answer: {str(e)} ---"