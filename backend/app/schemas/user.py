from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserRead(UserBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
