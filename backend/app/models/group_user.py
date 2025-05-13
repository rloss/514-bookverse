from sqlalchemy import Column, Enum, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base
from datetime import datetime

class GroupUserRole(str, Enum):
    owner = "owner"
    admin = "admin"
    member = "member"

class GroupUserStatus(str, Enum):
    active = "active"
    pending = "pending"
    banned = "banned"

class GroupUser(Base):
    __tablename__ = "group_user"
    __table_args__ = (UniqueConstraint("group_id", "user_id"), )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    group_id = Column(UUID(as_uuid=True), ForeignKey("group.id", ondelete="CASCADE"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"))
    role = Column(Enum(GroupUserRole), nullable=False)
    status = Column(Enum(GroupUserStatus), nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)
