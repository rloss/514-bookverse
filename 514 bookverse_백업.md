# 📁 프로젝트 구조

```
├── 📄 .gitignore
├── 📄 514 bookverse_백업.md
├── 📄 README.md
├── 📁 backend
│   ├── 📄 .env
│   ├── 📁 alembic
│   │   ├── 📄 README
│   │   ├── 📄 env.py
│   │   ├── 📄 script.py.mako
│   │   └── 📁 versions
│   │       ├── 📄 6728afd4e3b0_initial_tables.py
│   │       └── 📄 db2e16f81d79_add_remaining_models.py
│   ├── 📄 alembic.ini
│   ├── 📁 app
│   │   ├── 📁 api
│   │   │   └── 📁 v1
│   │   │       ├── 📄 auth.py
│   │   │       ├── 📄 books.py
│   │   │       ├── 📄 comments.py
│   │   │       ├── 📄 groups.py
│   │   │       ├── 📄 groups_activities.py
│   │   │       ├── 📄 my.py
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
│   │   │   ├── 📄 base.py
│   │   │   ├── 📄 book.py
│   │   │   ├── 📄 comment.py
│   │   │   ├── 📄 group.py
│   │   │   ├── 📄 group_activity.py
│   │   │   ├── 📄 group_activity_book.py
│   │   │   ├── 📄 group_activity_post.py
│   │   │   ├── 📄 group_activity_schedule.py
│   │   │   ├── 📄 group_user.py
│   │   │   ├── 📄 post.py
│   │   │   ├── 📄 post_book.py
│   │   │   ├── 📄 schedule.py
│   │   │   ├── 📄 social_account.py
│   │   │   ├── 📄 user.py
│   │   │   └── 📄 user_profile.py
│   │   ├── 📁 schemas
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

## 📄 `backend\alembic.ini`

```
# A generic, single database configuration.

[alembic]
# path to migration scripts
# Use forward slashes (/) also on windows to provide an os agnostic path
script_location = alembic

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.
prepend_sys_path = .

# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the python>=3.9 or backports.zoneinfo library and tzdata library.
# Any required deps can installed by adding `alembic[tz]` to the pip requirements
# string value is passed to ZoneInfo()
# leave blank for localtime
# timezone =

# max length of characters to apply to the "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to alembic/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "version_path_separator" below.
# version_locations = %(here)s/bar:%(here)s/bat:alembic/versions

# version path separator; As mentioned above, this is the character used to split
# version_locations. The default within new alembic.ini files is "os", which uses os.pathsep.
# If this key is omitted entirely, it falls back to the legacy behavior of splitting on spaces and/or commas.
# Valid values for version_path_separator are:
#
# version_path_separator = :
# version_path_separator = ;
# version_path_separator = space
# version_path_separator = newline
#
# Use os.pathsep. Default configuration used for new projects.
version_path_separator = os

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

sqlalchemy.url = postgresql+psycopg2://bookversedb_owner:npg_XH8Klm0fuBrS@ep-flat-smoke-a42pseb4-pooler.us-east-1.aws.neon.tech/bookversedb?sslmode=require


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the exec runner, execute a binary
# hooks = ruff
# ruff.type = exec
# ruff.executable = %(here)s/.venv/bin/ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARNING
handlers = console
qualname =

[logger_sqlalchemy]
level = WARNING
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S

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

## 📄 `backend\alembic\env.py`

```python
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from app.db.base import Base  # Base = declarative_base()
from app.models import *  # 모든 모델 import
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

# 이 부분에서 DB URL 설정
config = context.config
config.set_main_option(
    "sqlalchemy.url", os.getenv("SQLALCHEMY_DATABASE_URL")
)
# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

```

## 📄 `backend\alembic\README`

```
Generic single-database configuration.
```

## 📄 `backend\alembic\script.py.mako`

```
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    """Upgrade schema."""
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    """Downgrade schema."""
    ${downgrades if downgrades else "pass"}

```

## 📄 `backend\alembic\versions\6728afd4e3b0_initial_tables.py`

```python
"""initial tables

Revision ID: 6728afd4e3b0
Revises: 
Create Date: 2025-05-14 10:38:51.837644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6728afd4e3b0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

```

## 📄 `backend\alembic\versions\db2e16f81d79_add_remaining_models.py`

```python
"""add remaining models

Revision ID: db2e16f81d79
Revises: 6728afd4e3b0
Create Date: 2025-05-14 10:51:55.932935

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db2e16f81d79'
down_revision: Union[str, None] = '6728afd4e3b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

```

