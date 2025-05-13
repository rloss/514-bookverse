from pydantic import BaseModel
from uuid import UUID
from datetime import date

class BookBase(BaseModel):
    title: str
    author: str
    publisher: str | None = None
    published_date: date | None = None
    description: str | None = None
    isbn: str | None = None
    image_url: str | None = None

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: UUID

    class Config:
        from_attributes = True
