from typing import Optional
from pydantic import BaseModel

class ItemCreate(BaseModel):
    title: str
    owner_id: str

class ItemRead(BaseModel):
    id: int
    title: str
    owner_id: str

    model_config = {"from_attributes": True}
