from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_comment():
    return {"msg": "Comment created"}
