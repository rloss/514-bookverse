from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.schedule import ScheduleCreate, ScheduleOut
from app.services.schedule_service import (
    create_schedule,
    list_schedules_for_group,
    get_schedule_detail,
)

router = APIRouter(tags=["schedules"])


@router.post("/", response_model=ScheduleOut, status_code=status.HTTP_201_CREATED)
def create_schedule_endpoint(
    schedule_data: ScheduleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_schedule(db, schedule_data, current_user.id)


@router.get("/group/{group_id}", response_model=list[ScheduleOut])
def list_schedules_for_group_endpoint(
    group_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_schedules_for_group(db, group_id)


@router.get("/{schedule_id}", response_model=ScheduleOut)
def get_schedule_detail_endpoint(
    schedule_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    schedule = get_schedule_detail(db, schedule_id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule
