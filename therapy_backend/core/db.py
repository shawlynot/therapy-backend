from sqlmodel import create_engine, SQLModel
from therapy_backend.model import Account

db_url = "postgresql://localhost:5432/postgres?user=postgres&password=local"

engine = create_engine(db_url, echo=True)

SQLModel.metadata.create_all(engine)
