from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_ticket(issue:str):
    # will add db logic later
    return {"message": f"Ticket created for issue: {issue}"}