from fastapi import FastAPI
from app.api import routes_chat, routes_ticket
from app.core.database import init_db
from app.api import routes_analytics
import asyncio

app = FastAPI(title="AI Support Agent", version="1.0.0")

app.include_router(routes_chat.router, prefix="/chat", tags=["Chat"])
app.include_router(routes_ticket.router, prefix="/tickets", tags=["Tickets"])
app.include_router(routes_analytics.router, prefix="/analytics", tags=["Analytics"])

@app.on_event("startup")
async def startup_event():
    # Initialize database tables
    await init_db()
    print("✅ Database initialized")

@app.get("/")
def root():
    return {"message": "Welcome to the AI Support Agent API"}   