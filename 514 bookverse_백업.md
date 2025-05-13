# 📁 프로젝트 구조

```
├── 📄 .gitignore
├── 📄 514 bookverse_백업.md
├── 📄 README.md
├── 📁 backend
│   ├── 📄 .env
│   ├── 📁 alembic
│   │   └── 📁 versions
│   ├── 📁 app
│   │   ├── 📁 api
│   │   │   └── 📁 v1
│   │   │       ├── 📄 activities.py
│   │   │       ├── 📄 auth.py
│   │   │       ├── 📄 books.py
│   │   │       ├── 📄 comments.py
│   │   │       ├── 📄 groups.py
│   │   │       ├── 📄 posts.py
│   │   │       ├── 📄 schedules.py
│   │   │       └── 📄 users.py
│   │   ├── 📁 core
│   │   │   ├── 📄 config.py
│   │   │   ├── 📄 exceptions.py
│   │   │   ├── 📄 logging.py
│   │   │   └── 📄 security.py
│   │   ├── 📁 db
│   │   │   ├── 📄 base.py
│   │   │   ├── 📄 init_db.py
│   │   │   └── 📄 session.py
│   │   ├── 📄 main.py
│   │   ├── 📁 models
│   │   │   ├── 📄 activity.py
│   │   │   ├── 📄 base.py
│   │   │   ├── 📄 book.py
│   │   │   ├── 📄 comment.py
│   │   │   ├── 📄 group.py
│   │   │   ├── 📄 group_activity.py
│   │   │   ├── 📄 group_user.py
│   │   │   ├── 📄 post.py
│   │   │   ├── 📄 schedule.py
│   │   │   ├── 📄 social_account.py
│   │   │   └── 📄 user.py
│   │   ├── 📁 schemas
│   │   │   ├── 📄 activity.py
│   │   │   ├── 📄 auth.py
│   │   │   ├── 📄 book.py
│   │   │   ├── 📄 comment.py
│   │   │   ├── 📄 group.py
│   │   │   ├── 📄 group_activity.py
│   │   │   ├── 📄 group_user.py
│   │   │   ├── 📄 post.py
│   │   │   ├── 📄 schedule.py
│   │   │   └── 📄 user.py
│   │   ├── 📁 services
│   │   │   ├── 📄 activity_service.py
│   │   │   ├── 📄 auth_service.py
│   │   │   ├── 📄 book_service.py
│   │   │   ├── 📄 group_service.py
│   │   │   └── 📄 post_service.py
│   │   └── 📁 utils
│   │       ├── 📄 datetime.py
│   │       ├── 📄 enums.py
│   │       ├── 📄 hashing.py
│   │       └── 📄 id_generator.py
│   ├── 📄 requirements.txt
│   └── 📁 tests
├── 📄 bookverseERD.txt
├── 📁 docs
├── 📄 erd_schema.sql
├── 📁 frontend
│   ├── 📄 .env.production
│   ├── 📁 app
│   │   ├── 📁 books
│   │   │   └── 📁 [bookId]
│   │   ├── 📁 groups
│   │   │   └── 📁 [groupId]
│   │   │       ├── 📁 books
│   │   │       ├── 📁 calendar
│   │   │       ├── 📁 members
│   │   │       ├── 📁 my
│   │   │       ├── 📁 posts
│   │   │       └── 📁 settings
│   │   ├── 📄 layout.tsx
│   │   ├── 📁 login
│   │   ├── 📁 my
│   │   │   ├── 📁 books
│   │   │   ├── 📁 groups
│   │   │   ├── 📁 posts
│   │   │   └── 📁 settings
│   │   ├── 📄 page.tsx
│   │   ├── 📁 signup
│   │   └── 📁 write
│   ├── 📁 components
│   │   ├── 📁 auth
│   │   ├── 📁 book
│   │   ├── 📁 group
│   │   ├── 📁 layout
│   │   │   ├── 📄 RightSidebar.tsx
│   │   │   └── 📄 Topbar.tsx
│   │   ├── 📁 post
│   │   └── 📁 ui
│   ├── 📁 lib
│   │   └── 📁 api
│   │       ├── 📄 auth.ts
│   │       ├── 📄 books.ts
│   │       ├── 📄 groups.ts
│   │       ├── 📄 posts.ts
│   │       └── 📄 users.ts
│   ├── 📄 next.config.js
│   ├── 📄 package.json
│   ├── 📄 postcss.config.js
│   ├── 📁 public
│   ├── 📁 styles
│   │   └── 📄 globals.css
│   ├── 📄 tailwind.config.ts
│   └── 📄 tsconfig.json
└── 📄 requirements.txt
```

