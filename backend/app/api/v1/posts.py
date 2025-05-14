# backend/app/api/v1/posts.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.post import PostCreate, PostOut
from app.services.post_service import (
    create_post,
    get_all_posts,
    get_post_by_id,
    update_post,
    delete_post,
)

router = APIRouter(tags=["posts"])


@router.post("/", response_model=PostOut, status_code=status.HTTP_201_CREATED)
def create_new_post(
    post_data: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_post(db, user_id=current_user.id, post_data=post_data)


@router.get("/", response_model=list[PostOut])
def list_posts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_all_posts(db)


@router.get("/{post_id}", response_model=PostOut)
def get_post(
    post_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    post = get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/{post_id}", response_model=PostOut)
def edit_post(
    post_id: UUID,
    post_data: PostCreate,  # 단순화를 위해 PostCreate 재활용
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    post = update_post(db, post_id, post_data.dict())
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post_api(
    post_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    success = delete_post(db, post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return
