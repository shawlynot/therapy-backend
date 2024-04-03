from fastapi import APIRouter
from therapy_backend.model import CreateAccount, Account

router = APIRouter(prefix="/account", tags=["accounts"])


@router.get("/{accountId}")
async def getAccount(accountId: int):
    return {"message": "wazzzzup"}

@router.post("")
async def createAccount(account: CreateAccount) -> Account:
    dbAccount = Account(
        fullname = account.fullname,
        preferredname = account.preferredname,
        email = account.email,
        accountType = account.accounttype
    )
    
    return dbAccount

@router.put("/{accountId}")
async def updateAccount(accountId: int):
    pass