## 📄 `.gitignore`

```

```

## 📄 `514 bookverse_백업.md`

```markdown

```

## 📄 `bookverseERD.txt`

```
 Bookverse 데이터베이스 ERD v5.0 (2025-05-14 기준)
1. User
sql
복사
편집
User (
  id UUID PK,
  username VARCHAR NOT NULL,
  email VARCHAR UNIQUE NOT NULL,
  hashed_password VARCHAR NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
)
2. SocialAccount
sql
복사
편집
SocialAccount (
  id UUID PK,
  user_id UUID FK → User(id) ON DELETE CASCADE,
  provider VARCHAR CHECK ('google', 'kakao', 'github', 'naver'),
  provider_user_id VARCHAR NOT NULL,
  email VARCHAR,
  username VARCHAR,
  profile_image_url VARCHAR,
  created_at TIMESTAMP NOT NULL,
  UNIQUE (provider, provider_user_id)
)
3. UserProfile
sql
복사
편집
UserProfile (
  id UUID PK,
  user_id UUID FK → User(id) UNIQUE ON DELETE CASCADE,
  bio TEXT,
  profile_image_url VARCHAR,
  website_url VARCHAR,
  location VARCHAR,
  created_at TIMESTAMP NOT NULL
)
4. Group
sql
복사
편집
Group (
  id UUID PK,
  name VARCHAR NOT NULL,
  description TEXT,
  cover_image_url VARCHAR,
  owner_id UUID FK → User(id) ON DELETE SET NULL,
  created_at TIMESTAMP NOT NULL
)
5. GroupUser
sql
복사
편집
GroupUser (
  id UUID PK,
  group_id UUID FK → Group(id) ON DELETE CASCADE,
  user_id UUID FK → User(id) ON DELETE CASCADE,
  role VARCHAR CHECK ('owner', 'admin', 'member') NOT NULL,
  status VARCHAR CHECK ('active', 'pending', 'banned') NOT NULL,
  joined_at TIMESTAMP NOT NULL,
  UNIQUE (group_id, user_id)
)
6. Book
sql
복사
편집
Book (
  id UUID PK,
  title VARCHAR NOT NULL,
  author VARCHAR NOT NULL,
  publisher VARCHAR,
  published_date DATE,
  description TEXT,
  isbn VARCHAR,
  image_url VARCHAR
)
7. Post
sql
복사
편집
Post (
  id UUID PK,
  author_id UUID FK → User(id) ON DELETE SET NULL,
  group_id UUID FK → Group(id) ON DELETE SET NULL,
  activity_id UUID FK → GroupActivity(id) ON DELETE SET NULL,
  category VARCHAR CHECK ('review', 'announcement', 'community') NOT NULL,
  visibility VARCHAR CHECK ('public', 'group-only', 'private') NOT NULL,
  title VARCHAR NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
)
8. PostBook (N:M)
sql
복사
편집
PostBook (
  id UUID PK,
  post_id UUID FK → Post(id) ON DELETE CASCADE,
  book_id UUID FK → Book(id) ON DELETE CASCADE,
  note TEXT,
  is_primary BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP NOT NULL,
  UNIQUE (post_id, book_id)
)
9. Comment
sql
복사
편집
Comment (
  id UUID PK,
  post_id UUID FK → Post(id) ON DELETE CASCADE,
  author_id UUID FK → User(id) ON DELETE SET NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
)
10. GroupActivity
sql
복사
편집
GroupActivity (
  id UUID PK,
  group_id UUID FK → Group(id) ON DELETE CASCADE,
  type VARCHAR CHECK ('shared-reading', 'discussion', 'challenge') NOT NULL,
  title VARCHAR NOT NULL,
  description TEXT,
  start_at TIMESTAMP,
  end_at TIMESTAMP,
  created_by UUID FK → User(id) ON DELETE SET NULL,
  status VARCHAR CHECK ('planned', 'active', 'completed') NOT NULL,
  created_at TIMESTAMP NOT NULL
)
11. GroupActivityBook (N:M)
sql
복사
편집
GroupActivityBook (
  id UUID PK,
  activity_id UUID FK → GroupActivity(id) ON DELETE CASCADE,
  book_id UUID FK → Book(id) ON DELETE CASCADE,
  selected BOOLEAN DEFAULT FALSE,
  UNIQUE (activity_id, book_id)
)
12. GroupActivityPost
sql
복사
편집
GroupActivityPost (
  id UUID PK,
  activity_id UUID FK → GroupActivity(id) ON DELETE CASCADE,
  post_id UUID FK → Post(id) ON DELETE CASCADE,
  book_id UUID FK → Book(id) ON DELETE SET NULL,
  submitted_at TIMESTAMP NOT NULL,
  participation_style VARCHAR,
  UNIQUE (activity_id, post_id)
)
13. Schedule
sql
복사
편집
Schedule (
  id UUID PK,
  group_id UUID FK → Group(id) ON DELETE CASCADE,
  activity_id UUID FK → GroupActivity(id) ON DELETE SET NULL,
  title VARCHAR NOT NULL,
  description TEXT,
  scheduled_date DATE NOT NULL,
  created_by UUID FK → User(id) ON DELETE SET NULL,
  created_at TIMESTAMP NOT NULL
)
14. GroupActivitySchedule
sql
복사
편집
GroupActivitySchedule (
  id UUID PK,
  activity_id UUID FK → GroupActivity(id) ON DELETE CASCADE,
  schedule_id UUID FK → Schedule(id) ON DELETE CASCADE,
  UNIQUE (activity_id, schedule_id)
)
✅ 관계 요약
User → has many → Post, Comment, GroupUser, GroupActivity, Schedule, SocialAccount, UserProfile

Group → has many → GroupUser, Post, GroupActivity, Schedule

Post → has many → Comment, PostBook, (optionally) GroupActivityPost

GroupActivity → has many → GroupActivityBook, GroupActivityPost, GroupActivitySchedule
```

