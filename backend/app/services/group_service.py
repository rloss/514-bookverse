from app.models.group import Group
from app.schemas.group import GroupCreate
from sqlalchemy.orm import Session
from app.models.group_user import GroupUser, GroupUserRole, GroupUserStatus
import uuid

def create_group(db: Session, user_id: uuid.UUID, group_in: GroupCreate) -> Group:
    group = Group(
        name=group_in.name,
        description=group_in.description,
        owner_id=user_id
    )
    db.add(group)
    db.flush()  # ID 확보
    db.add(GroupUser(
        group_id=group.id,
        user_id=user_id,
        role=GroupUserRole.owner,
        status=GroupUserStatus.active
    ))
    db.commit()
    db.refresh(group)
    return group

def get_user_groups(db: Session, user_id: uuid.UUID) -> list[Group]:
    return db.query(Group).join(GroupUser).filter(
        GroupUser.user_id == user_id,
        GroupUser.status == GroupUserStatus.active
    ).all()
