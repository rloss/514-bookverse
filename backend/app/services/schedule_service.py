from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime

from app.models.schedule import Schedule
from app.schemas.schedule import ScheduleCreate


def create_schedule(db: Session, data: ScheduleCreate, created_by: UUID) -> Schedule:
    schedule = Schedule(
        group_id=data.group_id,
        activity_id=data.activity_id,
        title=data.title,
        description=data.description,
        scheduled_date=data.scheduled_date,
        created_by=created_by,
        created_at=datetime.utcnow(),
    )
    db.add(schedule)
    db.commit()
    db.refresh(schedule)
    return schedule


def list_schedules_for_group(db: Session, group_id: UUID) -> list[Schedule]:
    return db.query(Schedule).filter(Schedule.group_id == group_id).order_by(Schedule.scheduled_date).all()


def get_schedule_detail(db: Session, schedule_id: UUID) -> Schedule | None:
    return db.query(Schedule).filter(Schedule.id == schedule_id).first()
