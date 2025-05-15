from collections.abc import AsyncIterator
import os
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine

def get_url(): 
    db_pass = os.environ["DB_PASS"]
    db_host = os.environ["DB_HOST"]
    db_port = os.environ["DB_PORT"]
    return f"postgresql://{db_host}:{db_port}/therapy?user=therapy&password={db_pass}"

engine = create_engine(get_url(), echo=True)


async def get_db() -> AsyncIterator[Session]:
    with Session(engine) as session:
        yield session


SessionFactory = Annotated[Session, Depends(get_db)]
