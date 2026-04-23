#Connect and manage a session with our database
from pathlib import Path

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlmodel import SQLModel
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from fastapi import Depends


BASE_DIR = Path(__file__).resolve().parents[1]
DATABASE_PATH = BASE_DIR / "sqlite2.db"
DATABASE_URL = f"sqlite+aiosqlite:///{DATABASE_PATH.as_posix()}"
 
engine = create_async_engine(
    url=DATABASE_URL,
    echo=True,
    connect_args={
        "check_same_thread": False
    }
)

async def create_db_and_tables():
    async with engine.begin() as connection:  # using the async engine, we need to begin the connection
        await connection.run_sync(SQLModel.metadata.create_all)

async def get_session():
    async_session = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with async_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]
