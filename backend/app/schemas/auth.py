from pydantic import BaseModel
from app.schemas.user import UserOut

class SocialLoginRequest(BaseModel):
    provider: str  # 'google', etc.
    access_token: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class MeResponse(BaseModel):
    user: UserOut