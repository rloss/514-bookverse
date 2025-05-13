from sqlalchemy import Column, String, Date, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base

class Book(Base):
    __tablename__ = "book"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String)
    published_date = Column(Date)
    description = Column(Text)
    isbn = Column(String)
    image_url = Column(String)
