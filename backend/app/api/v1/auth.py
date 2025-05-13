from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.auth import SocialLoginRequest, TokenResponse
from app.services.auth_service import social_login

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/social-login", response_model=TokenResponse)
def login_social(request: SocialLoginRequest, db: Session = Depends(get_db)):
    try:
        token, user = social_login(request, db)
        return TokenResponse(access_token=token)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
