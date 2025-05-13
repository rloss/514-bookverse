from sqlalchemy import Column, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from app.db.base import Base

class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    group_id = Column(UUID(as_uuid=True), ForeignKey("group.id", ondelete="CASCADE"))
    activity_id = Column(UUID(as_uuid=True), ForeignKey("group_activity.id", ondelete="SET NULL"))
    title = Column(String, nullable=False)
    description = Column(Text)
    scheduled_date = Column(Date, nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="SET NULL"))
    created_at = Column(DateTime, default=datetime.utcnow)
