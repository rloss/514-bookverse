from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

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

class UserProfileOut(UserProfileBase):
    id: UUID
    user_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True

class UserProfileBase(BaseModel):
    bio: str | None = None
    profile_image_url: str | None = None
    website_url: str | None = None
    location: str | None = None

class UserProfileUpdate(UserProfileBase):
    pass