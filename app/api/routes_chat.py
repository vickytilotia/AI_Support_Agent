from fastapi import APIRouter
# from app.services.rag_engine import RAGEngine
from app.services.llm_agent import LLMResponder

router = APIRouter()
# rag  = RAGEngine()
agent = LLMResponder()

# @router.on_event("startup")
# def load_data():
#     rag.load_faqs()
#     rag.load_pdfs()

@router.post("/")
async def chat_endpoint(query: str):
    answer = agent.generate_answer(query)
    return {"query": query, "answer": answer}