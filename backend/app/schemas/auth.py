from pydantic import BaseModel

class SocialLoginRequest(BaseModel):
    provider: str  # 'google', etc.
    access_token: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"