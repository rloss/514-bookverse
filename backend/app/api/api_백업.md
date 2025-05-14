# 📁 프로젝트 구조

```
├── 📄 api_백업.md
└── 📁 v1
    ├── 📄 auth.py
    ├── 📄 books.py
    ├── 📄 comments.py
    ├── 📄 groups.py
    ├── 📄 groups_activities.py
    ├── 📄 my.py
    ├── 📄 posts.py
    ├── 📄 schedules.py
    └── 📄 users.py
```

## 📄 `api_백업.md`

```markdown

```

## 📄 `v1\auth.py`

```python
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

```

## 📄 `v1\books.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_books():
    return {"books": []}

```

## 📄 `v1\comments.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_comment():
    return {"msg": "Comment created"}

```

## 📄 `v1\groups.py`

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.group import GroupCreate, GroupRead, GroupJoinRequest
from app.schemas.group import GroupJoinRequest
from app.services.group_service import (
    create_group,
    get_user_groups,
    request_to_join_group,
    get_group_by_id,
)

router = APIRouter(prefix="/groups", tags=["groups"])


@router.post("/", response_model=GroupRead, status_code=status.HTTP_201_CREATED)
def create_my_group(
    group_in: GroupCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_group(db=db, owner_id=current_user.id, group_data=group_in)


@router.get("/my", response_model=list[GroupRead])
def list_my_groups(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_user_groups(db=db, user_id=current_user.id)


@router.post("/{group_id}/join", status_code=status.HTTP_200_OK)
def join_group(
    group_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    group = get_group_by_id(db=db, group_id=group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return request_to_join_group(db=db, user_id=current_user.id, group_id=group_id)

@router.post("/join")
def join_group(
    join_request: GroupJoinRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return request_to_join_group(
        db=db,
        user_id=current_user.id,
        group_id=join_request.group_id,
        message=join_request.message
    )

```

## 📄 `v1\groups_activities.py`

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.group_activity import GroupActivityCreate, GroupActivityOut
from app.services.activity_service import (
    create_activity,
    list_group_activities,
    get_activity_detail,
)

router = APIRouter(prefix="/groups-activities", tags=["activities"])


@router.post("/", response_model=GroupActivityOut, status_code=status.HTTP_201_CREATED)
def create_group_activity(
    activity_data: GroupActivityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_activity(db, current_user, activity_data)


@router.get("/group/{group_id}", response_model=list[GroupActivityOut])
def get_activities_for_group(
    group_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_group_activities(db, group_id)


@router.get("/{activity_id}", response_model=GroupActivityOut)
def get_activity_by_id(
    activity_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    activity = get_activity_detail(db, activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity

```

## 📄 `v1\my.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/my/posts")
async def my_posts():
    return {"my_posts": []}

```

## 📄 `v1\posts.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_posts():
    return {"posts": []}

```

## 📄 `v1\schedules.py`

```python

```

## 📄 `v1\users.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

```

