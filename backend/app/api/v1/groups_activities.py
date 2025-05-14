from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.group_activity import GroupActivityCreate, GroupActivityOut
from app.services.activity_service import (
    create_activity,
    list_group_activities,
    get_activity_detail,
)

router = APIRouter(tags=["activities"])


@router.post("/", response_model=GroupActivityOut, status_code=status.HTTP_201_CREATED)
def create_group_activity(
    activity_data: GroupActivityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_activity(db, current_user, activity_data)


@router.get("/group/{group_id}", response_model=list[GroupActivityOut])
def get_activities_for_group(
    group_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_group_activities(db, group_id)


@router.get("/{activity_id}", response_model=GroupActivityOut)
def get_activity_by_id(
    activity_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    activity = get_activity_detail(db, activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity
