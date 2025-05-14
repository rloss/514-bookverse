from sqlalchemy.orm import Session
from app.models.user_profile import UserProfile
from app.schemas.user import UserProfileUpdate
from uuid import UUID

def get_profile(db: Session, user_id: UUID) -> UserProfile | None:
    return db.query(UserProfile).filter(UserProfile.user_id == user_id).first()

def upsert_profile(db: Session, user_id: UUID, update_data: UserProfileUpdate) -> UserProfile:
    profile = get_profile(db, user_id)
    if profile:
        for key, value in update_data.model_dump().items():
            setattr(profile, key, value)
    else:
        profile = UserProfile(user_id=user_id, **update_data.model_dump())
        db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile
