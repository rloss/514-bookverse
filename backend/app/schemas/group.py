from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class GroupCreate(BaseModel):
    name: str
    description: str | None = None

class GroupRead(GroupCreate):
    id: UUID
    owner_id: UUID | None
    created_at: datetime

    class Config:
        orm_mode = True
