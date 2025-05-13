from fastapi import APIRouter

router = APIRouter()

@router.get("/my/posts")
async def my_posts():
    return {"my_posts": []}
