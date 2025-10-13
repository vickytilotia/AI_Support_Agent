from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./app/data/tickets.db")   

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

async def init_db():
    from app.services.ticket_system import Ticket  # Import models here to register them with Base
    async with engine.begin() as conn:
        # Pass bind=conn to create_all
        await conn.run_sync(lambda sync_conn: Base.metadata.create_all(bind=sync_conn))