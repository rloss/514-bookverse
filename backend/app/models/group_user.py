from sqlalchemy import Column, ForeignKey, Enum as SQLEnum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.db.base import Base
from app.utils.enums import GroupUserRole, GroupUserStatus

class GroupUser(Base):
    __tablename__ = "group_user"

    id = Column(UUID(as_uuid=True), primary_key=True)
    group_id = Column(UUID(as_uuid=True), ForeignKey("group.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    role = Column(SQLEnum(GroupUserRole, name="group_user_role", native_enum=False), nullable=False)
    status = Column(SQLEnum(GroupUserStatus, name="group_user_status", native_enum=False), nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)
