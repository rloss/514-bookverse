from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base

class GroupActivitySchedule(Base):
    __tablename__ = "group_activity_schedule"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    activity_id = Column(UUID(as_uuid=True), ForeignKey("group_activity.id", ondelete="CASCADE"), nullable=False)
    schedule_id = Column(UUID(as_uuid=True), ForeignKey("schedule.id", ondelete="CASCADE"), nullable=False)
