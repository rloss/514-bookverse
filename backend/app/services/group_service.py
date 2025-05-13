from sqlalchemy.orm import Session
from uuid import UUID
from app.models.group import Group
from app.models.group_user import GroupUser, GroupUserRole, GroupUserStatus
from app.schemas.group import GroupCreate

def create_group(db: Session, owner_id: UUID, group_data: GroupCreate) -> Group:
    group = Group(
        name=group_data.name,
        description=group_data.description,
        owner_id=owner_id,
    )
    db.add(group)
    db.commit()
    db.refresh(group)

    # 자동 그룹 등록
    group_user = GroupUser(
        group_id=group.id,
        user_id=owner_id,
        role=GroupUserRole.owner,
        status=GroupUserStatus.active,
    )
    db.add(group_user)
    db.commit()

    return group


def get_user_groups(db: Session, user_id: UUID):
    return (
        db.query(Group)
        .join(GroupUser)
        .filter(GroupUser.user_id == user_id)
        .all()
    )


def get_group_by_id(db: Session, group_id: UUID):
    return db.query(Group).filter(Group.id == group_id).first()


def request_to_join_group(db: Session, user_id: UUID, group_id: UUID):
    group_user = GroupUser(
        group_id=group_id,
        user_id=user_id,
        role=GroupUserRole.member,
        status=GroupUserStatus.pending,
    )
    db.add(group_user)
    db.commit()
    db.refresh(group_user)
    return {"msg": "Join request submitted", "group_user_id": str(group_user.id)}

