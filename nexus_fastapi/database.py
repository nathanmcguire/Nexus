"""
Database module for the nexus_fastapi application.

This module sets up the SQLAlchemy engine, session, and base for the ORM.

Attributes:
    engine (sqlalchemy.engine.Engine): The SQLAlchemy engine for database connections.
    SessionLocal (sqlalchemy.orm.session.Session): The session factory for database operations.
    Base (sqlalchemy.ext.declarative.api.Base): The declarative base class for ORM models.

Functions:
    get_db(): Dependency function to provide a database session.

Notes:
    Ensure that the `SQLALCHEMY_DATABASE_URI` in the settings is correctly configured.

References:
    SQLAlchemy Documentation: https://docs.sqlalchemy.org/en/latest/
    Connection Pooling: https://docs.sqlalchemy.org/en/latest/core/pooling.html
    Database URLs: https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls
"""

# sphinx-build-ignore
# Ignore specific warnings related to undefined labels and unknown documents in Sphinx documentation.
# These warnings are not critical and can be safely ignored.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Create the SQLAlchemy engine
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a declarative base class
Base = declarative_base()

# Import all models to ensure they are registered with the Base
from .models import *



def get_db():
    """
    Dependency function to provide a database session.

    Yields:
        sqlalchemy.orm.session.Session: A database session.

    Ensures that the session is properly closed after use.

    Example:
        >>> with get_db() as db:
        ...     db.query(User).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

__all__ = ["engine", "SessionLocal", "Base", "get_db"]
