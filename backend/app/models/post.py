from sqlalchemy import Column, Enum as SQLEnum, ForeignKey, DateTime, Text, String
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.db.base import Base
from app.utils.enums import PostCategory, PostVisibility

class Post(Base):
    __tablename__ = "post"

    id = Column(UUID(as_uuid=True), primary_key=True)
    author_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="SET NULL"))
    group_id = Column(UUID(as_uuid=True), ForeignKey("group.id", ondelete="SET NULL"))
    activity_id = Column(UUID(as_uuid=True), ForeignKey("group_activity.id", ondelete="SET NULL"))

    category = Column(SQLEnum(PostCategory, name="post_category", native_enum=False), nullable=False)
    visibility = Column(SQLEnum(PostVisibility, name="post_visibility", native_enum=False), nullable=False)

    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
