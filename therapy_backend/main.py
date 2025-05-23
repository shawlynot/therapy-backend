from fastapi import FastAPI, APIRouter
from therapy_backend.api import account

api_router = APIRouter(
    prefix="/api/v1"
)

api_router.include_router(account.router)

app = FastAPI()
app.include_router(api_router)
