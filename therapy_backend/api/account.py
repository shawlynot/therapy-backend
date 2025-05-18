from fastapi import APIRouter
from therapy_backend.core.db import ConnectionFactory

router = APIRouter(prefix="/account", tags=["accounts"])


@router.get("/{accountId}")
async def getAccount(accountId: int):
    return {"message": "wazzzzup"}


@router.post("")
async def create_account(session: ConnectionFactory):
    return {"message": "created"}
