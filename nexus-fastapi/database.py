from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    __name__: str

    # Automatically generate table names if not explicitly defined
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from config import settings

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