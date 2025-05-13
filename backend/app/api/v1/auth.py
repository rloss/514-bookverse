from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login():
    return {"msg": "Login"}

@router.post("/signup")
async def signup():
    return {"msg": "Signup"}

@router.get("/me")
async def get_me():
    return {"msg": "Current user info"}
