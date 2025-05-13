from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.group import GroupCreate, GroupRead
from app.services.group_service import create_group, get_user_groups
from app.core.security import get_current_user
from app.db.session import get_db
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=GroupRead)
def create_my_group(
    group_in: GroupCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_group(db, current_user.id, group_in)

@router.get("/my", response_model=list[GroupRead])
def list_my_groups(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_user_groups(db, current_user.id)
