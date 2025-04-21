from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from ..database import Base
from ..common.models import AuditMixIn
from passlib.hash import argon2
from datetime import datetime, timezone


class User(Base, AuditMixIn):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    guid: Mapped[str] = mapped_column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    enabled_at: Mapped[str] = mapped_column(String(32), nullable=True)
    enabled_by: Mapped[str] = mapped_column(String(32), nullable=True)
    disabled_at: Mapped[str] = mapped_column(String(32), nullable=True)
    disabled_by: Mapped[str] = mapped_column(String(32), nullable=True)


    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, raw_password: str) -> None:
        self._password = argon2.hash(raw_password)

    def verify_password(self, raw_password: str) -> bool:
        """
        Verifies if the provided raw password matches the stored hashed password.
        """
        return argon2.verify(raw_password, self._password)
    
    @property
    def is_enabled(self) -> bool:
        """
        Checks if the entity is enabled based on the conditions:
        - `enabled` is not None
        - `disabled` is None or `disabled_at` is earlier than `enabled_at`
        """
        return self.enabled is not None and (
            self.disabled is None or self.enabled_at > self.disabled_at
        )
    @is_enabled.setter
    def is_enabled(self, value: bool) -> None:
        """
        Sets the enabled status of the entity.
        If `value` is True, sets `enabled_at` to the current time and clears `disabled_at`.
        If `value` is False, sets `disabled_at` to the current time and clears `enabled_at`.
        """
        if value:
            self.enabled_at = datetime.now(timezone.utc)
            self.enabled_by = -1
        else:
            self.disabled_at = datetime.now(timezone.utc)
            self.disabled_by = -1


