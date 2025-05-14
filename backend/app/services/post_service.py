# backend/app/services/post_service.py

from sqlalchemy.orm import Session
from uuid import UUID
from app.models.post import Post
from app.schemas.post import PostCreate
from datetime import datetime


def create_post(db: Session, user_id: UUID, post_data: PostCreate) -> Post:
    post = Post(
        author_id=user_id,
        group_id=post_data.group_id,
        activity_id=post_data.activity_id,
        title=post_data.title,
        content=post_data.content,
        category=post_data.category,
        visibility=post_data.visibility,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_all_posts(db: Session) -> list[Post]:
    return db.query(Post).order_by(Post.created_at.desc()).all()


def get_post_by_id(db: Session, post_id: UUID) -> Post | None:
    return db.query(Post).filter(Post.id == post_id).first()


def update_post(db: Session, post_id: UUID, new_data: dict) -> Post | None:
    post = get_post_by_id(db, post_id)
    if not post:
        return None

    for key, value in new_data.items():
        setattr(post, key, value)
    post.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(post)
    return post


def delete_post(db: Session, post_id: UUID) -> bool:
    post = get_post_by_id(db, post_id)
    if not post:
        return False
    db.delete(post)
    db.commit()
    return True
