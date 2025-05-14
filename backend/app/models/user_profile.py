from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from app.db.base import Base

class UserProfile(Base):
    __tablename__ = "user_profile"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"), unique=True, nullable=False)
    bio = Column(Text)
    profile_image_url = Column(String)
    website_url = Column(String)
    location = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