## 📄 `backend\app\main.py`

```python
from fastapi import FastAPI
from app.api.v1 import auth, groups, groups_activities

app = FastAPI()

# ✅ 루트 경로 → API 리스트 제공
@app.get("/")
def root():
    return {
        "message": "📦 Bookverse API is running!",
        "routes": [
            route.path for route in app.routes if route.path.startswith("/api")
        ]
    }

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(groups.router, prefix="/api/v1/groups", tags=["groups"])
app.include_router(groups_activities.router, prefix="/api/v1/groups-activities", tags=["activities"])
```

## 📄 `backend\app\api\v1\auth.py`

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

## 📄 `backend\app\api\v1\books.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_books():
    return {"books": []}

```

## 📄 `backend\app\api\v1\comments.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_comment():
    return {"msg": "Comment created"}

```

## 📄 `backend\app\api\v1\groups.py`

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

## 📄 `backend\app\api\v1\groups_activities.py`

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

## 📄 `backend\app\api\v1\my.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/my/posts")
async def my_posts():
    return {"my_posts": []}

```

## 📄 `backend\app\api\v1\posts.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_posts():
    return {"posts": []}

```

## 📄 `backend\app\api\v1\schedules.py`

```python

```

## 📄 `backend\app\api\v1\users.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

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

## 📄 `backend\app\models\base.py`

```python
from sqlalchemy.ext.declarative import as_declarative

@as_declarative()
class Base: 
    pass

```

## 📄 `backend\app\models\book.py`

```python
from sqlalchemy import Column, String, Date, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base

class Book(Base):
    __tablename__ = "book"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String)
    published_date = Column(Date)
    description = Column(Text)
    isbn = Column(String)
    image_url = Column(String)

```

## 📄 `backend\app\models\comment.py`

```python
from sqlalchemy import Column, ForeignKey, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from app.db.base import Base

class Comment(Base):
    __tablename__ = "comment"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    post_id = Column(UUID(as_uuid=True), ForeignKey("post.id", ondelete="CASCADE"), nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="SET NULL"))
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

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

## 📄 `backend\app\models\group_activity_book.py`

```python
from sqlalchemy import Column, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base

class GroupActivityBook(Base):
    __tablename__ = "group_activity_book"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    activity_id = Column(UUID(as_uuid=True), ForeignKey("group_activity.id", ondelete="CASCADE"), nullable=False)
    book_id = Column(UUID(as_uuid=True), ForeignKey("book.id", ondelete="CASCADE"), nullable=False)
    selected = Column(Boolean, default=False)

```

## 📄 `backend\app\models\group_activity_post.py`

```python
from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from app.db.base import Base

class GroupActivityPost(Base):
    __tablename__ = "group_activity_post"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    activity_id = Column(UUID(as_uuid=True), ForeignKey("group_activity.id", ondelete="CASCADE"), nullable=False)
    post_id = Column(UUID(as_uuid=True), ForeignKey("post.id", ondelete="CASCADE"), nullable=False)
    book_id = Column(UUID(as_uuid=True), ForeignKey("book.id", ondelete="SET NULL"))
    submitted_at = Column(DateTime, default=datetime.utcnow)
    participation_style = Column(String)

```

## 📄 `backend\app\models\group_activity_schedule.py`

```python
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base

class GroupActivitySchedule(Base):
    __tablename__ = "group_activity_schedule"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    activity_id = Column(UUID(as_uuid=True), ForeignKey("group_activity.id", ondelete="CASCADE"), nullable=False)
    schedule_id = Column(UUID(as_uuid=True), ForeignKey("schedule.id", ondelete="CASCADE"), nullable=False)

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

## 📄 `backend\app\models\post_book.py`

```python
from sqlalchemy import Column, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from app.db.base import Base

class PostBook(Base):
    __tablename__ = "post_book"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    post_id = Column(UUID(as_uuid=True), ForeignKey("post.id", ondelete="CASCADE"), nullable=False)
    book_id = Column(UUID(as_uuid=True), ForeignKey("book.id", ondelete="CASCADE"), nullable=False)
    note = Column(Text)
    is_primary = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

```

## 📄 `backend\app\models\schedule.py`

```python
from sqlalchemy import Column, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from app.db.base import Base

class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    group_id = Column(UUID(as_uuid=True), ForeignKey("group.id", ondelete="CASCADE"))
    activity_id = Column(UUID(as_uuid=True), ForeignKey("group_activity.id", ondelete="SET NULL"))
    title = Column(String, nullable=False)
    description = Column(Text)
    scheduled_date = Column(Date, nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="SET NULL"))
    created_at = Column(DateTime, default=datetime.utcnow)

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
from datetime import datetime
import uuid

from app.db.base import Base

class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

```

