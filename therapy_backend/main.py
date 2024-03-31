from fastapi import FastAPI

from therapy_backend.account.model import Account

app = FastAPI()

@app.get("/account/{accountId}")
async def getAccount(accountId: int):
    return {"message": "wazzzzup"}

@app.post("/account")
async def createAccount(account: Account):
    return account

@app.put("/account/{accountId}")
async def updateAccount(accountId: int):
    pass