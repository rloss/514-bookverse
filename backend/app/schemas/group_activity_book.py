from pydantic import BaseModel
from uuid import UUID

class GroupActivityBookBase(BaseModel):
    activity_id: UUID
    book_id: UUID
    selected: bool = False

class GroupActivityBookCreate(GroupActivityBookBase):
    pass

class GroupActivityBookOut(GroupActivityBookBase):
    id: UUID

    class Config:
        from_attributes = True