## 📄 `erd_schema.sql`

```
-- 1. User
CREATE TABLE User (
  id UUID PRIMARY KEY,
  username VARCHAR NOT NULL,
  email VARCHAR UNIQUE NOT NULL,
  hashed_password VARCHAR NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

-- 2. SocialAccount
CREATE TABLE SocialAccount (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES User(id) ON DELETE CASCADE,
  provider VARCHAR CHECK (provider IN ('google', 'kakao', 'github', 'naver')) NOT NULL,
  provider_user_id VARCHAR NOT NULL,
  email VARCHAR,
  username VARCHAR,
  profile_image_url VARCHAR,
  created_at TIMESTAMP NOT NULL,
  UNIQUE (provider, provider_user_id)
);

-- 3. UserProfile
CREATE TABLE UserProfile (
  id UUID PRIMARY KEY,
  user_id UUID UNIQUE REFERENCES User(id) ON DELETE CASCADE,
  bio TEXT,
  profile_image_url VARCHAR,
  website_url VARCHAR,
  location VARCHAR,
  created_at TIMESTAMP NOT NULL
);

-- 4. Group
CREATE TABLE Group (
  id UUID PRIMARY KEY,
  name VARCHAR NOT NULL,
  description TEXT,
  cover_image_url VARCHAR,
  owner_id UUID REFERENCES User(id) ON DELETE SET NULL,
  created_at TIMESTAMP NOT NULL
);

-- 5. GroupUser
CREATE TABLE GroupUser (
  id UUID PRIMARY KEY,
  group_id UUID REFERENCES Group(id) ON DELETE CASCADE,
  user_id UUID REFERENCES User(id) ON DELETE CASCADE,
  role VARCHAR CHECK (role IN ('owner', 'admin', 'member')) NOT NULL,
  status VARCHAR CHECK (status IN ('active', 'pending', 'banned')) NOT NULL,
  joined_at TIMESTAMP NOT NULL,
  UNIQUE (group_id, user_id)
);

-- 6. Book
CREATE TABLE Book (
  id UUID PRIMARY KEY,
  title VARCHAR NOT NULL,
  author VARCHAR NOT NULL,
  publisher VARCHAR,
  published_date DATE,
  description TEXT,
  isbn VARCHAR,
  image_url VARCHAR
);

-- 7. Post
CREATE TABLE Post (
  id UUID PRIMARY KEY,
  author_id UUID REFERENCES User(id) ON DELETE SET NULL,
  group_id UUID REFERENCES Group(id) ON DELETE SET NULL,
  activity_id UUID REFERENCES GroupActivity(id) ON DELETE SET NULL,
  category VARCHAR CHECK (category IN ('review', 'announcement', 'community')) NOT NULL,
  visibility VARCHAR CHECK (visibility IN ('public', 'group-only', 'private')) NOT NULL,
  title VARCHAR NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

-- 8. PostBook
CREATE TABLE PostBook (
  id UUID PRIMARY KEY,
  post_id UUID REFERENCES Post(id) ON DELETE CASCADE,
  book_id UUID REFERENCES Book(id) ON DELETE CASCADE,
  note TEXT,
  is_primary BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP NOT NULL,
  UNIQUE (post_id, book_id)
);

-- 9. Comment
CREATE TABLE Comment (
  id UUID PRIMARY KEY,
  post_id UUID REFERENCES Post(id) ON DELETE CASCADE,
  author_id UUID REFERENCES User(id) ON DELETE SET NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

-- 10. GroupActivity
CREATE TABLE GroupActivity (
  id UUID PRIMARY KEY,
  group_id UUID REFERENCES Group(id) ON DELETE CASCADE,
  type VARCHAR CHECK (type IN ('shared-reading', 'discussion', 'challenge')) NOT NULL,
  title VARCHAR NOT NULL,
  description TEXT,
  start_at TIMESTAMP,
  end_at TIMESTAMP,
  created_by UUID REFERENCES User(id) ON DELETE SET NULL,
  status VARCHAR CHECK (status IN ('planned', 'active', 'completed')) NOT NULL,
  created_at TIMESTAMP NOT NULL
);

-- 11. GroupActivityBook
CREATE TABLE GroupActivityBook (
  id UUID PRIMARY KEY,
  activity_id UUID REFERENCES GroupActivity(id) ON DELETE CASCADE,
  book_id UUID REFERENCES Book(id) ON DELETE CASCADE,
  selected BOOLEAN DEFAULT FALSE,
  UNIQUE (activity_id, book_id)
);

-- 12. GroupActivityPost
CREATE TABLE GroupActivityPost (
  id UUID PRIMARY KEY,
  activity_id UUID REFERENCES GroupActivity(id) ON DELETE CASCADE,
  post_id UUID REFERENCES Post(id) ON DELETE CASCADE,
  book_id UUID REFERENCES Book(id) ON DELETE SET NULL,
  submitted_at TIMESTAMP NOT NULL,
  participation_style VARCHAR,
  UNIQUE (activity_id, post_id)
);

-- 13. Schedule
CREATE TABLE Schedule (
  id UUID PRIMARY KEY,
  group_id UUID REFERENCES Group(id) ON DELETE CASCADE,
  activity_id UUID REFERENCES GroupActivity(id) ON DELETE SET NULL,
  title VARCHAR NOT NULL,
  description TEXT,
  scheduled_date DATE NOT NULL,
  created_by UUID REFERENCES User(id) ON DELETE SET NULL,
  created_at TIMESTAMP NOT NULL
);

-- 14. GroupActivitySchedule
CREATE TABLE GroupActivitySchedule (
  id UUID PRIMARY KEY,
  activity_id UUID REFERENCES GroupActivity(id) ON DELETE CASCADE,
  schedule_id UUID REFERENCES Schedule(id) ON DELETE CASCADE,
  UNIQUE (activity_id, schedule_id)
);

```

