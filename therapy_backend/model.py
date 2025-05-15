from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "User"
    user: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str] 
