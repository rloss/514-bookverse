from pydantic import BaseModel
from uuid import UUID

class GroupActivityScheduleBase(BaseModel):
    activity_id: UUID
    schedule_id: UUID

class GroupActivityScheduleCreate(GroupActivityScheduleBase):
    pass

class GroupActivityScheduleOut(GroupActivityScheduleBase):
    id: UUID

    class Config:
        from_attributes = True