## 📄 `README.md`

```markdown

```

## 📄 `requirements.txt`

```
alembic==1.15.2
annotated-types==0.7.0
anyio==4.9.0
bcrypt==4.3.0
black==25.1.0
certifi==2025.4.26
cffi==1.17.1
charset-normalizer==3.4.2
click==8.2.0
colorama==0.4.6
cryptography==44.0.3
dnspython==2.7.0
ecdsa==0.19.1
email_validator==2.2.0
fastapi==0.115.12
greenlet==3.2.2
h11==0.16.0
httpcore==1.0.9
httptools==0.6.4
httpx==0.28.1
idna==3.10
iniconfig==2.1.0
isort==6.0.1
Mako==1.3.10
MarkupSafe==3.0.2
mypy==1.15.0
mypy_extensions==1.1.0
packaging==25.0
passlib==1.7.4
pathspec==0.12.1
platformdirs==4.3.8
pluggy==1.5.0
psycopg2-binary==2.9.10
pyasn1==0.4.8
pycparser==2.22
pydantic==2.11.4
pydantic-settings==2.9.1
pydantic_core==2.33.2
pytest==8.3.5
pytest-asyncio==0.26.0
python-dotenv==1.1.0
python-jose==3.4.0
PyYAML==6.0.2
requests==2.32.3
rsa==4.9.1
six==1.17.0
sniffio==1.3.1
SQLAlchemy==2.0.40
starlette==0.46.2
typing-inspection==0.4.0
typing_extensions==4.13.2
urllib3==2.4.0
uvicorn==0.34.2
watchfiles==1.0.5
websockets==15.0.1

```

