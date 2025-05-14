from fastapi import APIRouter

router = APIRouter()

@router.get("/posts")
async def my_posts():
    return {"my_posts": []}
