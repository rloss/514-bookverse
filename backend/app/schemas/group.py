from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class GroupCreate(BaseModel):
    name: str
    description: str | None = None

class GroupRead(BaseModel):
    id: UUID
    name: str
    description: str | None
    created_at: datetime

    class Config:
        from_attributes = True


from pydantic import BaseModel
from uuid import UUID

class GroupJoinRequest(BaseModel):
    group_id: UUID
    message: str | None = None