from collections.abc import AsyncIterator
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine, SQLModel
from therapy_backend.model import Account

db_url = "postgresql://localhost:5432/postgres?user=postgres&password=local"

engine = create_engine(db_url, echo=True)

SQLModel.metadata.create_all(engine)

async def get_db() -> AsyncIterator[Session]:
    with Session(engine) as session:
        yield session

SessionFactory = Annotated[Session, Depends(get_db)]