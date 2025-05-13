from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, date

class ScheduleBase(BaseModel):
    title: str
    description: str | None = None
    scheduled_date: date

class ScheduleCreate(ScheduleBase):
    group_id: UUID
    activity_id: UUID | None = None

class ScheduleOut(ScheduleBase):
    id: UUID
    group_id: UUID
    activity_id: UUID | None
    created_by: UUID | None
    created_at: datetime

    class Config:
        from_attributes = True
