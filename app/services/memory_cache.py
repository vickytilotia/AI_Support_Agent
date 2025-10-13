from app.core.redis_client import redis_client
import json

CACHE_TTL = 3600  # Cache time-to-live in seconds (1 hour)
MEMORY_KEY_PREFIX = "user_memory:"

def cache_query(query: str, answer: str):
    """Cache repeated query -> answer"""
    redis_client.setex(f"cache:{query}", CACHE_TTL, answer)

def get_cached_answer(query: str):
    """Retrieve cached answer if available."""
    return redis_client.get(f"cache:{query}")

def add_to_user_memory(user_id: str, query: str, answer: str, max_len=10):
    """Store last N interactions per user"""
    key = f"{MEMORY_KEY_PREFIX}{user_id}"
    entry = json.dumps({"query": query, "answer": answer})  
    redis_client.lpush(key, entry)
    redis_client.ltrim(key, 0, max_len - 1)  # Keep only the latest N entries   


def get_user_memory(user_id: str):
    """Retrieve user memory list"""
    key = f"{MEMORY_KEY_PREFIX}{user_id}"
    entries = redis_client.lrange(key, 0, -1)
    return [json.loads(e) for e in entries]