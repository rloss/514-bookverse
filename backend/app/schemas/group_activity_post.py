from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class GroupActivityPostBase(BaseModel):
    activity_id: UUID
    post_id: UUID
    book_id: UUID | None = None
    participation_style: str | None = None

class GroupActivityPostCreate(GroupActivityPostBase):
    pass

class GroupActivityPostOut(GroupActivityPostBase):
    id: UUID
    submitted_at: datetime

    class Config:
        from_attributes = True
