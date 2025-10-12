from fastapi import FastAPI
from app.api import routes_chat, routes_ticket

app = FastAPI(title="AI Support Agent", version="1.0.0")

app.include_router(routes_chat.router, prefix="/chat", tags=["Chat"])
app.include_router(routes_ticket.router, prefix="/tickets", tags=["Tickets"])

@app.get("/")
def root():
    return {"message": "Welcome to the AI Support Agent API"}   