from fastapi import FastAPI

app = FastAPI()

@app.get("/account")
async def getAccount():
    return {"message": "wazzzzup"}

@app.post("/account")
async def createAccount():
    pass