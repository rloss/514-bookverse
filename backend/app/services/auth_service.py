from app.models.user import User
from app.models.social_account import SocialAccount
from app.schemas.auth import SocialLoginRequest
from app.core.security import create_access_token
from sqlalchemy.orm import Session
import uuid, requests

def get_google_user_info(access_token: str) -> dict:
    resp = requests.get("https://www.googleapis.com/oauth2/v3/userinfo", headers={
        "Authorization": f"Bearer {access_token}"
    })
    if not resp.ok:
        raise Exception("Google token validation failed")
    return resp.json()

def social_login(request: SocialLoginRequest, db: Session):
    if request.provider != "google":
        raise Exception("Only Google login supported for now")

    profile = get_google_user_info(request.access_token)
    provider_user_id = profile["sub"]

    account = db.query(SocialAccount).filter_by(
        provider="google", provider_user_id=provider_user_id
    ).first()

    if account:
        user = db.query(User).filter_by(id=account.user_id).first()
    else:
        user = User(
            id=uuid.uuid4(),
            email=profile.get("email"),
            username=profile.get("name"),
            hashed_password="social_login"
        )
        db.add(user)
        db.flush()
        account = SocialAccount(
            user_id=user.id,
            provider="google",
            provider_user_id=provider_user_id,
            email=profile.get("email"),
            username=profile.get("name"),
            profile_image_url=profile.get("picture")
        )
        db.add(account)
        db.commit()

    token = create_access_token(user.id)
    return token, user