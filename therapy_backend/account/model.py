from enum import Enum
from pydantic import BaseModel

class AccountType(Enum):
    CLIENT = 1
    PROFFESIONAL = 2
    SUPPORT = 3

class Account(BaseModel):
    forename: str
    surname: str
    email: str
    type: AccountType