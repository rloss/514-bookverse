from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.group import GroupCreate, GroupRead, GroupJoinRequest
from app.schemas.group import GroupJoinRequest
from app.services.group_service import (
    create_group,
    get_user_groups,
    request_to_join_group,
    get_group_by_id,
)

router = APIRouter(prefix="/groups", tags=["groups"])


@router.post("/", response_model=GroupRead, status_code=status.HTTP_201_CREATED)
def create_my_group(
    group_in: GroupCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_group(db=db, owner_id=current_user.id, group_data=group_in)


@router.get("/my", response_model=list[GroupRead])
def list_my_groups(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_user_groups(db=db, user_id=current_user.id)


@router.post("/{group_id}/join", status_code=status.HTTP_200_OK)
def join_group(
    group_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    group = get_group_by_id(db=db, group_id=group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return request_to_join_group(db=db, user_id=current_user.id, group_id=group_id)

@router.post("/join")
def join_group(
    join_request: GroupJoinRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return request_to_join_group(
        db=db,
        user_id=current_user.id,
        group_id=join_request.group_id,
        message=join_request.message
    )