## 📄 `backend\app\models\user_profile.py`

```python
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from app.db.base import Base

class UserProfile(Base):
    __tablename__ = "user_profile"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"), unique=True, nullable=False)
    bio = Column(Text)
    profile_image_url = Column(String)
    website_url = Column(String)
    location = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

```

## 📄 `backend\app\schemas\auth.py`

```python
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
```

## 📄 `backend\app\schemas\book.py`

```python
from pydantic import BaseModel
from uuid import UUID
from datetime import date

class BookBase(BaseModel):
    title: str
    author: str
    publisher: str | None = None
    published_date: date | None = None
    description: str | None = None
    isbn: str | None = None
    image_url: str | None = None

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: UUID

    class Config:
        from_attributes = True

```

## 📄 `backend\app\schemas\comment.py`

```python
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    post_id: UUID

class CommentOut(CommentBase):
    id: UUID
    post_id: UUID
    author_id: UUID | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

```

## 📄 `backend\app\schemas\group.py`

```python
# ✅ 병합 제안

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
    created_at: datetime

    class Config:
        from_attributes = True

class GroupJoinRequest(BaseModel):
    group_id: UUID
    message: str | None = None

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
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, date

class ScheduleBase(BaseModel):
    title: str
    description: str | None = None
    scheduled_date: date

class ScheduleCreate(ScheduleBase):
    group_id: UUID
    activity_id: UUID | None = None

class ScheduleOut(ScheduleBase):
    id: UUID
    group_id: UUID
    activity_id: UUID | None
    created_by: UUID | None
    created_at: datetime

    class Config:
        from_attributes = True

```

## 📄 `backend\app\schemas\user.py`

```python
from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserProfileOut(BaseModel):
    id: UUID
    bio: str | None
    profile_image_url: str | None
    website_url: str | None
    location: str | None
    created_at: datetime

    class Config:
        from_attributes = True

```

## 📄 `backend\app\services\activity_service.py`

```python
from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime
from app.models.group_activity import GroupActivity
from app.schemas.group_activity import GroupActivityCreate
from app.models.user import User


def create_activity(db: Session, creator: User, activity_data: GroupActivityCreate) -> GroupActivity:
    new_activity = GroupActivity(
        id=UUID(),  # 또는 uuid.uuid4()
        group_id=activity_data.group_id,
        type=activity_data.type,
        status=activity_data.status,
        title=activity_data.title,
        description=activity_data.description,
        start_at=activity_data.start_at,
        end_at=activity_data.end_at,
        created_by=creator.id,
        created_at=datetime.utcnow()
    )
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    return new_activity


def list_group_activities(db: Session, group_id: UUID) -> list[GroupActivity]:
    return db.query(GroupActivity).filter(GroupActivity.group_id == group_id).all()


def get_activity_detail(db: Session, activity_id: UUID) -> GroupActivity | None:
    return db.query(GroupActivity).filter(GroupActivity.id == activity_id).first()

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
from sqlalchemy.orm import Session
from uuid import UUID
from app.models.group import Group
from app.models.group_user import GroupUser, GroupUserRole, GroupUserStatus
from app.schemas.group import GroupCreate

def create_group(db: Session, owner_id: UUID, group_data: GroupCreate) -> Group:
    group = Group(
        name=group_data.name,
        description=group_data.description,
        owner_id=owner_id,
    )
    db.add(group)
    db.commit()
    db.refresh(group)

    # 자동 그룹 등록
    group_user = GroupUser(
        group_id=group.id,
        user_id=owner_id,
        role=GroupUserRole.owner,
        status=GroupUserStatus.active,
    )
    db.add(group_user)
    db.commit()

    return group


def get_user_groups(db: Session, user_id: UUID):
    return (
        db.query(Group)
        .join(GroupUser)
        .filter(GroupUser.user_id == user_id)
        .all()
    )


def get_group_by_id(db: Session, group_id: UUID):
    return db.query(Group).filter(Group.id == group_id).first()


def request_to_join_group(db: Session, user_id: UUID, group_id: UUID, message: str | None = None):
    group_user = GroupUser(
        group_id=group_id,
        user_id=user_id,
        role=GroupUserRole.member,
        status=GroupUserStatus.pending,
    )
    db.add(group_user)
    db.commit()
    db.refresh(group_user)
    return {"msg": "Join request submitted", "group_user_id": str(group_user.id)}


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

