from app.api.v1.routers import items
from fastapi import APIRouter
from app.api.v1.routers import users

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(items.router, prefix="/items", tags=["items"])
