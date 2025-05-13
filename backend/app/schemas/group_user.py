from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.utils.enums import GroupUserRole, GroupUserStatus

class GroupUserBase(BaseModel):
    group_id: UUID
    user_id: UUID
    role: GroupUserRole
    status: GroupUserStatus

class GroupUserCreate(GroupUserBase):
    pass

class GroupUserOut(GroupUserBase):
    id: UUID
    joined_at: datetime

    class Config:
        from_attributes = True
