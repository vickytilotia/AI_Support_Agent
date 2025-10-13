from fastapi import APIRouter
# from app.services.rag_engine import RAGEngine
from app.services.llm_agent import LLMResponder
from app.services.memory_cache import cache_query, get_cached_answer, add_to_user_memory, get_user_memory


router = APIRouter()
# rag  = RAGEngine()
agent = LLMResponder()

# @router.on_event("startup")
# def load_data():
#     rag.load_faqs()
#     rag.load_pdfs()

@router.post("/")
async def chat_endpoint(query: str, user_id: str= "default_user"):
    # Check if cache first 
    cached = get_cached_answer(query)
    if cached:
        return {"query": query, "answer": cached, "source": "cache"}    
    
    # If not in cache, generate answer
    answer = agent.generate_answer(query)

    # Cache the answer 
    cache_query(query, answer)

    # Add to user memory
    add_to_user_memory(user_id, query, answer)

    # Retrieve short-term memory for context 
    memory = get_user_memory(user_id)


    return {"query": query, "answer": answer, "memory": memory, "source": "llm"}