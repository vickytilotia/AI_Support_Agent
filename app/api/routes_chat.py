from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def chat_endpoint(query: str):
    # will connect rag and llm later
    return {"response": f"Received query: {query}"}