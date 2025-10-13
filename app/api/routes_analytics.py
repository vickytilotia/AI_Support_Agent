from fastapi import APIRouter
from app.services.analytics import get_analytics


router = APIRouter()


@router.get("/")
async def analytics():
    data = await get_analytics()
    return data
