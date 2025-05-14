# backend/app/api/v1/comments.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.comment import CommentCreate, CommentOut
from app.services.comment_service import (
    create_comment,
    get_comments_for_post,
    delete_comment,
)

router = APIRouter(tags=["comments"])


@router.post("/", response_model=CommentOut, status_code=status.HTTP_201_CREATED)
def create_new_comment(
    comment_data: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_comment(db, comment_data, current_user.id)


@router.get("/post/{post_id}", response_model=list[CommentOut])
def list_comments_for_post(
    post_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_comments_for_post(db, post_id)


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment_api(
    comment_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    success = delete_comment(db, comment_id, current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Comment not found or not authorized")
