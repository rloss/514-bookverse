from sqlalchemy import Column, Enum as SQLEnum, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.db.base import Base
from app.utils.enums import GroupActivityType, GroupActivityStatus

class GroupActivity(Base):
    __tablename__ = "group_activity"

    id = Column(UUID(as_uuid=True), primary_key=True)
    group_id = Column(UUID(as_uuid=True), ForeignKey("group.id", ondelete="CASCADE"), nullable=False)
    type = Column(SQLEnum(GroupActivityType, name="activity_type", native_enum=False), nullable=False)
    status = Column(SQLEnum(GroupActivityStatus, name="activity_status", native_enum=False), nullable=False)

    title = Column(String, nullable=False)
    description = Column(Text)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    created_by = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="SET NULL"))
    created_at = Column(DateTime, default=datetime.utcnow)
