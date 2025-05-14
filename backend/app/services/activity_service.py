from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime
from app.models.group_activity import GroupActivity
from app.schemas.group_activity import GroupActivityCreate
from app.models.user import User


def create_activity(db: Session, creator: User, activity_data: GroupActivityCreate) -> GroupActivity:
    new_activity = GroupActivity(
        id=UUID(),  # 또는 uuid.uuid4()
        group_id=activity_data.group_id,
        type=activity_data.type,
        status=activity_data.status,
        title=activity_data.title,
        description=activity_data.description,
        start_at=activity_data.start_at,
        end_at=activity_data.end_at,
        created_by=creator.id,
        created_at=datetime.utcnow()
    )
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    return new_activity


def list_group_activities(db: Session, group_id: UUID) -> list[GroupActivity]:
    return db.query(GroupActivity).filter(GroupActivity.group_id == group_id).all()


def get_activity_detail(db: Session, activity_id: UUID) -> GroupActivity | None:
    return db.query(GroupActivity).filter(GroupActivity.id == activity_id).first()