## 📄 `backend\.env`

```
SQLALCHEMY_DATABASE_URL=postgresql+psycopg2://bookversedb_owner:npg_XH8Klm0fuBrS@ep-flat-smoke-a42pseb4-pooler.us-east-1.aws.neon.tech/bookversedb?sslmode=require

```

## 📄 `backend\requirements.txt`

```
alembic==1.15.2
annotated-types==0.7.0
anyio==4.9.0
bcrypt==4.3.0
black==25.1.0
certifi==2025.4.26
cffi==1.17.1
charset-normalizer==3.4.2
click==8.2.0
colorama==0.4.6
cryptography==44.0.3
dnspython==2.7.0
ecdsa==0.19.1
email_validator==2.2.0
fastapi==0.115.12
greenlet==3.2.2
h11==0.16.0
httpcore==1.0.9
httptools==0.6.4
httpx==0.28.1
idna==3.10
iniconfig==2.1.0
isort==6.0.1
Mako==1.3.10
MarkupSafe==3.0.2
mypy==1.15.0
mypy_extensions==1.1.0
packaging==25.0
passlib==1.7.4
pathspec==0.12.1
platformdirs==4.3.8
pluggy==1.5.0
psycopg2-binary==2.9.10
pyasn1==0.4.8
pycparser==2.22
pydantic==2.11.4
pydantic-settings==2.9.1
pydantic_core==2.33.2
pytest==8.3.5
pytest-asyncio==0.26.0
python-dotenv==1.1.0
python-jose==3.4.0
PyYAML==6.0.2
requests==2.32.3
rsa==4.9.1
six==1.17.0
sniffio==1.3.1
SQLAlchemy==2.0.40
starlette==0.46.2
typing-inspection==0.4.0
typing_extensions==4.13.2
urllib3==2.4.0
uvicorn==0.34.2
watchfiles==1.0.5
websockets==15.0.1

```

## 📄 `backend\app\main.py`

```python
from fastapi import FastAPI
from app.api.v1 import auth, groups

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Bookverse API"}

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(groups.router, prefix="/api/v1/groups", tags=["groups"])
```

## 📄 `backend\app\api\v1\activities.py`

```python

```

