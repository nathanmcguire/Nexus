from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from ..database import Base
from passlib.hash import argon2
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    guid: Mapped[str] = mapped_column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    _password: Mapped[str] = mapped_column(String(128), nullable=False)
    enabled: Mapped[str] = mapped_column(Boolean, nullable=False, default=False)
    archived: Mapped[str] = mapped_column(Boolean, nullable=False, default=False)
    deleted: Mapped[str] = mapped_column(Boolean, nullable=False, default=False)

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, plaintext_password: str) -> None:
        self._password = argon2.hash(plaintext_password)

    def check_password(self, plaintext_password: str) -> bool:
        return argon2.verify(plaintext_password, self._password)




