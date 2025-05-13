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
