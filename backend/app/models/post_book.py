from sqlalchemy import Column, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from app.db.base import Base

class PostBook(Base):
    __tablename__ = "post_book"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    post_id = Column(UUID(as_uuid=True), ForeignKey("post.id", ondelete="CASCADE"), nullable=False)
    book_id = Column(UUID(as_uuid=True), ForeignKey("book.id", ondelete="CASCADE"), nullable=False)
    note = Column(Text)
    is_primary = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
