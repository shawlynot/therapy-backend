from enum import StrEnum
from sqlmodel import SQLModel, Field
from pydantic import BaseModel

class AccountType(StrEnum):
    CLIENT = "CLIENT"
    PROFESSIONAL = "PROFESSIONAL"
    SUPPORT = "SUPPORT"

class Account(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    fullname: str
    preferredname: str
    email: str
    accounttype: AccountType
