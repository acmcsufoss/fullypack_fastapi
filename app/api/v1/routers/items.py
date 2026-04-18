from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemRead

router = APIRouter()
@router.get("", response_model=list[ItemRead])
async def list_items(
    db: Session = Depends(get_db),
):
    return db.query(Item).all()

@router.post("", response_model=ItemRead)
async def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
