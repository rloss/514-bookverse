import os

# 기본 경로 설정
BASE_DIR = os.path.join(os.getcwd(), "app", "api", "v1")
os.makedirs(BASE_DIR, exist_ok=True)

# 라우터 파일들 + 기본 템플릿
router_templates = {
    "auth.py": """from fastapi import APIRouter

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
""",

    "users.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}
""",

    "books.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_books():
    return {"books": []}
""",

    "posts.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_posts():
    return {"posts": []}
""",

    "comments.py": """from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_comment():
    return {"msg": "Comment created"}
""",

    "groups.py": """from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_group():
    return {"msg": "Group created"}
""",

    "my.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/my/posts")
async def my_posts():
    return {"my_posts": []}
""",

    "groups_activities.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/{group_id}/activities")
async def get_group_activities(group_id: str):
    return {"group_id": group_id, "activities": []}
"""
}

# 파일 생성
for filename, content in router_templates.items():
    file_path = os.path.join(BASE_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ API 라우터 파일들 생성 완료.")
