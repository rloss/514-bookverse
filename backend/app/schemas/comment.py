from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    post_id: UUID

class CommentOut(CommentBase):
    id: UUID
    post_id: UUID
    author_id: UUID | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
