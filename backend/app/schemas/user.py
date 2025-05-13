from pydantic import BaseModel
from uuid import UUID

class UserOut(BaseModel):
    id: UUID
    username: str
    email: str

    class Config:
        orm_mode = True
