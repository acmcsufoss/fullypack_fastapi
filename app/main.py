from fastapi import Depends, FastAPI
from app.api.v1 import router as api_v1_router

app = FastAPI(title="fullypack_fastapi")

app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the fullypack_fastapi!"}