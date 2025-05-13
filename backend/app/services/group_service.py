from app.models.group import Group
from app.models.group_user import GroupUser, GroupUserRole, GroupUserStatus
from app.schemas.group import GroupCreate
from sqlalchemy.orm import Session
from uuid import UUID

def create_group(db: Session, user_id: UUID, group_in: GroupCreate) -> Group:
    group = Group(
        name=group_in.name,
        description=group_in.description,
        owner_id=user_id,
    )
    db.add(group)
    db.flush()
    db.add(GroupUser(
        group_id=group.id,
        user_id=user_id,
        role=GroupUserRole.owner,
        status=GroupUserStatus.active
    ))
    db.commit()
    db.refresh(group)
    return group

def get_user_groups(db: Session, user_id: UUID) -> list[Group]:
    return db.query(Group).join(GroupUser).filter(
        GroupUser.user_id == user_id,
        GroupUser.status == GroupUserStatus.active
    ).all()

def request_to_join_group(db: Session, user_id: UUID, group_id: UUID):
    exists = db.query(GroupUser).filter_by(group_id=group_id, user_id=user_id).first()
    if exists:
        return exists  # 이미 요청 or 멤버

    gu = GroupUser(
        group_id=group_id,
        user_id=user_id,
        role=GroupUserRole.member,
        status=GroupUserStatus.pending
    )
    db.add(gu)
    db.commit()
    return gu
