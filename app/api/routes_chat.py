from fastapi import APIRouter
from app.services.rag_engine import RAGEngine

router = APIRouter()
rag  = RAGEngine()

@router.on_event("startup")
def load_data():
    rag.load_faqs()
    rag.load_pdfs()

@router.post("/")
async def chat_endpoint(query: str):
    results = rag.query(query)
    return {"query": query, "retrieved_context": results}