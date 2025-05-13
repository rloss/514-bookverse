from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.utils.enums import GroupActivityType, GroupActivityStatus

class GroupActivityBase(BaseModel):
    title: str
    description: str | None = None
    type: GroupActivityType
    status: GroupActivityStatus

class GroupActivityCreate(GroupActivityBase):
    group_id: UUID
    start_at: datetime | None = None
    end_at: datetime | None = None

class GroupActivityOut(GroupActivityBase):
    id: UUID
    group_id: UUID
    created_by: UUID | None
    created_at: datetime

    class Config:
        from_attributes = True
