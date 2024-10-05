import uuid
from enum import StrEnum
from sqlmodel import SQLModel, Field


class AccountType(StrEnum):
    CLIENT = "CLIENT"
    PROFESSIONAL = "PROFESSIONAL"
    SUPPORT = "SUPPORT"


class AccountBase(SQLModel):
    fullname: str
    preferredname: str
    email: str
    accounttype: AccountType


# Database model, database table inferred from class name
class Account(AccountBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str


class AccountCreate(AccountBase):
    password: str
