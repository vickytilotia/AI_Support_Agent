from app.core.redis_client import redis_client
from app.services.ticket_system import Ticket
from sqlalchemy.future import select
from app.core.database import AsyncSession, engine 
import asyncio

CACHE_HITS_KEY = "analytics:cache_hits"
LLM_CALLS_KEY = "analytics:llm_calls"


# Increment cache hit count
def record_cache_hit():
    redis_client.incr(CACHE_HITS_KEY)

def record_llm_call():
    redis_client.incr(LLM_CALLS_KEY)

def get_cache_hits():
    hits = redis_client.get(CACHE_HITS_KEY)
    return int(hits) if hits else 0

def get_llm_calls():
    calls = redis_client.get(LLM_CALLS_KEY)
    return int(calls) if calls else 0

async def get_ticket_count():
    async with AsyncSession(engine) as session:
        result = await session.execute(select(Ticket))
        tickets = result.scalars().all()
        return len(tickets)

async def get_analytics():
    tickets = await get_ticket_count()
    cache_hits = get_cache_hits()
    llm_calls = get_llm_calls()
    total_queries = cache_hits + llm_calls
    return {
        "total_queries": total_queries,
        "cache_hits": cache_hits,
        "llm_calls": llm_calls,
        "ticket_count": tickets
    }