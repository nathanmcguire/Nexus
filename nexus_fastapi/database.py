from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from typing import Any

@as_declarative()
class Base:
    __name__: str

    # Automatically generate table names if not explicitly defined
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

# Synchronous database engine
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

# Session maker for synchronous sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Removed Base.metadata.create_all(bind=engine) to let Alembic handle migrations

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to return Base and engine for Alembic
def get_base_and_engine() -> Any:
    return Base, engine
