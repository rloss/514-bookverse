from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.utils.enums import PostCategory, PostVisibility

class PostBase(BaseModel):
    title: str
    content: str
    category: PostCategory
    visibility: PostVisibility

class PostCreate(PostBase):
    group_id: UUID | None = None
    activity_id: UUID | None = None

class PostOut(PostBase):
    id: UUID
    author_id: UUID | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    category: PostCategory | None = None
    visibility: PostVisibility | None = None