## 📄 `backend\app\api\v1\auth.py`

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.auth import SocialLoginRequest, TokenResponse
from app.services.auth_service import social_login

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/social-login", response_model=TokenResponse)
def login_social(request: SocialLoginRequest, db: Session = Depends(get_db)):
    try:
        token, user = social_login(request, db)
        return TokenResponse(access_token=token)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

```

## 📄 `backend\app\api\v1\books.py`

```python

```

## 📄 `backend\app\api\v1\comments.py`

```python

```

## 📄 `backend\app\api\v1\groups.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.group import GroupCreate, GroupRead
from app.services.group_service import (
    create_group, get_user_groups, request_to_join_group
)
from app.core.security import get_current_user
from app.db.session import get_db
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=GroupRead)
def create_my_group(
    group_in: GroupCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_group(db, current_user.id, group_in)

@router.get("/my", response_model=list[GroupRead])
def list_my_groups(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_user_groups(db, current_user.id)

@router.post("/{group_id}/join")
def join_group(
    group_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return request_to_join_group(db, current_user.id, group_id)

```

## 📄 `backend\app\api\v1\posts.py`

```python

```

## 📄 `backend\app\api\v1\schedules.py`

```python

```

## 📄 `backend\app\api\v1\users.py`

```python

```

## 📄 `backend\app\core\config.py`

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str

    class Config:
        env_file = ".env"  # 루트 기준

settings = Settings()

```

## 📄 `backend\app\core\exceptions.py`

```python

```

## 📄 `backend\app\core\logging.py`

```python

```

## 📄 `backend\app\core\security.py`

```python
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from uuid import UUID
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

def create_access_token(user_id):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": str(user_id), "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.id == UUID(user_id)).first()
    if user is None:
        raise credentials_exception
    return user
```

## 📄 `backend\app\db\base.py`

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()

```

## 📄 `backend\app\db\init_db.py`

```python

```

## 📄 `backend\app\db\session.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 환경변수에서 가져온 DB URL
SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL

# 엔진 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    future=True,
    pool_pre_ping=True
)

# 세션 팩토리
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# FastAPI에서 사용할 의존성 주입용 DB 세션 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

## 📄 `backend\app\models\activity.py`

```python

```

## 📄 `backend\app\models\base.py`

```python
from sqlalchemy.ext.declarative import as_declarative

@as_declarative()
class Base: 
    pass

```

## 📄 `backend\app\models\book.py`

```python

```

## 📄 `backend\app\models\comment.py`

```python

```

## 📄 `backend\app\models\group.py`

```python
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.base import Base

class Group(Base):
    __tablename__ = "group"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(Text)
    cover_image_url = Column(String)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="SET NULL"))
    created_at = Column(DateTime, default=datetime.utcnow)

```

## 📄 `backend\app\models\group_activity.py`

```python
from sqlalchemy import Column, Enum as SQLEnum, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.db.base import Base
from app.utils.enums import GroupActivityType, GroupActivityStatus

class GroupActivity(Base):
    __tablename__ = "group_activity"

    id = Column(UUID(as_uuid=True), primary_key=True)
    group_id = Column(UUID(as_uuid=True), ForeignKey("group.id", ondelete="CASCADE"), nullable=False)
    type = Column(SQLEnum(GroupActivityType, name="activity_type", native_enum=False), nullable=False)
    status = Column(SQLEnum(GroupActivityStatus, name="activity_status", native_enum=False), nullable=False)

    title = Column(String, nullable=False)
    description = Column(Text)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    created_by = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="SET NULL"))
    created_at = Column(DateTime, default=datetime.utcnow)

```

## 📄 `backend\app\models\group_user.py`

```python
from sqlalchemy import Column, ForeignKey, Enum as SQLEnum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.db.base import Base
from app.utils.enums import GroupUserRole, GroupUserStatus

class GroupUser(Base):
    __tablename__ = "group_user"

    id = Column(UUID(as_uuid=True), primary_key=True)
    group_id = Column(UUID(as_uuid=True), ForeignKey("group.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    role = Column(SQLEnum(GroupUserRole, name="group_user_role", native_enum=False), nullable=False)
    status = Column(SQLEnum(GroupUserStatus, name="group_user_status", native_enum=False), nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)

```

## 📄 `backend\app\models\post.py`

```python
from sqlalchemy import Column, Enum as SQLEnum, ForeignKey, DateTime, Text, String
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.db.base import Base
from app.utils.enums import PostCategory, PostVisibility

class Post(Base):
    __tablename__ = "post"

    id = Column(UUID(as_uuid=True), primary_key=True)
    author_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="SET NULL"))
    group_id = Column(UUID(as_uuid=True), ForeignKey("group.id", ondelete="SET NULL"))
    activity_id = Column(UUID(as_uuid=True), ForeignKey("group_activity.id", ondelete="SET NULL"))

    category = Column(SQLEnum(PostCategory, name="post_category", native_enum=False), nullable=False)
    visibility = Column(SQLEnum(PostVisibility, name="post_visibility", native_enum=False), nullable=False)

    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

```

## 📄 `backend\app\models\schedule.py`

```python

```

## 📄 `backend\app\models\social_account.py`

```python
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base
import uuid
from datetime import datetime

class SocialAccount(Base):
    __tablename__ = "social_accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    provider = Column(String, nullable=False)  # e.g., 'google'
    provider_user_id = Column(String, nullable=False)
    email = Column(String)
    username = Column(String)
    profile_image_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        # Prevent duplicate provider-user_id combinations
        {'sqlite_autoincrement': True},
    )
```

## 📄 `backend\app\models\user.py`

```python
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

```

## 📄 `backend\app\schemas\activity.py`

```python

```

## 📄 `backend\app\schemas\auth.py`

```python
from pydantic import BaseModel

class SocialLoginRequest(BaseModel):
    provider: str  # 'google', etc.
    access_token: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
```

## 📄 `backend\app\schemas\book.py`

```python

```

## 📄 `backend\app\schemas\comment.py`

```python

```

## 📄 `backend\app\schemas\group.py`

```python
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class GroupCreate(BaseModel):
    name: str
    description: str | None = None

class GroupRead(BaseModel):
    id: UUID
    name: str
    description: str | None
    owner_id: UUID | None
    created_at: datetime

    class Config:
        orm_mode = True


```

## 📄 `backend\app\schemas\group_activity.py`

```python
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.utils.enums import GroupActivityType, GroupActivityStatus

class GroupActivityBase(BaseModel):
    title: str
    description: str | None = None
    type: GroupActivityType
    status: GroupActivityStatus

class GroupActivityCreate(GroupActivityBase):
    group_id: UUID
    start_at: datetime | None = None
    end_at: datetime | None = None

class GroupActivityOut(GroupActivityBase):
    id: UUID
    group_id: UUID
    created_by: UUID | None
    created_at: datetime

    class Config:
        from_attributes = True

```

## 📄 `backend\app\schemas\group_user.py`

```python
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.utils.enums import GroupUserRole, GroupUserStatus

class GroupUserBase(BaseModel):
    group_id: UUID
    user_id: UUID
    role: GroupUserRole
    status: GroupUserStatus

class GroupUserCreate(GroupUserBase):
    pass

class GroupUserOut(GroupUserBase):
    id: UUID
    joined_at: datetime

    class Config:
        from_attributes = True

```

## 📄 `backend\app\schemas\post.py`

```python
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.utils.enums import PostCategory, PostVisibility

class PostBase(BaseModel):
    title: str
    content: str
    category: PostCategory
    visibility: PostVisibility

class PostCreate(PostBase):
    group_id: UUID | None = None
    activity_id: UUID | None = None

class PostOut(PostBase):
    id: UUID
    author_id: UUID | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

```

## 📄 `backend\app\schemas\schedule.py`

```python

```

## 📄 `backend\app\schemas\user.py`

```python
from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserRead(UserBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True

```

## 📄 `backend\app\services\activity_service.py`

```python

```

## 📄 `backend\app\services\auth_service.py`

```python
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
```

## 📄 `backend\app\services\book_service.py`

```python

```

## 📄 `backend\app\services\group_service.py`

```python
from app.models.group import Group
from app.models.group_user import GroupUser, GroupUserRole, GroupUserStatus
from app.schemas.group import GroupCreate
from sqlalchemy.orm import Session
from uuid import UUID

def create_group(db: Session, user_id: UUID, group_in: GroupCreate) -> Group:
    group = Group(
        name=group_in.name,
        description=group_in.description,
        owner_id=user_id,
    )
    db.add(group)
    db.flush()
    db.add(GroupUser(
        group_id=group.id,
        user_id=user_id,
        role=GroupUserRole.owner,
        status=GroupUserStatus.active
    ))
    db.commit()
    db.refresh(group)
    return group

def get_user_groups(db: Session, user_id: UUID) -> list[Group]:
    return db.query(Group).join(GroupUser).filter(
        GroupUser.user_id == user_id,
        GroupUser.status == GroupUserStatus.active
    ).all()

def request_to_join_group(db: Session, user_id: UUID, group_id: UUID):
    exists = db.query(GroupUser).filter_by(group_id=group_id, user_id=user_id).first()
    if exists:
        return exists  # 이미 요청 or 멤버

    gu = GroupUser(
        group_id=group_id,
        user_id=user_id,
        role=GroupUserRole.member,
        status=GroupUserStatus.pending
    )
    db.add(gu)
    db.commit()
    return gu

```

## 📄 `backend\app\services\post_service.py`

```python

```

## 📄 `backend\app\utils\datetime.py`

```python

```

## 📄 `backend\app\utils\enums.py`

```python
from enum import Enum

class GroupUserRole(str, Enum):
    owner = "owner"
    admin = "admin"
    member = "member"

class GroupUserStatus(str, Enum):
    active = "active"
    pending = "pending"
    banned = "banned"

class GroupActivityType(str, Enum):
    shared_reading = "shared-reading"
    discussion = "discussion"
    challenge = "challenge"

class GroupActivityStatus(str, Enum):
    planned = "planned"
    active = "active"
    completed = "completed"

class PostCategory(str, Enum):
    review = "review"
    announcement = "announcement"
    community = "community"

class PostVisibility(str, Enum):
    public = "public"
    group_only = "group-only"
    private = "private"

```

## 📄 `backend\app\utils\hashing.py`

```python

```

## 📄 `backend\app\utils\id_generator.py`

```python

```

## 📄 `frontend\.env.production`

```

```

## 📄 `frontend\next.config.js`

```javascript

```

## 📄 `frontend\package.json`

```json

```

## 📄 `frontend\postcss.config.js`

```javascript

```

## 📄 `frontend\tailwind.config.ts`

```typescript

```

## 📄 `frontend\tsconfig.json`

```json

```

## 📄 `frontend\app\layout.tsx`

```
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ko">
      <body>{children}</body>
    </html>
  );
}

```

## 📄 `frontend\app\page.tsx`

```
export default function Home() {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">📚 Bookverse에 오신 것을 환영합니다</h1>
    </div>
  );
}

```

## 📄 `frontend\components\layout\RightSidebar.tsx`

```

```

## 📄 `frontend\components\layout\Topbar.tsx`

```
export default function Topbar() {
  return (
    <header className="w-full h-16 bg-white border-b px-6 flex items-center">
      <h1 className="text-xl font-bold">Bookverse</h1>
    </header>
  );
}

```

## 📄 `frontend\lib\api\auth.ts`

```typescript
import axios from 'axios';

export const login = async (providerToken: string) => {
  return axios.post('/api/v1/auth/social-login', { token: providerToken });
};

```

## 📄 `frontend\lib\api\books.ts`

```typescript

```

## 📄 `frontend\lib\api\groups.ts`

```typescript

```

## 📄 `frontend\lib\api\posts.ts`

```typescript

```

## 📄 `frontend\lib\api\users.ts`

```typescript

```

## 📄 `frontend\styles\globals.css`

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  @apply bg-gray-50 text-gray-800;
}

```

