from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
import os


CURRENT_APP_DIR = os.path.dirname(os.path.abspath(__file__))


DATABASE_URL = f"sqlite+aiosqlite:///{os.path.join(CURRENT_APP_DIR, 'items.db')}"

engine = create_async_engine(DATABASE_URL, connect_args={"check_same_thread": False})

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as db:
        yield db