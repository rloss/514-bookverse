from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime


# 기본 유저 스키마
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# 유저 프로필 관련 스키마
class UserProfileBase(BaseModel):
    bio: str | None = None
    profile_image_url: str | None = None
    website_url: str | None = None
    location: str | None = None

class UserProfileUpdate(UserProfileBase):
    pass

class UserProfileOut(UserProfileBase):
    id: UUID
    user_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
