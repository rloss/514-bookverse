from sqlalchemy import Column, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base

class GroupActivityBook(Base):
    __tablename__ = "group_activity_book"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    activity_id = Column(UUID(as_uuid=True), ForeignKey("group_activity.id", ondelete="CASCADE"), nullable=False)
    book_id = Column(UUID(as_uuid=True), ForeignKey("book.id", ondelete="CASCADE"), nullable=False)
    selected = Column(Boolean, default=False)
