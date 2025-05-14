from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime

from app.models.comment import Comment
from app.schemas.comment import CommentCreate


def create_comment(db: Session, comment_data: CommentCreate, user_id: UUID) -> Comment:
    comment = Comment(
        post_id=comment_data.post_id,
        content=comment_data.content,
        author_id=user_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get_comments_for_post(db: Session, post_id: UUID) -> list[Comment]:
    return db.query(Comment).filter(Comment.post_id == post_id).order_by(Comment.created_at.asc()).all()


def delete_comment(db: Session, comment_id: UUID, user_id: UUID) -> bool:
    comment = db.query(Comment).filter(Comment.id == comment_id).first()

    if not comment or comment.author_id != user_id:
        return False

    db.delete(comment)
    db.commit()
    return True
