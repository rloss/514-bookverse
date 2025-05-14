from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class PostBookBase(BaseModel):
    post_id: UUID
    book_id: UUID
    note: str | None = None
    is_primary: bool = False

class PostBookCreate(PostBookBase):
    pass

class PostBookOut(PostBookBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
