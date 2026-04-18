from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead

router = APIRouter()
@router.get("", response_model=list[UserRead])
async def list_users(
    db: Session = Depends(get_db),
):
    return db.query(User).all()

@router.post("", response_model=UserRead)
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
