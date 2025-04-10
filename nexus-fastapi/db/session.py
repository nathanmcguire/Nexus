from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from core.config import settings

# Synchronous database engine
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

# Asynchronous database engine (if needed)
# async_engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)

# Session maker for synchronous sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()