from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.core.database import Base, AsyncSession, engine
import asyncio

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    query = Column(Text, nullable=False)
    resolved = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

async def create_ticket(user_id: str, query: str):
    async with AsyncSession(engine) as session:
        ticket = Ticket(user_id=user_id, query=query)
        session.add(ticket)
        await session.commit()
        await session.refresh(ticket)
        return ticket