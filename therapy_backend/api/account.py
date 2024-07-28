from fastapi import APIRouter
from therapy_backend import db
from therapy_backend.core.db import SessionFactory
from therapy_backend.model import Account

router = APIRouter(prefix="/account", tags=["accounts"])


@router.get("/{accountId}")
async def getAccount(accountId: int):
    return {"message": "wazzzzup"}

@router.post("")
async def create_account(account: Account, session: SessionFactory) -> Account:
    return db.create_account(session, account)
