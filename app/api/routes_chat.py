from fastapi import APIRouter
from app.services.llm_agent import LLMResponder
from app.services.memory_cache import cache_query, get_cached_answer, add_to_user_memory, get_user_memory
from app.services.ticket_system import create_ticket
from app.services.analytics import record_cache_hit, record_llm_call
import asyncio

router = APIRouter()
agent = LLMResponder()


CONFIDENCE_THRESHOLD = 0.5  # Dummy logic for now

@router.post("/")
async def chat_endpoint(query: str, user_id: str= "default_user"):
    # Check if cache first 
    cached = get_cached_answer(query)
    if cached:
        record_cache_hit()
        return {"query": query, "answer": cached, "source": "cache"}    
    
    # If not in cache, generate answer
    answer = agent.generate_answer(query)
    record_llm_call()

    # Dummy "confidence" logic 
    if ("not sure" in answer) or len(answer) < 10:
        ticket = await create_ticket(user_id, query)
        ticket_msg = f"A support ticket has been created with ID: {ticket.id}. Our team will get back to you shortly."
        answer = f"{answer} {ticket_msg}"

    # Cache the answer 
    cache_query(query, answer)

    # Add to user memory
    add_to_user_memory(user_id, query, answer)

    # Retrieve short-term memory for context 
    memory = get_user_memory(user_id)


    return {"query": query, "answer": answer, "memory": memory, "source": "llm"}