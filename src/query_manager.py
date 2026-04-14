import config.settings as settings

class QueryManager:
    def __init__(self, vector_db):
        self.vector_db = vector_db
    
    def get_relevant_context(self, query):
        relevant_docs = self.vector_db.similarity_search(query, k=settings.RETRIEVAL_K)
        
        context_text = "\n\n---\n\n".join([doc.page_content for doc in relevant_docs])
        return context_text
    
    def build_prompt(self, query):
        context = self.get_relevant_context(query)
        
        final_prompt = settings.PROMPT_TEMPLATE.format(
            context = context,
            question = query
        )
        return final_prompt