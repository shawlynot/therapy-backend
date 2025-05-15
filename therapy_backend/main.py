from fastapi import FastAPI, APIRouter
from therapy_backend.api import account

api_router = APIRouter(
    prefix="/api/v1"
)

app = FastAPI()
app.include_router(api_router)
