from fastapi import APIRouter
from therapy_backend import db
from therapy_backend.core.db import SessionFactory
from therapy_backend.model import AccountBase, AccountCreate, Account

router = APIRouter(prefix="/account", tags=["accounts"])


@router.get("/{accountId}")
async def getAccount(accountId: int):
    return {"message": "wazzzzup"}


@router.post("")
async def create_account(account: AccountCreate, session: SessionFactory) -> AccountBase:
    account_db = Account.model_validate(account, update={"hashed_password": account.password})
    return db.create_account(session, account_db)
