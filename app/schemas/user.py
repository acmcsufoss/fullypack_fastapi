from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    id: str
    username: str
    email: Optional[EmailStr] = None

class UserRead(BaseModel):
    id: str
    username: str
    email: Optional[EmailStr] = None
    created_at: Optional[datetime] = None

    model_config = {"from_attributes": True}
