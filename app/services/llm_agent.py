from langchain_community.llms import Ollama 
from app.services.rag_engine import RAGEngine


class LLMResponder:
    def __init__(self):
        self.llm = Ollama(model="mistral")   #local model
        self.rag = RAGEngine()
        self.rag.load_faqs()
        self.rag.load_pdfs()

    
    def generate_answer(self, user_query: str):
        """Retrieve context + generate final answer."""
        context_docs = self.rag.query(user_query) 
        context_text = "\n".join(context_docs)

        prompt = f""" 
        You are an helpful AI customer support assistant. 
        Use the following context to answer the user's query accurately.
        If the context doesn't contain the answer, say "I'm not sure, would you like me to create a support ticket?".

        CONTEXT:
        {context_text}
        USER QUERY:
        {user_query}

        RESPONSE:
        """

        response = self.llm.invoke(prompt)
        return response