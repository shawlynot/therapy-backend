from sqlmodel import create_engine

db_url = "postgresql://localhost:5432/therapy"

engine = create_engine(db_url, echo=True)