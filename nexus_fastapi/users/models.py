from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from datetime import datetime
from nexus_fastapi.database import Base

class User(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    guid: Mapped[str] = mapped_column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    created_by: Mapped[str] = mapped_column(String, nullable=False)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    updated_by: Mapped[str | None] = mapped_column(String, nullable=True)
    archived_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    archived_by: Mapped[str | None] = mapped_column(String, nullable=True)
    unarchived_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    unarchived_by: Mapped[str | None] = mapped_column(String, nullable=True)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    deleted_by: Mapped[str | None] = mapped_column(String, nullable=True)
    undeleted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    undeleted_by: Mapped[str | None] = mapped_column(String, nullable=True)

    @property
    def is_archived(self) -> bool:
        return self.archived_at is not None and (self.unarchived_at is None or self.archived_at > self.unarchived_at)

    @is_archived.setter
    def is_archived(self, value: bool) -> None:
        if value:
            self.archived_at = datetime.utcnow()
            self.archived_by = -1
        else:
            self.unarchived_at = datetime.utcnow()
            self.unarchived_by = -1

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None and (self.undeleted_at is None or self.deleted_at > self.undeleted_at)

    @is_deleted.setter
    def is_deleted(self, value: bool) -> None:
        if value:
            self.deleted_at = datetime.utcnow()
            self.deleted_by = -1
        else:
            self.undeleted_at = datetime.utcnow()
            self.undeleted_by = -1



